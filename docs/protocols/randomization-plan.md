# Randomization Plan

Version: 0.1.0

## Purpose

Randomization prevents condition order, date, and operator expectations from becoming hidden explanations for a host-versus-stranger difference.

## Scope

This plan applies to pilot and confirmatory sessions. Phase 0 instrumentation checks may use fixed order, but they must not be interpreted biologically.

## Condition Set

Default pilot condition set:

```text
HOST_TOUCH_VOICE
REPEATED_NONHOST_TOUCH_VOICE
NOVEL_STRANGER_TOUCH_VOICE
OBJECT_TOUCH
VOICE_PLAYBACK_ONLY
NO_TOUCH_BASELINE
```

`ROBOT_TOUCH` may replace or supplement `OBJECT_TOUCH` when a repeatable actuator exists.

## Blocking

Randomize within each plant and week:

- each condition should appear once per block when feasible,
- avoid repeating the same condition on consecutive sessions for the same plant,
- keep session time of day as constant as possible,
- balance operator assignment if multiple operators exist.

## Blind Labels

Condition labels should be replaced with blind labels before feature extraction:

```text
B001, B002, B003, ...
```

The mapping from blind label to condition must be stored separately from blinded analysis exports.

## Script

Use:

```bash
python3 scripts/generate_randomization_schedule.py \
  --plants P001,P002,P003,P004,P005,P006 \
  --start-date 2026-08-01 \
  --weeks 4 \
  --seed 20260704 \
  --output experiments/pet-the-plant/randomization_schedule_example.csv
```

The example committed to the repo is synthetic and should be regenerated with a fresh seed before real data collection.

