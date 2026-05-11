#!/usr/bin/env python3
"""Validate Visual Lab color tokens across topic subrepositories.

This script checks Visual Lab CSS files without external dependencies. Colors
outside the central design guide token set are warnings, while red/orange/yellow
dominant colors, neon-like colors, dark-mode backgrounds, and external CSS/font
imports are failures.
"""

from __future__ import annotations

import configparser
import colorsys
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GITMODULES = ROOT / ".gitmodules"
VISUAL_LAB_DIR = Path("docs/visual-lab")
CSS_FILE_NAMES = (
    "design-tokens.css",
    "style.css",
    "components.css",
    "styles.css",
)
INDEX_FILE_NAME = "index.html"
HEX_PATTERN = re.compile(r"#[0-9A-Fa-f]{3,8}\b")
IMPORT_PATTERN = re.compile(
    r"@import\s+(?:url\()?['\"]?(https?:|//)[^;'\")]+",
    re.IGNORECASE,
)
EXTERNAL_CSS_PATTERN = re.compile(
    r"<link\b[^>]*\bhref=['\"](?:https?:|//)[^'\"]+['\"][^>]*>",
    re.IGNORECASE,
)
FONT_IMPORT_PATTERN = re.compile(
    r"(fonts\.googleapis|fonts\.gstatic|use\.typekit|fontawesome|cdn|unpkg|jsdelivr|cdnjs)",
    re.IGNORECASE,
)

ALLOWED_COLORS = {
    "#F8F9FB",
    "#FFFFFF",
    "#0C2691",
    "#2955E4",
    "#3F8996",
    "#111B3F",
    "#4B587C",
    "#C9D6F3",
    "#EAF0FB",
    "#D4E8E9",
    "#E8EEF9",
    "#CAD8F7",
    "#C7D5F1",
    "#D8DDEB",
    "#F1F7FF",
    "#8FB1FF",
    "#2F62F4",
    "#2C9FA0",
    "#ECFBFA",
    "#EEF4FF",
}

TOKEN_BY_COLOR = {
    "#F8F9FB": "--color-bg-base",
    "#FFFFFF": "--color-card-white",
    "#0C2691": "--color-title-navy",
    "#2955E4": "--color-accent-blue",
    "#3F8996": "--color-accent-teal",
    "#111B3F": "--color-body-navy",
    "#4B587C": "--color-subtext",
    "#C9D6F3": "--color-line-blue-light",
    "#EAF0FB": "--color-panel-blue-tint",
    "#D4E8E9": "--color-panel-mint-tint",
    "#E8EEF9": "--color-decor-blue",
    "#CAD8F7": "--color-decor-stripe",
    "#C7D5F1": "--color-dot-grid",
    "#D8DDEB": "--color-outline-soft",
    "#F1F7FF": "--color-summary-bg",
    "#8FB1FF": "--color-summary-border",
    "#2F62F4": "--color-summary-title / --color-incorrect",
    "#2C9FA0": "--color-correct",
    "#ECFBFA": "--color-correct-bg",
    "#EEF4FF": "--color-incorrect-bg",
}


@dataclass
class Issue:
    level: str
    path: str
    detail: str
    hint: str


@dataclass
class RepoResult:
    name: str
    path: Path
    issues: list[Issue] = field(default_factory=list)

    @property
    def has_failures(self) -> bool:
        return any(issue.level == "FAIL" for issue in self.issues)

    @property
    def has_warnings(self) -> bool:
        return any(issue.level == "WARN" for issue in self.issues)


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


def add_issue(result: RepoResult, level: str, path: Path, detail: str, hint: str) -> None:
    result.issues.append(Issue(level, relative_display(path), detail, hint))


def normalize_hex(value: str) -> str:
    raw = value.lstrip("#")
    if len(raw) in {3, 4}:
        raw = "".join(character * 2 for character in raw[:3])
    elif len(raw) in {6, 8}:
        raw = raw[:6]
    return f"#{raw.upper()}"


def rgb_from_hex(value: str) -> tuple[int, int, int]:
    normalized = normalize_hex(value).lstrip("#")
    return (
        int(normalized[0:2], 16),
        int(normalized[2:4], 16),
        int(normalized[4:6], 16),
    )


def relative_luminance(red: int, green: int, blue: int) -> float:
    channels = []
    for value in (red, green, blue):
        normalized = value / 255
        if normalized <= 0.03928:
            channels.append(normalized / 12.92)
        else:
            channels.append(((normalized + 0.055) / 1.055) ** 2.4)
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def forbidden_color_reason(color: str) -> str | None:
    if color in ALLOWED_COLORS:
        return None

    red, green, blue = rgb_from_hex(color)
    hue, lightness, saturation = colorsys.rgb_to_hls(red / 255, green / 255, blue / 255)
    hue_degrees = hue * 360
    luminance = relative_luminance(red, green, blue)

    if saturation >= 0.55 and (hue_degrees <= 18 or hue_degrees >= 342):
        return "strong red family"
    if saturation >= 0.5 and 18 < hue_degrees <= 50:
        return "strong orange family"
    if saturation >= 0.5 and 50 < hue_degrees <= 72:
        return "strong yellow family"
    if saturation >= 0.82 and lightness >= 0.52:
        return "neon-like high-saturation color"
    if luminance <= 0.08 and saturation <= 0.45:
        return "dark-mode background-like color"

    return None


def nearest_allowed_color(color: str) -> str:
    red, green, blue = rgb_from_hex(color)

    def distance(candidate: str) -> int:
        candidate_red, candidate_green, candidate_blue = rgb_from_hex(candidate)
        return (
            (red - candidate_red) ** 2
            + (green - candidate_green) ** 2
            + (blue - candidate_blue) ** 2
        )

    return min(ALLOWED_COLORS, key=distance)


def replacement_hint(color: str) -> str:
    nearest = nearest_allowed_color(color)
    token = TOKEN_BY_COLOR.get(nearest, "central design token")
    return f"{color} 대신 {token} ({nearest}) 토큰을 사용합니다."


def validate_role_tokens(result: RepoResult, path: Path, content: str) -> None:
    role_pattern = re.compile(r"--role-(?:error|warning)\s*:\s*(#[0-9A-Fa-f]{3,8})", re.IGNORECASE)
    for match in role_pattern.finditer(content):
        color = normalize_hex(match.group(1))
        if color not in {
            "#2955E4",
            "#3F8996",
            "#2F62F4",
            "#2C9FA0",
            "#EAF0FB",
            "#D4E8E9",
            "#ECFBFA",
            "#EEF4FF",
        }:
            add_issue(
                result,
                "FAIL",
                path,
                f"role-error/role-warning uses non blue/teal token: {color}",
                "role-error와 role-warning 이름은 유지해도 실제 색상은 blue/teal 계열 토큰으로 매핑합니다.",
            )


def validate_css_file(result: RepoResult, path: Path) -> None:
    content = path.read_text(encoding="utf-8")

    if IMPORT_PATTERN.search(content) or (FONT_IMPORT_PATTERN.search(content) and "@import" in content):
        add_issue(
            result,
            "FAIL",
            path,
            "external CSS or font import appears in CSS",
            "외부 CDN, 외부 CSS framework, 외부 폰트 import를 제거합니다.",
        )

    validate_role_tokens(result, path, content)

    seen_colors: set[str] = set()
    for match in HEX_PATTERN.finditer(content):
        color = normalize_hex(match.group(0))
        if color in seen_colors:
            continue
        seen_colors.add(color)

        forbidden_reason = forbidden_color_reason(color)
        if forbidden_reason:
            add_issue(
                result,
                "FAIL",
                path,
                f"{color} is forbidden: {forbidden_reason}",
                replacement_hint(color),
            )
        elif color not in ALLOWED_COLORS:
            add_issue(
                result,
                "WARN",
                path,
                f"{color} is not in central Visual Lab color tokens",
                replacement_hint(color),
            )


def validate_index_html(result: RepoResult, path: Path) -> None:
    if not path.exists():
        return
    content = path.read_text(encoding="utf-8")
    if EXTERNAL_CSS_PATTERN.search(content) or FONT_IMPORT_PATTERN.search(content):
        add_issue(
            result,
            "FAIL",
            path,
            "external CDN CSS or font link appears in index.html",
            "CSS와 font는 로컬 상대 경로 파일만 사용합니다.",
        )


def validate_repo(name: str, path: Path) -> RepoResult:
    result = RepoResult(name=name, path=path)
    lab_dir = ROOT / path / VISUAL_LAB_DIR
    if not lab_dir.exists():
        return result

    for file_name in CSS_FILE_NAMES:
        css_path = lab_dir / file_name
        if css_path.exists():
            validate_css_file(result, css_path)

    validate_index_html(result, lab_dir / INDEX_FILE_NAME)
    return result


def validate() -> list[RepoResult]:
    modules = parse_gitmodules()
    return [
        validate_repo(name, path)
        for name, path in sorted(modules.items(), key=lambda item: str(item[1]))
    ]


def print_results(results: list[RepoResult]) -> int:
    total_issues = sum(len(result.issues) for result in results)
    warning_groups = sum(1 for result in results if result.has_warnings)
    has_failures = any(result.has_failures for result in results)
    status = "FAIL" if has_failures else "PASS"
    print(f"{status}: {len(results)} repo group(s), {total_issues} issue(s), {warning_groups} warning group(s)")
    print()

    for result in results:
        repo_status = "FAIL" if result.has_failures else "WARN" if result.has_warnings else "PASS"
        print(f"[{repo_status}] {result.name} ({result.path})")
        if not result.issues:
            print("  - OK")
        for issue in result.issues:
            print(f"  - {issue.level}: {issue.path}")
            print(f"    detail: {issue.detail}")
            print(f"    hint: {issue.hint}")
        print()

    return 1 if has_failures else 0


def main() -> int:
    return print_results(validate())


if __name__ == "__main__":
    sys.exit(main())
