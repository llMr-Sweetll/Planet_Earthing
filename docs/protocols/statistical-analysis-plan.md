# Statistical Analysis Plan

Version: 0.1.0  
Status: draft

## Analysis Principles

- Analyze sessions, plants, and cohorts as structured repeated measures.
- Do not treat time-series rows as independent observations.
- Keep plant-only outcomes separate from human/confound channels.
- Use blind labels until feature extraction and model choices are locked.
- Report null results plainly.

## Preprocessing

For each sensor stream:

1. Validate clock synchronization and event markers.
2. Remove periods marked as sensor failure before unblinding.
3. Align to interaction start and stop.
4. Compute baseline-corrected response windows.
5. Flag but do not silently remove movement, cable, HVAC, watering, and entry/exit artifacts.
6. Export an auditable feature table with one row per session per channel/feature.

## Feature Families

Electrical:

- peak absolute change,
- signed mean shift,
- area under absolute curve,
- latency to threshold crossing,
- spike/event count,
- recovery half-time,
- low-frequency band power,
- entropy or complexity metric.

Vibration:

- RMS energy,
- peak amplitude,
- dominant frequency,
- spectral centroid,
- event count.

VOC/e-nose:

- baseline-corrected channel deltas,
- maximum response,
- response latency,
- drift-corrected principal components.

Water status:

- sap-flow proxy change,
- pot-mass slope,
- leaf temperature change,
- recovery trend.

Confounds:

- mean/peak pressure,
- pressure variance,
- stroke count,
- voice SPL,
- CO2 change,
- temperature/RH/light change,
- time of day,
- day since sensor install,
- day since watering.

## Primary Model

Use a mixed-effects model or Bayesian hierarchical model:

```text
feature ~ condition + pressure_summary + microclimate_summary
        + session_day + time_of_day + soil_moisture
        + (1 | plant_id) + (1 | participant_id) + (1 | cohort_id)
```

If repeated time trends are strong, include autocorrelation or smooth time terms.

Primary contrast:

```text
HOST_TOUCH_VOICE - NOVEL_STRANGER_TOUCH_VOICE
```

Secondary contrasts:

- `HOST_TOUCH_VOICE - REPEATED_NONHOST_TOUCH_VOICE`
- `NOVEL_STRANGER_TOUCH_VOICE - OBJECT_TOUCH`
- `HOST_TOUCH_VOICE - VOICE_PLAYBACK_ONLY`
- condition by study-day interaction for habituation/sensitization.

## Multiplicity

Before confirmatory analysis, freeze:

- the primary feature family,
- the primary time window,
- the correction method.

Default:

- Use Bonferroni for a small predefined primary set.
- Use false discovery rate for exploratory feature families.
- Mark all post-hoc discoveries as exploratory.

## Machine Learning Plan

Goal:

Classify `HOST_TOUCH_VOICE` versus `NOVEL_STRANGER_TOUCH_VOICE` using plant-derived features only.

Rules:

- No video, audio speech identity, pressure glove, participant ID, calendar date, or microclimate-only features in the plant-only model.
- Use nested cross-validation for model selection.
- Use grouped splits by plant, participant, and date block as appropriate.
- Keep a final holdout that includes unseen novel strangers.
- Run permutation-label tests.
- Train a confound-only model separately.
- Report AUC, balanced accuracy, sensitivity, specificity, calibration, and confidence intervals.

Leakage checks:

- Compare against a model trained on shuffled condition labels.
- Compare against row-wise split to show how much leakage would inflate results.
- Test whether model performance survives holding out entire days and entire plants.
- Inspect feature importance for pressure, drift, and microclimate surrogates.

## Interpretation Rules

If statistics are significant but confound-only models also perform well:

> Interpret as unresolved artifact or human-condition confounding.

If plant-only ML succeeds but classical features do not:

> Treat as exploratory until replicated with stronger controls and explainability.

If host response changes over time:

> Distinguish habituation, sensitization, plant aging, sensor drift, seasonal effects, and repeated touch stress.

If all tests are null:

> Report the detectable effect size and which hypotheses the design could meaningfully rule out.

