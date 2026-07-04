from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

from .features import summarize_response
from .schema import validate_session_metadata


def validate_metadata(path: Path) -> int:
    with path.open("r", encoding="utf-8") as handle:
        metadata = json.load(handle)
    errors = validate_session_metadata(metadata)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"valid metadata: {path}")
    return 0


def summarize_csv(path: Path, time_key: str, value_key: str) -> int:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    summary = summarize_response(rows, time_key=time_key, value_key=value_key)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="planetearthing")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate-metadata")
    validate.add_argument("path", type=Path)

    summarize = subparsers.add_parser("summarize-csv")
    summarize.add_argument("path", type=Path)
    summarize.add_argument("--time-key", default="time_s")
    summarize.add_argument("--value-key", default="value")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "validate-metadata":
        return validate_metadata(args.path)
    if args.command == "summarize-csv":
        return summarize_csv(args.path, args.time_key, args.value_key)

    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

