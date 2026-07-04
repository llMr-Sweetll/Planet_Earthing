# Preregistration Draft

Version: 0.1.0  
Status: draft, not frozen  
Study: Pet the Plant  
Parent project: PlanetEarthing  
Created: 2026-07-04

## Research Question

Do plant physiological signals differ between standardized interactions from a familiar human and matched interactions from unfamiliar humans after controlling for mechanical, thermal, chemical, acoustic, microclimate, and schedule confounds?

## Current Evidence Stance

This study is exploratory until a multi-plant preregistered cohort replicates. Plant signaling after touch and stress is well supported. Familiar-human discrimination is not established.

## Hypotheses

Primary null hypothesis:

> H0: After controlling for measured pressure, gesture, voice/audio, microclimate, time of day, soil moisture, and drift, plant sensor features do not differ between familiar-host and novel-stranger sessions.

Primary alternative hypothesis:

> H1: Plant sensor features differ between familiar-host and novel-stranger sessions after those controls.

Secondary hypotheses:

- Host-associated response magnitude changes over the study period, consistent with habituation, sensitization, or slow drift.
- A classifier using only plant-derived sensor channels can identify host versus novel-stranger test sessions above chance under grouped holdout validation.
- Any classifier advantage remains when confound channels are excluded and when a confound-only model performs worse.

## Operational Definitions

- **Host**: a designated person assigned to a plant who completes a defined familiarization exposure schedule before analyzed test sessions.
- **Repeated non-host**: a second person who repeats standardized interactions but does not provide care. This helps separate "known individual" from "caretaker/host."
- **Novel stranger**: a person with no prior interaction with the plant and no earlier presence in the test room during that plant's study.
- **Object touch**: an inert standardized applicator that matches pressure, contact area, stroke count, and duration.
- **Robot touch**: a motorized touch apparatus if available. If not available, object touch is the required mechanical control.
- **No-touch baseline**: full sensor run with no human in the room during the interaction window.

## Study Phases

### Phase 0: Instrumentation Demo

- One plant may be used to validate hardware and file conventions.
- No biological claim may be made from Phase 0.
- Use this phase to estimate drift, artifacts, sampling rates, and minimum viable sensor suite.

### Phase 1: Pilot Cohort

- Recommended: at least 6 plants of the same species and cultivar.
- Duration: 4 to 6 weeks.
- Goal: estimate variance components and failure modes.
- Outcome: revised power analysis and frozen confirmatory protocol.

### Phase 2: Confirmatory Cohort

- Recommended starting target: 24 plants across 3 independent cohorts of 8 plants each.
- Duration: up to 6 months after acclimation.
- The exact sample size must be recalculated from pilot variance before freezing.

## Conditions

| Code | Condition | Primary purpose |
|---|---|---|
| `HOST_TOUCH_VOICE` | Host touches and reads script for 60 seconds | Primary familiar condition |
| `REPEATED_NONHOST_TOUCH_VOICE` | Repeated non-host touches and reads same script | Separates host/caretaker from repeated person exposure |
| `NOVEL_STRANGER_TOUCH_VOICE` | New stranger touches and reads same script | Primary unfamiliar condition |
| `VOICE_PLAYBACK_ONLY` | Host/stranger voice recording played with no person present | Separates voice from touch and human presence |
| `OBJECT_TOUCH` | Inert object matches touch protocol | Mechanical artifact control |
| `ROBOT_TOUCH` | Motorized actuator matches touch protocol | Preferred mechanical control if available |
| `NO_TOUCH_BASELINE` | Sensors run, no human present | Drift and baseline control |

## Primary Outcome

Predefined multimodal feature vector extracted from the 5 minute baseline, 60 second interaction, and 10 minute recovery windows:

- Electrical: peak absolute change, area under curve, latency, spike count, spectral power, entropy, slope, recovery time.
- Vibration: RMS energy, peak frequency, event count, spectral centroid.
- VOC/e-nose: baseline-corrected sensor deltas, response latency, drift-corrected principal components.
- Water status: sap-flow or less-invasive proxy response if validated for the species.
- Microclimate: leaf-adjacent temperature, relative humidity, CO2, and light as covariates, not plant-response outcomes.

## Primary Statistical Contrast

`HOST_TOUCH_VOICE` versus `NOVEL_STRANGER_TOUCH_VOICE`, adjusted for:

- touch pressure and pressure variance,
- contact duration and stroke count,
- session day and time,
- plant ID,
- person ID,
- room temperature, humidity, CO2, light,
- soil moisture,
- recent watering/fertilization,
- sensor drift and electrode impedance.

## Success Criteria

The original success criteria are retained as aspirational thresholds, but interpreted at the plant/cohort level:

- Corrected `p < 0.01` for primary features or a preregistered multivariate model.
- Effect size equivalent to Cohen's `d > 0.8` on held-out plant/session aggregates, not only on autocorrelated row-level samples.
- Plant-only classifier AUC `> 0.85` on grouped holdout data.
- Permutation-label test `p < 0.01`.
- Effect direction replicates in 3 independent cohorts.
- Confound-only model does not explain the result.

## Exclusion Rules

Exclude a session before unblinding if:

- sensor stream missing more than 20 percent of the baseline or response window,
- pressure glove failed or contact duration deviated by more than 10 percent,
- participant used wrong script or nonstandard gesture,
- room entry/exit timing violated the protocol,
- watering, pruning, pest treatment, or sensor maintenance occurred inside the exclusion window,
- video verification shows accidental extra touch, leaf damage, or plant movement unrelated to the protocol.

Do not exclude because the signal looks inconvenient.

## Blinding

- Raw session condition names are replaced with blind labels before feature extraction.
- Video reviewers score pressure/gesture protocol adherence without seeing plant signal plots.
- Analysts lock feature extraction and model selection before condition labels are revealed.

## Confirmatory Claim Rule

The phrase "plant recognition of familiar humans" may not be used in public results unless:

1. the primary contrast succeeds,
2. confound-only and mechanical-control analyses fail to explain it,
3. the effect replicates across cohorts,
4. alternative explanations are discussed plainly.

Until then, use "familiarity-associated signal difference."

