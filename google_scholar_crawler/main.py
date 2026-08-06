from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = SCRIPT_DIR / "results"
DATA_FILENAME = "gs_data.json"
SHIELD_FILENAME = "gs_data_shieldsio.json"


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


def _normalise_author(author: dict, expected_scholar_id: str) -> dict:
    if not isinstance(author, dict):
        raise ValueError("Google Scholar returned an invalid author record")

    returned_scholar_id = author.get("scholar_id")
    if returned_scholar_id and returned_scholar_id != expected_scholar_id:
        raise ValueError(
            f"Google Scholar returned scholar_id {returned_scholar_id!r}, "
            f"expected {expected_scholar_id!r}"
        )

    citedby = author.get("citedby")
    if isinstance(citedby, bool) or not isinstance(citedby, int) or citedby < 0:
        raise ValueError(f"Invalid citation count returned by Google Scholar: {citedby!r}")

    publications = author.get("publications", [])
    if isinstance(publications, list):
        author["publications"] = {
            publication["author_pub_id"]: publication
            for publication in publications
            if isinstance(publication, dict) and publication.get("author_pub_id")
        }
    elif not isinstance(publications, dict):
        raise ValueError("Google Scholar returned an invalid publications collection")

    author["updated"] = datetime.now(timezone.utc).isoformat()
    return author


def fetch_once(output_dir: Path) -> None:
    # Import only in the worker process so a timed-out request can be terminated cleanly.
    from scholarly import scholarly

    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not scholar_id:
        raise ValueError("GOOGLE_SCHOLAR_ID is not configured")

    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
    author = _normalise_author(author, scholar_id)

    shield_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author["citedby"]),
    }
    _write_json(output_dir / DATA_FILENAME, author)
    _write_json(output_dir / SHIELD_FILENAME, shield_data)
    print(f"Fetched {author['citedby']} citations for {author.get('name', scholar_id)}")


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
    max_attempts = _positive_int_from_env("SCHOLAR_MAX_ATTEMPTS", 3)
    timeout_seconds = _positive_int_from_env("SCHOLAR_ATTEMPT_TIMEOUT_SECONDS", 120)
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
                delay_seconds = min(15 * (2 ** (attempt - 1)), 60)
                print(f"Retrying in {delay_seconds} seconds")
                time.sleep(delay_seconds)

    raise RuntimeError(
        f"Unable to fetch valid Google Scholar data after {max_attempts} attempts"
    ) from last_error


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch Google Scholar citation data")
    parser.add_argument("--fetch-once", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--output-dir", type=Path, default=RESULTS_DIR, help=argparse.SUPPRESS)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.fetch_once:
        fetch_once(args.output_dir)
    else:
        fetch_with_retries()


if __name__ == "__main__":
    main()
