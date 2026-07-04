# Decision Log

## 2026-07-04: Initialize Planet_Earthing Repo

Decision:

Create a local git repo with Pet the Plant as the first experiment.

Rationale:

The project needs a stable place for evidence, protocol versions, data schemas, code, and claim discipline.

Status:

Accepted.

## 2026-07-04: Publish As Public Open-Source Repo

Decision:

Publish the project on GitHub as `Planet_Earthing` under the MIT License.

Rationale:

The project benefits from public scrutiny, replication, and contributions. MIT keeps reuse simple while the data management plan protects human participant data through separate consent-aware release rules.

Status:

Accepted.

## 2026-07-04: Require Evidence Ledger For Scientific Claims

Decision:

Use `docs/research/evidence-ledger.json` as the source-of-truth matrix for claim status, source type, empirical support, limitations, and design implications.

Rationale:

The README and research docs must not rely on vague statements. A machine-readable evidence ledger lets CI verify that public claims have explicit source boundaries and that the project states when it has no data yet.

Status:

Accepted.

## 2026-07-04: Split Validation Into CI, Link Check, And Protocol Packet Workflows

Decision:

Replace the single `Validate` workflow with:

- `CI` for Python matrix tests and repository evaluation,
- `Link Check` for scheduled/manual/PR documentation link checks,
- `Protocol Packet` for freeze-tag research artifacts.

Rationale:

The project needs both code validation and research-documentation evaluation. Protocol snapshots should be reproducible when preregistration, pilot, or analysis freezes are tagged.

Status:

Accepted.

## 2026-07-04: Treat Familiar-Human Recognition As Exploratory

Decision:

The repo will not treat plant recognition of familiar humans as established background. It will treat it as the hypothesis under test.

Rationale:

Plant response to touch and stress is well supported. Backster-style primary perception claims are not supported by controlled replication, and plant consciousness claims remain outside the working assumptions of this experiment.

Status:

Accepted.

## 2026-07-04: Single Plant Only For Instrumentation

Decision:

An N=1 plant run can be used for instrument validation, but not for confirmatory biological claims.

Rationale:

A single specimen cannot separate condition effects from plant-specific drift, sensor aging, care events, or unmeasured environmental changes.

Status:

Accepted.
