#!/usr/bin/env python3
"""Validate Visual Lab files across topic subrepositories.

This script intentionally uses only the Python standard library so it can run
in a fresh checkout without package manager setup.
"""

from __future__ import annotations

import configparser
import html.parser
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GITMODULES = ROOT / ".gitmodules"
MANIFEST = ROOT / "docs" / "manifest" / "sequences.yml"
VISUAL_LAB_DIR = Path("docs/visual-lab")
REQUIRED_FILES = [
    "index.html",
    "styles.css",
    "visual-lab.js",
    "visual-lab-data.js",
]
DATA_FIELDS = ["sequence", "title", "goal", "flow"]
EXPECTED_LOCAL_ASSETS = {
    "link": {"./styles.css", "styles.css"},
    "script": {"./visual-lab-data.js", "visual-lab-data.js", "./visual-lab.js", "visual-lab.js"},
}
EXTERNAL_PREFIXES = ("http://", "https://", "//", "data:")
CDN_PATTERNS = re.compile(
    r"(cdn|unpkg|jsdelivr|cdnjs|bootstrap|tailwind|react|vue|next)",
    re.IGNORECASE,
)
ANSWER_EXPOSURE_FAIL = re.compile(
    r"(sourceAnswerBranch|answerBranch|\b\d{2}-answer\b|git\s+(checkout|switch)\s+\S*answer)",
    re.IGNORECASE,
)
ANSWER_EXPOSURE_WARN = re.compile(
    r"(\banswer\b|정답\s*코드|@RestController|@Service|@Transactional)",
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
        self.buttons: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {name.lower(): value or "" for name, value in attrs}
        if tag == "script" and "src" in attr:
            self.scripts.append(attr["src"])
        elif tag == "link" and "href" in attr:
            self.links.append(attr["href"])
        elif tag == "button":
            self.buttons.append(attr)


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


def missing_visual_lab_level(result: RepoResult) -> str:
    return "WARN" if result.statuses and result.statuses <= {"planned"} else "FAIL"


def is_relative_asset(value: str) -> bool:
    value = value.strip()
    return bool(value) and not value.startswith(EXTERNAL_PREFIXES) and not value.startswith("/")


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


def validate_required_files(result: RepoResult) -> bool:
    repo_root = ROOT / result.path
    lab_dir = repo_root / VISUAL_LAB_DIR
    level = missing_visual_lab_level(result)

    if not repo_root.exists():
        add_issue(
            result,
            level,
            repo_root,
            "subrepository path is missing locally",
            "서브모듈을 초기화하거나 manifest의 repoPath를 확인합니다.",
        )
        return False

    all_present = True
    for filename in REQUIRED_FILES:
        path = lab_dir / filename
        if not path.exists():
            all_present = False
            add_issue(
                result,
                level,
                path,
                f"missing required Visual Lab file: {filename}",
                "공통 구조는 index.html, styles.css, visual-lab.js, visual-lab-data.js입니다.",
            )

    return all_present


def validate_index_html(result: RepoResult) -> None:
    index_path = ROOT / result.path / VISUAL_LAB_DIR / "index.html"
    if not index_path.exists():
        return

    content = index_path.read_text(encoding="utf-8")
    parser = AssetParser()
    parser.feed(content)

    if CDN_PATTERNS.search(content) and re.search(r"https?:|//", content):
        add_issue(
            result,
            "FAIL",
            index_path,
            "external CDN or library URL appears in index.html",
            "외부 CDN 대신 같은 docs/visual-lab 폴더의 상대 경로 파일만 사용합니다.",
        )

    for src in parser.scripts:
        if not is_relative_asset(src):
            add_issue(
                result,
                "FAIL",
                index_path,
                f"script src is not relative: {src}",
                "script src는 ./visual-lab-data.js처럼 상대 경로로 작성합니다.",
            )
    for href in parser.links:
        if not is_relative_asset(href):
            add_issue(
                result,
                "FAIL",
                index_path,
                f"link href is not relative: {href}",
                "link href는 ./styles.css처럼 상대 경로로 작성합니다.",
            )

    script_set = set(parser.scripts)
    link_set = set(parser.links)
    if not EXPECTED_LOCAL_ASSETS["link"].intersection(link_set):
        add_issue(
            result,
            "FAIL",
            index_path,
            "styles.css is not linked from index.html",
            "index.html에서 ./styles.css를 link로 불러옵니다.",
        )
    if "./visual-lab-data.js" not in script_set and "visual-lab-data.js" not in script_set:
        add_issue(
            result,
            "FAIL",
            index_path,
            "visual-lab-data.js is not loaded from index.html",
            "데이터 파일을 visual-lab.js보다 먼저 script로 불러옵니다.",
        )
    if "./visual-lab.js" not in script_set and "visual-lab.js" not in script_set:
        add_issue(
            result,
            "FAIL",
            index_path,
            "visual-lab.js is not loaded from index.html",
            "공통 렌더러인 ./visual-lab.js를 script로 불러옵니다.",
        )

    for button in parser.buttons:
        if button.get("disabled") or button.get("tabindex") == "-1" or button.get("aria-hidden") == "true":
            add_issue(
                result,
                "WARN",
                index_path,
                "button may not be focusable",
                "버튼은 기본 focus 흐름을 유지하고, 비활성 상태는 JS 상태로 최소화합니다.",
            )


def validate_data_js(result: RepoResult) -> None:
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

    for field_name in DATA_FIELDS:
        if not re.search(rf"\b{re.escape(field_name)}\s*:", content):
            add_issue(
                result,
                "FAIL",
                data_path,
                f"required data field is missing: {field_name}",
                "sequence, title, goal, flow는 최소 필드로 유지합니다.",
            )

    if re.search(r"\bflow\s*:\s*\[\s*\]", content, re.DOTALL):
        add_issue(
            result,
            "WARN",
            data_path,
            "flow is present but empty",
            "최소 1개 이상의 흐름 단계를 넣어 학생이 따라갈 수 있게 합니다.",
        )


def validate_answer_exposure(result: RepoResult) -> None:
    lab_dir = ROOT / result.path / VISUAL_LAB_DIR
    if not lab_dir.exists():
        return

    for file_path in sorted(lab_dir.glob("*")):
        if not file_path.is_file() or file_path.suffix not in {".html", ".css", ".js"}:
            continue
        content = file_path.read_text(encoding="utf-8")
        if ANSWER_EXPOSURE_FAIL.search(content):
            add_issue(
                result,
                "FAIL",
                file_path,
                "answer branch or answer-oriented implementation detail appears in Visual Lab",
                "학생용 Visual Lab에는 정답 브랜치와 구현 상세를 앞세우지 않습니다.",
            )
        elif ANSWER_EXPOSURE_WARN.search(content):
            add_issue(
                result,
                "WARN",
                file_path,
                "possible answer/code detail string appears in Visual Lab",
                "긴 코드 또는 정답 비교 안내는 강사용 문서로 옮기는 것이 안전합니다.",
            )


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

    return [repo_map[key] for key in sorted(repo_map)]


def validate() -> list[RepoResult]:
    results = build_repo_results()
    root_result = RepoResult(name="central-root", path=Path("."))
    validate_root(root_result)

    for result in results:
        validate_required_files(result)
        validate_index_html(result)
        validate_data_js(result)
        validate_answer_exposure(result)

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
        print(f"[{repo_status}] {result.name} ({result.path}) - {status_text}")
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
