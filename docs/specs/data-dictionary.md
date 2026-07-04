# Data Dictionary

Version: 0.1.0

## Session Metadata

| Field | Required | Type | Example | Notes |
|---|---|---|---|---|
| `session_id` | Yes | string | `S0001` | Unique within project |
| `cohort_id` | Recommended | string | `C01` | Confirmatory cohort or pilot cohort |
| `plant_id` | Yes | string | `P003` | Stable plant ID |
| `condition_code` | Yes | enum | `HOST_TOUCH_VOICE` | See condition codes below |
| `blind_label` | Recommended | string | `B17` | Used for blinded analysis |
| `scheduled_start_iso` | Yes | datetime | `2026-07-04T09:00:00+05:30` | Planned start |
| `actual_start_iso` | Yes | datetime | `2026-07-04T09:00:12+05:30` | Actual event start |
| `operator_id` | Yes | string | `OP001` | Person operating sensors |
| `participant_id` | Yes | string | `H001` | Human condition participant, or `NONE` |
| `protocol_version` | Yes | string | `0.1.0` | Protocol used |
| `randomization_block` | Recommended | string | `W03-B2` | Weekly/block ID |
| `pressure_glove_file` | Recommended | path | `pressure.csv` | Required for human touch |
| `electrical_file` | Recommended | path | `electrical.csv` | Main plant channel |
| `vibration_file` | Optional | path | `vibration.csv` | If used |
| `microclimate_file` | Recommended | path | `microclimate.csv` | Confound channel |
| `audio_video_file` | Recommended | path | `video.mp4` | Restricted storage |
| `soil_moisture_pre` | Recommended | number | `0.31` | Units must be specified |
| `soil_moisture_post` | Recommended | number | `0.31` | Units must be specified |
| `watered_within_24h` | Recommended | boolean | `false` | Care confound |
| `electrode_impedance_pre` | Recommended | number | `12500` | Ohms |
| `electrode_impedance_post` | Recommended | number | `13000` | Ohms |
| `quality_flag` | Recommended | enum | `PASS` | `PASS`, `WARN`, `FAIL` |
| `failure_reason` | Conditional | string | `pressure glove dropout` | Required if `FAIL` |
| `notes` | Optional | string | `leaf brushed cable once` | Keep factual |

## Condition Codes

| Code | Meaning |
|---|---|
| `HOST_TOUCH_VOICE` | Familiar host touches and speaks script |
| `REPEATED_NONHOST_TOUCH_VOICE` | Repeated non-host touches and speaks script |
| `NOVEL_STRANGER_TOUCH_VOICE` | New stranger touches and speaks script |
| `VOICE_PLAYBACK_ONLY` | Recorded script played with no touch |
| `OBJECT_TOUCH` | Inert object touch |
| `ROBOT_TOUCH` | Motorized touch |
| `NO_TOUCH_BASELINE` | No person present |

## Electrical CSV

One row per sample:

| Column | Type | Unit | Notes |
|---|---|---|---|
| `time_s` | number | seconds | Relative to interaction start |
| `channel_id` | string | none | Electrode pair/channel |
| `value` | number | millivolts | Raw or calibrated value |
| `quality_flag` | string | none | Optional per-sample flag |

## Pressure CSV

| Column | Type | Unit | Notes |
|---|---|---|---|
| `time_s` | number | seconds | Relative to interaction start |
| `sensor_id` | string | none | Glove taxel or force channel |
| `force_n` | number | newtons | Calibrated force |
| `contact` | boolean | none | Optional contact detector |

## Microclimate CSV

| Column | Type | Unit | Notes |
|---|---|---|---|
| `time_s` | number | seconds | Relative to interaction start |
| `leaf_temp_c` | number | C | Leaf-adjacent or IR leaf temp |
| `air_temp_c` | number | C | Local air |
| `relative_humidity_pct` | number | percent | Local RH |
| `co2_ppm` | number | ppm | Human breath confound |
| `light_umol_m2_s` | number | umol/m2/s | PAR if available |

## Feature Table

One row per session-feature:

| Column | Type | Notes |
|---|---|---|
| `session_id` | string | Join key |
| `plant_id` | string | Join key |
| `blind_label` | string | Used before unblinding |
| `channel_family` | string | `electrical`, `vibration`, `voc`, etc. |
| `feature_name` | string | Predefined feature |
| `feature_value` | number | Numeric value |
| `window_name` | string | `baseline`, `interaction`, `recovery` |
| `normalization` | string | e.g. `baseline_corrected` |
| `quality_flag` | string | Feature-level quality |

