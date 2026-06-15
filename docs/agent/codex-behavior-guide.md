# Agent Behavior Guide

이 문서는 Codex, Cursor, Claude 같은 자동화 작업자가 중앙 레포에서 지켜야 할 짧은 진입 규칙입니다.
상세한 기존 기준은 [기존 Codex behavior guide](../codex-behavior-guide.md)를 함께 참고합니다.

## 작업 전

1. 루트 `README.md`를 읽습니다.
2. [manifest](../manifest/sequences.yml)에서 대상 시퀀스를 확인합니다.
3. 관련 학생용, 강사용, 에이전트용 문서를 구분해서 읽습니다.
4. 작업 범위와 검증 방법을 먼저 정합니다.

## 편집 원칙

- 작은 변경을 선호합니다.
- 기존 구조와 문체를 맞춥니다.
- 사용자 요청 없는 시퀀스 상태 변경을 하지 않습니다.
- 중앙 docs를 상세 이론 저장소로 만들지 않습니다.
- 학생용 문서에는 운영 규칙과 정답 코드를 과도하게 넣지 않습니다.
- 새 블로그 산출물이나 새 멘토 문서를 만들지 않습니다.
- 멘토용 진행 포인트는 기존 문서 안의 `<details>` 영역에 둡니다.
- 기존 문서는 Problem -> Analyze -> Action -> Result 흐름으로 다듬되, 문서 수를 늘리지 않습니다.
- Codex는 GitHub 원격 default branch를 직접 바꾸지 못합니다.
- 원격 default branch 변경이 필요하면 manifest와 강사용 checklist에 수동 조치로 남깁니다.

## 코드 변경 시

- 관련 테스트를 실행합니다.
- 테스트를 실행하지 못하면 이유를 남깁니다.
- 불필요한 리팩토링을 섞지 않습니다.

## 문서 변경 시

- 학생용, 강사용, 에이전트용 위치가 맞는지 확인합니다.
- Markdown fence가 깨지지 않았는지 확인합니다.
- 링크가 실제 파일을 가리키는지 확인합니다.
- 기본 문서 세트는 `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`입니다.
- legacy 문서가 있으면 먼저 기본 문서에 흡수 가능한지 확인하고, 외부 링크 가능성이 있으면 바로 삭제하지 않습니다.

## 마무리 확인

```bash
git diff --check
git status --short
```
