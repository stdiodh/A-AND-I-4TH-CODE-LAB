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
- 반복: 없음. 단계는 학습자가 이전/다음으로 한 번에 하나씩 이동한다.
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
| 11 | Behavior Change Ledger | 유지된 계약과 의도적으로 바뀐 동작을 테스트 증거와 함께 분리한다 |
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

## 14. Semantic Diagram Revision

### 14.1 문제 정의

첫 적용의 `Learning Signal Trace`는 실제 route 순서와 도달 상태를 보여주지만, node가 명사 label만 가지며 connector에 동작과 전달물이 없다. 이론을 읽은 학습자도 `PostCreateRequest`, `PostEntity`, `save(...)`, `201 Created`가 어느 책임 사이에서 어떻게 바뀌는지 도식만으로 설명하기 어렵다.

새 Single Job은 다음처럼 좁힌다.

```text
학습자가 각 화살표를 “누가 무엇을 어떤 형태로 다음 책임에 넘기는가”라는 한 문장으로 읽게 한다.
```

### 14.2 Layout Comparison

#### Direction A — Annotated Actor Trace

```text
┌────────────┐  요청 · POST /posts + JSON  ┌────────────┐
│ Client     │ ───────────────────────────> │ Controller │
│ 요청 주체  │                              │ HTTP 입구  │
└────────────┘                              └────────────┘
```

장점: actor와 전달 행위를 가장 빠르게 읽을 수 있다. 단점: 인증, 이벤트, 리팩토링처럼 분기나 비교가 있는 주제는 한 줄로 왜곡될 수 있다.

#### Direction B — Semantic Lanes

```text
Request lane   Client -- 요청 · JSON --> Controller -- 호출 --> Service
Response lane  Client <-- 응답 · 201 -- Response DTO <-- 변환 -- Service
Event lane                                  Service -- 발행 · Event --> Broker
Not reached                                 Repository · DB mutation
```

장점: 응답, 비동기 분기, side input과 실행되지 않은 경로를 구분할 수 있다. 단점: 단순한 시퀀스에도 lane을 강제하면 화면이 무거워진다.

#### 선택

기본은 Direction A를 사용하고, 실제 이론에 분기·비교·side input이 있을 때만 Direction B를 사용한다. 00은 HTTP/Git/DB 준비를 병렬 lane으로, 11은 Before/After 비교로, 12는 요청 응답과 event delivery를 분리한다. 모바일에서는 모든 lane을 세로 trace로 바꾸되 edge label은 숨기지 않는다.

### 14.3 Diagram Grammar

- node는 사람, client, controller, service, repository, database, provider, broker, consumer처럼 책임을 수행하는 주체만 사용한다.
- DTO, Entity, token, row, command, status, event payload는 connector 위의 Utility/Data capsule로 표시한다.
- connector는 `동사 · 전달물` 형식을 사용한다. 예: `변환 · PostCreateRequest → PostEntity`, `저장 · save(entity)`, `응답 · 201 + PostResponse`.
- node에는 local SVG icon, 종류, 역할, 책임 경계를 visible text로 함께 표시한다. icon은 장식 보조이며 `aria-hidden="true"`로 둔다.
- connector가 선택 가능한 학습 단계다. 선택하면 해당 동작의 개념, 코드와 확인 증거가 갱신된다.
- 실패 경로는 실제 exception/handler/response까지 그린다. 정상 downstream은 `실행되지 않음` 영역에 원인과 함께 표시한다.
- diagram 위에는 현재 scenario를 한 문장으로 읽는 caption을 둔다.
- line style은 요청/호출, 응답/결과, 실패, event/config를 보조 구분하지만 verb와 상태 label을 항상 함께 쓴다.

### 14.4 Icon Asset System

초기안에서는 저장소 로컬 `docs/visual-lab/assets/system-icons.svg` sprite 하나를 사용하려 했다. 그러나 `<symbol>` 기반 sprite는 파일을 직접 열면 비어 보이고 실제 화면에서도 아이콘 크기가 작아 학생이 종류를 구분하기 어려웠다. 따라서 이 안은 15.4의 직접 렌더링 SVG 계약으로 대체한다. `system-icons.svg`는 원본·호환 자료로만 남기고, 실제 화면은 `assets/icons/{icon}.svg`를 `<img>`로 표시한다.

외부 icon library, CDN, bitmap illustration은 사용하지 않는다. 아이콘 자체에 기술 의미를 맡기지 않고 label, role, boundary를 항상 함께 표시한다.

### 14.5 Motion

기존 240ms signal transition을 connector active state에만 적용한다. 자동 반복은 없고, reduced motion에서는 connector와 evidence를 즉시 바꾼다. 화살표를 따라 움직이는 particle이나 반복 pulse는 추가하지 않는다.

### 14.6 Genericity Critique

첫 보정안도 아이콘이 붙은 일반 flowchart가 될 위험이 있었다. 아이콘만 바꾸거나 모든 주차를 같은 horizontal pipeline으로 만들면 다른 개발자 문서에도 그대로 붙일 수 있고 백엔드 학습 범위를 다시 왜곡한다.

이를 다음처럼 수정한다.

- 아이콘보다 `동사 · payload`, 책임 경계와 실제 검증 증거를 primary information으로 둔다.
- DTO, token, artifact와 event를 actor 상자로 만들지 않고 전달 단위로 분리한다.
- 03/04/10은 실제 차단과 응답 경로, 07은 cache hit/miss branch, 08은 구독자 fan-out, 09는 build/runtime 경계, 11은 unchanged contract와 intentional change 두 lane, 12는 request/event 두 lane을 사용한다.
- 실패 시 단순히 이후 node를 회색으로 만들지 않고 무엇이 반환됐고 어떤 mutation이 실행되지 않았는지 설명한다.
- 번호는 실제 실행 순서에만 사용하고, 장식 badge나 의미 없는 terminal·metric은 추가하지 않는다.

이 revision critique를 완료했으므로 semantic diagram 구현을 시작할 수 있다.

## 15. Student Comprehension Revision

### 15.1 조사 결과

Semantic lane은 기술 구조를 더 정확히 표현했지만 학생이 읽어야 할 actor와 edge를 한 번에 모두 펼쳤다. 07은 조건에 따라 최대 25개 edge, 08은 20개 edge가 보여 조작부와 현재 증거가 첫 화면에서 멀어졌다. scenario 이름에 `miss`, `hit`, `blocked` 같은 결과가 들어가 예측 전에 답을 공개했고, 21px sprite icon은 유효한 파일이어도 반복 카드 안에서 사실상 보이지 않았다.

따라서 최종 경험을 다음 학습 순서로 수정한다.

```text
필수 전제
-> 결과를 숨긴 입력 조건
-> 학생의 예측
-> 한 단계씩 관찰
-> 현재 단계의 이유와 증거
-> 반대 조건 비교
-> 자기 말로 인과 규칙 정리
```

### 15.2 Revised Subject, Audience, Single Job

- Subject: 운영 중인 백엔드 요청과 상태 변화를 증거로 설명하는 학습 환경.
- Audience: DTO, Entity, Repository, JWT, Redis, STOMP와 runtime 경계를 아직 자연스럽게 연결하지 못하는 Spring Boot 학습자.
- Single Job: 한 화면 안에서 조건을 예측하고, 현재 한 단계의 상태 변화를 관찰하며, 누가 무엇을 왜 다음 책임에 넘겼는지 설명하게 한다.

### 15.3 Layout Comparison

#### Direction A — System Inspector

```text
┌────────────────────────────────────────────────────────┐
│ Question                                                │
├────────────────────────────────────────────────────────┤
│ Every lane / every actor / every transition            │
│                                                        │
│                                                        │
├────────────────────────────────────────────────────────┤
│ Controls / evidence                                    │
└────────────────────────────────────────────────────────┘
```

정확한 전체 구조를 한 번에 볼 수 있지만 초보자는 현재 관찰 대상과 조작 순서를 잃는다.

#### Direction B — Guided System Story

```text
┌────────────────────────────────────────────────────────┐
│ 이번 질문 · 꼭 알아야 할 전제                          │
├──────────────────────┬─────────────────────────────────┤
│ 결과를 숨긴 조건      │ 모르는 용어 details            │
│ 내 예측               │ 예측 뒤 주제 설명 SVG          │
├──────────────────────┴─────────────────────────────────┤
│ 이전 | 현재 전이 1개 | 다음                            │
│ 왜 일어났나 · 무엇으로 확인하나                        │
├────────────────────────────────────────────────────────┤
│ 반대 조건 비교 · 내가 수정한 인과 규칙                 │
└────────────────────────────────────────────────────────┘
```

Direction B를 선택한다. 필수 용어는 예측 전에 접근 가능한 기본 닫힌 `details`로 두어 모르는 학생은 확인할 수 있고, 아는 학생의 첫 행동은 밀어내지 않는다. 전체 topology는 고정된 배경 문맥으로 남기고 현재 transition 하나만 확장한다. 한 화면에 표시하는 edge는 최대 7개이며 actor를 행마다 반복하지 않는다. 자동 재생과 속도 control은 제거하고 학생이 이전/다음으로 관찰 속도를 직접 결정한다.

### 15.4 Visible Asset Contract

`system-icons.svg`는 원본과 호환성을 위한 sprite로 보존하되 primary runtime asset으로 사용하지 않는다. `<symbol>`만 있는 sprite는 파일 자체를 열면 빈 화면처럼 보이고, 외부 `<use>`는 `file://` 환경에서 안정적이지 않기 때문이다.

```text
docs/visual-lab/assets/
├── icons/{icon}.svg
├── diagrams/{sequence-topic}.svg
├── visual-lab-mark.svg
├── system-icons.svg
├── SOURCE.md
└── LICENSES.md
```

- node icon은 직접 렌더링 가능한 `assets/icons/{icon}.svg`를 `<img>`로 표시한다.
- hub와 sequence entry는 같은 로컬 `visual-lab-mark.svg`를 favicon으로 연결해 깨진 외부 brand asset 요청을 만들지 않는다.
- 주제 설명은 `workbench.visual = { src, alt, caption }`으로 연결한다.
- 정적 설명 asset은 `<img>`와 visible `figcaption`을 사용하고, interactive path는 semantic HTML button으로 유지한다.
- icon은 40~48px로 표시한다. 주제 설명 visual은 관계를 3~6개로 제한하고 원본 비율을 유지한다. desktop에서는 최대 360px 높이, mobile에서는 전체 폭을 사용하며, 390px 화면의 약 320px 그림 영역에서도 가장 작은 visible text가 10.5px 이상이 되도록 viewBox와 내부 font-size를 맞춘다.
- load error에는 기술 역할 label을 visible fallback으로 남긴다.
- 모든 SVG는 `viewBox`를 가지며 외부 font, script, URL을 포함하지 않는다.
- `SOURCE.md`와 `LICENSES.md`에 자체 제작·파생 관계와 사용 조건을 기록한다.

### 15.5 Topic Asset Mapping

| Sequence | 설명 asset | 한눈에 보여줄 관계 |
|---|---|---|
| 00 | `00-request-tool-map.svg` | HTTP request/response와 Git·DB 도구 경계 |
| 01 | `01-memory-crud-map.svg` | 메모리 CRUD 요청과 재시작 경계 |
| 02 | `02-persistence-boundary.svg` | process memory와 외부 DB 생명주기 |
| 03 | `03-request-gates.svg` | 잘못된 입력이 멈추는 경계 |
| 04 | `04-auth-boundaries.svg` | token 발급과 검증의 분리 |
| 05 | `05-external-trust.svg` | 외부 identity와 계정 복구 경계 |
| 06 | `06-test-scope.svg` | test double과 실제 보장 범위 |
| 07 | `07-cache-state-cycle.svg` | empty, hit, expire, evict, refill |
| 08 | `08-connection-subscription-fanout.svg` | transport, STOMP session, subscription |
| 09 | `09-runtime-nesting.svg` | jar, image, container, process 포함 관계 |
| 10 | `10-pipeline-gates.svg` | build, deploy, verify gate |
| 11 | `11-behavior-invariant.svg` | 유지되는 계약과 의도적으로 달라지는 동작 |
| 12 | `12-response-event-fork.svg` | 동기 응답과 비동기 event 분기 |

### 15.6 Genericity Critique와 보정

- 이전안은 아이콘이 붙은 시스템 inspector로서 다른 개발자 dashboard에도 적용할 수 있었다. `예측을 먼저 제출해야 관찰 결과를 공개`하는 학습 상태를 primary interaction으로 바꾼다.
- 카드 수를 줄이는 것만으로는 충분하지 않았다. 현재 step의 이유와 evidence를 control 바로 옆에 놓아 정보 거리를 줄인다.
- terminal과 status badge를 줄이고, 각 번호와 divider는 실제 sequence 또는 현재 transition 순서에만 사용한다.
- 검은 배경이나 accent를 제거해도 `조건 -> 예측 -> 관찰 -> 인과 규칙 수정`이 남도록 정체성을 색상이 아니라 학습 구조에 둔다.
- SVG를 장식 삽화로 만들지 않고 memory/DB 생명주기, cache state, subscription fan-out처럼 해당 주제에서만 성립하는 관계를 표현한다.

### 15.7 Completion Gate

- 390px 첫 viewport에 질문, 입력 조건, 첫 행동이 보인다.
- scenario 선택에서 현재 전이 control까지 keyboard 8회 이내로 도달한다.
- 현재 단계, 이유, evidence와 이전/다음 control이 같은 viewport에 있다.
- 결과를 scenario label이 미리 말하지 않는다.
- page-level horizontal overflow, broken image와 console error가 0이다.
- asset은 `naturalWidth > 0`이고 desktop과 390px에서 실제 크기로 표시된다.
- 주제 SVG의 가장 작은 visible text는 390px 화면에서 10.5px 이상으로 계산되고 브라우저에서 읽을 수 있다.
- 200% zoom, keyboard focus, reduced motion에서도 같은 의미를 읽을 수 있다.
- 색상이나 icon 하나만으로 상태와 기술 의미를 전달하지 않는다.

## 16. Sequence Diagram과 Theory 동기화 계획

이 절은 2026-07-16 학생 관점 재검수 뒤 추가한 다음 구현 계획이다. 이번 단계에서는 계획만 확정하고 Visual Lab runtime, 시퀀스 데이터와 토픽 저장소의 `docs/theory.md`는 아직 수정하지 않는다.

### 16.1 Goal Result

현재 `Guided System Story`는 actor와 transition을 정확히 나열하지만 실제 sequence diagram처럼 읽히지 않는다. actor는 위쪽 카드 목록, transition은 아래쪽 카드 grid로 분리되어 있고 `Client → Controller`는 화살표가 아니라 카드 안의 글자로만 보인다. viewport가 달라지면 transition grid가 다른 위치에서 줄바꿈되어 시간축도 고정되지 않는다.

다음 구현의 목표는 한 문장으로 정한다.

```text
학생이 다음 단계를 누를 때마다
누가 누구에게 무엇을 넘겼고
그 순간 데이터·상태·보장 범위가 무엇에서 무엇으로 바뀌었는지
10초 안에 말할 수 있게 한다.
```

적용 범위는 중앙 manifest의 00~12 전체 Visual Lab과 8개 토픽 저장소의 기존 `docs/theory.md`다. 커리큘럼 범위, 시퀀스 순서, 기술 사실, 구현·정답 브랜치와 답안 코드는 바꾸지 않는다.

### 16.2 Current Audit

- 공통 renderer는 `story-topology` actor strip과 `story-transitions` auto-fit card grid를 따로 만든다. lifeline, source/target column과 수직 시간축이 없다.
- self-call, 역방향 응답, event 분기와 실행되지 않은 경로는 텍스트를 읽어야만 구분된다.
- active transition은 step card, `story-current`, evidence section에 반복되어 정보가 많지만 변화의 전후는 한곳에 없다.
- 모바일에서는 actor card가 먼저 세로로 쌓여 첫 message를 보기 전에 긴 목록을 지나야 한다.
- topic SVG와 actor strip이 topology를 연달아 설명해 실제 조작 지점이 아래로 밀린다.
- 13개 Visual Lab은 theory 문서 루트로만 연결되고 anchor가 없다. 8개 `docs/theory.md`에는 Visual Lab으로 돌아오는 링크가 없다.
- 50개 scenario는 prediction을 가지지만 07·08의 8개를 제외한 42개에는 관찰 후 인과 규칙을 다시 쓰는 `observationTitle`과 `reflection`이 없다.
- `spring-boot-db-access-lab/docs/theory.md` 85줄이 02~06 다섯 시퀀스를 함께 다루고, deployment theory도 09·10의 서로 다른 실패 경계를 충분히 분리하지 못한다.
- theory 문서 7개가 `왜 이 코드를 보는지 먼저 정리합니다.`를 같은 문장으로 반복한다. `선택한 방식`, `핵심 코드로 연결하기`, `실행/테스트 결과로 확인할 것`, `한계와 다음 개선 방향`도 주제와 관계없이 같은 리듬으로 반복된다.
- UI에는 `SYSTEM STORY`, `PREDICT 01`, `PREDICT → OBSERVE`, `Selected evidence`, `Verification`, `Next question`처럼 한국어 학습 흐름과 분리된 meta label이 남아 있다.
- `docs/sequences/08-realtime-communication.md`의 SockJS 표현은 현재 native WebSocket demo와 맞지 않는다. broadcast 대상도 단순히 연결된 client가 아니라 해당 topic을 구독한 session으로 좁혀야 한다.

### 16.3 `im-not-ai` 적용 범위

참고한 저장소는 [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai)이며 기준 commit은 [`14aeb52d13e737beb4e999cb7cb92275d0969689`](https://github.com/epoko77-ai/im-not-ai/tree/14aeb52d13e737beb4e999cb7cb92275d0969689), license는 [MIT](https://github.com/epoko77-ai/im-not-ai/blob/14aeb52d13e737beb4e999cb7cb92275d0969689/LICENSE)다.

이 저장소는 UI 디자인 시스템이 아니라 한국어 윤문 skill이다. 따라서 palette나 component를 가져오지 않고 [quick rules](https://github.com/epoko77-ai/im-not-ai/blob/14aeb52d13e737beb4e999cb7cb92275d0969689/.claude/skills/humanize-korean/references/quick-rules.md)와 [rewriting playbook](https://github.com/epoko77-ai/im-not-ai/blob/14aeb52d13e737beb4e999cb7cb92275d0969689/.claude/skills/humanize-korean/references/rewriting-playbook.md)의 다음 원칙만 A&I 문서 검수 기준으로 다시 쓴다.

- 기술 사실, 수치, 상태 코드, 파일 경로, 고유명사와 인과관계를 보존한다.
- 문서 전체를 자동 윤문하지 않고 문제가 확인된 span만 수정한다.
- theory를 칼럼이나 마케팅 문구로 바꾸지 않고 교육 문서의 register를 유지한다.
- 추상적인 강조 대신 실제 actor, 입력 조건, 상태 변화, 테스트와 runtime 증거를 쓴다.
- 과도한 영어 병기, `X: Y` 헤딩 반복, 기계적인 병렬, 같은 종결어미, 불필요한 접속사와 meta 문장을 줄인다.
- 절차를 나타내는 번호와 checklist는 유지한다. 실제 순서가 아닌 장식 번호와 반복 badge만 제거한다.
- 자연스러움 검수와 기술 정확성 검수를 분리하고 의미가 달라지면 해당 edit를 롤백한다.

원본 Skill, 표, 스크립트와 긴 설명은 복사하지 않는다. 이후 실질적인 원문을 가져와야 한다면 저작권 문구와 MIT license를 함께 보존한다.

### 16.4 Revised Subject, Audience, Single Job

- Subject: 실제 백엔드 요청이 책임 경계를 통과하며 객체, 상태, 권한, artifact 또는 event로 바뀌는 과정을 추적하는 학습 환경.
- Audience: 개별 용어는 배웠지만 `PostCreateRequest → PostEntity → row`, `Bearer token → Authentication`, `cache miss → DB read → refill`처럼 시간 순서와 상태 변화를 아직 연결하지 못하는 A&I 백엔드 학습자.
- Single Job: 현재 message의 출발, 도착, 전달물과 변화 전후를 같은 시야에 두어 다음 단계의 결과를 자기 말로 설명하게 한다.

### 16.5 Palette와 Typography 사용 보정

4절의 core palette와 5절의 system font 원칙은 유지한다. 새 색을 추가하지 않고 사용량만 줄인다.

- A&I Navy는 participant heading과 중요한 책임 경계에만 쓴다.
- Signal Blue는 현재 message와 현재 `before → after` 한 곳에만 쓴다.
- Evidence Teal은 실제로 관찰한 code, test, runtime 또는 manual evidence에만 쓴다.
- Boundary Line은 lifeline과 system boundary를 그리는 구조선이다. 모든 card border로 반복하지 않는다.
- Display role은 현재 질문 하나에만 사용한다.
- Body role은 이론과 단계 설명에 사용한다.
- Utility/Data role은 HTTP, DTO, Entity, status, command, path와 payload에만 사용한다. 한국어 meta label과 버튼을 전부 mono나 uppercase로 만들지 않는다.

### 16.6 Layout Comparison

#### Direction A — Step Card Inspector

```text
┌──────────────────────────────────────────────────────────┐
│ [Client] [Controller] [Service] [Repository] [DB]       │
├──────────────────────────────────────────────────────────┤
│ [01 A → B] [02 B → C] [03 C → C] [04 C → D] [05 D → E]│
├──────────────────────────────────────────────────────────┤
│ Current step card                 Reason card            │
└──────────────────────────────────────────────────────────┘
```

현재 구현과 가깝고 구현 비용은 낮다. 그러나 actor와 message가 공간적으로 연결되지 않아 학생은 카드 안의 문자열을 다시 조립해야 한다. viewport에 따라 시간 순서도 줄바꿈된다.

#### Direction B — Lifeline Sequence와 변화 기록

```text
┌──────────────────────────────────────────────────────────┐
│ Client       Controller       Service       Repo      DB │
│   │              │               │             │       │ │
│ 1 │── POST + JSON ──────────────>│             │       │ │
│   │   변화: JSON body → PostCreateRequest       │       │ │
│   │              │               │             │       │ │
│ 2 │              │── create(req) ─────────────>│       │ │
│   │              │   책임: HTTP 입구 → 처리 순서       │ │
│   │              │               │             │       │ │
│ 3 │              │               └─ self call ┐│       │ │
│   │              │   변화: Request DTO → Entity│       │ │
│   │              │               │             │       │ │
│ 4 │              │               │── save ────>│       │ │
│ 5 │              │               │             │─INSERT>│ │
│   │              │               │  상태: row 없음 → id가 있는 row│
└──────────────────────────────────────────────────────────┘
```

Direction B를 선택한다. participant는 한 번만 선언하고 시간은 위에서 아래로 흐른다. 현재 message 바로 아래에 `들어온 것`, `이 책임에서 한 일`, `나간 것 또는 남은 상태`, `확인 근거`를 붙인다.

모바일에서는 desktop lifeline을 축소하지 않는다. 한 단계가 하나의 세로 문장이 된다.

```text
단계 3 / 5

PostService
  └─ 변환: PostCreateRequest → PostEntity
     들어온 것  PostCreateRequest
     바뀐 것    저장 가능한 PostEntity
     확인       PostService.create(...)

[이전 단계]                         [다음 단계]
```

### 16.7 Signature Element와 Motion

공통 signature는 `Diagnostic Lifeline` 하나만 사용한다. 이 영문 이름을 화면 badge로 노출하지 않고, 학생이 보는 제목은 `요청이 바뀌는 과정`, `토큰이 인증으로 바뀌는 과정`, `캐시가 다시 채워지는 과정`처럼 해당 주제의 실제 변화로 쓴다.

signature의 물리적 형태는 lifeline 위 현재 message와 그 아래의 `before → after` 변화 기록이다. topic SVG는 선행 관계를 설명하는 보조 자료이고 두 번째 signature가 아니다.

- 핵심 순간: 다음 단계 선택 뒤 현재 message와 변화 기록이 함께 갱신되는 순간.
- duration: `240ms`.
- easing: `cubic-bezier(0.2, 0.8, 0.2, 1)`.
- 반복: 없음.
- motion 대상: 현재 message 선 한 개와 변화 기록의 배경 전환.
- reduced motion: animation과 smooth scroll을 제거하고 같은 message, label과 before/after를 즉시 표시.

### 16.8 Sequence Diagram Grammar

- participant header와 lifeline은 `workbench.nodes`의 stable id, label, icon, role과 boundary를 사용한다.
- 시간은 항상 위에서 아래로 흐른다. CSS auto-fit grid로 순서를 표현하지 않는다.
- message는 실제 `from`, `to`, `verb`, `payload`, `kind`를 사용한다.
- request/call은 실선, response는 역방향 화살표, event는 점선, failure는 중단 표식으로 보조 구분한다. 동사와 상태 label은 항상 visible text로 남긴다.
- self-call은 같은 participant에서 나갔다 돌아오는 loop로 표시한다.
- 지나간 message는 읽을 수 있는 상태로 남기고, 현재 message만 강조하며, 다음 message는 `다음` label과 점선으로 구분한다.
- lane이 순차 관계라면 마지막 단계의 다음 버튼은 `다음 경로 · 저장 결과와 응답`처럼 이어진다. 분기 관계라면 `다른 조건 경로`로 명시하고 자동으로 정답 경로를 선택하지 않는다.
- `notReached`는 회색 장식이 아니라 `왜 실행되지 않았는가`를 해당 중단 message 가까이에 표시한다.
- actor role을 `title` 속성에만 두지 않는다. touch와 keyboard에서도 보이는 짧은 책임 설명을 제공한다.
- topic SVG는 예측 뒤 compact premise로 한 번만 표시한다. 같은 topology를 actor card로 다시 반복하지 않는다.

### 16.9 Data Contract Revision

현재 `nodes`, `from`, `to`, `verb`, `payload`, `kind`, `concept`, `check`, `codePointIds`, `notReached`는 유지한다. 좌표나 중복 message 데이터를 추가하지 않는다.

stable participant 순서와 lane 관계를 위해 다음 optional field를 추가한다.

```js
diagram: {
  participants: ["client", "postController", "postService", "postRepository", "mysql"],
  lanes: [
    {
      id: "request-persist",
      nextLaneIds: ["saved-response"],
      steps: []
    }
  ]
}
```

학생이 변화 전후를 읽을 수 있도록 모든 semantic step에 `effect`를 작성한다. 이는 message payload를 복제하는 필드가 아니라 그 단계가 시스템에 남긴 차이를 설명한다.

```js
{
  from: "postService",
  to: "postService",
  verb: "변환",
  payload: "PostCreateRequest → PostEntity",
  kind: "transform",
  effect: {
    kind: "transform",
    subject: "게시글 데이터",
    before: "PostCreateRequest",
    after: "PostEntity"
  },
  evidenceScope: "code",
  check: "PostService.create(...)에서 Entity 생성 지점을 봅니다."
}
```

`effect.kind`는 `transfer`, `transform`, `persist`, `gate`, `return`, `fanout`, `verify`, `preserve`로 제한한다.

- 데이터가 바뀌지 않고 책임만 이동하면 `transfer`로 쓰고 before/after가 같음을 숨기지 않는다.
- DB, cache, session, artifact가 생기거나 사라지면 `persist`로 상태 전후를 쓴다.
- 400, 401, 403 또는 pipeline failure에서 멈추면 `gate`로 도달하지 않은 상태를 쓴다.
- 리팩토링처럼 동작을 지키는 주제는 `preserve`로 같은 입력, 반환, 예외와 협력자 호출을 명시한다.
- event와 broadcast는 `fanout`으로 한 message가 어떤 queue 또는 subscribed session으로 전달됐는지 쓴다.

`evidenceScope`는 `code`, `test`, `runtime`, `manual`, `concept` 중 하나다. 기존 `check`와 `codePointIds`를 그대로 사용하되 UI에서 보장 범위를 색상이 아닌 text label로 표시한다.

legacy fallback은 renderer가 읽을 수 있게 남기지만, 00~12 전체 적용 완료 시에는 50개 scenario의 모든 visible step이 새 계약을 만족해야 한다. content spec과 validator를 먼저 고친 뒤 데이터를 수정한다.

### 16.10 Theory Document Structure

새 theory 파일은 만들지 않는다. 아래 8개 기존 파일 안에 00~12의 안정적인 anchor를 둔다.

```text
#seq-00
#seq-01
#seq-02
...
#seq-12
```

각 시퀀스 절은 같은 제목을 복사하지 않고 주제에서 나온 질문으로 시작한다. 다만 정보 역할은 다음 순서를 지킨다.

```text
구체적인 상황
-> 한 번에 읽는 주 경로
-> 단계에서 바뀌는 것
-> 이 책임을 나눈 이유
-> 코드에서 볼 위치
-> 실행으로 확인할 증거와 아직 보장하지 않는 것
-> 결과를 숨긴 Visual Lab 진입 링크
```

Theory에는 시퀀스별 핵심 path 하나를 Mermaid `sequenceDiagram`으로 넣는다. alternate scenario를 모두 펼치지 않고 기본 인과를 이해하는 데 필요한 3~7개 message만 둔다. diagram 바로 아래에는 다음 text table을 두어 Mermaid를 렌더링하지 못하거나 screen reader를 사용하는 학생도 같은 의미를 읽게 한다.

| 단계 | 들어온 것 | 이 책임에서 한 일 | 나간 것 또는 남은 상태 |
|---|---|---|---|
| 실제 순서 | 실제 입력 | 실제 동작 | 실제 출력·상태 |

Theory diagram은 개념 경로를 설명하고 Visual Lab은 조건을 바꿔 실제 분기, 미도달 지점과 evidence를 관찰한다. 두 문서에 50개 scenario를 그대로 복제하지 않는다.

상호 링크는 다음처럼 연결한다.

- theory 절 끝: `Visual Lab에서 입력 조건을 보고 경로 예측하기`.
- Visual Lab evidence: 현재 sequence의 정확한 theory anchor 한 개.
- 필요한 경우에만 `scenario.theoryRef`로 더 좁은 절을 가리킨다. 모든 edge에 같은 링크를 반복하지 않는다.
- link 문구에서 `HIT`, `401`, `성공`, `blocked` 같은 결과를 먼저 말하지 않는다.

DB Access theory는 새 파일로 나누지 않고 02 영속성, 03 검증, 04 인증·인가, 05 외부 신뢰·복구, 06 테스트 범위를 각각 독립 절로 확장한다. Deployment theory도 09 runtime과 10 pipeline을 분리한다.

### 16.11 Korean Copy Rules

화면 안 meta label은 다음 기준으로 정리한다.

| 현재 표현 | 계획 표현 |
|---|---|
| `SYSTEM STORY` | 제거. 주제별 `요청이 바뀌는 과정` 계열 제목 사용 |
| `PREDICT 01` | 제거. 실제 두 번째 단계가 없는 장식 번호를 쓰지 않음 |
| `PREDICT → OBSERVE` | `내 예상 / 실제 흐름` |
| `Selected evidence` | `이 단계에서 확인할 근거` |
| `Verification` | `내 말로 설명해 보기` |
| `Next question` | `다음에 이어서 볼 것` |
| 결과 공개 직후 `확인 완료` | `경로 공개됨` 또는 label 제거. checklist 완료와 구분 |
| 반복되는 `워크벤치` | `요청 왕복`, `영속화 경계`, `인증 경계`, `테스트 범위`처럼 주제 명사 사용 |

버튼은 `확인하기`, `열기`보다 결과를 예측할 수 있는 동사를 쓴다. 예: `실제 전달 순서 보기`, `다음 message 보기`, `다른 조건과 비교하기`.

코드 설명은 파일 경로 badge나 tag로 시작하지 않는다. 학생이 먼저 읽어야 할 것은 경로가 아니라 코드가 맡은 일이다.

```text
한 문장 주석
-> 실제 핵심 코드 3~12줄
-> 이 코드가 바꾸는 상태 또는 다음 책임 한 문장
```

- Visual Lab의 code evidence는 파일 경로 tag를 숨기고 짧은 한국어 주석을 code block 바로 위에 둔다.
- theory의 `핵심 코드로 연결하기` 파일 목록은 주제별 핵심 code block으로 바꾼다.
- code block은 실제 저장소 코드에서 가져오고 긴 완성 답안이나 관계없는 boilerplate를 붙이지 않는다.
- 주석은 `// 여기서 요청을 Service로 넘깁니다.`처럼 학생이 지금 볼 판단을 말한다. class 이름을 다시 읽어주는 설명은 쓰지 않는다.
- Kotlin, JavaScript, YAML, shell, Dockerfile 등 언어에 맞는 주석 문법을 code block 안에 쓸 수 있다. 문법을 깨뜨릴 위험이 있으면 code block 바로 위의 짧은 문장으로 대신한다.
- 전체 파일 경로가 꼭 필요하면 primary label이 아니라 접힌 reference shelf의 `전체 코드 위치` link로만 제공한다.

Theory copy 검수에서는 다음 반복을 우선 찾는다.

- `왜 이 코드를 보는지 먼저 정리합니다.` 같은 meta 문장.
- 모든 단락의 `이번 시퀀스는`, `확인합니다`, `문제를 해결합니다` 반복.
- 의미 없는 `배경:`, `선택한 방식:` colon heading.
- 불필요한 영어 병기와 uppercase label.
- 같은 길이와 같은 종결어미가 이어지는 문단.
- 기술 근거 없이 `핵심`, `완벽한`, `강력한`, `중요한`으로만 강조한 문장.

API, JWT, Redis, STOMP, DTO, Entity, class·method 이름, 상태 코드와 파일 경로는 임의로 번역하거나 쉬운 말로 바꾸지 않는다. 첫 등장에만 짧은 한국어 역할을 덧붙인다.

### 16.12 Sequence and Theory Mapping

| Seq | Visual sequence grammar | 단계 변화의 중심 | Theory 보강 |
|---|---|---|---|
| 00 | 독립 HTTP·Git·DB lane | request/response, working tree→commit, row→PK 식별 | body만 보던 상태에서 status와 body를 함께 읽는 이유 |
| 01 | request와 reverse response | Request DTO→Post→memory→Response DTO | 메모리 수명과 DTO 책임 |
| 02 | persistence와 response 연속 lane | Request DTO→Entity→row/id→Response DTO | memory와 DB 수명, 없는 id에서 save 미도달 |
| 03 | early-stop gate | invalid input→400, missing entity→404 | Validation과 Service failure 경계 |
| 04 | token issuance와 다음 request 분리 | credentials→JWT, header→Authentication, author mismatch→403 | 인증 401과 인가 403의 다른 최초 분기 |
| 05 | callback·collision·recovery branch | verified identity→internal account→JWT, recovery request→mail request | 외부 신뢰, LOCAL 충돌, link 생성과 reset 완료의 차이 |
| 06 | Given→When→Then과 보장 범위 lane | fixture/mock→service result→assertion | unit test와 HTTP policy evidence 분리 |
| 07 | cache state sequence | empty→miss→DB→refill, warm→hit, write success→evict | 원본과 복사본, TTL과 invalidation |
| 08 | transport→session→subscription→fan-out | OPEN→CONNECTED→SUBSCRIBED, message→구독 session | native WebSocket, Origin, 연결과 구독의 차이 |
| 09 | artifact/runtime sequence | source→jar→build context gate→image→container→process→health evidence | `.dockerignore` blocker, 명령 성공과 실행 정상의 차이 |
| 10 | gated pipeline | source→artifact→deploy shell→verify, 첫 failure→later blocked | answer-only job 구조와 현재 heredoc blocker를 성공 목표와 분리 |
| 11 | paired before/after sequence | 유지된 계약과 trim·예외·저장 같은 의도적 변경을 별도 lane으로 분리 | 실제 Before/After, unchanged test subset과 change ledger |
| 12 | sync response와 async event lane | request→response와 event→broker→consumer 분리 | consumer 완료, 중복, 재시작과 publish failure 한계 |

모든 주제에 Before/After card를 강제하지 않는다. 03·04·05는 조건과 최초 분기, 07·09·10은 상태 전이, 11은 실제 Before/After, 12는 동기·비동기 lane 비교가 주 문법이다.

### 16.13 Component Mapping

#### 변경

- Hero의 구조는 유지하고 meta copy와 높이를 줄여 현재 질문과 첫 조건을 더 가깝게 둔다.
- prediction gate는 유지하되 장식 영문, quiz praise와 조기 `확인 완료`를 제거한다.
- actor card strip과 transition card grid를 participant header, lifeline과 message row로 교체한다.
- `story-current` 중복 panel을 없애고 현재 message 안에 변화 기록과 evidence를 펼친다.
- lane button은 direct 선택과 함께 순차 `다음 경로` 또는 분기 `다른 조건 경로` 관계를 말한다.
- scenario-wide snapshot과 outcome은 마지막 message 뒤의 정리 영역으로 옮겨 현재 step 설명과 경쟁하지 않게 한다.
- Evidence section은 현재 step에서 이미 보인 설명을 반복하지 않고 code/test/runtime detail만 확장한다.
- theory link는 문서 루트가 아니라 현재 시퀀스 anchor를 가리킨다.
- 50개 scenario에 observation title과 reflection을 둬 실제 경로를 본 뒤 인과 규칙을 한 문장으로 다시 쓰게 한다.
- 모바일은 participant card 선행 목록을 제거하고 한 단계씩 `from → message → to → effect`로 읽는다.

#### 유지

- 기존 local SVG icon과 13개 topic SVG는 실제 asset이 보이고 주제별 관계를 설명하므로 유지한다.
- prediction 전에 결과를 숨기는 계약은 답을 먼저 노출하지 않기 위해 유지한다.
- native radio, button, progress, checkbox와 focus restoration은 keyboard 접근성을 위해 유지한다.
- `window.visualLabData`, scenario, flow, node, code point, checklist와 next 계약은 기술 콘텐츠와 기존 경로 호환 때문에 유지한다.
- hub journey, topbar의 repository/sequence context와 static HTML entry는 독립 GitHub Pages 실행 때문에 유지한다.
- empty, fatal, image fallback과 `notReached` 데이터는 실패 원인과 확인 파일을 안내하므로 유지하고 새 diagram 문법에 맞춰 표현만 바꾼다.

### 16.14 Implementation Phases

#### Phase 0 — 정확성 및 기준 화면

1. 08의 SockJS와 broadcast 범위를 실제 native WebSocket·topic subscription 기준으로 교정한다.
2. 00~12 현재 화면을 같은 scenario와 viewport로 다시 저장한다.
3. 50개 scenario의 lane 관계, self-call, reverse response, branch와 evidence 범위를 표로 확정한다.

#### Phase 1 — Contract and Validator

1. central content spec에 `participants`, `nextLaneIds`, `effect`, `evidenceScope`, `theoryRef`, `reflection`을 정의한다.
2. validator에 node·lane reference, effect enum, theory anchor와 상대 link 검사를 추가한다.
3. 공통 renderer가 legacy data도 안전하게 읽는 fallback을 먼저 만든다.

#### Phase 2 — Four-sequence Prototype Gate

다음 네 주제를 먼저 구현해 같은 template을 복제하기 전에 문법을 검증한다.

- 02: self-call, DTO→Entity, persist와 reverse response.
- 04: token issuance, 다음 request, 401/403 gate.
- 07: miss/hit/TTL/evict 상태 변화.
- 12: sync response와 async event branch.

1440×1000과 390×844에서 학생이 현재 actor, 전달물, before/after와 증거를 한 viewport에서 읽을 수 있어야 다음 시퀀스로 확장한다. 이 gate에서 screenshot과 genericity critique를 다시 수행한다.

#### Phase 3 — Theory Rewrite

1. DB Access theory를 02~06 절로, Deployment theory를 09·10 절로 확장한다.
2. 나머지 theory에 시퀀스 anchor, 핵심 Mermaid sequence, text table과 Visual Lab 링크를 추가한다.
3. `im-not-ai` 기준으로 탐지된 meta copy만 국소 수정한다.
4. 각 수정은 기술 사실·코드 경로·테스트 보장 범위 fidelity audit를 별도로 통과한다.

#### Phase 4 — 00~12 Rollout

1. 00·01·03·05·06·08·09·10·11을 주제별 문법으로 구현한다.
2. shared CSS/JavaScript를 8개 토픽 저장소에 같은 checksum으로 동기화한다.
3. 50개 scenario의 effect, evidence scope, theory reference와 reflection을 채운다.

#### Phase 5 — Browser and Documentation Review

1. 00~12 모든 scenario, 8개 hub와 theory 왕복 link를 검수한다.
2. visual design guide, content spec, implementation plan, agent rule과 review 문서를 실제 코드에 맞춘다.
3. child repository를 먼저 검증·commit·push하고 중앙 submodule pointer는 별도 commit으로 갱신한다.

### 16.15 Genericity Critique와 보정

첫 계획을 단순한 UML sequence diagram으로 끝내면 다른 API 문서에도 그대로 붙일 수 있고 초보자에게는 화살표 수만 늘어난다. 이를 다음처럼 보정한다.

- sequence diagram의 signature는 lifeline 자체가 아니라 현재 message에 붙는 실제 `before → after` 변화 기록이다.
- actor마다 동일한 card를 반복하지 않고 topic SVG, lifeline, effect가 서로 다른 역할을 맡는다.
- 03의 중단, 07의 cache 수명, 08의 subscription, 09의 runtime, 11의 contract/change ledger, 12의 async branch를 같은 사각형 template으로 만들지 않는다.
- 번호는 실제 message 순서에만 사용한다. `PREDICT 01` 같은 장식 번호는 제거한다.
- 다크 배경, blue accent, icon을 제거해도 `조건 → 예측 → message → 상태 변화 → evidence → 다음 질문`이 남게 한다.

`im-not-ai` 원칙을 과하게 적용해 모든 문장을 구어체로 바꾸거나 목록을 산문으로 합치면 기술 문서가 더 어려워진다. 절차 list, command, API, 전문 용어는 그대로 두고 반복 meta 문장과 번역투만 고친다. 변화율이 큰 절은 자연스러움보다 fidelity를 먼저 재검수한다.

Theory에 13개 Mermaid diagram을 넣는 것 역시 template가 될 수 있다. 각 diagram은 한 개의 실제 인과만 설명하고, heading은 `배경`, `선택한 방식`을 복사하지 않고 `MISS 뒤에 DB를 읽는 이유`, `401과 403이 갈라지는 지점`처럼 주제에서 직접 가져온다.

### 16.16 Completion Gate

- 13개 sequence와 50개 scenario의 모든 visible message에 from, to, verb, payload, kind와 effect가 있다.
- participant id, next lane, code point와 theory anchor reference가 모두 유효하다.
- 50개 scenario에 결과를 먼저 노출하지 않는 prediction과 관찰 뒤 reflection이 있다.
- 8개 theory 문서에서 Visual Lab으로 이동하고 13개 Visual Lab에서 정확한 theory 절로 돌아온다.
- theory와 code evidence를 각 시퀀스의 guide·implementation·answer branch 실제 코드와 대조하고, TODO와 완성 뒤 코드의 범위를 구분한다.
- visible effect에는 `호출 전/후 책임`, `반환 대기/보유`, `판정 입력/결과` 같은 자동 생성형 틀 문장이 없고 실제 값 또는 시스템 상태가 적힌다.
- DB Access 02~06과 Deployment 09·10이 theory 안에서 독립된 인과 흐름을 가진다.
- 08 문서는 native WebSocket, topic subscribed session과 실제 자동 테스트 범위를 정확히 말한다.
- desktop에서 participant lifeline과 수직 시간축이 보이며 self-call, response, event, failure가 text와 선 방향으로 구분된다.
- 390px에서 첫 message가 actor 목록 아래로 밀리지 않고 page-level horizontal overflow가 없다.
- 현재 message, effect, reason, evidence와 이전/다음 control이 한 viewport에 있다.
- 200% zoom에서 message label, 긴 한국어, command와 code가 겹치지 않는다.
- keyboard focus가 visible하고 scenario, lane, message 변경 뒤 복원된다.
- reduced motion에서 같은 상태가 정적으로 보인다.
- console error, broken image와 clipped focus outline이 0이다.
- 학생 관점 smoke에서 현재 단계의 `누가`, `누구에게`, `무엇을`, `무엇으로 바뀌었는지`, `어디서 확인할지` 다섯 질문에 답할 수 있다.
- theory의 Mermaid가 지원되지 않는 환경에서도 인접 text table로 같은 순서를 읽을 수 있다.
- `node --check`, manifest, sequence, Visual Lab, color, link/anchor validator와 `git diff --check`가 모두 통과한다.

### 16.17 Planned File Scope

중앙 저장소에서 갱신할 후보는 다음과 같다.

```text
docs/audit/visual-lab-design-system-audit.md
docs/audit/visual-lab-design-system-plan.md
docs/audit/visual-lab-design-system-review.md
docs/visual-lab-design-guide.md
docs/visual-lab-content-spec.md
docs/visual-lab-implementation-plan.md
docs/agent/visual-lab-rules.md
scripts/validate-visual-labs.py
```

각 토픽 저장소에서 갱신할 후보는 다음과 같다.

```text
docs/theory.md
docs/visual-lab/styles.css
docs/visual-lab/visual-lab.js
docs/visual-lab/sequences/NN/visual-lab-data.js
```

기존 `index.html`, icon과 topic SVG는 경로 계약 또는 기술 설명이 바뀌지 않는 한 유지한다. 새 framework, package, external font, CDN과 장식 asset은 추가하지 않는다.

## 17. System Layer Color와 읽기 부담 보정 계획

이 절은 2026-07-16에 02, 07, 12를 1440px과 390px에서 다시 읽은 뒤 추가한다. 기존 구현은 현재 message와 상태 변화는 보여주지만 participant가 어느 시스템 레이어에 속하는지는 같은 흰색 node, 같은 회색 lifeline과 시퀀스마다 다른 `boundary` 문구를 읽어야만 알 수 있다.

### 17.1 Subject, Audience, Single Job

- Subject: 실제 백엔드 요청이 외부 호출자, 입구, 애플리케이션 판단, 상태 자원, 외부 연동과 실행 기반 사이를 이동하는 위치 추적 환경.
- Audience: Controller, Service, Repository, DB를 개별 용어로는 알지만 Redis, broker, container까지 포함한 전체 흐름에서 현재 위치를 즉시 구분하기 어려운 학습자.
- Single Job: 학생이 현재 message의 출발·도착 node가 어느 레이어에 있고 어떤 경계를 건너는지 5초 안에 말하게 한다.

### 17.2 Layer Contract와 지원 Palette

기존 `kind`와 자유로운 `boundary` 문구에서 위치를 추론하지 않는다. 모든 `workbench.nodes`에 다음 `systemLayer` 중 하나를 명시한다.

```text
outside      외부·호출자
interface    입구·출구
application  서비스·정책
resource     상태·데이터
integration  연동·메시징
runtime      실행·배포
```

core palette는 유지한다. 아래 색은 participant header, layer rail, lifeline, mobile actor와 topic SVG의 실제 system node에만 쓰는 지원 palette다. 본문은 항상 System Ink를 사용한다.

```css
:root {
  --layer-outside-surface: #F1F5F9;
  --layer-outside-line: #5B677A;
  --layer-interface-surface: #E6F4F7;
  --layer-interface-line: #0E7490;
  --layer-application-surface: #F2EDFF;
  --layer-application-line: #6D43A8;
  --layer-resource-surface: #EAF5EE;
  --layer-resource-line: #2C7352;
  --layer-integration-surface: #FFF4D6;
  --layer-integration-line: #926000;
  --layer-runtime-surface: #EEF2F7;
  --layer-runtime-line: #52627A;

  --state-current: #2955E4;
  --state-passed: #176F72;
  --state-failed: #B4233C;
  --state-pending: #6F82B8;
}
```

작은 layer label 대비를 실제 surface 위에서 다시 계산해 `outside` line은 `#5B677A`(5.23:1), `resource` line은 `#2C7352`(5.11:1)로 확정했다. 두 값은 4.5:1 경계에 걸치지 않도록 여유를 둔다.

레이어와 상태는 같은 CSS property를 덮어쓰지 않는다.

```text
레이어: 옅은 node surface, 상단 strip, lifeline, visible 한국어 label
상태: 현재 outline, message arrow, check·× marker, 현재·지남·다음·중단 text
```

### 17.3 Layout Comparison

#### Direction A — Participant 색상만 변경

```text
[외부 Client] [입구 Controller] [앱 Service] [상태 DB]
      │               │              │          │
```

변경량은 작지만 색을 모르면 그룹과 경계를 다시 각 node에서 읽어야 한다.

#### Direction B — Layer Rail과 Active-lane Lifeline

```text
외부          입구·출구       서비스·정책         상태·데이터
Client   ->   Controller  ->  Service  -> Repo -> MySQL
  │               │              │          │       │
  └──────── 현재 message와 before -> after ─────────┘
```

Direction B를 선택한다. 연속된 participant의 `systemLayer`를 한 번 묶어 읽고, node에도 같은 label과 tint를 반복해 가로·세로 위치를 함께 확인한다. 여러 lane이 있는 시퀀스는 전체 diagram의 participant 합집합이 아니라 현재 lane에 등장하는 participant만 배치한다. 다른 lane은 selector와 분기 설명으로 유지한다.

모바일에서는 desktop lifeline을 축소하지 않고 다음처럼 현재 경계를 직접 표시한다.

```text
[외부·호출자] Client
       요청 ↓
[입구·출구] PostController
```

### 17.4 Topic SVG 적용

- 00~06의 복제된 blue/teal node 문법을 실제 `systemLayer` node 색으로 교체한다.
- 07의 EMPTY, HIT, TTL, DEL 상태 문법은 유지하고 조회 정책은 application, Redis와 MySQL은 resource로 직접 표시한다.
- 08의 transport, subscription과 fan-out 구조는 유지하고 outside, interface, integration, resource 위치를 구분한다.
- 09~10은 artifact와 실행 기반, build/deploy/verify gate를 구분한다. 실패는 layer fill이 아니라 state marker로 표시한다.
- 11의 유지/변경 lane 색은 보존하고 lane 안 node에만 layer 색을 적용한다.
- 12의 producer return/broker delivery fork 색은 보존하고 Controller, Service, broker, queue와 consumer node 위치를 별도로 표시한다. 고정 SVG와 선택 scenario가 다른 이야기를 하지 않도록 필요한 scenario에 선택적 visual을 제공한다.

### 17.5 Motion

기존 Diagnostic Lifeline의 수동 step 전환 한 번만 유지한다. layer color는 움직이지 않고 현재 message의 state outline과 arrow만 240ms로 갱신한다. reduced motion에서는 같은 위치·state label을 즉시 표시한다.

### 17.6 Genericity Critique와 보정

첫 안처럼 6색을 page card 전체에 적용하면 일반 pastel architecture dashboard가 된다. icon 종류마다 색을 주면 기술 위치가 아니라 장식 분류가 되고, 모든 SVG를 같은 6단 column으로 만들면 cache cycle, runtime nesting과 event fork의 고유 구조가 사라진다.

따라서 다음처럼 제한한다.

- page chrome, 질문, code, evidence와 checklist는 기존 중립 표면을 유지한다.
- layer 색은 실제 system node와 lifeline에만 쓴다.
- 상태는 layer background를 덮지 않고 outline, line style, marker와 text로 표현한다.
- 각 SVG의 주제별 topology는 유지하고 node의 위치 문법만 통일한다.
- 색을 제거해도 visible layer label, boundary, from/to, verb와 payload로 같은 의미를 읽을 수 있어야 한다.

### 17.7 Completion Gate

- Visual Lab HTML의 raw `&` lint 오류가 0이다.
- 147개 node가 허용된 `systemLayer`를 가진다.
- 13개 SVG가 승인된 layer/state palette만 사용하고 layer 이름을 visible text로 제공한다.
- 12의 active lane은 필요한 participant만 렌더링하며 desktop에서 전체 lane 합집합을 강제하지 않는다.
- 390px current message에 출발·도착 layer와 boundary가 남는다.
- text 대비 4.5:1, non-text boundary 3:1을 만족한다.
- 13개 sequence와 50개 scenario에서 page overflow, broken image, console error가 0이다.
- keyboard focus, 200% zoom, reduced motion과 forced colors에서도 위치와 상태를 구분할 수 있다.
- shared CSS와 JavaScript는 8개 토픽 저장소에서 같은 hash를 유지한다.
