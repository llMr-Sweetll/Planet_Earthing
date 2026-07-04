from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta


DEFAULT_CONDITIONS = [
    "HOST_TOUCH_VOICE",
    "REPEATED_NONHOST_TOUCH_VOICE",
    "NOVEL_STRANGER_TOUCH_VOICE",
    "OBJECT_TOUCH",
    "VOICE_PLAYBACK_ONLY",
    "NO_TOUCH_BASELINE",
]


@dataclass(frozen=True)
class ScheduleRow:
    session_id: str
    cohort_id: str
    plant_id: str
    date_block: str
    scheduled_start_iso: str
    condition_code: str
    blind_label: str
    randomization_block: str


def parse_start_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def make_balanced_week(
    *,
    conditions: list[str],
    rng: random.Random,
    previous_condition: str | None,
) -> list[str]:
    shuffled = list(conditions)
    rng.shuffle(shuffled)
    if previous_condition and len(shuffled) > 1 and shuffled[0] == previous_condition:
        shuffled[0], shuffled[-1] = shuffled[-1], shuffled[0]
    return shuffled


def generate_schedule(
    *,
    plants: list[str],
    start_date: date,
    weeks: int,
    seed: int,
    cohort_id: str = "C01",
    conditions: list[str] | None = None,
    session_time: time = time(9, 0),
    utc_offset: str = "+05:30",
) -> list[ScheduleRow]:
    if weeks < 1:
        raise ValueError("weeks must be >= 1")
    if not plants:
        raise ValueError("at least one plant is required")

    active_conditions = list(conditions or DEFAULT_CONDITIONS)
    rng = random.Random(seed)
    rows: list[ScheduleRow] = []
    blind_counter = 1
    session_counter = 1

    for plant_id in plants:
        previous_condition: str | None = None
        for week_index in range(weeks):
            week_conditions = make_balanced_week(
                conditions=active_conditions,
                rng=rng,
                previous_condition=previous_condition,
            )
            for day_index, condition in enumerate(week_conditions):
                scheduled_date = start_date + timedelta(days=(week_index * 7) + day_index)
                rows.append(
                    ScheduleRow(
                        session_id=f"S{session_counter:04d}",
                        cohort_id=cohort_id,
                        plant_id=plant_id,
                        date_block=f"W{week_index + 1:02d}",
                        scheduled_start_iso=(
                            f"{scheduled_date.isoformat()}T"
                            f"{session_time.strftime('%H:%M:%S')}{utc_offset}"
                        ),
                        condition_code=condition,
                        blind_label=f"B{blind_counter:04d}",
                        randomization_block=f"{plant_id}-W{week_index + 1:02d}",
                    )
                )
                blind_counter += 1
                session_counter += 1
            previous_condition = week_conditions[-1]

    return rows

