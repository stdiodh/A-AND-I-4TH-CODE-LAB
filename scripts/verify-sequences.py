#!/usr/bin/env python3
"""Smoke-check curriculum sequence repositories before class.

The script reads docs/manifest/sequences.yml, checks local subrepository paths,
branches, standard documents, Visual Lab entry points, and run/test command
configuration. Test commands are printed by default and run only with
--run-tests.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "manifest" / "sequences.yml"
REQUIRED_DOCS = [
    "README.md",
    "docs/theory.md",
    "docs/implementation.md",
    "docs/checklist.md",
]
BRANCH_FIELDS = ["guideBranch", "implementationBranch", "answerBranch"]
MANUAL_DEFAULT_BRANCH_IDS = {"01", "12"}


@dataclass
class CheckLine:
    level: str
    message: str


@dataclass
class SequenceResult:
    sequence_id: str
    title: str
    repo_path: str
    lines: list[CheckLine] = field(default_factory=list)

    @property
    def has_failures(self) -> bool:
        return any(line.level == "FAIL" for line in self.lines)

    @property
    def has_warnings(self) -> bool:
        return any(line.level == "WARN" for line in self.lines)

    def add(self, level: str, message: str) -> None:
        self.lines.append(CheckLine(level, message))


def strip_yaml_value(raw: str) -> str | None:
    value = raw.strip()
    if value == "null":
        return None
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_manifest() -> list[dict[str, str | None]]:
    if not MANIFEST.exists():
        raise FileNotFoundError(f"missing manifest: {MANIFEST}")

    sequences: list[dict[str, str | None]] = []
    current: dict[str, str | None] | None = None

    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if line.startswith("  - id:"):
            if current:
                sequences.append(current)
            current = {"id": strip_yaml_value(line.split(":", 1)[1])}
            continue

        if current is None:
            continue

        if not line.startswith("    ") or line.startswith("      "):
            continue

        key, separator, raw_value = line.strip().partition(":")
        if separator:
            current[key] = strip_yaml_value(raw_value)

    if current:
        sequences.append(current)

    return sequences


def path_display(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def run_git(repo: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def branch_exists(repo: Path, branch: str) -> bool:
    refs = [
        f"refs/heads/{branch}",
        f"refs/remotes/origin/{branch}",
    ]
    for ref in refs:
        result = run_git(repo, ["show-ref", "--verify", "--quiet", ref])
        if result.returncode == 0:
            return True
    return False


def check_file(result: SequenceResult, repo: Path, relative_path: str, label: str) -> None:
    path = repo / relative_path
    if path.exists():
        result.add("OK", f"{label}: {relative_path}")
    else:
        result.add("FAIL", f"{label} missing: {path_display(path)}")


def check_command_field(
    result: SequenceResult,
    sequence: dict[str, str | None],
    field_name: str,
) -> str | None:
    if field_name not in sequence:
        result.add("FAIL", f"{field_name} field missing from manifest")
        return None

    value = sequence.get(field_name)
    if value:
        result.add("OK", f"{field_name}: {value}")
    else:
        result.add("INFO", f"{field_name}: null")
    return value


def run_test_command(result: SequenceResult, repo: Path, command: str) -> None:
    result.add("RUN", f"running testCommand: {command}")
    completed = subprocess.run(command, cwd=repo, shell=True, check=False)
    if completed.returncode == 0:
        result.add("OK", f"testCommand passed: {command}")
    else:
        result.add("FAIL", f"testCommand failed ({completed.returncode}): {command}")


def check_sequence(sequence: dict[str, str | None], run_tests: bool) -> SequenceResult:
    sequence_id = str(sequence.get("id") or "<unknown>")
    title = str(sequence.get("title") or "<untitled>")
    repo_path_value = sequence.get("repoPath")
    repo_path = str(repo_path_value or "")
    result = SequenceResult(sequence_id, title, repo_path)

    if not repo_path_value:
        result.add("FAIL", "repoPath field missing or null")
        return result

    repo = ROOT / repo_path
    if repo.exists():
        result.add("OK", f"repoPath exists: {repo_path}")
    else:
        result.add("FAIL", f"repoPath missing: {path_display(repo)}")
        return result

    if not (repo / ".git").exists():
        result.add("WARN", f"repoPath is not a git checkout: {repo_path}")

    for field_name in BRANCH_FIELDS:
        branch = sequence.get(field_name)
        if not branch:
            result.add("FAIL", f"{field_name} field missing or null")
            continue
        if branch_exists(repo, branch):
            result.add("OK", f"{field_name} exists: {branch}")
        else:
            result.add("FAIL", f"{field_name} missing locally/remotely: {branch}")

    for doc in REQUIRED_DOCS:
        check_file(result, repo, doc, "document")

    visual_lab_path = sequence.get("visualLabPath")
    if visual_lab_path:
        check_file(result, repo, visual_lab_path, "visualLabPath")
    else:
        result.add("FAIL", "visualLabPath field missing or null")

    check_command_field(result, sequence, "runCommand")
    test_command = check_command_field(result, sequence, "testCommand")

    if test_command:
        if run_tests:
            run_test_command(result, repo, test_command)
        else:
            result.add("INFO", f"testCommand not run; use --run-tests to execute: {test_command}")

    if sequence_id in MANUAL_DEFAULT_BRANCH_IDS:
        result.add(
            "MANUAL",
            "Check GitHub default branch in GitHub Settings or gh CLI; this script does not call GitHub API.",
        )

    return result


def print_results(results: list[SequenceResult]) -> None:
    for result in results:
        print(f"\n[{result.sequence_id}] {result.title} ({result.repo_path})")
        for line in result.lines:
            print(f"  {line.level}: {line.message}")

    failures = sum(1 for result in results if result.has_failures)
    warnings = sum(1 for result in results if result.has_warnings)
    print("\nSummary")
    print(f"- sequences checked: {len(results)}")
    print(f"- sequences with failures: {failures}")
    print(f"- sequences with warnings: {warnings}")
    print("- manual default branch checks: 01 REST CRUD, 12 Event Driven")


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify sequence repositories before class.")
    parser.add_argument(
        "--run-tests",
        action="store_true",
        help="Run non-null testCommand values. Defaults to printing test commands only.",
    )
    args = parser.parse_args()

    try:
        sequences = parse_manifest()
    except FileNotFoundError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    results = [check_sequence(sequence, args.run_tests) for sequence in sequences]
    print_results(results)

    if any(result.has_failures for result in results):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
