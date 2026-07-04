# Phase 0 Instrumentation Validation

Version: 0.1.0  
Status: ready to execute when hardware exists

## Purpose

Phase 0 proves that the sensor stack, metadata, event markers, and analysis pipeline work before any host-versus-stranger sessions are interpreted.

No biological claim may be made from Phase 0.

## Required Inputs

- Selected species: `Solanum lycopersicum cv. Micro-Tom`
- At least one acclimated plant.
- Surface electrical channel.
- Pressure/touch channel or calibrated force proxy.
- Leaf-adjacent temperature/RH/CO2/light.
- Event marker for interaction start/stop.
- Fixed camera view.
- Session metadata JSON using the project schema.

## Validation Blocks

### Block A: Electronics Baseline

Goal:

Quantify electronic noise and drift independent of the plant.

Sessions:

- 3 dummy-load sessions.
- 30 minutes per session.
- No plant connected.

Pass criteria:

- no unlogged dropouts,
- timestamp monotonicity,
- stable sample interval,
- no large unassigned step changes.

### Block B: Plant Baseline

Goal:

Quantify plant-attached baseline drift with no human interaction.

Sessions:

- 3 no-touch baseline sessions per plant.
- Minimum 30 minutes per session.

Pass criteria:

- electrode impedance logged before and after,
- no room entry during marked quiet window,
- microclimate data complete,
- electrical stream aligns with metadata timestamps.

### Block C: Mechanical Artifact Test

Goal:

Estimate signal contamination from touch mechanics.

Sessions:

- 3 `OBJECT_TOUCH` sessions per plant.
- Same target duration and contact path planned for human sessions.
- Pressure/touch channel required.

Pass criteria:

- force profile repeatable enough to define tolerance,
- contact start/stop visible in pressure channel,
- no electrode/cable contact visible in video.

### Block D: Human Procedure Rehearsal

Goal:

Test script timing, operator workflow, video scoring, and metadata capture without interpreting biological differences.

Sessions:

- 2 human rehearsals with non-study labels.
- Participant IDs may be synthetic if no real participant is used.

Pass criteria:

- exact script read inside the 60 second window,
- event markers correct,
- metadata complete,
- video can verify hand path and accidental contact.

## Phase 0 Exit Criteria

Phase 0 is complete only when:

- all required channels produce readable files,
- metadata validates with `planetearthing validate-metadata`,
- at least one feature table is generated from synthetic or demo data,
- baseline drift and dropouts are documented,
- pressure/touch tolerance is defined,
- failure modes are recorded in the calibration report.

## Required Output

Create a Phase 0 report using:

- [calibration-report-template.md](../specs/calibration-report-template.md)

Store public, de-identified summaries under:

```text
outputs/
```

Do not commit raw video, raw audio, participant identifiers, or unreviewed raw sensor streams from real human sessions.

