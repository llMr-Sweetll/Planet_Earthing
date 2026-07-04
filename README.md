# Planet_Earthing

[![CI](https://github.com/llMr-Sweetll/Planet_Earthing/actions/workflows/ci.yml/badge.svg)](https://github.com/llMr-Sweetll/Planet_Earthing/actions/workflows/ci.yml)
[![Link Check](https://github.com/llMr-Sweetll/Planet_Earthing/actions/workflows/link-check.yml/badge.svg)](https://github.com/llMr-Sweetll/Planet_Earthing/actions/workflows/link-check.yml)
[![Protocol Packet](https://github.com/llMr-Sweetll/Planet_Earthing/actions/workflows/protocol-packet.yml/badge.svg)](https://github.com/llMr-Sweetll/Planet_Earthing/actions/workflows/protocol-packet.yml)

Planet_Earthing is an open-source research repository for designing and auditing controlled human-plant interaction experiments. The first experiment is **Pet the Plant**: a proposed study of whether plant-derived sensor data can distinguish standardized familiar-host sessions from standardized novel-stranger sessions after controlling for touch pressure, voice, heat, CO2, VOCs, timing, room entry, and sensor drift.

This repository is currently a **design, evidence-review, and analysis-infrastructure repo**. It is not yet a results repo.

## Current Project Status

As of 2026-07-04:

- Public repo: [llMr-Sweetll/Planet_Earthing](https://github.com/llMr-Sweetll/Planet_Earthing)
- License: [MIT](LICENSE)
- Study stage: preregistration draft and protocol design
- Empirical Planet_Earthing sessions collected: **0**
- Primary experiment package: [experiments/pet-the-plant](experiments/pet-the-plant)
- Evidence ledger: [docs/research/evidence-ledger.json](docs/research/evidence-ledger.json)
- Claim status for familiar-host versus stranger discrimination: **no project data yet**

## Current Evidence

The project separates external plant-science evidence from claims this repository has not yet tested.

| Evidence ID | Evidence-backed statement | What the evidence does not show |
|---|---|---|
| `E001` | Plant electrophysiological responses can be recorded from multiple species after tactile or damaging stimuli. | It does not show familiar-human recognition or emotional intent detection. |
| `E002` | Brief repeated touch changed potato morphology, volatile emissions, and aphid responses in a controlled experiment. | It does not show person-specific plant discrimination. |
| `E003` | Mechanistic touch-response pathways can regulate plant growth responses. | It does not show that a 60 second human session produces a host-specific signature. |
| `E004` | Wounding can trigger long-distance calcium-based plant defense signaling. | It does not show human recognition or communication. |
| `E005` | Stressed tomato and tobacco plants emitted informative airborne ultrasonic sounds under dehydration or cutting stress. | It does not show that gentle petting or familiar humans cause ultrasonic emissions. |
| `E006` | Electronic noses can discriminate some plant VOC signatures. | It does not show that VOCs recorded during human sessions are plant-only rather than human odor, breath, humidity, or airflow. |
| `E007` | A controlled Backster-style brine-shrimp replication did not find the claimed electrophysiological plant response. | It does not support primary perception as background evidence. |
| `E008` | Animal-like consciousness, pain, emotion, and preference claims are outside this project's working assumptions. | It does not deny measurable plant signaling. |
| `E009` | Planet_Earthing has not yet produced host-versus-stranger empirical results. | It does not support any claim that an effect has been observed here. |

Read the source-backed details in:

- [Evidence summary](docs/research/evidence-summary.md)
- [Evidence ledger JSON](docs/research/evidence-ledger.json)
- [Fact check](docs/research/fact-check.md)
- [Literature map](docs/research/literature-map.md)

## What Pet The Plant Tests

Primary research question:

> Can plant-derived sensor features distinguish `HOST_TOUCH_VOICE` from `NOVEL_STRANGER_TOUCH_VOICE` sessions after measured physical and environmental confounds are controlled?

Primary confirmatory contrast:

```text
HOST_TOUCH_VOICE - NOVEL_STRANGER_TOUCH_VOICE
```

Required controls before any stronger interpretation:

- `NO_TOUCH_BASELINE`
- `OBJECT_TOUCH` or `ROBOT_TOUCH`
- `VOICE_PLAYBACK_ONLY`
- `REPEATED_NONHOST_TOUCH_VOICE`
- pressure-instrumented human touch
- leaf-adjacent temperature, relative humidity, CO2, and light
- audio/video verification of session timing, script, and gesture
- grouped holdout validation by plant, participant, and date block
- confound-only model comparison

The planned measurements are described in [sensor-suite.md](docs/protocols/sensor-suite.md). The statistical rules are in [statistical-analysis-plan.md](docs/protocols/statistical-analysis-plan.md).

## What This Project Does Not Claim

Planet_Earthing does not claim that:

- plants recognize people,
- plants read thoughts,
- plants detect emotional intent,
- plants feel affection, fear, pain, or preference in an animal-like sense,
- a single plant can prove a biological effect,
- a classifier result is meaningful without grouped holdouts and confound checks.

The permitted phrase until strong replicated evidence exists is:

> familiarity-associated plant signal difference

## CI/CD And Evaluation

The repository now has three GitHub Actions workflows:

| Workflow | Trigger | Purpose |
|---|---|---|
| [CI](.github/workflows/ci.yml) | push to `main`, pull request | Runs Python tests on 3.10, 3.11, and 3.12; runs repository evaluation. |
| [Link Check](.github/workflows/link-check.yml) | pull request docs changes, weekly schedule, manual run | Checks README, docs, and evidence-ledger links. |
| [Protocol Packet](.github/workflows/protocol-packet.yml) | manual run, `protocol-v*`, `pilot-freeze-v*`, `analysis-freeze-v*` tags | Builds a reproducible protocol packet artifact and attaches it to freeze-tag releases. |

The repository evaluation script, [scripts/validate_repo.py](scripts/validate_repo.py), checks:

- required README sections,
- required evidence IDs in README,
- evidence-ledger schema and status labels,
- JSON templates,
- session metadata template validity,
- required workflow files,
- disallowed unqualified claim phrases,
- ASCII portability.

## How To Reproduce The Current Repo State

```bash
git clone https://github.com/llMr-Sweetll/Planet_Earthing.git
cd Planet_Earthing
PYTHONPATH=src python3 -m unittest discover -s tests
PYTHONPATH=src python3 scripts/validate_repo.py
PYTHONPATH=src python3 -m planetearthing.cli --help
```

Expected validation output:

```text
valid metadata: experiments/pet-the-plant/session_template.json
repository validation passed
```

## Repository Map

```text
.github/
  workflows/     CI, link checks, protocol packet release workflow
  ISSUE_TEMPLATE/ Research and evidence issue templates
docs/
  research/      Evidence ledger, evidence summary, fact check, literature map
  protocols/     Preregistration, sensor plan, analysis plan, data plan
  specs/         Data dictionary, hardware notes, session checklist
  governance/    Project plan, claim ladder, living-repo rules, decisions
experiments/
  pet-the-plant/ Experiment statement, analysis config, session template
scripts/
  validate_repo.py Repository evaluation script used by CI
src/
  planetearthing/ Metadata validation and feature-summary helpers
tests/           Unit tests
data/            Ignored local data placeholders
outputs/         Ignored generated local outputs
```

## How To Contribute

Good contributions make the experiment easier to falsify, replicate, audit, or understand.

1. Read [HOW_TO_WORK.md](HOW_TO_WORK.md).
2. Check the [evidence summary](docs/research/evidence-summary.md) and [claim ladder](docs/governance/claim-ladder.md).
3. Open a research task or evidence claim issue.
4. Add sources to the evidence ledger when adding scientific claims.
5. Run local validation before opening a pull request.

## Privacy And Ethics

This study design involves human participants, video/audio, pressure traces, possible human VOC traces, and timestamps. Do not commit raw participant media, consent forms, names, or identifiable raw streams. Public data releases must be de-identified, consent-reviewed, and separated from the MIT-licensed repository code/docs.

## License

Original repository code, protocols, and documentation are released under the [MIT License](LICENSE). Future datasets may use separate release terms after participant consent and de-identification review.
