from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from planetearthing.features import Window, summarize_response
from planetearthing.schema import validate_session_metadata


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def summarize_pressure(rows: list[dict[str, str]]) -> dict[str, float]:
    interaction = [row for row in rows if 0 <= float(row["time_s"]) < 60]
    forces = [float(row["force_n"]) for row in interaction]
    contact = [force for force in forces if force > 0]
    return {
        "mean_force_n": sum(forces) / len(forces) if forces else 0.0,
        "contact_fraction": len(contact) / len(forces) if forces else 0.0,
        "peak_force_n": max(forces) if forces else 0.0,
    }


def summarize_session(session_dir: Path) -> list[dict[str, object]]:
    metadata_path = session_dir / "metadata.json"
    with metadata_path.open("r", encoding="utf-8") as handle:
        metadata = json.load(handle)
    errors = validate_session_metadata(metadata)
    if errors:
        raise ValueError(f"{metadata_path}: {errors}")

    electrical = read_csv(session_dir / metadata["electrical_file"])
    pressure = read_csv(session_dir / metadata["pressure_glove_file"])

    electrical_summary = summarize_response(
        electrical,
        time_key="time_s",
        value_key="value",
        baseline=Window(-300, 0),
        response=Window(0, 300),
    )
    pressure_summary = summarize_pressure(pressure)

    base = {
        "session_id": metadata["session_id"],
        "plant_id": metadata["plant_id"],
        "blind_label": metadata["blind_label"],
        "condition_code": metadata["condition_code"],
        "quality_flag": metadata["quality_flag"],
    }
    rows: list[dict[str, object]] = []
    for feature_name, feature_value in electrical_summary.items():
        rows.append(
            {
                **base,
                "channel_family": "electrical",
                "feature_name": feature_name,
                "feature_value": "" if feature_value is None else feature_value,
                "window_name": "baseline_to_response",
                "normalization": "baseline_corrected",
            }
        )
    for feature_name, feature_value in pressure_summary.items():
        rows.append(
            {
                **base,
                "channel_family": "pressure",
                "feature_name": feature_name,
                "feature_value": feature_value,
                "window_name": "interaction",
                "normalization": "none",
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=Path("data/examples/synthetic_pet_the_plant"))
    parser.add_argument("--output", type=Path, default=Path("data/examples/synthetic_pet_the_plant/feature_table.csv"))
    args = parser.parse_args()

    all_rows: list[dict[str, object]] = []
    for session_dir in sorted(path for path in args.input_dir.iterdir() if path.is_dir()):
        all_rows.extend(summarize_session(session_dir))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "session_id",
        "plant_id",
        "blind_label",
        "condition_code",
        "channel_family",
        "feature_name",
        "feature_value",
        "window_name",
        "normalization",
        "quality_flag",
    ]
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)
    print(f"wrote {len(all_rows)} feature rows to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

