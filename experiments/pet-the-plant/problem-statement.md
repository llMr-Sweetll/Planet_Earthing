# Detailed Problem Statement: Pet The Plant

## Background

Plants have measurable physiological responses to mechanical stimulation, wounding, abiotic stress, volatile cues, and environmental change. The controversial part is not whether plants signal; they do. The controversial part is whether a plant produces repeatable, person-specific differences when interacting with a familiar human versus unfamiliar humans under matched physical conditions.

## Objective

Determine whether plant-derived sensor signatures differ between standardized familiar-host and novel-stranger interactions after controlling for mechanical, thermal, chemical, acoustic, microclimate, and schedule confounds.

## Primary Research Question

Is there a statistically significant and repeatable difference in plant sensor features between host and novel-stranger sessions under the preregistered protocol?

## Secondary Research Questions

- Does host-associated response magnitude change over time?
- Can a plant-only classifier identify host versus stranger sessions under grouped holdout validation?
- Which features, if any, drive classification?
- Do object-touch, voice-playback, and no-touch controls explain the apparent effect?

## Hypotheses

H0:

No plant-derived feature or feature set differs between host and novel-stranger sessions after adjustment for measured confounds.

H1:

One or more plant-derived feature sets differs between host and novel-stranger sessions after adjustment for measured confounds.

## Success Criteria

- Corrected `p < 0.01` for the preregistered primary contrast.
- Effect size equivalent to `d > 0.8` on plant/session aggregates.
- Plant-only classifier AUC `> 0.85` on grouped holdout sessions.
- Effect replicates across 3 independent cohorts.
- Confound-only and mechanical-control analyses do not explain the result.

## Known Limitations

- Human identity is bundled with pressure, heat, breath, voice, odor, and behavior.
- A single plant cannot prove generality.
- Repeated touch can itself change plant state.
- Sensors can drift over months.
- Positive ML results are vulnerable to leakage.
- Even a real effect would not, by itself, prove sentience or emotion.

## Project Principle

The experiment should be designed so that a clean null result is valuable and publishable.

