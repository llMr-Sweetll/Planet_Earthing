# Calibration Report Template

Version: 0.1.0

## Report Metadata

| Field | Value |
|---|---|
| Report ID | |
| Date range | |
| Operator ID | |
| Protocol version | |
| Plant species/cultivar | |
| Plant IDs | |
| Sensor stack version | |

## Sensor Inventory

| Channel | Device/model | Serial/ID | Firmware/software | Calibration method |
|---|---|---|---|---|
| Electrical | | | | |
| Pressure/touch | | | | |
| Microclimate | | | | |
| Camera | | | | |
| Event marker | | | | |

## Electrical Baseline

| Session ID | Dummy/plant | Duration | Sample rate | Dropouts | Drift summary | Pass/fail |
|---|---|---:|---:|---:|---|---|
| | | | | | | |

Notes:

```text

```

## Electrode Impedance

| Session ID | Pre impedance | Post impedance | Change | Notes |
|---|---:|---:|---:|---|
| | | | | |

## Pressure/Touch Calibration

| Check | Target | Observed | Tolerance | Pass/fail |
|---|---:|---:|---:|---|
| Zero force | | | | |
| Known force low | | | | |
| Known force high | | | | |
| 60 sec object touch | | | | |

Recommended derived tolerance:

```text
Mean contact force target:
Allowed deviation:
Allowed contact duration deviation:
Allowed stroke-count deviation:
```

## Microclimate Calibration

| Sensor | Reference | Observed difference | Action |
|---|---|---:|---|
| Temperature | | | |
| RH | | | |
| CO2 | | | |
| Light | | | |

## Timing And Sync

| Device pair | Sync method | Max observed offset | Pass/fail |
|---|---|---:|---|
| Sensor logger/event marker | | | |
| Video/event marker | | | |
| Microclimate/electrical | | | |

## Phase 0 Failures

| Session ID | Failure | Root cause | Corrective action |
|---|---|---|---|
| | | | |

## Phase 0 Decision

Choose one:

- [ ] Ready for pilot scheduling.
- [ ] Repeat Phase 0 after corrective actions.
- [ ] Redesign hardware stack before continuing.

Rationale:

```text

```

