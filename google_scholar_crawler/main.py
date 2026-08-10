from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, quote, urlparse
from urllib.request import Request, urlopen


SCRIPT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = SCRIPT_DIR / "results"
DATA_FILENAME = "gs_data.json"
SHIELD_FILENAME = "gs_data_shieldsio.json"
MAX_PROFILE_BYTES = 2_000_000

USER_AGENTS = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/127.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36",
)

BLOCK_PAGE_MARKERS = (
    "unusual traffic",
    "not a robot",
    "g-recaptcha",
    "/sorry/",
)


def _positive_int_from_env(name: str, default: int) -> int:
    raw_value = os.environ.get(name, str(default))
    try:
        value = int(raw_value)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer, got {raw_value!r}") from exc
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero")
    return value


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as outfile:
        json.dump(payload, outfile, ensure_ascii=False, default=str)
        outfile.write("\n")


class ScholarProfileParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.description = ""
        self.canonical_url = ""
        self.profile_name = ""
        self.stats: list[str] = []
        self._capture_name = False
        self._capture_stat = False
        self._name_parts: list[str] = []
        self._stat_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {key: value or "" for key, value in attrs}

        if tag == "meta" and attributes.get("name", "").lower() == "description":
            self.description = attributes.get("content", "")
        elif tag == "link" and "canonical" in attributes.get("rel", "").lower().split():
            self.canonical_url = attributes.get("href", "")

        if tag == "div" and attributes.get("id") == "gsc_prf_in":
            self._capture_name = True
            self._name_parts = []

        classes = set(attributes.get("class", "").split())
        if tag in {"a", "span", "td"} and "gsc_rsb_std" in classes:
            self._capture_stat = True
            self._stat_parts = []

    def handle_data(self, data: str) -> None:
        if self._capture_name:
            self._name_parts.append(data)
        if self._capture_stat:
            self._stat_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "div" and self._capture_name:
            self.profile_name = "".join(self._name_parts).strip()
            self._capture_name = False
        if tag in {"a", "span", "td"} and self._capture_stat:
            value = "".join(self._stat_parts).strip()
            if value:
                self.stats.append(value)
            self._capture_stat = False


def _parse_count(raw_value: str) -> int | None:
    digits = re.sub(r"[^0-9]", "", raw_value)
    return int(digits) if digits else None


def parse_profile_html(html: str, expected_scholar_id: str) -> tuple[str, int]:
    lowered = html.lower()
    if any(marker in lowered for marker in BLOCK_PAGE_MARKERS):
        raise ValueError("Google Scholar returned a bot-check page")

    parser = ScholarProfileParser()
    parser.feed(html)

    if parser.canonical_url:
        canonical_id = parse_qs(urlparse(parser.canonical_url).query).get("user", [""])[0]
        if canonical_id and canonical_id != expected_scholar_id:
            raise ValueError(
                f"Google Scholar returned scholar_id {canonical_id!r}, "
                f"expected {expected_scholar_id!r}"
            )

    counts: list[int] = []
    description_match = re.search(r"Cited\s+by\s+([0-9][0-9,]*)", parser.description, re.I)
    if description_match:
        counts.append(int(description_match.group(1).replace(",", "")))

    if parser.stats:
        first_stat = _parse_count(parser.stats[0])
        if first_stat is not None:
            counts.append(first_stat)

    if not counts:
        raise ValueError("Google Scholar profile did not contain a citation count")
    if len(set(counts)) != 1:
        raise ValueError(f"Google Scholar returned conflicting citation counts: {counts}")

    name = parser.profile_name or "Zhen Sun"
    return name, counts[0]


def _fetch_profile_html(scholar_id: str, attempt: int) -> str:
    timeout_seconds = _positive_int_from_env("SCHOLAR_HTTP_TIMEOUT_SECONDS", 30)
    profile_url = (
        "https://scholar.google.com/citations?"
        f"user={quote(scholar_id)}&hl=en&oi=ao"
    )
    request = Request(
        profile_url,
        headers={
            "User-Agent": USER_AGENTS[(attempt - 1) % len(USER_AGENTS)],
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
        },
    )

    try:
        with urlopen(request, timeout=timeout_seconds) as response:
            status = getattr(response, "status", 200)
            if status != 200:
                raise ValueError(f"Google Scholar returned HTTP {status}")
            payload = response.read(MAX_PROFILE_BYTES + 1)
            if len(payload) > MAX_PROFILE_BYTES:
                raise ValueError("Google Scholar profile response was unexpectedly large")
            charset = response.headers.get_content_charset() or "utf-8"
    except HTTPError as exc:
        raise RuntimeError(f"Google Scholar returned HTTP {exc.code}") from exc
    except (URLError, TimeoutError) as exc:
        raise RuntimeError(f"Google Scholar request failed: {exc}") from exc

    return payload.decode(charset, errors="replace")


def _load_previous_author(expected_scholar_id: str) -> dict:
    previous_path = RESULTS_DIR / DATA_FILENAME
    if not previous_path.exists():
        return {}
    try:
        with previous_path.open(encoding="utf-8") as infile:
            author = json.load(infile)
    except (OSError, json.JSONDecodeError):
        return {}
    if not isinstance(author, dict):
        return {}
    previous_id = author.get("scholar_id")
    if previous_id and previous_id != expected_scholar_id:
        return {}
    return author


def _build_author(name: str, scholar_id: str, citedby: int) -> dict:
    author = _load_previous_author(scholar_id)
    previous_citedby = author.get("citedby")
    if isinstance(previous_citedby, int) and citedby < previous_citedby:
        allowed_drop = max(5, round(previous_citedby * 0.02))
        if previous_citedby - citedby > allowed_drop:
            raise ValueError(
                f"Citation count dropped unexpectedly from {previous_citedby} to {citedby}"
            )

    author.update(
        {
            "name": name,
            "scholar_id": scholar_id,
            "citedby": citedby,
            "updated": datetime.now(timezone.utc).isoformat(),
            "source": "GOOGLE_SCHOLAR_PROFILE_PAGE",
        }
    )
    publications = author.get("publications")
    if not isinstance(publications, dict):
        author["publications"] = {}
    return author


def fetch_once(output_dir: Path, attempt: int) -> None:
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not scholar_id:
        raise ValueError("GOOGLE_SCHOLAR_ID is not configured")

    html = _fetch_profile_html(scholar_id, attempt)
    name, citedby = parse_profile_html(html, scholar_id)
    author = _build_author(name, scholar_id, citedby)

    shield_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(citedby),
    }
    _write_json(output_dir / DATA_FILENAME, author)
    _write_json(output_dir / SHIELD_FILENAME, shield_data)
    print(f"Fetched {citedby} citations for {name}")


def validate_outputs(output_dir: Path) -> int:
    with (output_dir / DATA_FILENAME).open(encoding="utf-8") as infile:
        author = json.load(infile)
    with (output_dir / SHIELD_FILENAME).open(encoding="utf-8") as infile:
        shield = json.load(infile)

    citedby = author.get("citedby")
    if isinstance(citedby, bool) or not isinstance(citedby, int) or citedby < 0:
        raise ValueError("Generated author data does not contain a valid citation count")
    if shield.get("message") != str(citedby):
        raise ValueError("Generated badge data does not match the author citation count")
    return citedby


def fetch_with_retries() -> None:
    max_attempts = _positive_int_from_env("SCHOLAR_MAX_ATTEMPTS", 4)
    timeout_seconds = _positive_int_from_env("SCHOLAR_ATTEMPT_TIMEOUT_SECONDS", 45)
    last_error: Exception | None = None

    with tempfile.TemporaryDirectory(prefix=".scholar-", dir=SCRIPT_DIR) as temp_dir_name:
        temp_dir = Path(temp_dir_name)
        for attempt in range(1, max_attempts + 1):
            print(f"Google Scholar fetch attempt {attempt}/{max_attempts}")
            env = os.environ.copy()
            command = [
                sys.executable,
                str(Path(__file__).resolve()),
                "--fetch-once",
                "--attempt",
                str(attempt),
                "--output-dir",
                str(temp_dir),
            ]
            try:
                completed = subprocess.run(
                    command,
                    check=True,
                    capture_output=True,
                    text=True,
                    timeout=timeout_seconds,
                    env=env,
                )
                if completed.stdout:
                    print(completed.stdout.strip())
                citedby = validate_outputs(temp_dir)
                RESULTS_DIR.mkdir(parents=True, exist_ok=True)
                for filename in (DATA_FILENAME, SHIELD_FILENAME):
                    os.replace(temp_dir / filename, RESULTS_DIR / filename)
                print(f"Validated and saved citation data ({citedby} citations)")
                return
            except subprocess.TimeoutExpired as exc:
                last_error = exc
                print(
                    f"Attempt {attempt} timed out after {timeout_seconds} seconds",
                    file=sys.stderr,
                )
            except (subprocess.CalledProcessError, OSError, ValueError, json.JSONDecodeError) as exc:
                last_error = exc
                print(f"Attempt {attempt} failed: {exc}", file=sys.stderr)
                if isinstance(exc, subprocess.CalledProcessError) and exc.stderr:
                    print(exc.stderr.strip(), file=sys.stderr)

            if attempt < max_attempts:
                delay_seconds = min(10 * (2 ** (attempt - 1)), 60)
                print(f"Retrying in {delay_seconds} seconds")
                time.sleep(delay_seconds)

    raise RuntimeError(
        f"Unable to fetch valid Google Scholar data after {max_attempts} attempts"
    ) from last_error


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch Google Scholar citation data")
    parser.add_argument("--fetch-once", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--attempt", type=int, default=1, help=argparse.SUPPRESS)
    parser.add_argument("--output-dir", type=Path, default=RESULTS_DIR, help=argparse.SUPPRESS)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.fetch_once:
        fetch_once(args.output_dir, args.attempt)
    else:
        fetch_with_retries()


if __name__ == "__main__":
    main()
