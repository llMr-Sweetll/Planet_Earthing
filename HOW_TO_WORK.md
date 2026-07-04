# How To Work In Planet_Earthing

This guide explains the day-to-day workflow for contributors.

## 1. Understand The Project Posture

Planet_Earthing is open source and open research, but it is not a claim machine. The first experiment, Pet the Plant, tests an exploratory hypothesis:

> Can plant-derived sensor data distinguish familiar-host sessions from novel-stranger sessions after strong controls?

The repo should make that question easier to answer, including if the answer is no.

## 2. Set Up Locally

```bash
git clone https://github.com/llMr-Sweetll/Planet_Earthing.git
cd Planet_Earthing
PYTHONPATH=src python3 -m unittest discover -s tests
PYTHONPATH=src python3 -m planetearthing.cli --help
```

## 3. Pick The Right Work Type

Use these paths:

| Work type | Start with | Update |
|---|---|---|
| Evidence or claim | GitHub evidence claim issue | `docs/research/`, `docs/governance/claim-ladder.md` |
| Protocol design | GitHub research task issue | `docs/protocols/`, `experiments/pet-the-plant/` |
| Hardware or sensors | GitHub research task issue | `docs/specs/hardware-bom.md`, `docs/protocols/sensor-suite.md` |
| Analysis code | GitHub research task issue | `src/`, `tests/`, `docs/protocols/statistical-analysis-plan.md` |
| Data schema | GitHub research task issue | `docs/specs/data-dictionary.md`, templates |
| Public project docs | Pull request | `README.md`, `CONTRIBUTING.md`, `HOW_TO_WORK.md` |

## 4. Branch Naming

Use focused branch names:

```text
research/add-touch-response-sources
protocol/refine-randomization
hardware/add-pressure-glove-options
analysis/add-feature-extractor
docs/improve-quickstart
```

## 5. Change Rules

Before preregistration is frozen:

- improve protocol freely,
- record major decisions,
- cite evidence,
- keep claim labels current.

After preregistration is frozen:

- separate confirmatory changes from exploratory changes,
- record deviations,
- never rewrite history to make a post-hoc decision look planned.

## 6. Validation Commands

Run these before committing:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
python3 -m json.tool experiments/pet-the-plant/session_template.json >/dev/null
python3 -m json.tool experiments/pet-the-plant/analysis_config.json >/dev/null
PYTHONPATH=src python3 -m planetearthing.cli validate-metadata experiments/pet-the-plant/session_template.json
rg -nP "[^\\x00-\\x7F]" .
```

The ASCII scan keeps files portable. Use non-ASCII only when there is a clear reason.

## 7. How To Add A Source

1. Prefer peer-reviewed sources, official datasets, or primary technical documentation.
2. Add the source to the relevant research doc.
3. Add a BibTeX entry to `docs/research/source-register.bib` when appropriate.
4. State the limitation or alternative explanation.
5. Update the claim label if the source changes the evidence posture.

## 8. How To Add A Sensor

1. Explain what response or confound the sensor measures.
2. Add it to `docs/protocols/sensor-suite.md`.
3. Add hardware notes to `docs/specs/hardware-bom.md`.
4. Add metadata fields to `docs/specs/data-dictionary.md`.
5. Add calibration and failure rules.
6. Update analysis plans only if the sensor becomes part of a predefined outcome.

## 9. How To Change The Protocol

1. Open a research task issue.
2. Describe the problem with the current protocol.
3. Update the protocol doc and any templates it affects.
4. Add an entry to `docs/governance/decisions.md` for major changes.
5. Note whether the change affects preregistration.

## 10. How To Handle Data

Do not commit:

- raw participant video,
- raw participant audio,
- full names,
- consent forms,
- identifiable VOC/session traces,
- private sensor streams from human sessions.

Do commit:

- schemas,
- synthetic examples,
- de-identified feature tables when release-approved,
- manifests and checksums,
- analysis code.

## 11. Pull Request Shape

A good pull request says:

- what changed,
- why it matters,
- what evidence supports it,
- what validation was run,
- what remains uncertain.

