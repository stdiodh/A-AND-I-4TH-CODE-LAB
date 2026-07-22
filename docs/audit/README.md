# Audit 기록 사용법

이 디렉터리는 조사, 계획, 화면 증거와 완료 검토를 보존한다.
현재 구현 규칙은 아래 중앙 문서를 기준으로 판단한다.

- `../visual-lab-design-guide.md`
- `../visual-lab-content-spec.md`
- `../visual-lab-implementation-plan.md`
- `../visual-lab-sequence-workflow.md`

## Visual Lab 기록

| 문서 | 상태 | 역할 |
|---|---|---|
| `visual-lab-design-system-audit.md` | 완료된 기준 조사 | 초기 카드형 화면의 문제와 유지·변경 대상을 기록한다. |
| `visual-lab-design-system-plan.md` | 완료된 1차 계획 | Guided Story, Diagnostic Lifeline과 system layer 도입 결정을 보존한다. |
| `visual-lab-design-system-review.md` | 누적 완료 검토 | 실제 적용 범위, 브라우저·정적 검증과 남은 문제를 기록한다. |
| `visual-lab-readability-reduction-plan.md` | 완료된 2차 가독성 계획 | SVG 글자 geometry와 단계별 반복 문구 감량의 기준, 적용 결과와 8.2 후속 검수를 보존한다. |
| `visual-lab-refactor-sweep.md` | 완료된 과거 이력 | 초기 Visual Lab 구조 정리와 legacy 조사 결과를 보존한다. |

계획 문서는 구현이 끝나면 삭제하지 않는다. 상단 상태를 `완료`로 바꾸고 실제 결과, 검증 명령과 최종 review 위치를 연결한다. 새로운 구현 규칙은 계획 문서에만 남기지 않고 위 중앙 기준 문서와 validator에 함께 반영한다.

## 시퀀스 브랜치 기록

| 문서 | 상태 | 역할 |
|---|---|---|
| `sequence-06-testing-refactoring-plan.md` | 06 원격 전환 완료, Visual Lab·중앙 draft PR 검토 대기 | 최신 05 기준으로 06 브랜치를 재정렬한 결과, Service 테스트 학습 범위, legacy 문서 정리와 후속 반영 gate를 기록한다. |

## 화면 증거

- `screenshots/visual-lab-redesign`: 최초 Guided Story 개편의 before/after 기록
- `screenshots/visual-lab-layer-system`: Diagnostic Lifeline과 system layer 도입 뒤 기록
- `screenshots/visual-lab-readability`: 현재 단계 Inspector, 모바일 단일 surface와 SVG 가독성 보정 기록

화면 증거는 같은 sequence와 viewport를 기준으로 비교한다. 이전 screenshot을 현재 구현의 after 증거로 재사용하지 않는다.
