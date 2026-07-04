# Species Selection

Version: 0.1.0  
Decision status: selected for Phase 0 and pilot planning

## Selected Species

Primary species:

```text
Solanum lycopersicum cv. Micro-Tom
```

Plain name:

```text
Micro-Tom tomato
```

## Rationale

Micro-Tom tomato is selected because it balances practicality and scientific relevance:

- Tomato is represented in plant bioacoustics work where stressed plants emitted ultrasonic airborne sounds under dehydration and cutting conditions.
- Micro-Tom is compact, short-cycle, and widely used as a tomato model system.
- The plant is small enough for repeated indoor chamber work, camera framing, and replicated cohorts.
- Tomato leaves and stems can support non-invasive surface observation better than very small model plants.
- Tomato VOC, trichome, water-stress, and physiology literature is richer than for many ornamental houseplants.

This selection does **not** assume that tomato can distinguish humans. It only makes the first controlled instrumentation and pilot work practical.

## Evidence Used

- Micro-Tom is a recognized compact tomato cultivar and has been genetically and physiologically characterized as a dwarf tomato model.
- Tomato was one of the species used in the plant-stress sound work by Khait et al. 2023.
- The broader electrophysiology literature supports measuring plant electrical responses after tactile or damaging stimuli, but does not specifically prove person-level discrimination.

Primary species reference:

- Marti et al. 2006, *Journal of Experimental Botany*, DOI: `10.1093/jxb/erj154`

## Inclusion Criteria

Use plants that meet all criteria:

- same seed source or documented source lot,
- same cultivar label,
- same sowing date window,
- no visible disease or pest damage,
- comparable height and leaf count at sensor installation,
- no flowering/fruiting mismatch across the cohort unless explicitly included as a covariate,
- acclimated to the chamber for at least 14 days.

## Exclusion Criteria

Exclude or replace plants before study start if they show:

- visible disease,
- pest infestation,
- severe mechanical damage,
- unstable potting medium,
- growth outside cohort range,
- sensor attachment failure during stabilization,
- repeated wilting under standard watering.

## Cohort Recommendation

Phase 0 instrumentation demo:

- 1 to 2 Micro-Tom plants.
- Purpose: hardware, data shape, drift, and artifact testing only.
- No biological host-versus-stranger claim allowed.

Pilot cohort:

- Minimum 6 Micro-Tom plants.
- Purpose: estimate variance, failure modes, and power requirements.

Confirmatory cohort:

- Starting planning target: 24 plants across 3 independent cohorts of 8 plants.
- Final size must be recalculated from pilot variance.

## Fallback Species

If Micro-Tom is unavailable:

1. Use another compact tomato cultivar with documented cultivar and source.
2. Use a standard tomato cultivar only if the chamber, lighting, and camera setup can support the plant size.
3. Do not switch to an unrelated houseplant without rewriting the evidence rationale and pilot design.

## Decision Log Entry

Add this decision to `docs/governance/decisions.md` whenever the first real plant is procured:

```text
Date:
Decision: Use Solanum lycopersicum cv. Micro-Tom for Phase 0.
Source lot:
Reason:
Deviations:
```
