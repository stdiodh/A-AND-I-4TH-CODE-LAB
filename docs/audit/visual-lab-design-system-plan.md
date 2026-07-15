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
- 03/04/10은 실제 차단과 응답 경로, 07은 cache hit/miss branch, 08은 구독자 fan-out, 09는 build/runtime 경계, 11은 invariant comparison, 12는 request/event 두 lane을 사용한다.
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
| 11 | `11-behavior-invariant.svg` | 구조 변화와 유지되는 동작 |
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
