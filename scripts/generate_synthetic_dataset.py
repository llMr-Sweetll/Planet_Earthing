from __future__ import annotations

import argparse
import csv
import json
import math
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path


CONDITIONS = [
    "HOST_TOUCH_VOICE",
    "NOVEL_STRANGER_TOUCH_VOICE",
    "OBJECT_TOUCH",
    "NO_TOUCH_BASELINE",
]


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def condition_pulse(condition: str, time_s: int) -> float:
    if condition == "NO_TOUCH_BASELINE":
        return 0.0
    if not 0 <= time_s < 60:
        return 0.0

    envelope = math.exp(-((time_s - 20.0) ** 2) / 450.0)
    if condition == "HOST_TOUCH_VOICE":
        return 0.22 * envelope
    if condition == "NOVEL_STRANGER_TOUCH_VOICE":
        return 0.12 * envelope
    if condition == "OBJECT_TOUCH":
        return 0.08 * envelope
    return 0.0


def generate_session(
    *,
    output_dir: Path,
    session_index: int,
    condition: str,
    rng: random.Random,
) -> dict[str, object]:
    session_id = f"SYN{session_index:03d}"
    plant_id = "SYN-P001"
    start = datetime(2026, 8, 1, 9, 0, tzinfo=timezone(timedelta(hours=5, minutes=30)))
    scheduled = start + timedelta(days=session_index - 1)
    session_dir = output_dir / session_id

    electrical_rows: list[dict[str, object]] = []
    pressure_rows: list[dict[str, object]] = []
    microclimate_rows: list[dict[str, object]] = []

    baseline_offset = rng.uniform(-0.04, 0.04)
    for time_s in range(-300, 301):
        slow_drift = 0.00008 * time_s
        noise = rng.gauss(0.0, 0.018)
        value = baseline_offset + slow_drift + condition_pulse(condition, time_s) + noise
        electrical_rows.append(
            {
                "time_s": time_s,
                "channel_id": "E1",
                "value": round(value, 6),
                "quality_flag": "PASS",
            }
        )

        force = 0.0
        if condition in {"HOST_TOUCH_VOICE", "NOVEL_STRANGER_TOUCH_VOICE", "OBJECT_TOUCH"}:
            if 0 <= time_s < 60:
                target = 0.45 if condition != "OBJECT_TOUCH" else 0.42
                force = max(0.0, rng.gauss(target, 0.035))
        pressure_rows.append(
            {
                "time_s": time_s,
                "sensor_id": "F1",
                "force_n": round(force, 5),
                "contact": bool(force > 0),
            }
        )

        co2_bump = 18.0 if condition in {"HOST_TOUCH_VOICE", "NOVEL_STRANGER_TOUCH_VOICE"} and 0 <= time_s < 90 else 0.0
        microclimate_rows.append(
            {
                "time_s": time_s,
                "leaf_temp_c": round(24.0 + rng.gauss(0, 0.03), 3),
                "air_temp_c": round(24.1 + rng.gauss(0, 0.03), 3),
                "relative_humidity_pct": round(55.0 + rng.gauss(0, 0.2), 3),
                "co2_ppm": round(420.0 + co2_bump + rng.gauss(0, 1.5), 3),
                "light_umol_m2_s": round(180.0 + rng.gauss(0, 1.0), 3),
            }
        )

    write_csv(
        session_dir / "electrical.csv",
        ["time_s", "channel_id", "value", "quality_flag"],
        electrical_rows,
    )
    write_csv(
        session_dir / "pressure.csv",
        ["time_s", "sensor_id", "force_n", "contact"],
        pressure_rows,
    )
    write_csv(
        session_dir / "microclimate.csv",
        [
            "time_s",
            "leaf_temp_c",
            "air_temp_c",
            "relative_humidity_pct",
            "co2_ppm",
            "light_umol_m2_s",
        ],
        microclimate_rows,
    )

    metadata = {
        "session_id": session_id,
        "cohort_id": "SYN-C01",
        "plant_id": plant_id,
        "condition_code": condition,
        "blind_label": f"SYN-B{session_index:03d}",
        "scheduled_start_iso": scheduled.isoformat(),
        "actual_start_iso": scheduled.isoformat(),
        "operator_id": "SYN-OP001",
        "participant_id": "NONE" if condition in {"NO_TOUCH_BASELINE", "OBJECT_TOUCH"} else f"SYN-H{session_index:03d}",
        "protocol_version": "0.1.0",
        "randomization_block": "SYN-W01",
        "pressure_glove_file": "pressure.csv",
        "electrical_file": "electrical.csv",
        "vibration_file": "",
        "microclimate_file": "microclimate.csv",
        "audio_video_file": "",
        "soil_moisture_pre": 0.31,
        "soil_moisture_post": 0.31,
        "watered_within_24h": False,
        "electrode_impedance_pre": 12500,
        "electrode_impedance_post": 12600,
        "quality_flag": "PASS",
        "failure_reason": "",
        "notes": "Synthetic demo data; not empirical.",
    }
    with (session_dir / "metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2, sort_keys=True)
        handle.write("\n")

    return metadata


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("data/examples/synthetic_pet_the_plant"))
    parser.add_argument("--seed", type=int, default=20260704)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    metadata_rows = [
        generate_session(
            output_dir=args.output_dir,
            session_index=index,
            condition=condition,
            rng=rng,
        )
        for index, condition in enumerate(CONDITIONS, start=1)
    ]
    write_csv(
        args.output_dir / "sessions.csv",
        [
            "session_id",
            "cohort_id",
            "plant_id",
            "condition_code",
            "blind_label",
            "scheduled_start_iso",
            "actual_start_iso",
            "operator_id",
            "participant_id",
            "protocol_version",
            "randomization_block",
            "quality_flag",
            "notes",
        ],
        [
            {
                key: row[key]
                for key in [
                    "session_id",
                    "cohort_id",
                    "plant_id",
                    "condition_code",
                    "blind_label",
                    "scheduled_start_iso",
                    "actual_start_iso",
                    "operator_id",
                    "participant_id",
                    "protocol_version",
                    "randomization_block",
                    "quality_flag",
                    "notes",
                ]
            }
            for row in metadata_rows
        ],
    )
    print(f"wrote synthetic dataset to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

