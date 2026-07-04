# Experimental Protocol

Version: 0.1.0  
Status: draft

## Species Choice

The first confirmatory species should be selected for broad leaves, tolerance of repeated non-damaging touch, stable indoor growth, and compatibility with surface electrodes.

Recommended path:

1. Use tomato or another lab-friendly potted plant for the main sensor-rich study if sap/VOC/bioacoustic channels matter.
2. Use Mimosa pudica only as a positive-control sidecar for visible touch response, not as the main familiarity proof.
3. Do not use a fragile plant for a 6 month repeated-touch protocol.

Record species, cultivar, source, age estimate, pot size, substrate, fertilizer, and acclimation date.

## Environment

Maintain and log:

- Temperature: 24 C +/- 1 C unless species-specific requirements differ.
- Relative humidity: 55 percent +/- 5 percent.
- Light cycle: fixed photoperiod and intensity at canopy height.
- Soil moisture: automated or standardized target range, with watering events logged.
- Airflow: fixed fan/HVAC state during sessions.
- Room access: no unlogged human entry during baseline, interaction, or recovery.

## Acclimation

Before analyzed sessions:

- Acclimate plants to the chamber for at least 14 days.
- Install sensors and allow at least 48 hours of stabilization.
- Record at least 3 no-touch baseline sessions per plant.
- Run pressure/object controls before recruiting novel strangers.

## Session Timeline

Recommended windows:

| Window | Duration | Action |
|---|---:|---|
| Pre-check | 10 min | Confirm sensors, room, plant state, pressure glove calibration |
| Baseline | 5 min minimum | No entry or motion near plant |
| Interaction | 60 sec | Execute assigned condition |
| Exit buffer | 30 sec | Participant exits silently |
| Recovery | 10 min minimum | No entry or motion near plant |
| Post-check | 5 min | Verify data files and checklist |

For slow channels such as VOC and water status, extend baseline and recovery as needed.

## Human Interaction Script

Use the exact same words, pace, and volume target for host, repeated non-host, and novel stranger conditions.

Draft script:

> Hello. I am here for today's session. I will touch your leaves gently for one minute. The room is calm, and the session is beginning now.

Avoid emotional improvisation. The hypothesis concerns familiarity under standard physical conditions, not persuasion.

## Touch Protocol

- Use the same hand position, glove, stroke path, and contact area for all human sessions.
- Target duration: 60 seconds.
- Target contact force: set after pilot, then hold constant within +/- 10 percent.
- Stroke count: set after pilot and log automatically or by video review.
- Do not touch electrodes, cables, pot, soil, or damaged tissue.

## Randomization

Use blocked randomization by plant and time window:

- Balance conditions within each week.
- Avoid long streaks of the same condition.
- Keep test sessions inside a narrow circadian window.
- Randomize stranger assignment while enforcing "no prior plant exposure."

## Controls

Required:

- No-touch baseline.
- Object-touch with matched pressure and duration.
- Human-nearby/no-touch or voice-playback-only.
- Pressure-glove data for every human touch session.
- Video verification of gesture consistency.

Recommended:

- Robot-touch if a repeatable actuator is available.
- Positive-control stimulus on a separate plant.
- Blank VOC chamber runs.
- Electrode dummy load recording to estimate electronic drift.

## Human Participants

Before participation:

- Obtain written consent for audio/video and sensor-derived interaction data.
- Assign a participant ID.
- Record height/handedness only if needed for protocol matching.
- Ask participants to avoid perfume, scented lotion, smoking, and strong foods before sessions if VOC is used.
- Use gloves consistently; if bare-hand touch is scientifically required, document the increased odor/microbiome confound.

## Session Failure Handling

If a session fails:

- Mark it failed in metadata.
- Keep raw files with a failure reason.
- Do not rerun the same condition immediately unless the randomization plan allows replacement.
- Exclude according to preregistered rules only.

## Safety

- Ensure electrical sensors are isolated and low voltage.
- Do not expose participants to unsafe equipment, hot probes, sharp electrodes, or allergenic plants without review.
- If using invasive plant probes, keep a separate instrumented plant or document wound effects.

