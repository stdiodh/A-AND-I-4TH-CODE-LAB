# Visual Lab Design System Application Plan

## 1. Subject

실행 중인 백엔드 요청, 객체, 상태, 경계와 전달 단위를 직접 추적하며 이론을 확인하는 정적 학습 환경.

## 2. Audience

Spring Boot 기초부터 DB, 검증, 인증, 외부 연동, 테스트, 캐시, 실시간 통신, 배포, 리팩토링과 이벤트 기반 사고를 순서대로 학습하는 A&I 백엔드 학습자.

## 3. Single Job

학습자가 이번 시퀀스에서 조작할 조건, 관찰할 시스템 변화, 설명해야 할 다음 판단을 첫 화면에서 놓치지 않도록 돕는다.

## 4. Core Palette

| 이름 | HEX | 의미와 사용 | 사용하지 않는 곳 | 대비 기준 |
|---|---|---|---|---|
| Lab Paper | `#F8F9FB` | 전체 학습 canvas | active panel 전체 채움 | Ink 본문과 WCAG AA |
| System Ink | `#111B3F` | 본문, 핵심 시스템 구조 | 넓은 장식 배경 | Paper 위 본문 AA 이상 |
| A&I Navy | `#0C2691` | Display, 현재 질문, 중요한 경계 | 모든 badge와 링크 | 흰색 또는 Paper 위 AA |
| Signal Blue | `#2955E4` | 사용자가 선택한 입력과 현재 경로 | 일반 본문 | 흰색 위 작은 글자는 피하고 outline/굵은 글자 사용 |
| Evidence Teal | `#3F8996` | 관찰된 결과, 회복, 검증 증거 | 모든 성공 의미를 색상만으로 표현 | 흰색 위 큰 글자 또는 진한 Ink와 조합 |
| Boundary Line | `#C9D6F3` | 계층, trust, runtime, pipeline 경계 | 본문 텍스트 | 비텍스트 구조 구분에 사용 |

상태 색상은 `danger`, `warning`, `recovered`, `blocked` semantic token으로 별도 관리하고 label과 icon을 항상 함께 쓴다. 빨강·주황·노랑을 core palette나 장식 accent로 확장하지 않는다.

## 5. Typography Roles

| 역할 | Stack | 크기 / 굵기 | Line height / spacing | 사용 위치 | 금지 위치 |
|---|---|---|---|---|---|
| Display | `Pretendard, SUIT, Noto Sans KR, system-ui, sans-serif` | `clamp(2rem, 5vw, 4.5rem)`, 800~900 | 1.04~1.15, `-0.035em` | 질문, 시퀀스의 핵심 판단 | 긴 설명, 버튼 |
| Body | 같은 system sans | 0.95~1.1rem, 400~700 | 1.55~1.75, `-0.01em` | 설명, 개념, 검증 질문 | 코드·경로 정렬 |
| Utility / Data | `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` | 0.75~0.95rem, 500~700 | 1.4~1.6, `0` 또는 `0.02em` | HTTP, 상태, 파일, 명령, 토큰, timestamp | Hero 문장과 긴 한국어 본문 |

외부 font import는 사용하지 않는다.

## 6. Layout Concepts

### Direction A — Signal Trace Workbench

```text
┌────────────────────────────────────────────────────────────┐
│ Sequence context         Current question          Next   │
├────────────────────────────────────────────────────────────┤
│ Input / state      Learning Signal Trace                  │
│ selector           [A] -> [boundary] -> [state] -> [B]    │
│                    ───────────────────────────────────────  │
│                    Selected evidence + concept + code      │
├────────────────────────────────────────────────────────────┤
│ Verification                              Next question    │
└────────────────────────────────────────────────────────────┘
```

장점: 조작, 관찰, 개념과 확인이 같은 맥락에 있다. 주차별 고유 system model을 중앙 작업면에 배치할 수 있다.

### Direction B — Course Briefing Board

```text
┌────────────────────────────────────────────────────────────┐
│ Large sequence thesis                                     │
├────────────────────┬───────────────────────────────────────┤
│ Problem brief      │ Diagram / explanation cards           │
│ Concept index      │ Code / glossary / references          │
│ Checklist          │                                       │
└────────────────────┴───────────────────────────────────────┘
```

장점: 읽기에는 익숙하다. 단점: 현재 구현의 문서형 카드 모음과 차이가 작고 주차별 판단이 수동적이다.

### 선택

Direction A를 선택한다. Visual Lab은 문서 요약이 아니라 학습자가 조건을 바꿔 시스템 변화를 관찰하는 공간이어야 한다.

## 7. Signature Element

`Learning Signal Trace`를 전체 사이트에서 하나의 signature로 사용한다.

```text
Selected input/state
-> observed request/object/token/cache/artifact/event path
-> active responsibility boundary
-> evidence
-> next question
```

선택한 시퀀스와 시나리오에 따라 node, state, boundary와 evidence가 실제 데이터로 갱신된다. 단순한 연결선이나 glow로 쓰지 않는다.

## 8. Motion

- 핵심 순간: 입력 또는 시나리오를 바꿨을 때 Signal Trace의 active path가 다음 관찰 지점으로 이동하는 순간.
- 목적: 어떤 시스템 경계를 지나 결과가 바뀌었는지 전달.
- duration: 220~280ms.
- easing: `cubic-bezier(0.2, 0.8, 0.2, 1)`.
- 반복: 자동 반복 없음. 재생은 학습자가 명시적으로 시작할 때만 단계 이동.
- reduced motion: smooth scroll과 transition을 제거하고 active node, route, evidence label을 즉시 갱신.

## 9. Shared Experience Grammar

```text
Current question
-> controllable input or state
-> observed system path
-> concept or responsibility boundary
-> failure or alternative comparison
-> verification evidence
-> next question
```

## 10. Sequence Workbench Mapping

| Sequence | Primary workbench | 실제 판단 |
|---|---|---|
| 00 | Request Workbench | method, URL, JSON, status와 Git/DB 기본 표식을 읽는다 |
| 01 | Request Packet Trace | 요청과 응답 객체가 계층별로 어떻게 바뀌는지 본다 |
| 02 | Persistence Boundary | memory와 MySQL, DTO와 Entity의 경계를 비교한다 |
| 03 | Failure Gate | invalid body와 missing id가 어느 경계에서 멈추는지 본다 |
| 04 | Auth Boundary | 발급과 검증, 401과 403의 도달 지점을 구분한다 |
| 05 | Trust & Recovery Map | verified identity, account collision, JWT, reset mail 경계를 구분한다 |
| 06 | Test Harness | fixture, mock, assertion과 테스트가 보장하지 않는 범위를 본다 |
| 07 | Cache State Inspector | empty, warm, expired, evicted, refreshed 상태를 비교한다 |
| 08 | Connection Console | connect, subscribe, send, broadcast와 fan-out을 관찰한다 |
| 09 | Runtime Boundary | jar, image, container, environment와 health evidence를 구분한다 |
| 10 | Pipeline Gate | 최초 실패 단계와 이후 blocked 단계를 확인한다 |
| 11 | Behavior Invariant Map | 구조 변경 전후 API 계약과 테스트 증거를 비교한다 |
| 12 | Event Delivery Trace | direct call, broker path, duplicate delivery와 consumer 상태를 비교한다 |

## 11. Component Mapping

- Topbar는 compact context bar로 유지한다.
- Hub는 카드 grid 대신 sequence journey를 primary로 하고 링크 자체는 유지한다.
- Hero는 현재 질문과 goal만 남긴다.
- Sequence switcher는 다중 시퀀스 hub에서만 제공한다.
- Section nav는 6단계 Learning Trace로 교체한다.
- Flow tab은 실제 시나리오 selector로 유지한다.
- Sequence Diagram은 fallback으로 유지하고, `workbench.kind`가 있으면 주차별 primary workbench를 렌더링한다.
- Step rail, 이전/다음, progress는 키보드 동작과 순서를 유지하되 전체 DOM을 교체하지 않는다.
- Code Points, Responsibilities, Concepts는 선택 단계의 evidence/context drawer로 결합한다.
- Glossary와 References는 secondary reference shelf로 유지한다.
- Checklist는 상태를 저장하지 않는 session-local interactive check로 변경한다.
- Next는 실제 다음 상세 페이지가 존재할 때 link를 제공한다.
- Empty, error, disabled는 이유와 확인 대상을 함께 표시한다.

## 12. Genericity Critique와 수정

### 첫 계획의 일반적인 부분

- `Learning Signal Trace`만 공통으로 두면 이름만 다른 stepper가 될 위험이 있었다.
- 좌측 selector와 우측 detail은 일반 관리자 도구에도 붙일 수 있는 구조였다.
- 기존 palette를 그대로 쓰는 것만으로는 A&I Visual Lab 정체성이 생기지 않는다.
- 모든 주차에 incident와 candidate cause를 강제하면 00, 06, 11의 실제 학습 범위를 왜곡한다.

### 수정

- 공통 trace는 navigation이 아니라 실제 request, object, token, cache, artifact, test, event path만 표현하도록 제한했다.
- 13개 시퀀스에 주제별 workbench를 배정하고 같은 actor diagram을 기본 답으로 사용하지 않는다.
- Hero를 marketing thesis에서 learner question으로 축소하고 첫 viewport에 조작과 관찰을 배치한다.
- terminal은 실제 명령이나 로그가 있는 00, 09, 10에서만 utility evidence로 쓴다.
- 번호는 실제 시퀀스와 단계 순서에만 사용한다.
- incident가 맞는 주차에는 failure evidence를 쓰고, 기초·테스트·리팩토링에는 입력, 보장 범위, invariant를 중심으로 둔다.

## 13. Implementation Order

1. Semantic tokens and typography.
2. Page shell, context bar, hub journey and learning trace.
3. Shared workbench renderer and state model.
4. Topic-specific workbench variants.
5. Evidence/context drawer, verification and next question.
6. Empty, error, disabled and fallback states.
7. Mobile, focus preservation and reduced motion.
8. UI copy cleanup.
9. Static and browser regression across 00~12.

이 critique를 완료했으므로 구현 단계로 이동할 수 있다.
