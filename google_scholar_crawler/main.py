from __future__ import annotations

import json
import os
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


SCRIPT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = SCRIPT_DIR / "results"
DATA_FILENAME = "gs_data.json"
SHIELD_FILENAME = "gs_data_shieldsio.json"
SERPAPI_ENDPOINT = "https://serpapi.com/search.json"
MAX_RESPONSE_BYTES = 2_000_000


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


def parse_serpapi_payload(payload: dict, expected_scholar_id: str) -> tuple[str, int]:
    if not isinstance(payload, dict):
        raise ValueError("SerpApi returned an invalid response")
    if payload.get("error"):
        raise ValueError("SerpApi reported an error")

    metadata = payload.get("search_metadata")
    if not isinstance(metadata, dict) or metadata.get("status") != "Success":
        raise ValueError("SerpApi search did not complete successfully")

    parameters = payload.get("search_parameters")
    if not isinstance(parameters, dict) or parameters.get("author_id") != expected_scholar_id:
        raise ValueError("SerpApi returned data for an unexpected Scholar profile")

    author = payload.get("author")
    name = author.get("name") if isinstance(author, dict) else None
    if not isinstance(name, str) or not name.strip():
        raise ValueError("SerpApi response is missing the author name")

    cited_by = payload.get("cited_by")
    table = cited_by.get("table") if isinstance(cited_by, dict) else None
    citations = table[0].get("citations") if isinstance(table, list) and table else None
    citedby = citations.get("all") if isinstance(citations, dict) else None
    if isinstance(citedby, bool) or not isinstance(citedby, int) or citedby < 0:
        raise ValueError("SerpApi response is missing a valid citation count")

    return name.strip(), citedby


def _fetch_serpapi_payload(scholar_id: str, api_key: str, timeout_seconds: int) -> dict:
    query = urlencode(
        {
            "engine": "google_scholar_author",
            "author_id": scholar_id,
            "hl": "en",
            "api_key": api_key,
        }
    )
    request = Request(
        f"{SERPAPI_ENDPOINT}?{query}",
        headers={"Accept": "application/json", "User-Agent": "citation-sync/1.0"},
    )
    try:
        with urlopen(request, timeout=timeout_seconds) as response:
            body = response.read(MAX_RESPONSE_BYTES + 1)
    except HTTPError as exc:
        raise RuntimeError(f"SerpApi request failed with HTTP {exc.code}") from exc
    except (URLError, TimeoutError) as exc:
        raise RuntimeError("SerpApi request failed because of a network error") from exc

    if len(body) > MAX_RESPONSE_BYTES:
        raise ValueError("SerpApi response exceeded the safety limit")
    try:
        payload = json.loads(body)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("SerpApi returned invalid JSON") from exc
    if not isinstance(payload, dict):
        raise ValueError("SerpApi returned an invalid response")
    return payload


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


def _validate_citation_change(previous_author: dict, citedby: int) -> None:
    previous_citedby = previous_author.get("citedby")
    if (
        isinstance(previous_citedby, bool)
        or not isinstance(previous_citedby, int)
        or citedby >= previous_citedby
    ):
        return
    allowed_drop = max(5, round(previous_citedby * 0.02))
    if previous_citedby - citedby > allowed_drop:
        raise ValueError(
            f"Citation count dropped unexpectedly from {previous_citedby} to {citedby}"
        )


def _build_author(previous_author: dict, scholar_id: str, name: str, citedby: int) -> dict:
    _validate_citation_change(previous_author, citedby)
    author = dict(previous_author)
    author.update(
        {
            "name": name,
            "scholar_id": scholar_id,
            "citedby": citedby,
            "updated": datetime.now(timezone.utc).isoformat(),
            "source": "SERPAPI_GOOGLE_SCHOLAR_AUTHOR",
        }
    )
    publications = author.get("publications")
    if publications is not None and not isinstance(publications, (dict, list)):
        author.pop("publications")
    return author


def _validate_outputs(output_dir: Path) -> int:
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
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    api_key = os.environ.get("SERPAPI_API_KEY", "").strip()
    if not scholar_id:
        raise ValueError("GOOGLE_SCHOLAR_ID is not configured")
    if not api_key:
        raise ValueError("SERPAPI_API_KEY is not configured")

    max_attempts = _positive_int_from_env("SCHOLAR_MAX_ATTEMPTS", 3)
    timeout_seconds = _positive_int_from_env("SCHOLAR_HTTP_TIMEOUT_SECONDS", 30)
    previous_author = _load_previous_author(scholar_id)
    last_error: Exception | None = None

    with tempfile.TemporaryDirectory(prefix=".scholar-", dir=SCRIPT_DIR) as temp_name:
        temp_dir = Path(temp_name)
        for attempt in range(1, max_attempts + 1):
            print(f"SerpApi Scholar fetch attempt {attempt}/{max_attempts}")
            try:
                payload = _fetch_serpapi_payload(scholar_id, api_key, timeout_seconds)
                name, citedby = parse_serpapi_payload(payload, scholar_id)
                author = _build_author(previous_author, scholar_id, name, citedby)
                shield = {
                    "schemaVersion": 1,
                    "label": "citations",
                    "message": str(citedby),
                }
                _write_json(temp_dir / DATA_FILENAME, author)
                _write_json(temp_dir / SHIELD_FILENAME, shield)
                _validate_outputs(temp_dir)

                RESULTS_DIR.mkdir(parents=True, exist_ok=True)
                for filename in (DATA_FILENAME, SHIELD_FILENAME):
                    os.replace(temp_dir / filename, RESULTS_DIR / filename)
                print(f"Validated and saved citation data ({citedby} citations)")
                return
            except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
                last_error = exc
                print(f"Attempt {attempt} failed: {exc}")

            if attempt < max_attempts:
                delay_seconds = min(10 * (2 ** (attempt - 1)), 40)
                print(f"Retrying in {delay_seconds} seconds")
                time.sleep(delay_seconds)

    raise RuntimeError(
        f"Unable to fetch valid Scholar data after {max_attempts} attempts"
    ) from last_error


if __name__ == "__main__":
    fetch_with_retries()
