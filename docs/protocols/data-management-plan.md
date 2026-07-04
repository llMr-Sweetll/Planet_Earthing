# Data Management Plan

Version: 0.1.0

## Data Classes

| Class | Examples | Commit to git? |
|---|---|---|
| Public docs | Protocols, schemas, analysis code | Yes |
| Raw plant sensor streams | Electrical CSV, e-nose logs, pressure logs | No by default |
| Human media | Video, audio, consent forms | No |
| De-identified metadata | Session IDs, condition blind labels, plant IDs | Yes if privacy reviewed |
| Derived features | One row per session/feature | Yes after de-identification |
| Final reports | Figures, summaries, preregistered results | Yes |

## Local Folder Convention

```text
data/raw/
  cohort_id/
    plant_id/
      session_id/
        metadata.json
        electrical.csv
        pressure.csv
        microclimate.csv
        video.mp4
data/processed/
  feature_tables/
  quality_flags/
outputs/
  figures/
  reports/
```

Raw media and raw streams are ignored by git. Store them in an encrypted or access-controlled location for real studies.

## File Naming

Use stable IDs, not names:

```text
YYYYMMDD_C01_P003_S014_electrical.csv
YYYYMMDD_C01_P003_S014_metadata.json
```

## Metadata

Every session requires:

- `session_id`
- `plant_id`
- `condition_code`
- `scheduled_start_iso`
- `actual_start_iso`
- `operator_id`
- `participant_id`
- `protocol_version`
- sensor file paths or missing-file flags
- quality flags

See [data dictionary](../specs/data-dictionary.md).

## Privacy

Human participants may be identifiable through:

- video,
- voice,
- hand appearance,
- gait,
- pressure patterns,
- scent/VOC traces,
- timestamps.

Required controls:

- written consent,
- participant ID mapping stored outside the repo,
- raw media access restricted,
- de-identified exports for analysis,
- deletion plan for withdrawal requests,
- no public release of raw human media without explicit consent.

## Integrity

For each session:

- write metadata immediately after acquisition,
- compute checksums for raw files,
- mark failed sessions rather than overwriting them,
- keep sensor firmware/software versions,
- log every manual correction.

## Reproducibility

Each analysis release should include:

- commit hash,
- protocol version,
- raw data manifest with checksums,
- feature extraction script version,
- model configuration,
- blinded and unblinded analysis notebooks or scripts,
- exact exclusion list and reasons.

