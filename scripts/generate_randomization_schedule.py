from __future__ import annotations

import argparse
import csv
from pathlib import Path

from planetearthing.randomization import DEFAULT_CONDITIONS, generate_schedule, parse_start_date


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plants", required=True, help="Comma-separated plant IDs")
    parser.add_argument("--start-date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--weeks", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--cohort-id", default="C01")
    parser.add_argument("--conditions", default=",".join(DEFAULT_CONDITIONS))
    parser.add_argument("--output", type=Path, required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    plants = [plant.strip() for plant in args.plants.split(",") if plant.strip()]
    conditions = [
        condition.strip() for condition in args.conditions.split(",") if condition.strip()
    ]
    rows = generate_schedule(
        plants=plants,
        start_date=parse_start_date(args.start_date),
        weeks=args.weeks,
        seed=args.seed,
        cohort_id=args.cohort_id,
        conditions=conditions,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].__dict__.keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(row.__dict__)

    print(f"wrote {len(rows)} scheduled sessions to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

