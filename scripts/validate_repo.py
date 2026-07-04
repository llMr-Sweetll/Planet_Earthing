from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_README_SECTIONS = [
    "## Current Project Status",
    "## Current Evidence",
    "## What Pet The Plant Tests",
    "## CI/CD And Evaluation",
    "## How To Reproduce The Current Repo State",
    "## What This Project Does Not Claim",
]

REQUIRED_WORKFLOWS = [
    ".github/workflows/ci.yml",
    ".github/workflows/link-check.yml",
    ".github/workflows/protocol-packet.yml",
]

ALLOWED_EVIDENCE_STATUSES = {
    "supported",
    "supported-with-limitations",
    "exploratory",
    "unsupported",
    "no-project-data-yet",
}

DISALLOWED_UNQUALIFIED_PHRASES = [
    "we proved plants",
    "we prove plants",
    "we have shown that plants",
    "this proves that plants",
    "the project proves plants",
    "we have shown that plants recognize people",
]

ASCII_IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
ASCII_IGNORED_SUFFIXES = {".pyc"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def run_quiet(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True, stdout=subprocess.DEVNULL)


def validate_readme() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for section in REQUIRED_README_SECTIONS:
        if section not in readme:
            fail(f"README.md is missing section: {section}")
    for evidence_id in ["E001", "E002", "E005", "E007", "E009"]:
        if evidence_id not in readme:
            fail(f"README.md does not cite required evidence id: {evidence_id}")


def validate_evidence_ledger() -> None:
    path = ROOT / "docs/research/evidence-ledger.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    entries = payload.get("entries")
    if not isinstance(entries, list) or not entries:
        fail("evidence ledger must contain non-empty entries list")

    ids: set[str] = set()
    required_fields = {
        "id",
        "claim",
        "status",
        "evidence_type",
        "source_type",
        "species_or_system",
        "source",
        "url",
        "supports",
        "does_not_support",
        "design_implication",
    }

    for entry in entries:
        missing = sorted(field for field in required_fields if not entry.get(field))
        if missing:
            fail(f"evidence entry {entry.get('id', '<missing id>')} missing fields: {missing}")
        evidence_id = entry["id"]
        if evidence_id in ids:
            fail(f"duplicate evidence id: {evidence_id}")
        ids.add(evidence_id)
        if entry["status"] not in ALLOWED_EVIDENCE_STATUSES:
            fail(f"{evidence_id} has invalid status: {entry['status']}")
        if not entry["url"].startswith("https://"):
            fail(f"{evidence_id} url must be https: {entry['url']}")

    statuses = {entry["status"] for entry in entries}
    if "unsupported" not in statuses:
        fail("evidence ledger must include unsupported evidence boundaries")
    if "no-project-data-yet" not in statuses:
        fail("evidence ledger must explicitly state project data status")


def validate_json_templates() -> None:
    run_quiet(["python3", "-m", "json.tool", "experiments/pet-the-plant/session_template.json"])
    run_quiet(["python3", "-m", "json.tool", "experiments/pet-the-plant/analysis_config.json"])
    run_quiet(["python3", "-m", "json.tool", "docs/research/evidence-ledger.json"])


def validate_cli_metadata() -> None:
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"
    subprocess.run(
        [
            "python3",
            "-m",
            "planetearthing.cli",
            "validate-metadata",
            "experiments/pet-the-plant/session_template.json",
        ],
        cwd=ROOT,
        env=env,
        check=True,
    )


def validate_workflows() -> None:
    for workflow in REQUIRED_WORKFLOWS:
        if not (ROOT / workflow).exists():
            fail(f"missing workflow: {workflow}")


def validate_claim_language() -> None:
    checked_paths = [
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and "__pycache__" not in path.parts
    ]
    for path in checked_paths:
        text = path.read_text(encoding="utf-8").lower()
        for phrase in DISALLOWED_UNQUALIFIED_PHRASES:
            if phrase in text:
                fail(f"disallowed unqualified phrase in {path.relative_to(ROOT)}: {phrase}")


def validate_ascii() -> None:
    failures: list[str] = []
    for path in ROOT.rglob("*"):
        if any(part in ASCII_IGNORED_DIRS for part in path.parts) or not path.is_file():
            continue
        if path.suffix in ASCII_IGNORED_SUFFIXES:
            continue
        try:
            path.read_bytes().decode("ascii")
        except UnicodeDecodeError:
            failures.append(str(path.relative_to(ROOT)))
    if failures:
        fail("non-ASCII files:\n" + "\n".join(f"  {item}" for item in failures))


def main() -> int:
    validate_readme()
    validate_evidence_ledger()
    validate_json_templates()
    validate_cli_metadata()
    validate_workflows()
    validate_claim_language()
    validate_ascii()
    print("repository validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
