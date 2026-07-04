# Contributing

PlanetEarthing welcomes careful skepticism. Contributions should make the experiment easier to falsify, easier to replicate, or easier to audit.

## Evidence Standard

When adding a claim, include:

- What the claim says.
- Whether it is supported, plausible but unproven, exploratory, or unsupported.
- The best source you found.
- The biggest limitation or alternative explanation.

## Design Standard

Prefer controls that can disprove the favorite hypothesis:

- Pressure and contact geometry should be measured, not assumed.
- Session order should be randomized or blocked.
- Analysts should work with blinded condition labels where possible.
- Classifiers must be evaluated with grouped splits that prevent date, plant, and person leakage.

## Data Standard

Do not commit raw participant media, full names, consent forms, or raw sensor streams that include identifiable participant data. Commit schemas, de-identified examples, derived feature tables, and checksums where appropriate.

