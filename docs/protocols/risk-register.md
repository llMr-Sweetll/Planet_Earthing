# Risk Register

Version: 0.1.0

| Risk | Likelihood | Impact | Mitigation |
|---|---:|---:|---|
| Host and strangers touch differently | High | High | Pressure glove, video scoring, object/robot control |
| Classifier learns date, plant drift, or person artifacts | High | High | Grouped holdouts, permutation tests, confound-only model |
| Electrical electrode drift dominates signal | High | High | Stabilization period, impedance logs, dummy channel |
| E-nose learns human odor rather than plant VOCs | High | High | Blanks, airflow control, gloves, scented-product ban, GC-MS validation |
| Sap-flow probe wounds small plant | Medium | High | Make sap flow optional; use pot mass or leaf temperature proxy |
| Single-plant result is overinterpreted | High | High | Label Phase 0 as instrumentation only |
| Participants vary voice volume and timing | Medium | Medium | Script, metronome, SPL logging, voice playback control |
| Environmental micro-changes mimic condition effect | Medium | High | Leaf-adjacent microclimate logging, blocked randomization |
| Video/audio creates privacy obligations | High | High | Consent, ID mapping outside repo, restricted raw media |
| Repeated touch changes plant growth over months | High | Medium | Include time trends, repeated non-host, no-touch plants |
| Watering/fertilizer schedule confounds day effects | Medium | Medium | Automated or logged care schedule; exclusion windows |
| Positive result attracts overclaiming | High | High | Claim discipline and preregistered interpretation rules |

