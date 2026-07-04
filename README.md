# PlanetEarthing

PlanetEarthing is a living research repo for careful human-plant interaction experiments. The first study is **Pet the Plant**, a skeptical, sensor-rich test of whether plant physiological signals differ during interactions with a familiar human versus unfamiliar humans after controlling for mechanical, thermal, chemical, acoustic, and schedule confounds.

The project is intentionally bold, but the claims stay modest until the data earn more. Current evidence strongly supports plant responses to touch, wounding, light, humidity, chemistry, and other stimuli. It does **not** yet establish that plants recognize familiar humans or respond to human emotion or intent. This repo is built to test that question without smuggling the answer into the design.

## Current Status

- Repo initialized: 2026-07-04
- Study stage: design and preregistration draft
- Primary experiment: `experiments/pet-the-plant`
- Claim posture: exploratory until a preregistered multi-plant cohort replicates

## Start Here

- [Fact check](docs/research/fact-check.md)
- [Literature map](docs/research/literature-map.md)
- [Preregistration draft](docs/protocols/preregistration.md)
- [Experimental protocol](docs/protocols/experimental-protocol.md)
- [Sensor suite](docs/protocols/sensor-suite.md)
- [Statistical analysis plan](docs/protocols/statistical-analysis-plan.md)
- [Data management plan](docs/protocols/data-management-plan.md)
- [Roadmap](ROADMAP.md)

## First Study: Pet the Plant

Research question:

> Do plant sensor signatures differ between standardized interactions from a familiar host and matched interactions from unfamiliar humans, after controlling for pressure, timing, microclimate, VOCs, voice/audio, and other measurable confounds?

Primary design stance:

- A single plant can validate instrumentation, but cannot support a general biological claim.
- The confirmatory study needs multiple plants, randomized blocks, sham/object controls, pressure-instrumented touch, blind analysis, and leakage-resistant machine learning.
- The strongest possible result would be a reproducible plant-level effect that persists after confound-only models fail and after sessions are held out by plant, date, and stranger identity.

## Repo Layout

```text
docs/
  research/      Evidence, fact checks, source register
  protocols/     Preregistration, sensor, analysis, and data plans
  specs/         Data dictionary, hardware notes, session checklists
  governance/    Living-repo practices and claim standards
experiments/
  pet-the-plant/ First experiment package
src/
  planetearthing/ Small analysis helpers for session validation and features
tests/           Unit tests for analysis helpers
data/            Local, ignored raw/processed data placeholders
outputs/         Local, ignored generated reports/figures
```

## Development

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
PYTHONPATH=src python3 -m planetearthing.cli --help
```

The package is intentionally small for now. Its job is to encode stable conventions early, not to pretend the analysis is finished before real pilot data exists.

## Claim Discipline

Use these labels throughout the repo:

- **Supported**: replicated or broadly accepted in plant physiology.
- **Plausible but unproven**: compatible with known biology, but not demonstrated for this specific setting.
- **Exploratory**: worth testing, not suitable for public claims.
- **Unsupported**: contradicted by controlled evidence or lacking reproducible support.

## Privacy And Ethics

This study records humans through video/audio, pressure gloves, and possibly human VOC-related signals. Use explicit consent, participant IDs, restricted raw media storage, and de-identified analysis exports. If run through an institution, submit for ethics or IRB review before recruitment.
