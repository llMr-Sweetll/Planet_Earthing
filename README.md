# Planet_Earthing

[![Validate](https://github.com/llMr-Sweetll/Planet_Earthing/actions/workflows/validate.yml/badge.svg)](https://github.com/llMr-Sweetll/Planet_Earthing/actions/workflows/validate.yml)

Planet_Earthing is an open-source, open-research project for careful human-plant interaction experiments. The first study is **Pet the Plant**, a skeptical, sensor-rich test of whether plant physiological signals differ during interactions with a familiar human versus unfamiliar humans after controlling for mechanical, thermal, chemical, acoustic, and schedule confounds.

The project is intentionally bold, but the claims stay modest until the data earn more. Current evidence strongly supports plant responses to touch, wounding, light, humidity, chemistry, and other stimuli. It does **not** yet establish that plants recognize familiar humans or respond to human emotion or intent. This repo is built to test that question without smuggling the answer into the design.

## Open Project Promise

This repository is public by design. Anyone may read, fork, adapt, critique, and contribute to the project under the [MIT License](LICENSE).

Open source does not mean careless data release. Human participant video, audio, consent records, scent/VOC traces, and raw identifiable session data must stay private unless a participant has explicitly consented to public release and the release has been reviewed for privacy.

## Current Status

- Repo initialized: 2026-07-04
- GitHub repo name: `Planet_Earthing`
- Study stage: design and preregistration draft
- Primary experiment: `experiments/pet-the-plant`
- Claim posture: exploratory until a preregistered multi-plant cohort replicates

## Start Here

- [How to work in this repo](HOW_TO_WORK.md)
- [Contributing](CONTRIBUTING.md)
- [Code of conduct](CODE_OF_CONDUCT.md)
- [Fact check](docs/research/fact-check.md)
- [Literature map](docs/research/literature-map.md)
- [Preregistration draft](docs/protocols/preregistration.md)
- [Experimental protocol](docs/protocols/experimental-protocol.md)
- [Sensor suite](docs/protocols/sensor-suite.md)
- [Statistical analysis plan](docs/protocols/statistical-analysis-plan.md)
- [Data management plan](docs/protocols/data-management-plan.md)
- [Roadmap](ROADMAP.md)
- [Project plan](docs/governance/project-plan.md)

## First Study: Pet the Plant

Research question:

> Do plant sensor signatures differ between standardized interactions from a familiar host and matched interactions from unfamiliar humans, after controlling for pressure, timing, microclimate, VOCs, voice/audio, and other measurable confounds?

Primary design stance:

- A single plant can validate instrumentation, but cannot support a general biological claim.
- The confirmatory study needs multiple plants, randomized blocks, sham/object controls, pressure-instrumented touch, blind analysis, and leakage-resistant machine learning.
- The strongest possible result would be a reproducible plant-level effect that persists after confound-only models fail and after sessions are held out by plant, date, and stranger identity.

## Repo Layout

```text
.github/        Issue templates
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

## Quickstart

```bash
git clone https://github.com/llMr-Sweetll/Planet_Earthing.git
cd Planet_Earthing
PYTHONPATH=src python3 -m unittest discover -s tests
PYTHONPATH=src python3 -m planetearthing.cli --help
```

The Python package is intentionally small for now. Its job is to encode stable conventions early, not to pretend the analysis is finished before real pilot data exists.

## How To Contribute

Good contributions make the experiment easier to falsify, replicate, audit, or understand.

1. Read the [fact check](docs/research/fact-check.md) and [claim ladder](docs/governance/claim-ladder.md).
2. Open an issue using the research task or evidence claim template.
3. Work from a focused branch.
4. Update docs, templates, and tests together when behavior changes.
5. Run the validation commands in [HOW_TO_WORK.md](HOW_TO_WORK.md).
6. Open a pull request with a concise explanation of the change and the evidence behind it.

## Claim Discipline

Use these labels throughout the repo:

- **Supported**: replicated or broadly accepted in plant physiology.
- **Plausible but unproven**: compatible with known biology, but not demonstrated for this specific setting.
- **Exploratory**: worth testing, not suitable for public claims.
- **Unsupported**: contradicted by controlled evidence or lacking reproducible support.

## Privacy And Ethics

This study records humans through video/audio, pressure gloves, and possibly human VOC-related signals. Use explicit consent, participant IDs, restricted raw media storage, and de-identified analysis exports. If run through an institution, submit for ethics or IRB review before recruitment.

## License

Original repository code, protocols, and documentation are released under the [MIT License](LICENSE). Future datasets may use separate release terms after participant consent and de-identification review.
