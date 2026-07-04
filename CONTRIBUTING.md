# Contributing

Planet_Earthing welcomes careful skepticism. Contributions should make the experiment easier to falsify, easier to replicate, easier to audit, or easier for a newcomer to run safely.

## Ways To Help

- Improve the literature map with high-quality sources.
- Challenge weak claims and propose better controls.
- Improve protocol clarity, session templates, or data schemas.
- Add hardware notes and calibration procedures.
- Improve analysis code, tests, or validation scripts.
- Review privacy, consent, and data-release practices.
- Translate complex research ideas into clearer public-facing docs.

## Ground Rules

- Be precise, kind, and evidence-oriented.
- Prefer falsifiable claims over persuasive claims.
- Keep human participant privacy central.
- Do not present exploratory results as proof.
- Do not add raw participant media, consent forms, full names, or identifiable data.

## Local Setup

```bash
git clone https://github.com/llMr-Sweetll/Planet_Earthing.git
cd Planet_Earthing
PYTHONPATH=src python3 -m unittest discover -s tests
PYTHONPATH=src python3 -m planetearthing.cli --help
```

No package install is required for the current lightweight helper code. If future dependencies are added, update `pyproject.toml` and this section in the same pull request.

## Workflow

1. Check existing issues before starting.
2. Open an issue for new research claims, hardware changes, or protocol changes.
3. Create a branch named `docs/...`, `research/...`, `hardware/...`, `analysis/...`, or `protocol/...`.
4. Keep pull requests focused.
5. Run validation before opening the pull request.
6. Include sources for evidence changes.

Suggested commands:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
python3 -m json.tool experiments/pet-the-plant/session_template.json >/dev/null
python3 -m json.tool experiments/pet-the-plant/analysis_config.json >/dev/null
PYTHONPATH=src python3 -m planetearthing.cli validate-metadata experiments/pet-the-plant/session_template.json
rg -nP "[^\\x00-\\x7F]" .
```

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

## Pull Request Checklist

- [ ] The change has a clear reason.
- [ ] The claim label is correct: supported, plausible but unproven, exploratory, unsupported, or superseded.
- [ ] Sources are linked for evidence changes.
- [ ] Protocol or schema version impact is noted.
- [ ] Privacy-sensitive data are not included.
- [ ] Tests and validation commands pass, or failures are explained.

## Review Standard

Reviewers should ask:

- Does this make the project more testable?
- Does it reduce confounding or overclaiming?
- Does it preserve participant privacy?
- Is the documentation clear enough for an independent team to reproduce?
