#!/usr/bin/env python3
"""Validate the central curriculum manifest and local document links.

The manifest uses a small, predictable YAML subset. This validator reads only
the fields needed for repository integrity checks and avoids external packages.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "manifest" / "sequences.yml"
README = ROOT / "README.md"
SEQUENCE_DIR = ROOT / "docs" / "sequences"
EXPECTED_IDS = {f"{index:02d}" for index in range(13)}
REQUIRED_FIELDS = {
    "id",
    "title",
    "repoName",
    "repoPath",
    "guideBranch",
    "implementationBranch",
    "answerBranch",
    "sequenceDoc",
    "visualLabPath",
    "status",
}
README_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


@dataclass
class Issue:
    level: str
    path: str
    reason: str
    hint: str


@dataclass
class Result:
    name: str
    issues: list[Issue] = field(default_factory=list)

    @property
    def has_failures(self) -> bool:
        return any(issue.level == "FAIL" for issue in self.issues)

    @property
    def has_warnings(self) -> bool:
        return any(issue.level == "WARN" for issue in self.issues)


def strip_yaml_value(raw: str) -> str:
    value = raw.strip()
    if value == "null":
        return ""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def relative_display(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def add_issue(result: Result, level: str, path: Path, reason: str, hint: str) -> None:
    result.issues.append(Issue(level, relative_display(path), reason, hint))


def parse_manifest() -> list[dict[str, str]]:
    if not MANIFEST.exists():
        return []

    sequences: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    field_pattern = re.compile(r"^\s{4}([A-Za-z][A-Za-z0-9]*):\s*(.*)$")

    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if line.startswith("  - id:"):
            if current:
                sequences.append(current)
            current = {"id": strip_yaml_value(line.split(":", 1)[1])}
            continue

        if current is None:
            continue

        match = field_pattern.match(line)
        if match:
            key, value = match.groups()
            current[key] = strip_yaml_value(value)

    if current:
        sequences.append(current)

    return sequences


def validate_manifest_exists(result: Result) -> None:
    if not MANIFEST.exists():
        add_issue(
            result,
            "FAIL",
            MANIFEST,
            "docs/manifest/sequences.yml is missing",
            "중앙 manifest를 복구하거나 docs/manifest/sequences.yml 경로에 생성합니다.",
        )


def validate_sequences(result: Result, sequences: list[dict[str, str]]) -> None:
    by_id: dict[str, dict[str, str]] = {}
    for sequence in sequences:
        sequence_id = sequence.get("id", "")
        if sequence_id in by_id:
            add_issue(
                result,
                "FAIL",
                MANIFEST,
                f"duplicate sequence id: {sequence_id}",
                "각 시퀀스 id는 한 번만 정의합니다.",
            )
        by_id[sequence_id] = sequence

        missing_fields = sorted(REQUIRED_FIELDS - set(sequence))
        if missing_fields:
            add_issue(
                result,
                "FAIL",
                MANIFEST,
                f"sequence {sequence_id or '<unknown>'} is missing fields: {', '.join(missing_fields)}",
                "manifest 필수 필드를 채워 CI가 문서와 브랜치 기준을 검증할 수 있게 합니다.",
            )

    missing_ids = sorted(EXPECTED_IDS - set(by_id))
    extra_ids = sorted(set(by_id) - EXPECTED_IDS)
    if missing_ids:
        add_issue(
            result,
            "FAIL",
            MANIFEST,
            f"manifest is missing sequence ids: {', '.join(missing_ids)}",
            "시퀀스 00부터 12까지 모두 manifest에 포함합니다.",
        )
    if extra_ids:
        add_issue(
            result,
            "WARN",
            MANIFEST,
            f"manifest has unexpected sequence ids: {', '.join(extra_ids)}",
            "새 시퀀스가 필요한 경우 커리큘럼 범위 변경을 먼저 합의합니다.",
        )

    for sequence_id in sorted(EXPECTED_IDS):
        sequence = by_id.get(sequence_id)
        if not sequence:
            continue

        expected_implementation = f"{sequence_id}-implementation"
        expected_answer = f"{sequence_id}-answer"
        if sequence.get("implementationBranch") != expected_implementation:
            add_issue(
                result,
                "FAIL",
                MANIFEST,
                f"sequence {sequence_id} implementationBranch is {sequence.get('implementationBranch')!r}",
                f"implementationBranch는 {expected_implementation}이어야 합니다.",
            )
        if sequence.get("answerBranch") != expected_answer:
            add_issue(
                result,
                "FAIL",
                MANIFEST,
                f"sequence {sequence_id} answerBranch is {sequence.get('answerBranch')!r}",
                f"answerBranch는 {expected_answer}이어야 합니다.",
            )
        if sequence.get("guideBranch") != "main":
            add_issue(
                result,
                "FAIL",
                MANIFEST,
                f"sequence {sequence_id} guideBranch is {sequence.get('guideBranch')!r}",
                "토픽 레포의 가이드 브랜치는 main으로 고정합니다.",
            )

        sequence_doc = sequence.get("sequenceDoc", "")
        if not sequence_doc:
            continue
        sequence_path = ROOT / sequence_doc
        if not sequence_path.exists():
            add_issue(
                result,
                "FAIL",
                sequence_path,
                f"sequence {sequence_id} sequenceDoc path does not exist",
                "manifest의 sequenceDoc를 실제 docs/sequences 문서 경로와 맞춥니다.",
            )


def validate_sequence_docs(result: Result) -> None:
    if not SEQUENCE_DIR.exists():
        add_issue(
            result,
            "FAIL",
            SEQUENCE_DIR,
            "docs/sequences directory is missing",
            "시퀀스 문서를 docs/sequences 아래에 유지합니다.",
        )
        return

    present_ids = {
        match.group(1)
        for path in SEQUENCE_DIR.glob("*.md")
        if (match := re.match(r"^(\d{2})-", path.name))
    }
    missing_ids = sorted(EXPECTED_IDS - present_ids)
    if missing_ids:
        add_issue(
            result,
            "FAIL",
            SEQUENCE_DIR,
            f"docs/sequences is missing documents for: {', '.join(missing_ids)}",
            "각 시퀀스 문서는 파일명 앞에 00~12 번호를 유지합니다.",
        )


def normalize_readme_link(raw_link: str) -> str | None:
    link = raw_link.strip()
    if not link or link.startswith("#"):
        return None
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", link):
        return None

    link = link.split("#", 1)[0]
    if not link:
        return None

    if len(link) >= 2 and link[0] == "<" and link[-1] == ">":
        link = link[1:-1]
    return unquote(link)


def validate_readme_links(result: Result) -> None:
    if not README.exists():
        add_issue(
            result,
            "FAIL",
            README,
            "README.md is missing",
            "중앙 README를 복구합니다.",
        )
        return

    for line_number, line in enumerate(README.read_text(encoding="utf-8").splitlines(), start=1):
        for match in README_LINK_PATTERN.finditer(line):
            normalized = normalize_readme_link(match.group(1))
            if not normalized:
                continue
            target = (README.parent / normalized).resolve()
            if ROOT not in target.parents and target != ROOT:
                add_issue(
                    result,
                    "WARN",
                    README,
                    f"README link on line {line_number} points outside the repository: {match.group(1)}",
                    "중앙 README의 로컬 링크는 가능하면 레포 내부 파일을 가리키게 합니다.",
                )
                continue
            if not target.exists():
                add_issue(
                    result,
                    "FAIL",
                    README,
                    f"README link on line {line_number} is broken: {match.group(1)}",
                    "링크 경로를 실제 파일 위치와 맞춥니다.",
                )


def validate_no_root_visualizer(result: Result) -> None:
    root_index = ROOT / "docs" / "index.html"
    if root_index.exists():
        add_issue(
            result,
            "FAIL",
            root_index,
            "root docs/index.html exists",
            "중앙 레포에는 Visual Lab 구현 파일을 만들지 않습니다.",
        )


def validate() -> list[Result]:
    manifest_result = Result("manifest")
    docs_result = Result("docs")
    readme_result = Result("readme")
    root_result = Result("root")

    validate_manifest_exists(manifest_result)
    sequences = parse_manifest()
    if sequences:
        validate_sequences(manifest_result, sequences)

    validate_sequence_docs(docs_result)
    validate_readme_links(readme_result)
    validate_no_root_visualizer(root_result)

    return [manifest_result, docs_result, readme_result, root_result]


def print_results(results: list[Result]) -> int:
    issue_count = sum(len(result.issues) for result in results)
    warning_groups = sum(1 for result in results if result.has_warnings)
    has_failures = any(result.has_failures for result in results)
    status = "FAIL" if has_failures else "PASS"
    print(f"{status}: {len(results)} check group(s), {issue_count} issue(s), {warning_groups} warning group(s)")
    print()

    for result in results:
        group_status = "FAIL" if result.has_failures else "WARN" if result.has_warnings else "PASS"
        print(f"[{group_status}] {result.name}")
        if not result.issues:
            print("  - OK")
        for issue in result.issues:
            print(f"  - {issue.level}: {issue.path}")
            print(f"    reason: {issue.reason}")
            print(f"    hint: {issue.hint}")
        print()

    return 1 if has_failures else 0


def main() -> int:
    return print_results(validate())


if __name__ == "__main__":
    sys.exit(main())
