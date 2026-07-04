from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

from .features import summarize_response
from .randomization import DEFAULT_CONDITIONS, generate_schedule, parse_start_date
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


def write_schedule(
    path: Path,
    plants: str,
    start_date: str,
    weeks: int,
    seed: int,
    cohort_id: str,
) -> int:
    import csv

    rows = generate_schedule(
        plants=[plant.strip() for plant in plants.split(",") if plant.strip()],
        start_date=parse_start_date(start_date),
        weeks=weeks,
        seed=seed,
        cohort_id=cohort_id,
        conditions=DEFAULT_CONDITIONS,
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].__dict__.keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(row.__dict__)
    print(f"wrote {len(rows)} scheduled sessions to {path}")
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

    schedule = subparsers.add_parser("generate-schedule")
    schedule.add_argument("--plants", required=True)
    schedule.add_argument("--start-date", required=True)
    schedule.add_argument("--weeks", type=int, required=True)
    schedule.add_argument("--seed", type=int, required=True)
    schedule.add_argument("--cohort-id", default="C01")
    schedule.add_argument("--output", type=Path, required=True)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "validate-metadata":
        return validate_metadata(args.path)
    if args.command == "summarize-csv":
        return summarize_csv(args.path, args.time_key, args.value_key)
    if args.command == "generate-schedule":
        return write_schedule(
            args.output,
            args.plants,
            args.start_date,
            args.weeks,
            args.seed,
            args.cohort_id,
        )

    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
