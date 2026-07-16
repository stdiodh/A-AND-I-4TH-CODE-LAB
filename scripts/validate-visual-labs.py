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
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
GITMODULES = ROOT / ".gitmodules"
MANIFEST = ROOT / "docs" / "manifest" / "sequences.yml"
VISUAL_LAB_DIR = Path("docs/visual-lab")
REQUIRED_HUB_FILES = [
    "index.html",
    "styles.css",
    "visual-lab.js",
    "visual-lab-data.js",
    "assets/visual-lab-mark.svg",
    "assets/system-icons.svg",
    "assets/SOURCE.md",
    "assets/LICENSES.md",
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
    "workbench",
]
WORKBENCH_KINDS = {
    "request",
    "request-trace",
    "persistence",
    "gate",
    "auth",
    "trust",
    "test",
    "cache",
    "realtime",
    "runtime",
    "pipeline",
    "refactor",
    "event",
}
WORKBENCH_TONES = {"signal", "blocked", "warning", "recovered"}
SYSTEM_LAYERS = {
    "outside",
    "interface",
    "application",
    "resource",
    "integration",
    "runtime",
}
DIAGRAM_EDGE_KINDS = {
    "request",
    "call",
    "transform",
    "persist",
    "response",
    "failure",
    "event",
    "config",
    "compare",
}
STEP_EFFECT_KINDS = {
    "transfer",
    "transform",
    "persist",
    "gate",
    "return",
    "fanout",
    "verify",
    "preserve",
}
EVIDENCE_SCOPES = {"code", "test", "runtime", "manual", "concept"}
THEORY_CODE_LANGUAGES = {
    "bash",
    "dockerfile",
    "http",
    "java",
    "javascript",
    "json",
    "jsonc",
    "kotlin",
    "properties",
    "shell",
    "sql",
    "yaml",
    "yml",
}
GENERIC_EFFECT_STATE = re.compile(
    r"(?:"
    r"변환 전|변환 완료|확인 전|확인 결과가 명확해짐|반환 결과가 없음|조건 판정 전|조건에서 다음 단계가 중단됨|"
    r"^호출 전 책임:|^호출 후 책임:|^호출자 상태:|^호출자 보유 값:|"
    r"^판정 입력:|^판정 결과:.*후속 변경 차단$|^입력 상태:|^출력 상태:|"
    r"evidence가 아직 관찰되지 않음$|상태가 판정됨$|"
    r"가 돌아와 다음 경로가 이어짐$|입력 재료가 있음$"
    r")"
)
SYSTEM_ICON_NAMES = {
    "person",
    "client",
    "tool",
    "api",
    "service",
    "repository",
    "database",
    "gate",
    "security",
    "token",
    "external",
    "mail",
    "test",
    "fixture",
    "cache",
    "websocket",
    "broker",
    "runtime",
    "artifact",
    "config",
    "pipeline",
    "host",
    "refactor",
    "event",
    "queue",
    "consumer",
    "evidence",
    "memory",
    "handler",
    "response",
}
BRANCH_FIELDS = ["guideBranch", "implementationBranch", "answerBranch"]
EXTERNAL_PREFIXES = ("http://", "https://", "//", "data:")
CDN_URL_PATTERN = re.compile(
    r"(cdn|unpkg|jsdelivr|cdnjs|bootstrap|tailwind|react|vue|nextjs|next\.js)",
    re.IGNORECASE,
)
REMOTE_CSS_PATTERN = re.compile(r"@import\s+url\((['\"])?https?://", re.IGNORECASE)
REMOTE_SVG_VALUE_PATTERN = re.compile(r"(?:https?:)?//|data:", re.IGNORECASE)
RAW_HTML_AMPERSAND = re.compile(r"&(?!#\d+;|#x[0-9A-Fa-f]+;|[A-Za-z][A-Za-z0-9]+;)")
RAW_HTML_AMPERSAND_EXCLUDED_BLOCK = re.compile(
    r"<!--.*?-->|<(script|style)\b[^>]*>.*?</\1\s*>",
    re.IGNORECASE | re.DOTALL,
)
ANSWER_EXPOSURE_FAIL = re.compile(
    r"(sourceAnswerBranch|answerBranch|\b\d{2}-answer\b|git\s+(checkout|switch)\s+\S*answer)",
    re.IGNORECASE,
)
DIAGRAM_DATA_NODE_KIND = re.compile(r"\b(payload|dto|http result|comparison path)\b", re.IGNORECASE)
ENGLISH_META_COPY = re.compile(r'"(?:concept|boundary|label)"\s*:\s*"Verification(?: failure)?"')
MOBILE_VISUAL_WIDTH = 308
FORBIDDEN_VISUAL_LAB_COPY = (
    "관계를 먼저 읽고, 아래에서 한 단계씩 확인합니다.",
)
FORBIDDEN_RENDERER_MARKERS = (
    "sequence-current-detail__payload",
    "sequence-mobile-current__sentence",
    "sequence-step-jump",
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


def normalize_ui_copy(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return re.sub(r"[^0-9A-Za-z가-힣]+", "", value).casefold()


def run_git(repo: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def resolve_branch_ref(repo: Path, branch: str) -> str | None:
    refs = [
        (f"refs/heads/{branch}", branch),
        (f"refs/remotes/origin/{branch}", f"origin/{branch}"),
    ]
    for full_ref, short_ref in refs:
        completed = run_git(repo, ["show-ref", "--verify", "--quiet", full_ref])
        if completed.returncode == 0:
            return short_ref
    return None


def tree_path_exists(repo: Path, ref: str, relative_path: str) -> bool:
    completed = run_git(repo, ["cat-file", "-e", f"{ref}:{relative_path}"])
    return completed.returncode == 0


def is_relative_asset(value: str) -> bool:
    value = value.strip()
    return bool(value) and not value.startswith(EXTERNAL_PREFIXES) and not value.startswith("/")


def validate_data_links(
    result: RepoResult,
    repo_root: Path,
    data_path: Path,
    items: Any,
    field_name: str,
) -> None:
    if not isinstance(items, list):
        add_issue(
            result,
            "FAIL",
            data_path,
            f"{field_name} must be a list",
            f"{field_name}는 href 객체 배열로 작성합니다.",
        )
        return

    resolved_repo = repo_root.resolve()
    for index, item in enumerate(items):
        href = item.get("href") if isinstance(item, dict) else None
        if not isinstance(href, str) or not href.strip():
            add_issue(
                result,
                "FAIL",
                data_path,
                f"{field_name}[{index}] has no href",
                "각 링크 객체에는 비어 있지 않은 상대 href를 넣습니다.",
            )
            continue

        href_value = href.strip()
        parsed = urlsplit(href_value)
        if parsed.scheme or parsed.netloc or href_value.startswith("/") or not parsed.path:
            add_issue(
                result,
                "FAIL",
                data_path,
                f"{field_name}[{index}] href is not a local relative path: {href}",
                "Visual Lab 데이터 링크는 레포 내부 파일을 가리키는 상대 경로로 작성합니다.",
            )
            continue

        target = (data_path.parent / unquote(parsed.path)).resolve()
        try:
            target.relative_to(resolved_repo)
        except ValueError:
            add_issue(
                result,
                "FAIL",
                data_path,
                f"{field_name}[{index}] href escapes the repository: {href}",
                "링크 대상은 현재 토픽 레포 내부에 있어야 합니다.",
            )
            continue

        if not target.exists():
            add_issue(
                result,
                "FAIL",
                data_path,
                f"{field_name}[{index}] href target is missing: {href}",
                "상대 경로와 실제 문서 또는 페이지 위치를 일치시킵니다.",
            )


def validate_theory_reference(
    result: RepoResult,
    repo_root: Path,
    data_path: Path,
    href: Any,
    location: str,
) -> None:
    if not isinstance(href, str) or not href.strip():
        add_issue(result, "FAIL", data_path, f"{location} has no theoryRef", "관련 theory 절의 상대 경로와 안정적인 anchor를 연결합니다.")
        return

    parsed = urlsplit(href.strip())
    if parsed.scheme or parsed.netloc or href.startswith("/") or not parsed.path or not parsed.fragment:
        add_issue(result, "FAIL", data_path, f"{location} theoryRef must be a local path with an anchor", "../../../theory.md#seq-NN-topic 형태로 작성합니다.")
        return

    target = (data_path.parent / unquote(parsed.path)).resolve()
    try:
        target.relative_to(repo_root.resolve())
    except ValueError:
        add_issue(result, "FAIL", data_path, f"{location} theoryRef escapes the repository", "현재 토픽 레포의 theory.md 절만 연결합니다.")
        return

    if not target.exists():
        add_issue(result, "FAIL", data_path, f"{location} theoryRef target is missing: {href}", "상대 경로를 실제 theory.md 위치와 맞춥니다.")
        return

    content = target.read_text(encoding="utf-8")
    fragment = re.escape(unquote(parsed.fragment))
    anchor_match = re.search(rf"\bid\s*=\s*['\"]{fragment}['\"]", content)
    if not anchor_match:
        add_issue(result, "FAIL", data_path, f"{location} theoryRef anchor is missing: #{parsed.fragment}", "theory.md에 같은 id의 명시적 anchor를 둡니다.")

    sequence_match = re.fullmatch(r"seq-(\d{2})", unquote(parsed.fragment))
    if sequence_match and anchor_match:
        sequence_id = sequence_match.group(1)
        next_anchor = re.search(r"<a\s+id=['\"]seq-\d{2}['\"]", content[anchor_match.end() :])
        section_end = anchor_match.end() + next_anchor.start() if next_anchor else len(content)
        section = content[anchor_match.end() : section_end]

        if not re.search(r"```mermaid\s*\n\s*sequenceDiagram\b", section):
            add_issue(result, "FAIL", data_path, f"{location} theory section has no Mermaid sequenceDiagram", f"theory.md의 seq-{sequence_id} 절에 실제 주 경로 sequenceDiagram을 둡니다.")

        if not re.search(r"\|\s*단계\s*\|\s*들어온 것\s*\|\s*한 일\s*\|\s*나간 것 또는 상태\s*\|", section):
            add_issue(result, "FAIL", data_path, f"{location} theory section has no four-column state table", f"theory.md의 seq-{sequence_id} 절에 단계·입력·행동·출력 상태 표를 둡니다.")

        code_blocks = re.findall(r"```([\w-]+)\s*\n(.*?)```", section, flags=re.DOTALL)
        has_short_code = any(
            language.lower() in THEORY_CODE_LANGUAGES
            and 3 <= len([line for line in block.splitlines() if line.strip()]) <= 12
            for language, block in code_blocks
        )
        if not has_short_code:
            add_issue(result, "FAIL", data_path, f"{location} theory section has no 3-12 line code block", f"theory.md의 seq-{sequence_id} 절에 학생 설명 뒤 실제 핵심 코드 3~12줄을 둡니다.")

        backlink = rf"\]\(\./visual-lab/sequences/{sequence_id}/(?:index\.html)?\)"
        if not re.search(backlink, content):
            add_issue(result, "FAIL", data_path, f"{location} theory section has no Visual Lab backlink", f"theory.md의 seq-{sequence_id} 절에서 ./visual-lab/sequences/{sequence_id}/ 로 돌아가는 링크를 제공합니다.")


def canonical_branch_refs(repo: Path, sequence: dict[str, str]) -> dict[str, str]:
    refs: dict[str, str] = {}
    for field_name in BRANCH_FIELDS:
        branch = sequence.get(field_name)
        if branch:
            ref = resolve_branch_ref(repo, branch)
            if ref:
                refs[field_name] = ref
    return refs


def validate_code_point_files(
    result: RepoResult,
    repo_root: Path,
    sequence: dict[str, str],
    data_path: Path,
    code_points: Any,
) -> None:
    if not isinstance(code_points, list):
        return

    branch_refs = canonical_branch_refs(repo_root, sequence)
    if not branch_refs:
        add_issue(
            result,
            "FAIL",
            data_path,
            "cannot validate codePoint files because no canonical branch is available",
            "manifest의 guide, implementation, answer 브랜치를 로컬 또는 origin에서 확인합니다.",
        )
        return

    for index, point in enumerate(code_points):
        snippet = None
        if isinstance(point, dict):
            snippet = point.get("snippet") or point.get("example")
        if not isinstance(snippet, str) or not snippet.strip():
            add_issue(result, "FAIL", data_path, f"codePoints[{index}] has no snippet", "파일 tag 대신 설명 바로 아래에 실제 핵심 코드 3-12줄을 제공합니다.")
        else:
            line_count = len(snippet.strip("\n").splitlines())
            if not 3 <= line_count <= 12:
                add_issue(result, "FAIL", data_path, f"codePoints[{index}] snippet has {line_count} lines", "학생이 현재 판단에 필요한 실제 핵심 코드만 3-12줄로 줄입니다.")

        file_value = point.get("file") if isinstance(point, dict) else None
        if not isinstance(file_value, str) or not file_value.strip():
            add_issue(
                result,
                "FAIL",
                data_path,
                f"codePoints[{index}] has no file path",
                "각 코드 포인트에는 canonical 브랜치에서 확인할 수 있는 file 경로를 넣습니다.",
            )
            continue

        file_path = file_value.strip()
        normalized = PurePosixPath(file_path)
        if file_path.startswith("/") or "\\" in file_path or ".." in normalized.parts:
            add_issue(
                result,
                "FAIL",
                data_path,
                f"codePoints[{index}] file is not a repository-relative path: {file_value}",
                "file은 토픽 레포 루트 기준 POSIX 상대 경로로 작성합니다.",
            )
            continue

        relative_path = normalized.as_posix()
        if relative_path == "." or not any(
            tree_path_exists(repo_root, ref, relative_path) for ref in branch_refs.values()
        ):
            checked = ", ".join(branch_refs.values())
            add_issue(
                result,
                "FAIL",
                data_path,
                f"codePoints[{index}] file is missing from canonical branches: {file_value}",
                f"경로를 수정하거나 canonical 브랜치({checked})의 실제 파일과 맞춥니다.",
            )


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
                "허브 파일과 assets/system-icons.svg, SOURCE.md, LICENSES.md를 유지합니다.",
            )

    return all_present


def validate_html_assets(result: RepoResult, path: Path, expected_scripts: set[str], expected_links: set[str]) -> None:
    if not path.exists():
        return

    content = path.read_text(encoding="utf-8")
    entity_check_content = RAW_HTML_AMPERSAND_EXCLUDED_BLOCK.sub("", content)
    if RAW_HTML_AMPERSAND.search(entity_check_content):
        add_issue(
            result,
            "FAIL",
            path,
            "Visual Lab HTML contains an unescaped ampersand",
            "HTML text와 속성의 &는 &amp;처럼 유효한 character reference로 작성합니다.",
        )
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

    missing_links = sorted(expected_links.difference(set(parser.links)))
    if missing_links:
        add_issue(
            result,
            "FAIL",
            path,
            f"expected link(s) are missing: {', '.join(missing_links)}",
            "공통 stylesheet와 저장소 로컬 brand mark를 올바른 상대 경로로 연결합니다.",
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


def validate_icon_sprite(result: RepoResult, path: Path) -> None:
    if not path.exists():
        return

    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as error:
        add_issue(
            result,
            "FAIL",
            path,
            f"system icon sprite is not valid SVG XML: {error}",
            "로컬 SVG sprite가 브라우저에서 읽히도록 XML 문법을 수정합니다.",
        )
        return

    symbol_ids = {
        element.get("id", "").removeprefix("icon-")
        for element in root.iter()
        if element.tag.endswith("symbol") and element.get("id", "").startswith("icon-")
    }
    missing = sorted(SYSTEM_ICON_NAMES - symbol_ids)
    if missing:
        add_issue(
            result,
            "FAIL",
            path,
            f"system icon sprite is missing symbols: {', '.join(missing)}",
            "semantic diagram이 사용하는 모든 icon-* symbol을 sprite에 포함합니다.",
        )


def validate_asset_metadata(result: RepoResult, path: Path, label: str) -> None:
    if not path.exists():
        return
    content = path.read_text(encoding="utf-8").strip()
    if len(content) < 40:
        add_issue(
            result,
            "FAIL",
            path,
            f"{label} asset metadata is empty or incomplete",
            "SVG의 자체 제작·파생 관계와 사용 조건을 검수 가능한 문장으로 기록합니다.",
        )


def validate_renderable_svg(result: RepoResult, path: Path, purpose: str) -> None:
    if not path.exists():
        add_issue(
            result,
            "FAIL",
            path,
            f"missing {purpose} SVG asset",
            "데이터가 가리키는 저장소 로컬 SVG 파일을 추가합니다.",
        )
        return

    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as error:
        add_issue(
            result,
            "FAIL",
            path,
            f"{purpose} asset is not valid SVG XML: {error}",
            "브라우저가 직접 렌더링할 수 있도록 SVG XML 문법을 수정합니다.",
        )
        return

    if not root.tag.endswith("svg"):
        add_issue(result, "FAIL", path, f"{purpose} asset root is not <svg>", "SVG 파일의 최상위 요소를 <svg>로 작성합니다.")
    view_box = root.get("viewBox")
    if not view_box:
        add_issue(result, "FAIL", path, f"{purpose} asset has no viewBox", "반응형 크기에서도 보이도록 SVG viewBox를 작성합니다.")

    for element in root.iter():
        if element.tag.endswith("script"):
            add_issue(result, "FAIL", path, f"{purpose} asset contains a script", "학습 에셋은 정적 SVG 요소만 사용합니다.")
        for name, value in element.attrib.items():
            if name.endswith("href") and REMOTE_SVG_VALUE_PATTERN.search(value):
                add_issue(result, "FAIL", path, f"{purpose} asset uses an external href: {value}", "SVG 내부 참조도 저장소 로컬 또는 fragment만 사용합니다.")
            if name == "style" and REMOTE_SVG_VALUE_PATTERN.search(value):
                add_issue(result, "FAIL", path, f"{purpose} asset uses an external style URL", "외부 폰트·이미지·스타일 URL을 제거합니다.")

    if purpose.endswith(" visual") and view_box:
        text_nodes = [element for element in root.iter() if element.tag.endswith("text")]
        if text_nodes:
            source = path.read_text(encoding="utf-8")
            font_sizes = [
                float(value)
                for value in re.findall(
                    r"(?:font-size\s*(?::|=)\s*[\"']?\s*|font\s*:[^;{}]*?)([0-9]+(?:\.[0-9]+)?)(?:px)?",
                    source,
                    re.IGNORECASE,
                )
            ]
            try:
                view_box_width = float(view_box.replace(",", " ").split()[2])
            except (IndexError, ValueError):
                view_box_width = 0

            if not font_sizes or view_box_width <= 0:
                add_issue(
                    result,
                    "FAIL",
                    path,
                    "workbench visual text size cannot be verified",
                    "루트 viewBox와 px 기반 font-size를 명시해 모바일에서도 글자 크기를 검증할 수 있게 합니다.",
                )
            else:
                estimated_mobile_size = min(font_sizes) * min(1.0, MOBILE_VISUAL_WIDTH / view_box_width)
                if estimated_mobile_size < 10.5:
                    add_issue(
                        result,
                        "FAIL",
                        path,
                        f"workbench visual text becomes too small on mobile: about {estimated_mobile_size:.1f}px",
                        "관계를 단순화하고 viewBox 폭을 줄이거나 최소 font-size를 키워 390px 화면에서 10.5px 이상으로 표시합니다.",
                    )


def validate_renderer_copy(result: RepoResult, path: Path) -> None:
    if not path.exists():
        return

    source = path.read_text(encoding="utf-8")
    for copy in FORBIDDEN_VISUAL_LAB_COPY:
        if copy in source:
            add_issue(
                result,
                "FAIL",
                path,
                f"renderer contains repeated filler copy: {copy}",
                "경로, 상태 변화 또는 근거처럼 이 화면에서만 전달할 정보로 교체합니다.",
            )
    for marker in FORBIDDEN_RENDERER_MARKERS:
        if marker in source:
            add_issue(
                result,
                "FAIL",
                path,
                f"renderer reintroduces a duplicate current-step surface: {marker}",
                "message, current inspector와 evidence가 각각 route, change와 source 한 역할만 맡도록 유지합니다.",
            )


def resolve_visual_asset(result: RepoResult, data_path: Path, src: str, purpose: str) -> Path | None:
    if not is_relative_asset(src):
        add_issue(result, "FAIL", data_path, f"{purpose} src is not a local relative path: {src}", "../../assets/...처럼 현재 Visual Lab 내부의 상대 경로를 사용합니다.")
        return None

    lab_dir = data_path.parents[2].resolve()
    target = (data_path.parent / unquote(urlsplit(src).path)).resolve()
    try:
        target.relative_to(lab_dir)
    except ValueError:
        add_issue(result, "FAIL", data_path, f"{purpose} src escapes docs/visual-lab: {src}", "설명 에셋은 현재 토픽 레포의 docs/visual-lab/assets 아래에 둡니다.")
        return None
    return target


def validate_visual_definition(
    result: RepoResult,
    data_path: Path,
    visual: Any,
    purpose: str,
) -> None:
    if not isinstance(visual, dict):
        add_issue(
            result,
            "FAIL",
            data_path,
            f"{purpose} must be an object",
            "주제 설명 SVG를 src, alt, caption 문자열로 연결합니다.",
        )
        return

    for field_name in ("src", "alt", "caption"):
        if not isinstance(visual.get(field_name), str) or not visual[field_name].strip():
            add_issue(
                result,
                "FAIL",
                data_path,
                f"{purpose} has no {field_name}",
                "설명 에셋에는 src, 대체 텍스트, 학생용 caption을 모두 작성합니다.",
            )

    src = visual.get("src")
    if not isinstance(src, str) or not src.strip():
        return

    target = resolve_visual_asset(result, data_path, src.strip(), purpose)
    if not target:
        return
    if target.suffix.lower() != ".svg":
        add_issue(
            result,
            "FAIL",
            data_path,
            f"{purpose} is not SVG: {src}",
            "외부 의존 없이 확대 가능한 저장소 로컬 SVG를 사용합니다.",
        )
        return
    validate_renderable_svg(result, target, purpose)


def validate_semantic_workbench(
    result: RepoResult,
    data_path: Path,
    workbench: dict[str, Any],
    code_points: list[Any],
) -> None:
    visual = workbench.get("visual")
    validate_visual_definition(result, data_path, visual, "workbench visual")

    nodes = workbench.get("nodes")
    if not isinstance(nodes, dict) or not nodes:
        add_issue(
            result,
            "FAIL",
            data_path,
            "workbench nodes must be a non-empty object",
            "행동 주체와 책임 경계를 workbench.nodes에 선언합니다.",
        )
        return

    code_point_ids = {
        point.get("id")
        for point in code_points
        if isinstance(point, dict) and isinstance(point.get("id"), str)
    }

    def validate_code_point_ids(value: Any, location: str) -> None:
        if value is None:
            return
        if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
            add_issue(result, "FAIL", data_path, f"{location} codePointIds must be a string list", "기존 codePoints[].id만 배열로 연결합니다.")
            return
        unknown = sorted(set(value) - code_point_ids)
        if unknown:
            add_issue(result, "FAIL", data_path, f"{location} references unknown codePointIds: {', '.join(unknown)}", "codePointIds를 현재 시퀀스의 codePoints[].id와 맞춥니다.")

    for node_id, node in nodes.items():
        if not isinstance(node_id, str) or not node_id.strip() or not isinstance(node, dict):
            add_issue(result, "FAIL", data_path, "workbench nodes contain an invalid entry", "node key와 값 객체를 유효하게 작성합니다.")
            continue
        for field_name in ("label", "icon", "kind", "role", "boundary", "systemLayer"):
            if not isinstance(node.get(field_name), str) or not node[field_name].strip():
                add_issue(result, "FAIL", data_path, f"workbench node {node_id!r} has no {field_name}", "각 node에 label, icon, kind, role, boundary, systemLayer를 작성합니다.")
        if node.get("systemLayer") not in SYSTEM_LAYERS:
            add_issue(
                result,
                "FAIL",
                data_path,
                f"workbench node {node_id!r} uses an unsupported systemLayer",
                "outside, interface, application, resource, integration, runtime 중 실제 위치 하나를 사용합니다.",
            )
        if node.get("icon") not in SYSTEM_ICON_NAMES:
            add_issue(result, "FAIL", data_path, f"workbench node {node_id!r} uses an unsupported icon", "assets/icons에 정의된 icon 이름을 사용합니다.")
        elif isinstance(node.get("icon"), str):
            icon_path = data_path.parents[2] / "assets" / "icons" / f"{node['icon']}.svg"
            validate_renderable_svg(result, icon_path, f"node icon {node['icon']}")
        if isinstance(node.get("kind"), str) and DIAGRAM_DATA_NODE_KIND.search(node["kind"]):
            add_issue(
                result,
                "FAIL",
                data_path,
                f"workbench node {node_id!r} represents transferable data instead of a responsibility",
                "DTO, event payload, HTTP result와 비교 경로는 node가 아니라 edge verb/payload로 표현합니다.",
            )
        validate_code_point_ids(node.get("codePointIds"), f"workbench node {node_id!r}")

    scenarios = workbench.get("scenarios")
    if not isinstance(scenarios, list):
        return
    for scenario_index, scenario in enumerate(scenarios):
        if not isinstance(scenario, dict):
            continue
        if scenario.get("visual") is not None:
            validate_visual_definition(result, data_path, scenario.get("visual"), "scenario visual")
        diagram = scenario.get("diagram")
        location = f"workbench scenario {scenario_index} diagram"
        if not isinstance(diagram, dict):
            add_issue(result, "FAIL", data_path, f"{location} is missing", "모든 관찰 조건에 caption과 실제 경로 lane을 선언합니다.")
            continue
        if not isinstance(diagram.get("caption"), str) or not diagram["caption"].strip():
            add_issue(result, "FAIL", data_path, f"{location} has no caption", "학습자가 흐름을 한 문장으로 읽을 수 있는 caption을 작성합니다.")

        prediction = scenario.get("prediction")
        reflection = scenario.get("reflection")
        copy_roles = {
            "prompt": scenario.get("prompt"),
            "prediction prompt": prediction.get("prompt") if isinstance(prediction, dict) else None,
            "prediction explanation": prediction.get("explanation") if isinstance(prediction, dict) else None,
            "observation title": scenario.get("observationTitle"),
            "diagram caption": diagram.get("caption"),
            "evidence": scenario.get("evidence"),
            "outcome": scenario.get("outcome"),
            "reflection prompt": reflection.get("prompt") if isinstance(reflection, dict) else None,
        }
        normalized_roles = {
            role: normalize_ui_copy(value)
            for role, value in copy_roles.items()
            if normalize_ui_copy(value)
        }
        duplicate_groups: dict[str, list[str]] = {}
        for role, normalized in normalized_roles.items():
            duplicate_groups.setdefault(normalized, []).append(role)
        for roles in duplicate_groups.values():
            if len(roles) > 1:
                add_issue(
                    result,
                    "WARN",
                    data_path,
                    f"workbench scenario {scenario_index} repeats the same copy across roles: {', '.join(roles)}",
                    "조건, 판단 질문, 경로, 증거, 결론과 회상 질문이 각각 한 역할만 맡도록 문장을 나눕니다.",
                )

        participants = diagram.get("participants")
        if participants is not None:
            if (
                not isinstance(participants, list)
                or not participants
                or any(not isinstance(item, str) or item not in nodes for item in participants)
                or len(participants) != len(set(participants))
            ):
                add_issue(result, "FAIL", data_path, f"{location} has invalid participants", "표시 순서가 필요할 때 중복 없이 workbench.nodes key만 나열합니다.")

        lanes = diagram.get("lanes")
        if not isinstance(lanes, list) or not lanes:
            add_issue(result, "FAIL", data_path, f"{location} has no lanes", "정상, 실패, 비교처럼 의미가 다른 경로를 lane으로 나눕니다.")
            continue
        declared_lane_ids = {
            lane.get("id")
            for lane in lanes
            if isinstance(lane, dict) and isinstance(lane.get("id"), str) and lane["id"].strip()
        }
        lane_ids: set[str] = set()
        for lane_index, lane in enumerate(lanes):
            lane_location = f"{location} lane {lane_index}"
            if not isinstance(lane, dict):
                add_issue(result, "FAIL", data_path, f"{lane_location} must be an object", "lane을 id, label, description, steps 객체로 작성합니다.")
                continue
            lane_id = lane.get("id")
            if not isinstance(lane_id, str) or not lane_id.strip() or lane_id in lane_ids:
                add_issue(result, "FAIL", data_path, f"{lane_location} has an invalid or duplicate id", "시나리오 안에서 고유한 lane id를 사용합니다.")
            else:
                lane_ids.add(lane_id)
            for field_name in ("label", "description"):
                if not isinstance(lane.get(field_name), str) or not lane[field_name].strip():
                    add_issue(result, "FAIL", data_path, f"{lane_location} has no {field_name}", "lane의 책임과 관찰 목적을 설명합니다.")

            lane_participants = lane.get("participants")
            if lane_participants is not None and (
                not isinstance(lane_participants, list)
                or not lane_participants
                or any(not isinstance(item, str) or item not in nodes for item in lane_participants)
                or len(lane_participants) != len(set(lane_participants))
            ):
                add_issue(result, "FAIL", data_path, f"{lane_location} has invalid participants", "현재 lane에 실제 등장하는 workbench.nodes key만 중복 없이 나열합니다.")

            next_lane_ids = lane.get("nextLaneIds")
            if next_lane_ids is not None and (
                not isinstance(next_lane_ids, list)
                or any(not isinstance(item, str) or item not in declared_lane_ids for item in next_lane_ids)
                or len(next_lane_ids) != len(set(next_lane_ids))
            ):
                add_issue(result, "FAIL", data_path, f"{lane_location} has invalid nextLaneIds", "다음에 비교할 수 있는 현재 diagram의 lane id만 중복 없이 작성합니다.")

            steps = lane.get("steps")
            if not isinstance(steps, list) or not (2 <= len(steps) <= 7):
                add_issue(result, "FAIL", data_path, f"{lane_location} must have 2-7 steps", "한 lane은 읽을 수 있는 전이 2-7개로 제한합니다.")
                continue
            for step_index, step in enumerate(steps):
                step_location = f"{lane_location} step {step_index}"
                if not isinstance(step, dict):
                    add_issue(result, "FAIL", data_path, f"{step_location} must be an object", "전이를 from, to, verb, payload, kind로 작성합니다.")
                    continue
                for endpoint in ("from", "to"):
                    if step.get(endpoint) not in nodes:
                        add_issue(result, "FAIL", data_path, f"{step_location} references unknown {endpoint} node", "from과 to는 workbench.nodes key를 참조합니다.")
                for field_name in ("verb", "payload"):
                    if not isinstance(step.get(field_name), str) or not step[field_name].strip():
                        add_issue(result, "FAIL", data_path, f"{step_location} has no {field_name}", "화살표에 동작 동사와 이동 데이터를 함께 작성합니다.")
                if step.get("kind") not in DIAGRAM_EDGE_KINDS:
                    add_issue(result, "FAIL", data_path, f"{step_location} has an unsupported kind", "요청, 호출, 변환, 저장, 응답, 실패, 이벤트, 설정, 비교 kind 중 하나를 사용합니다.")
                effect = step.get("effect")
                if not isinstance(effect, dict):
                    add_issue(result, "FAIL", data_path, f"{step_location} has no effect", "학생이 단계 전후를 비교하도록 kind, subject, before, after를 작성합니다.")
                else:
                    if effect.get("kind") not in STEP_EFFECT_KINDS:
                        add_issue(result, "FAIL", data_path, f"{step_location} effect has an unsupported kind", "전달, 변환, 저장, 분기, 반환, 확산, 검증, 보존 중 하나를 사용합니다.")
                    for field_name in ("subject", "before", "after"):
                        if not isinstance(effect.get(field_name), str) or not effect[field_name].strip():
                            add_issue(result, "FAIL", data_path, f"{step_location} effect has no {field_name}", "바뀌는 대상과 단계 전후 상태를 짧고 구체적으로 씁니다.")
                    before = effect.get("before")
                    after = effect.get("after")
                    if isinstance(before, str) and isinstance(after, str):
                        if before.strip() == after.strip():
                            add_issue(result, "FAIL", data_path, f"{step_location} effect before and after are identical", "책임 이동이면 위치를, 변환·저장·검증이면 실제 상태 차이를 적습니다.")
                        if GENERIC_EFFECT_STATE.search(before.strip()) or GENERIC_EFFECT_STATE.search(after.strip()):
                            add_issue(result, "FAIL", data_path, f"{step_location} uses a generic effect state", "'호출 전/후' 같은 틀 문장 대신 실제 값, 저장 여부, 인증 주체, 연결 대상 또는 검증 결과를 씁니다.")
                if step.get("evidenceScope") not in EVIDENCE_SCOPES:
                    add_issue(result, "FAIL", data_path, f"{step_location} has an invalid evidenceScope", "code, test, runtime, manual, concept 중 실제 확인 범위를 하나 고릅니다.")
                validate_code_point_ids(step.get("codePointIds"), step_location)

            if isinstance(lane_participants, list) and steps:
                step_node_ids = {
                    step.get(endpoint)
                    for step in steps
                    if isinstance(step, dict)
                    for endpoint in ("from", "to")
                    if step.get(endpoint) in nodes
                }
                missing_participants = sorted(step_node_ids - set(lane_participants))
                if missing_participants:
                    add_issue(
                        result,
                        "FAIL",
                        data_path,
                        f"{lane_location} participants omit step nodes: {', '.join(missing_participants)}",
                        "lane.participants에는 현재 lane의 모든 from/to node를 포함합니다.",
                    )

        not_reached = diagram.get("notReached")
        if not_reached is not None:
            if not isinstance(not_reached, list) or not not_reached:
                add_issue(result, "FAIL", data_path, f"{location} notReached must be a non-empty list", "실행되지 않은 경로가 있을 때 label과 reason을 함께 작성합니다.")
            else:
                for item in not_reached:
                    if not isinstance(item, dict) or not all(isinstance(item.get(field), str) and item[field].strip() for field in ("label", "reason")):
                        add_issue(result, "FAIL", data_path, f"{location} has an incomplete notReached item", "notReached 항목에 label과 reason을 작성합니다.")
def validate_hub_data(result: RepoResult) -> None:
    repo_root = ROOT / result.path
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
        validate_data_links(result, repo_root, data_path, parsed.get("sequences"), "sequences")


def validate_sequence_data(result: RepoResult, sequence: dict[str, str], data_path: Path) -> None:
    repo_root = ROOT / result.path
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

    if ENGLISH_META_COPY.search(content):
        add_issue(
            result,
            "FAIL",
            data_path,
            "generic English Verification label remains in learner-facing data",
            "검증 대상이나 실패 경계를 주제에 맞는 짧은 한국어로 적습니다.",
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
    if "sequences" in parsed:
        add_issue(
            result,
            "FAIL",
            data_path,
            "sequence data duplicates content inside a sequences array",
            "kind: 'sequence' 파일은 하나의 canonical 객체만 유지합니다.",
        )

    actors = parsed.get("actors") or []
    flows = parsed.get("flows") or []
    code_points = parsed.get("codePoints") or []
    workbench = parsed.get("workbench") or {}
    if not isinstance(actors, list) or not actors:
        add_issue(result, "FAIL", data_path, "actors must be a non-empty list", "actor kind 기반 다이어그램을 위해 actors를 선언합니다.")
    if not isinstance(flows, list) or not flows:
        add_issue(result, "FAIL", data_path, "flows must be a non-empty list", "시퀀스 상세는 최소 1개 이상의 flow를 가져야 합니다.")
    if not isinstance(code_points, list) or len(code_points) < 2:
        add_issue(result, "FAIL", data_path, "codePoints must contain at least 2 items", "각 시퀀스에는 최소 2개 이상의 주요 코드 포인트를 넣습니다.")

    if not isinstance(workbench, dict):
        add_issue(
            result,
            "FAIL",
            data_path,
            "workbench must be an object",
            "주차별 primary workbench의 kind, title, instruction, scenarios를 객체로 선언합니다.",
        )
    else:
        workbench_kind = workbench.get("kind")
        if workbench_kind not in WORKBENCH_KINDS:
            add_issue(
                result,
                "FAIL",
                data_path,
                f"unsupported workbench kind: {workbench_kind!r}",
                "중앙 Visual Lab design plan에 정의된 topic-specific workbench kind를 사용합니다.",
            )
        for field_name in ("title", "instruction"):
            if not isinstance(workbench.get(field_name), str) or not workbench[field_name].strip():
                add_issue(
                    result,
                    "FAIL",
                    data_path,
                    f"workbench {field_name} must be a non-empty string",
                    "워크벤치의 학습 목적과 조작 안내를 짧은 문장으로 작성합니다.",
                )

        terms = workbench.get("terms")
        if not isinstance(terms, list) or len(terms) < 2:
            add_issue(result, "FAIL", data_path, "workbench terms must contain at least 2 items", "첫 화면에 필요한 기술 용어를 term과 짧은 한국어 meaning으로 설명합니다.")
        else:
            for term_index, term_item in enumerate(terms):
                if not isinstance(term_item, dict) or not all(
                    isinstance(term_item.get(field), str) and term_item[field].strip()
                    for field in ("term", "meaning")
                ):
                    add_issue(result, "FAIL", data_path, f"workbench term {term_index} is incomplete", "각 용어에 term과 한 역할만 설명하는 meaning을 작성합니다.")

        comparison = workbench.get("comparison")
        if not isinstance(comparison, dict) or not isinstance(comparison.get("label"), str) or not comparison["label"].strip():
            add_issue(result, "FAIL", data_path, "workbench comparison is missing", "관찰 뒤 구분할 두 조건을 comparison.label, left, right로 작성합니다.")
        else:
            for side in ("left", "right"):
                item = comparison.get(side)
                if not isinstance(item, dict) or not all(
                    isinstance(item.get(field), str) and item[field].strip()
                    for field in ("title", "body")
                ):
                    add_issue(result, "FAIL", data_path, f"workbench comparison {side} is incomplete", "각 비교 항목에 title과 하나의 인과 차이를 설명하는 body를 작성합니다.")

        scenarios = workbench.get("scenarios")
        flow_ids = {flow.get("id") for flow in flows if isinstance(flow, dict)}
        if not isinstance(scenarios, list) or not (3 <= len(scenarios) <= 4):
            add_issue(
                result,
                "FAIL",
                data_path,
                "workbench scenarios must contain 3-4 items",
                "정상, 실패 또는 대안이 드러나는 실제 조건 3-4개를 제공합니다.",
            )
        else:
            scenario_ids: set[str] = set()
            for index, scenario_item in enumerate(scenarios):
                if not isinstance(scenario_item, dict):
                    add_issue(result, "FAIL", data_path, f"workbench scenario {index} must be an object", "각 시나리오를 객체로 작성합니다.")
                    continue
                scenario_id = scenario_item.get("id")
                if not isinstance(scenario_id, str) or not scenario_id.strip() or scenario_id in scenario_ids:
                    add_issue(result, "FAIL", data_path, f"workbench scenario {index} has an invalid or duplicate id", "시나리오 id를 고유한 문자열로 작성합니다.")
                else:
                    scenario_ids.add(scenario_id)
                for field_name in ("label", "prompt", "observationTitle", "evidence", "outcome"):
                    if not isinstance(scenario_item.get(field_name), str) or not scenario_item[field_name].strip():
                        add_issue(result, "FAIL", data_path, f"workbench scenario {index} has no {field_name}", "입력 조건, 관찰 질문, 증거와 판단을 실제 학습 내용으로 작성합니다.")
                reflection = scenario_item.get("reflection")
                if not isinstance(reflection, dict) or not all(
                    isinstance(reflection.get(field), str) and reflection[field].strip()
                    for field in ("prompt", "hint")
                ):
                    add_issue(result, "FAIL", data_path, f"workbench scenario {index} has no reflection", "관찰 뒤 인과 규칙을 자기 말로 정리할 prompt와 짧은 hint를 작성합니다.")
                validate_theory_reference(
                    result,
                    repo_root,
                    data_path,
                    scenario_item.get("theoryRef"),
                    f"workbench scenario {index}",
                )
                prediction = scenario_item.get("prediction")
                if not isinstance(prediction, dict):
                    add_issue(result, "FAIL", data_path, f"workbench scenario {index} has no prediction", "관찰 결과를 열기 전에 답할 prompt, options, answer, explanation을 작성합니다.")
                else:
                    for field_name in ("prompt", "answer", "explanation"):
                        if not isinstance(prediction.get(field_name), str) or not prediction[field_name].strip():
                            add_issue(result, "FAIL", data_path, f"workbench scenario {index} prediction has no {field_name}", "예측 질문, 정답 id와 관찰 뒤 설명을 모두 작성합니다.")
                    options = prediction.get("options")
                    if not isinstance(options, list) or not (2 <= len(options) <= 4):
                        add_issue(result, "FAIL", data_path, f"workbench scenario {index} prediction options must contain 2-4 items", "학생이 비교할 수 있는 2~4개 예측 선택지를 제공합니다.")
                    else:
                        option_ids: set[str] = set()
                        for option_index, option in enumerate(options):
                            if not isinstance(option, dict) or not all(
                                isinstance(option.get(field), str) and option[field].strip()
                                for field in ("id", "label")
                            ):
                                add_issue(result, "FAIL", data_path, f"workbench scenario {index} prediction option {option_index} is incomplete", "각 예측 선택지에 id와 학생이 판단할 label을 작성합니다.")
                                continue
                            option_ids.add(option["id"])
                        if isinstance(prediction.get("answer"), str) and prediction["answer"] not in option_ids:
                            add_issue(result, "FAIL", data_path, f"workbench scenario {index} prediction answer is not an option id", "answer를 같은 prediction.options의 id와 맞춥니다.")
                if scenario_item.get("flowId") not in flow_ids:
                    add_issue(result, "FAIL", data_path, f"workbench scenario {index} references an unknown flowId", "기존 flows[].id 중 하나를 연결합니다.")
                if scenario_item.get("tone") not in WORKBENCH_TONES:
                    add_issue(result, "FAIL", data_path, f"workbench scenario {index} has an invalid tone", "signal, blocked, warning, recovered 중 하나를 사용합니다.")
                route = scenario_item.get("route")
                if not isinstance(route, list) or len(route) < 2 or any(not isinstance(item, str) or not item.strip() for item in route):
                    add_issue(result, "FAIL", data_path, f"workbench scenario {index} has an invalid route", "실제 actor와 boundary를 2개 이상의 문자열 경로로 작성합니다.")
                snapshot = scenario_item.get("snapshot")
                if not isinstance(snapshot, list) or len(snapshot) < 2:
                    add_issue(result, "FAIL", data_path, f"workbench scenario {index} has an invalid snapshot", "현재 조건에서 관찰할 상태를 2개 이상 제공합니다.")
                else:
                    for snapshot_item in snapshot:
                        if not isinstance(snapshot_item, dict) or not snapshot_item.get("label") or not snapshot_item.get("value"):
                            add_issue(result, "FAIL", data_path, f"workbench scenario {index} has an incomplete snapshot item", "snapshot 항목에 label과 value를 작성합니다.")
                stop_after = scenario_item.get("stopAfter")
                if stop_after is not None and (
                    not isinstance(stop_after, int)
                    or not isinstance(route, list)
                    or not 0 <= stop_after < len(route)
                ):
                    add_issue(result, "FAIL", data_path, f"workbench scenario {index} has an invalid stopAfter", "마지막으로 도달한 route의 0-based index를 사용합니다.")
                fan_out = scenario_item.get("fanOut")
                if fan_out is not None and (
                    not isinstance(fan_out, list)
                    or not fan_out
                    or any(not isinstance(item, str) or not item.strip() for item in fan_out)
                ):
                    add_issue(result, "FAIL", data_path, f"workbench scenario {index} has an invalid fanOut", "실제로 메시지를 받는 대상 label만 배열로 작성합니다.")

        validate_semantic_workbench(result, data_path, workbench, code_points)

    validate_data_links(result, repo_root, data_path, parsed.get("relatedDocs", []), "relatedDocs")
    source_docs = parsed.get("sourceDocs", [])
    validate_data_links(result, repo_root, data_path, source_docs, "sourceDocs")

    source = parsed.get("source")
    source_items: list[dict[str, Any]] = []
    if source is not None:
        if isinstance(source, dict):
            source_items = [{"href": href} for href in source.values()]
            validate_data_links(result, repo_root, data_path, source_items, "source")
        else:
            add_issue(
                result,
                "FAIL",
                data_path,
                "source must be an object",
                "source는 theory, implementation, checklist 상대 경로를 담는 객체로 작성합니다.",
            )

    if not source_items and not source_docs:
        add_issue(
            result,
            "FAIL",
            data_path,
            "sequence data has no source document links",
            "source 또는 sourceDocs에 표준 문서 상대 경로를 연결합니다.",
        )

    validate_code_point_files(result, repo_root, sequence, data_path, code_points)

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
        expected_links={"./styles.css", "./assets/visual-lab-mark.svg"},
    )
    validate_css_assets(result, lab_dir / "styles.css")
    validate_renderer_copy(result, lab_dir / "visual-lab.js")
    validate_renderable_svg(result, lab_dir / "assets" / "visual-lab-mark.svg", "brand mark")
    validate_icon_sprite(result, lab_dir / "assets" / "system-icons.svg")
    validate_asset_metadata(result, lab_dir / "assets" / "SOURCE.md", "source")
    validate_asset_metadata(result, lab_dir / "assets" / "LICENSES.md", "license")
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
                expected_links={"../../styles.css", "../../assets/visual-lab-mark.svg"},
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
