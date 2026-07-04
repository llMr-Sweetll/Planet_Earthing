# Replication Plan

Version: 0.1.0

## Goal

An effect is not considered robust until it replicates across independent plants, cohorts, and operators under the same preregistered analysis.

## Replication Tiers

### Tier 1: Internal Technical Replication

- Same plant species.
- Same room and sensor stack.
- Different plant individuals.
- Confirms that the hardware and analysis can reproduce the direction of effect.

### Tier 2: Internal Biological Replication

- Same species and protocol.
- New cohort, new plants, partially new participants.
- Confirms that the result is not tied to one plant or one stranger pool.

### Tier 3: External Replication

- Different site or independently assembled sensor stack.
- Same preregistered feature definitions.
- Confirms that the result is not lab-specific.

## Minimum Reporting For Each Replication

- cohort ID and dates,
- plant source and cultivar,
- environmental settings,
- sensor versions,
- participant count,
- session counts by condition,
- exclusions and reasons,
- primary contrast estimate,
- confidence interval,
- ML holdout performance,
- confound-only model performance,
- deviations from protocol.

## Failure Handling

Replication failure is informative. Do not bury it. Update the evidence label:

- one positive cohort: exploratory,
- positive plus one internal replication: plausible but unproven,
- three independent successful cohorts: supported for that species/protocol only,
- mixed outcomes: unresolved.

