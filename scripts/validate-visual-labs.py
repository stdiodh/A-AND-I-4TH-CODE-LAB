#!/usr/bin/env python3
"""Validate Visual Lab hub and sequence pages across topic subrepositories.

This script intentionally uses only the Python standard library so it can run
in a fresh checkout without package manager setup.
"""

from __future__ import annotations

import configparser
import html.parser
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
GITMODULES = ROOT / ".gitmodules"
MANIFEST = ROOT / "docs" / "manifest" / "sequences.yml"
VISUAL_LAB_DIR = Path("docs/visual-lab")
REQUIRED_HUB_FILES = [
    "index.html",
    "styles.css",
    "visual-lab.js",
    "visual-lab-data.js",
]
HUB_DATA_FIELDS = ["kind", "title", "sequences"]
SEQUENCE_DATA_FIELDS = [
    "kind",
    "sequence",
    "title",
    "goal",
    "problem",
    "actors",
    "flows",
    "codePoints",
]
EXTERNAL_PREFIXES = ("http://", "https://", "//", "data:")
CDN_URL_PATTERN = re.compile(
    r"(cdn|unpkg|jsdelivr|cdnjs|bootstrap|tailwind|react|vue|nextjs|next\.js)",
    re.IGNORECASE,
)
REMOTE_CSS_PATTERN = re.compile(r"@import\s+url\((['\"])?https?://", re.IGNORECASE)
ANSWER_EXPOSURE_FAIL = re.compile(
    r"(sourceAnswerBranch|answerBranch|\b\d{2}-answer\b|git\s+(checkout|switch)\s+\S*answer)",
    re.IGNORECASE,
)


@dataclass
class Issue:
    level: str
    path: str
    reason: str
    hint: str


@dataclass
class RepoResult:
    name: str
    path: Path
    statuses: set[str] = field(default_factory=set)
    sequences: list[dict[str, str]] = field(default_factory=list)
    issues: list[Issue] = field(default_factory=list)

    @property
    def has_failures(self) -> bool:
        return any(issue.level == "FAIL" for issue in self.issues)

    @property
    def has_warnings(self) -> bool:
        return any(issue.level == "WARN" for issue in self.issues)


class AssetParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.scripts: list[str] = []
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {name.lower(): value or "" for name, value in attrs}
        if tag == "script" and "src" in attr:
            self.scripts.append(attr["src"])
        elif tag == "link" and "href" in attr:
            self.links.append(attr["href"])


def strip_yaml_value(raw: str) -> str:
    value = raw.strip()
    if value == "null":
        return ""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_manifest() -> list[dict[str, str]]:
    if not MANIFEST.exists():
        return []

    sequences: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    key_pattern = re.compile(r"^\s{4}([A-Za-z][A-Za-z0-9]*):\s*(.*)$")

    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if line.startswith("  - id:"):
            if current:
                sequences.append(current)
            current = {"id": strip_yaml_value(line.split(":", 1)[1])}
            continue

        if current is None:
            continue

        match = key_pattern.match(line)
        if match:
            key, value = match.groups()
            current[key] = strip_yaml_value(value)

    if current:
        sequences.append(current)

    return sequences


def parse_gitmodules() -> dict[str, Path]:
    if not GITMODULES.exists():
        return {}

    parser = configparser.ConfigParser()
    parser.read(GITMODULES, encoding="utf-8")

    modules: dict[str, Path] = {}
    for section in parser.sections():
        name_match = re.match(r'submodule\s+"(.+)"', section)
        name = name_match.group(1) if name_match else section
        path = parser.get(section, "path", fallback=name)
        modules[name] = Path(path)
    return modules


def relative_display(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def add_issue(result: RepoResult, level: str, path: Path, reason: str, hint: str) -> None:
    result.issues.append(Issue(level, relative_display(path), reason, hint))


def is_relative_asset(value: str) -> bool:
    value = value.strip()
    return bool(value) and not value.startswith(EXTERNAL_PREFIXES) and not value.startswith("/")


def data_file_to_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None

    content = path.read_text(encoding="utf-8")
    match = re.search(r"window\.visualLabData\s*=\s*(\{.*\})\s*;\s*$", content, re.DOTALL)
    if not match:
        return None

    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return None


def has_field(content: str, field_name: str) -> bool:
    return bool(re.search(rf"['\"]?{re.escape(field_name)}['\"]?\s*:", content))


def validate_root(result: RepoResult) -> None:
    root_index = ROOT / "docs" / "index.html"
    if root_index.exists():
        add_issue(
            result,
            "FAIL",
            root_index,
            "central docs/index.html exists",
            "Visual Lab 구현물은 각 서브레포의 docs/visual-lab 아래에 둡니다.",
        )

    root_visualizer = ROOT / "docs" / "visualizer"
    if root_visualizer.exists():
        add_issue(
            result,
            "FAIL",
            root_visualizer,
            "central docs/visualizer exists",
            "루트 레포에는 Visual Lab 구현 디렉터리를 만들지 않습니다.",
        )


def validate_required_hub_files(result: RepoResult) -> bool:
    repo_root = ROOT / result.path
    lab_dir = repo_root / VISUAL_LAB_DIR

    if not repo_root.exists():
        add_issue(
            result,
            "FAIL",
            repo_root,
            "subrepository path is missing locally",
            "서브모듈을 초기화하거나 manifest의 repoPath를 확인합니다.",
        )
        return False

    all_present = True
    for filename in REQUIRED_HUB_FILES:
        path = lab_dir / filename
        if not path.exists():
            all_present = False
            add_issue(
                result,
                "FAIL",
                path,
                f"missing required Visual Lab hub file: {filename}",
                "허브 구조는 index.html, styles.css, visual-lab.js, visual-lab-data.js를 유지합니다.",
            )

    return all_present


def validate_html_assets(result: RepoResult, path: Path, expected_scripts: set[str], expected_links: set[str]) -> None:
    if not path.exists():
        return

    content = path.read_text(encoding="utf-8")
    parser = AssetParser()
    parser.feed(content)

    for src in parser.scripts:
        if not is_relative_asset(src):
            add_issue(
                result,
                "FAIL",
                path,
                f"script src is not relative: {src}",
                "script src는 같은 Visual Lab 폴더 안의 상대 경로만 사용합니다.",
            )
        if CDN_URL_PATTERN.search(src):
            add_issue(
                result,
                "FAIL",
                path,
                f"script src appears to use a CDN/library: {src}",
                "외부 JS 라이브러리와 CDN을 사용하지 않습니다.",
            )

    for href in parser.links:
        if not is_relative_asset(href):
            add_issue(
                result,
                "FAIL",
                path,
                f"link href is not relative: {href}",
                "link href는 ./styles.css 또는 ../../styles.css처럼 상대 경로로 작성합니다.",
            )
        if CDN_URL_PATTERN.search(href):
            add_issue(
                result,
                "FAIL",
                path,
                f"link href appears to use a CDN/library: {href}",
                "외부 CSS CDN을 사용하지 않습니다.",
            )

    if expected_links and not expected_links.intersection(set(parser.links)):
        add_issue(
            result,
            "FAIL",
            path,
            "styles.css is not linked with the expected relative path",
            f"허용 경로: {', '.join(sorted(expected_links))}",
        )

    missing_scripts = sorted(expected_scripts.difference(set(parser.scripts)))
    if missing_scripts:
        add_issue(
            result,
            "FAIL",
            path,
            f"expected script(s) are missing: {', '.join(missing_scripts)}",
            "데이터 파일을 visual-lab.js보다 먼저 불러옵니다.",
        )


def validate_css_assets(result: RepoResult, path: Path) -> None:
    if not path.exists():
        return

    content = path.read_text(encoding="utf-8")
    if REMOTE_CSS_PATTERN.search(content):
        add_issue(
            result,
            "FAIL",
            path,
            "remote CSS import appears in styles.css",
            "외부 폰트나 CSS CDN import를 사용하지 않습니다.",
        )
    if CDN_URL_PATTERN.search(content) and re.search(r"https?:|//", content):
        add_issue(
            result,
            "FAIL",
            path,
            "external CDN/library URL appears in styles.css",
            "CSS는 로컬 파일과 CSS 기본 기능만 사용합니다.",
        )


def validate_hub_data(result: RepoResult) -> None:
    data_path = ROOT / result.path / VISUAL_LAB_DIR / "visual-lab-data.js"
    if not data_path.exists():
        return

    content = data_path.read_text(encoding="utf-8")
    if not re.search(r"window\.visualLabData\s*=", content):
        add_issue(
            result,
            "FAIL",
            data_path,
            "window.visualLabData assignment is missing",
            "visual-lab-data.js는 window.visualLabData = { ... } 형태로 작성합니다.",
        )
        return

    for field_name in HUB_DATA_FIELDS:
        if not has_field(content, field_name):
            add_issue(
                result,
                "FAIL",
                data_path,
                f"required hub data field is missing: {field_name}",
                "허브 데이터에는 kind, title, sequences를 포함합니다.",
            )

    parsed = data_file_to_json(data_path)
    if parsed:
        if parsed.get("kind") != "hub":
            add_issue(
                result,
                "FAIL",
                data_path,
                "hub data kind is not 'hub'",
                "토픽 레포 main Visual Lab 데이터는 kind: 'hub'로 둡니다.",
            )
        if not parsed.get("sequences"):
            add_issue(
                result,
                "FAIL",
                data_path,
                "hub data has no sequence links",
                "허브에는 이 레포가 담는 시퀀스 목록과 상세 href를 넣습니다.",
            )


def validate_sequence_data(result: RepoResult, sequence: dict[str, str], data_path: Path) -> None:
    if not data_path.exists():
        add_issue(
            result,
            "FAIL",
            data_path,
            "missing sequence Visual Lab data file",
            "각 시퀀스 상세 페이지는 자기 visual-lab-data.js를 가져야 합니다.",
        )
        return

    content = data_path.read_text(encoding="utf-8")
    if not re.search(r"window\.visualLabData\s*=", content):
        add_issue(
            result,
            "FAIL",
            data_path,
            "window.visualLabData assignment is missing",
            "시퀀스 상세 데이터는 window.visualLabData = { ... } 형태로 작성합니다.",
        )

    for field_name in SEQUENCE_DATA_FIELDS:
        if not has_field(content, field_name):
            add_issue(
                result,
                "FAIL",
                data_path,
                f"required sequence data field is missing: {field_name}",
                "상세 데이터에는 kind, sequence, title, goal, problem, actors, flows, codePoints를 포함합니다.",
            )

    parsed = data_file_to_json(data_path)
    if not parsed:
        return

    sequence_id = sequence["id"]
    if parsed.get("kind") != "sequence":
        add_issue(
            result,
            "FAIL",
            data_path,
            "sequence data kind is not 'sequence'",
            "시퀀스 상세 데이터는 kind: 'sequence'로 둡니다.",
        )
    if parsed.get("sequence") != sequence_id:
        add_issue(
            result,
            "FAIL",
            data_path,
            f"sequence id mismatch: expected {sequence_id}, got {parsed.get('sequence')!r}",
            "manifest 시퀀스 번호와 상세 데이터 sequence 값을 맞춥니다.",
        )

    actors = parsed.get("actors") or []
    flows = parsed.get("flows") or []
    code_points = parsed.get("codePoints") or []
    if not isinstance(actors, list) or not actors:
        add_issue(result, "FAIL", data_path, "actors must be a non-empty list", "actor kind 기반 다이어그램을 위해 actors를 선언합니다.")
    if not isinstance(flows, list) or not flows:
        add_issue(result, "FAIL", data_path, "flows must be a non-empty list", "시퀀스 상세는 최소 1개 이상의 flow를 가져야 합니다.")
    if not isinstance(code_points, list) or len(code_points) < 2:
        add_issue(result, "FAIL", data_path, "codePoints must contain at least 2 items", "각 시퀀스에는 최소 2개 이상의 주요 코드 포인트를 넣습니다.")

    for flow in flows if isinstance(flows, list) else []:
        steps = flow.get("steps") if isinstance(flow, dict) else None
        if not isinstance(steps, list) or not (4 <= len(steps) <= 6):
            add_issue(
                result,
                "FAIL",
                data_path,
                f"flow {flow.get('id', '<unknown>') if isinstance(flow, dict) else '<unknown>'} must have 4-6 steps",
                "각 상세 flow는 4-6단계로 제한합니다.",
            )

    for point in code_points if isinstance(code_points, list) else []:
        snippet = point.get("snippet", "") if isinstance(point, dict) else ""
        line_count = len(str(snippet).splitlines())
        if line_count > 20:
            add_issue(
                result,
                "FAIL",
                data_path,
                f"codePoint {point.get('id', '<unknown>')} snippet is too long: {line_count} lines",
                "코드 포인트는 핵심 5-20줄 정도로 제한합니다.",
            )


def validate_answer_exposure(result: RepoResult) -> None:
    lab_dir = ROOT / result.path / VISUAL_LAB_DIR
    if not lab_dir.exists():
        return

    for file_path in sorted(lab_dir.rglob("*")):
        if not file_path.is_file() or file_path.suffix not in {".html", ".css", ".js"}:
            continue
        content = file_path.read_text(encoding="utf-8")
        if ANSWER_EXPOSURE_FAIL.search(content):
            add_issue(
                result,
                "FAIL",
                file_path,
                "answer branch string or answer-oriented metadata appears in Visual Lab",
                "학생용 Visual Lab 화면/데이터에는 정답 브랜치명과 answerBranch류 필드를 넣지 않습니다.",
            )


def validate_repo(result: RepoResult) -> None:
    if not validate_required_hub_files(result):
        return

    lab_dir = ROOT / result.path / VISUAL_LAB_DIR
    validate_html_assets(
        result,
        lab_dir / "index.html",
        expected_scripts={"./visual-lab-data.js", "./visual-lab.js"},
        expected_links={"./styles.css"},
    )
    validate_css_assets(result, lab_dir / "styles.css")
    validate_hub_data(result)

    for sequence in result.sequences:
        sequence_id = sequence["id"]
        sequence_path = sequence.get("visualLabSequencePath") or f"docs/visual-lab/sequences/{sequence_id}/index.html"
        sequence_index = ROOT / result.path / sequence_path
        sequence_data = sequence_index.with_name("visual-lab-data.js")

        if not sequence_index.exists():
            add_issue(
                result,
                "FAIL",
                sequence_index,
                "missing sequence Visual Lab page",
                "manifest의 각 시퀀스는 docs/visual-lab/sequences/NN/index.html을 가져야 합니다.",
            )
        else:
            validate_html_assets(
                result,
                sequence_index,
                expected_scripts={"./visual-lab-data.js", "../../visual-lab.js"},
                expected_links={"../../styles.css"},
            )
        validate_sequence_data(result, sequence, sequence_data)

    validate_answer_exposure(result)


def build_repo_results() -> list[RepoResult]:
    modules = parse_gitmodules()
    sequences = parse_manifest()

    repo_map: dict[str, RepoResult] = {}
    for name, path in modules.items():
        repo_map[str(path)] = RepoResult(name=name, path=path)

    for sequence in sequences:
        repo_path = sequence.get("repoPath") or sequence.get("repoName")
        if not repo_path:
            continue
        result = repo_map.setdefault(
            repo_path,
            RepoResult(name=sequence.get("repoName", repo_path), path=Path(repo_path)),
        )
        status = sequence.get("status")
        if status:
            result.statuses.add(status)
        result.sequences.append(sequence)

    return [repo_map[key] for key in sorted(repo_map)]


def validate() -> list[RepoResult]:
    results = build_repo_results()
    root_result = RepoResult(name="central-root", path=Path("."))
    validate_root(root_result)

    for result in results:
        validate_repo(result)

    if root_result.issues:
        return [root_result, *results]
    return results


def print_results(results: list[RepoResult]) -> int:
    total_failures = sum(1 for result in results if result.has_failures)
    total_warnings = sum(1 for result in results if result.has_warnings)
    total_issues = sum(len(result.issues) for result in results)

    status = "FAIL" if total_failures else "PASS"
    print(f"{status}: {len(results)} repo group(s), {total_issues} issue(s), {total_warnings} warning group(s)")
    print()

    for result in results:
        repo_status = "FAIL" if result.has_failures else "WARN" if result.has_warnings else "PASS"
        status_text = ", ".join(sorted(result.statuses)) if result.statuses else "no manifest status"
        sequence_text = ", ".join(sequence["id"] for sequence in result.sequences) or "-"
        print(f"[{repo_status}] {result.name} ({result.path}) - {status_text} - sequences: {sequence_text}")
        if not result.issues:
            print("  - OK")
        for issue in result.issues:
            print(f"  - {issue.level}: {issue.path}")
            print(f"    reason: {issue.reason}")
            print(f"    hint: {issue.hint}")
        print()

    return 1 if total_failures else 0


def main() -> int:
    return print_results(validate())


if __name__ == "__main__":
    sys.exit(main())
