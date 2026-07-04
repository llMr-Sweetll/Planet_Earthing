# Project Plan

Version: 0.1.0  
Status: public working plan

## Mission

Planet_Earthing exists to turn unusual human-plant interaction questions into careful, falsifiable, reproducible experiments.

The first project, Pet the Plant, asks whether plant-derived sensor data differ between familiar-host and novel-stranger interactions under strong controls. The expected standard is not "prove the weird thing." The standard is "make the answer trustworthy."

## Workstreams

| Workstream | Goal | Current owner model | Main docs |
|---|---|---|---|
| Evidence | Keep claims aligned with literature | Open contributors, maintainer review | `docs/research/` |
| Protocol | Make the experiment reproducible | Issue-driven changes | `docs/protocols/` |
| Hardware | Specify and validate sensors | Hardware contributors | `docs/specs/hardware-bom.md`, `docs/protocols/sensor-suite.md` |
| Data | Protect privacy and standardize schemas | Maintainer review required | `docs/specs/data-dictionary.md`, `docs/protocols/data-management-plan.md` |
| Analysis | Build leakage-resistant analysis | Code review and tests | `src/`, `tests/`, statistical plan |
| Community | Keep public work useful and respectful | Maintainers plus contributors | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` |

## Milestones

### M0: Public Repo Ready

Done when:

- repository is public,
- MIT license is present,
- README states project status, current evidence, non-claims, and reproduction commands,
- contributing docs require evidence-ledger updates for scientific claims,
- CI passes across supported Python versions,
- link checking is available,
- protocol packet release workflow is available,
- issue templates exist,
- roadmap and project plan exist.

### M1: Instrumentation Demo Ready

Done when:

- primary species is chosen,
- minimum sensor stack is selected,
- calibration checklist is complete,
- synthetic data example exists,
- feature extraction works on synthetic data,
- one non-human object-touch demo can be recorded.

### M2: Pilot Study Ready

Done when:

- pilot cohort size is chosen,
- consent language is drafted,
- randomization plan is generated,
- metadata schema is frozen,
- blinded-label workflow is tested,
- failure/exclusion rules are dry-run on demo sessions.

### M3: Confirmatory Study Ready

Done when:

- pilot variance informs power analysis,
- preregistration is frozen and tagged,
- analysis code is locked,
- data storage and privacy workflow is tested,
- all operators can run the checklist independently.

### M4: Replication Ready

Done when:

- materials are sufficient for another team to reproduce,
- protocol deviations are tracked,
- de-identified derived data and code are release-ready,
- negative controls are reported alongside primary results.

## Issue Labels

Recommended labels:

- `evidence`
- `protocol`
- `hardware`
- `analysis`
- `data`
- `privacy`
- `documentation`
- `good first issue`
- `needs source`
- `claim-review`
- `blocked`

## Decision Flow

Small edits:

- Fix directly in a pull request.
- Mention validation in the PR body.

Scientific claims:

- Open an evidence claim issue.
- Add or update an evidence-ledger entry with source, status, supports, and does-not-support fields.
- Add sources and limitations in prose docs.
- Update claim label if needed.

Protocol changes:

- Open a research task issue.
- Explain the confound or reproducibility problem.
- Update affected templates.
- Add a decision log entry for major changes.

Data/privacy changes:

- Require maintainer review.
- Treat human participant protection as a release blocker.

## Definition Of Done

A task is done when:

- the repo file that future contributors will read has been updated,
- tests or validation commands pass where relevant,
- sources are linked for claims,
- privacy implications are considered,
- uncertainty is still visible.

## Public Communication Rule

Use this phrase until stronger evidence exists:

> We are testing for familiarity-associated plant signal differences.

Do not use:

> This project has demonstrated plant recognition of people.
