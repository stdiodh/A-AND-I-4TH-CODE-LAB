# Visual Lab 시퀀스 가독성·문구 감량 계획

작성일: 2026-07-16

완료일: 2026-07-16

상태: 완료

적용 Skill: `aandi-visual-lab-design`, `frontend-design`

## 1. Goal

시퀀스 다이어그램의 글자를 작게 만드는 방식으로 문제를 숨기지 않는다.
글자와 도형의 실제 경계를 다시 맞추고, 같은 사실을 여러 패널에서 반복하는 구조를 줄여 학생이 현재 한 단계를 빠르게 읽게 한다.

```text
누가
-> 누구에게
-> 무엇을 보냈고
-> 어떤 상태가 바뀌었으며
-> 어디서 확인하는가
```

이번 수정의 목표는 위 다섯 질문에 답하는 데 필요한 정보만 현재 단계에 남기는 것이다.
커리큘럼 범위, 기술 사실, 시퀀스 순서와 증거 범위는 바꾸지 않는다.

## 2. Current Audit

### 2.1 조사 범위

| 항목 | 수량 |
|---|---:|
| 토픽 저장소 | 8 |
| 시퀀스 | 13 |
| 시나리오 | 50 |
| lane | 89 |
| message step | 388 |
| 설명 SVG | 16 |

8개 저장소의 공통 `visual-lab.js`와 `styles.css`는 현재 같은 내용이다.
따라서 renderer와 responsive layout은 한 번 설계하고 8개 저장소에 같은 checksum으로 반영한다.

### 2.2 반복이 생기는 위치

현재 한 step의 정보는 다음 순서로 반복된다.

```text
lifeline message
-> mobile current card
-> current detail heading
-> before / after
-> current evidence
-> 아래 evidence section
-> mobile step jump list
```

정량 조사 결과는 다음과 같다.

- `effect.subject === step.payload`: 237 / 388 step, 61.1%
- `step.check`가 있는 115개 step은 current detail과 evidence section에 같은 확인 문장을 두 번 표시한다.
- desktop은 active payload를 message와 current detail에 두 번 표시한다.
- mobile은 actor, verb, payload와 before/after를 각각 두 번 표시한다.
- `observationTitle`과 `diagram.caption`은 21 / 50 scenario에서 의미가 크게 겹친다.
- `prediction.explanation`과 `outcome`은 17 / 50 scenario에서 같은 결론을 다시 말한다.
- `diagram.caption`과 `evidence`는 16 / 50 scenario에서 경로와 증거가 섞여 반복된다.

390×844의 02 첫 step에서 반복 영역의 현재 높이는 다음과 같다.

| 영역 | 높이 |
|---|---:|
| mobile current card | 약 446px |
| current detail | 약 654px |
| 이전·다음 controls | 약 93px |
| step jump list | 약 340px |
| 합계 | 약 1,533px |

같은 `Client -> PostController`, `POST /posts + JSON body`, before/after를 읽기 위해 모바일 viewport 약 두 개를 사용하고 있다.

### 2.3 SVG에서 확인한 문제

P0는 실제 글자·선 겹침 또는 사실상 padding이 없는 상태다.

| 우선순위 | Asset | 현재 문제 |
|---|---|---|
| P0 | `05-external-trust.svg` | `외부 신뢰 경계` 글자와 failure box가 겹치며 `OAuth 인증 성공`의 좌우 여백이 약 5 unit이다. |
| P0 | `08-connection-subscription-fanout.svg` | `구독자 집합 생성` 글자가 수직 event arrow를 가로지른다. |
| P0 | `09-runtime-nesting.svg` | `SPRING PROCESS`가 box 폭을 거의 모두 사용하고 다음 레이어 문구와 충돌한다. |
| P0 | `12-duplicate-idempotency.svg` | 54 unit 높이 box 안에 24px 두 줄을 22 unit 간격으로 배치해 글자가 붙어 보인다. |
| P1 | `01-memory-crud-map.svg` | response label과 return stroke의 간격이 부족하다. |
| P1 | `02-persistence-boundary.svg` | `Request DTO`, `서비스·정책`의 내부 여백이 약 4 unit이며 `Request DTO`가 box 밖으로 보인다. |
| P1 | `03-request-gates.svg` | Repository와 404 card 중심이 8 unit 어긋나고 card가 outer frame보다 오른쪽으로 나간다. |
| P1 | `06-test-scope.svg` | 설명과 HTTP box가 붙고 HTTP box가 outer frame 하단에 사실상 닿는다. |
| P1 | `10-pipeline-gates.svg` | 긴 node text 여백이 부족하고 `빌드·실행`을 다섯 번 반복한다. |
| P1 | `11-behavior-invariant.svg` | pass bar의 수직 padding이 거의 없고 footer가 위 badge를 다시 설명한다. |
| P1 | `12-response-event-fork.svg` | `연동·메시징`을 네 번 반복하고 footer가 lane 결론을 다시 말한다. |
| P1 | `12-failure-boundaries.svg` | title, subtitle, lane, failure box가 같은 실패 경계를 반복한다. |
| P2 | `00-request-tool-map.svg` | 연속 node에 `시스템 밖`을 네 번 반복한다. |
| P2 | `04-auth-boundaries.svg` | 충돌은 없지만 같은 레이어명을 각 node에서 반복한다. |
| P2 | `07-cache-state-cycle.svg` | 네 node의 `상태·데이터`를 group label 하나로 합칠 수 있다. |
| P2 | `12-direct-call.svg` | `같은 call stack`, `같은 thread`, `동기 경로`가 같은 사실을 세 번 말한다. |

## 3. Design Direction

### Subject

백엔드 요청과 상태가 실제 책임 경계를 지나는 한 순간을 읽는 학습 환경.

### Audience

Controller, Service, Repository, DB, broker와 runtime 용어는 배웠지만 긴 다이어그램 안에서 현재 변화를 빠르게 찾기 어려운 Spring Boot 학습자.

### Single Job

학생이 현재 step에서 `출발 책임`, `도착 책임`, `전달 값`, `상태 변화`, `확인 근거`를 한 시선 흐름으로 읽게 한다.

### Core Palette

이번 문제는 색 부족이 아니라 정보 중복과 geometry 문제이므로 기존 palette를 유지한다.

| 이름 | HEX | 역할 |
|---|---|---|
| Lab Paper | `#F8F9FB` | canvas |
| System Ink | `#111B3F` | 본문과 node 이름 |
| A&I Navy | `#0C2691` | 질문과 판단 제목 |
| Signal Blue | `#2955E4` | 현재 message |
| Evidence Teal | `#3F8996` | 확인 근거와 변화 이후 |
| Boundary Line | `#C9D6F3` | 실제 책임 경계 |

기존 여섯 `systemLayer` 지원색도 유지한다. 새 색, gradient와 glow는 추가하지 않는다.

### Typography Roles

| 역할 | 기준 | 사용 위치 | 금지 |
|---|---|---|---|
| Display | system sans, 700~900, line-height 1.08~1.2 | H1과 주차의 핵심 질문 | SVG node 설명, 긴 문장 |
| Body | system sans, 400~700, line-height 1.55~1.7 | 한국어 이유, 비교, reflection | path·class 정렬 |
| Utility/Data | system mono, 500~800, line-height 1.4~1.55 | verb, payload, status, code, progress | 긴 한국어 결론 |
| SVG node | system sans 또는 실제 identifier만 mono, 650~850 | actor와 state | 레이어 label과 같은 크기·굵기 |

외부 font와 font import는 추가하지 않는다.

## 4. Layout Comparison

### Direction A — Lifeline + Current Inspector

```text
┌──────────────────────────────────────────────────────────┐
│ 현재 조건 · 관찰할 질문                                 │
├───────────────────────────────┬──────────────────────────┤
│ 외부 ┆ 입구 ┆ 서비스 ┆ 상태   │ 현재 2 / 5 · 저장       │
│                               │                          │
│ Client ┆ Controller ┆ Service │ PostService -> Repository│
│        -- 이전 message --     │ save(PostEntity)        │
│        == 현재 message ==     │                          │
│        -- 다음 message --     │ 이전        이후        │
│                               │ Entity  ->  저장 요청    │
│                               │ [코드 근거 보기]         │
├───────────────────────────────┴──────────────────────────┤
│ 이전 단계              2 / 5              다음 단계     │
└──────────────────────────────────────────────────────────┘
```

장점:

- 전체 시스템 위치와 현재 상태 변화를 동시에 본다.
- 기존 `Diagnostic Lifeline` 정체성을 유지한다.
- message와 before/after 사이의 시선 이동이 짧다.

### Direction B — Expanded Step Timeline

```text
┌──────────────────────────────────────────────┐
│ 1  Client -> Controller · 요청        완료  │
├──────────────────────────────────────────────┤
│ 2  Controller -> Service · 호출       현재  │
│    create(request)                           │
│    Request DTO -> Service 입력               │
│    [근거 보기]                               │
├──────────────────────────────────────────────┤
│ 3  Service -> Repository · 저장        다음 │
└──────────────────────────────────────────────┘
```

장점은 단순함이지만 일반적인 stepper처럼 보이고 participant 사이 거리와 lifeline 의미가 약해진다.

### 선택

Direction A를 선택한다.

- 1100px 이상: lifeline과 current inspector를 나란히 둔다.
- 720~1099px: 전체 stage를 축소하거나 가로 스크롤하지 않고 현재 step 집중 layout을 사용한다.
- 719px 이하: `from actor -> verb/payload -> to actor -> before/after` 한 열만 남긴다.

390px 집중 layout은 다음 한 surface로 끝낸다.

```text
현재 2 / 5 · 호출

[입구] Controller
       ↓ create(request)
[서비스] Service

Request DTO -> Service 입력

[이전]       2 / 5       [다음]
[코드 근거 보기]
```

별도의 mobile current card와 current detail을 연이어 만들지 않는다.

## 5. Signature and Motion

Signature는 새로 만들지 않고 `Diagnostic Lifeline` 하나를 유지한다.
이번 수정의 기억 요소는 더 많은 장식이 아니라 현재 message와 바로 옆의 상태 변화 기록이다.

- motion moment: 이전·다음 step을 선택해 active message가 바뀌는 순간
- duration: 240ms
- easing: `cubic-bezier(0.2, 0.8, 0.2, 1)`
- 반복: 없음
- reduced motion: active outline, 방향, state label을 즉시 갱신

SVG 글자, layer 색과 주변 panel에는 animation을 추가하지 않는다.

## 6. Information Ownership

같은 내용을 짧게 바꿔 말하는 방식도 반복으로 본다. 각 필드와 화면 영역은 아래 역할 하나만 맡는다.

| 데이터·영역 | 남길 역할 | 제거할 내용 |
|---|---|---|
| `problem` | 이 주차가 필요한 한 가지 문제 | goal의 학습 결과 반복 |
| `workbench.instruction` | 학생이 선택하고 관찰할 행동 | 전체 경로 결론 |
| `scenario.label` | 짧은 입력 조건 | 결과와 완성 문장 |
| `scenario.prompt` | 현재 주어진 상태 | prediction 질문 전체 재서술 |
| `prediction.prompt` | 학생이 내려야 할 판단 하나 | 입력 조건 반복 |
| `prediction.explanation` | 선택이 갈린 기준 | 최종 outcome 복사 |
| `visual.caption` | 정적인 구조를 읽는 기준 | 아래 lifeline 순서와 결론 |
| `observationTitle` | 20~35자의 관찰 대상 | diagram caption 축약본 |
| `diagram.caption` | 선택 조건의 실제 경로 한 문장 | 테스트·로그·코드 증거 |
| `lane.description` | 다른 lane과 구분되는 책임 | scenario 전체 경로 |
| message | `from/to + verb + payload` | before/after와 긴 설명 |
| current inspector | `before -> after + evidence scope` | actor, verb, payload 재출력 |
| evidence section | `check + 실제 코드·테스트·실행 근거` | 현재 경로와 before/after 반복 |
| `scenario.evidence` | 증거 종류, 범위와 한계 | 경로와 outcome |
| `scenario.outcome` | 관찰 뒤 남길 인과 규칙 하나 | prediction explanation |
| reflection | 학생이 자기 말로 재구성할 질문 | outcome의 단순 의문형 복사 |

다음 공통 문구는 삭제한다.

- 모든 topic visual 뒤의 `관계를 먼저 읽고, 아래에서 한 단계씩 확인합니다.`
- prediction의 `내 예상`과 `실제 흐름을 보기 전에 예상해보세요` 중 하나
- prediction control 아래에서 같은 잠금 상태를 다시 설명하는 두 문장
- evidence section의 eyebrow, 제목, lede 중 같은 역할을 하는 문장
- verification section의 저장 방식과 목적을 반복하는 도입 문장

시나리오 선택 button과 현재 stage heading은 위치 확인을 위해 모두 유지하되 같은 문장을 쓰지 않는다.
button은 입력 조건, stage heading은 `observationTitle`을 사용한다.

### Current Step 표시 규칙

Desktop:

```text
message          from/to + verb + payload
inspector        before -> after + evidence scope
evidence section check + source
```

Mobile:

```text
single card      from/to + verb/payload + before/after
evidence section check + source
```

- `effect.subject`가 정규화된 `payload`와 같으면 별도 제목으로 출력하지 않는다.
- mobile의 `sequence-mobile-current__sentence`는 actor route와 같으므로 제거한다.
- mobile `sequence-step-jump`는 기본 접힌 `전체 단계` 또는 짧은 index로 바꾼다.
- 공개 뒤 prediction은 선택 문장 전체를 다시 쓰지 않고 `예상과 같음` 또는 `다름`과 차이만 표시한다.
- 최종 outcome은 lane의 마지막 step에서만 강조한다.

## 7. SVG Geometry Contract

### 7.1 표시 폭과 글자 크기

기존 validator는 약 320px 표시 폭을 가정했지만 실제 390px 화면의 asset 폭은 약 308px이었다.
새 검증은 308px을 worst-case 기준으로 사용한다.

```text
mobile size = SVG font-size * 308 / viewBox width
```

- hard fail: mobile 환산 글자 10.5px 미만
- 목표 body/layer: 12px 이상
- 목표 actor/node: 13px 이상
- 목표 diagram heading: 15px 이상

예시 최소 SVG font-size:

| viewBox width | body/layer 12px | actor 13px | heading 15px |
|---:|---:|---:|---:|
| 720 | 29 | 31 | 36 |
| 640 | 25 | 28 | 32 |

글자를 줄여서 맞추지 않는다. 공간이 부족하면 node 수를 줄이거나 행을 나눈다.

### 7.2 Box와 Text

- visible SVG title과 subtitle은 HTML figure caption과 중복되면 제거한다.
- SVG 내부에는 접근성용 `<title>`과 `<desc>`를 유지한다.
- 같은 레이어가 연속되면 group 또는 band label을 한 번만 표시한다.
- node 이름은 semantic break를 정해 `<tspan>`으로 최대 두 줄만 사용한다.
- identifier 중간 자동 줄바꿈, `textLength`, `lengthAdjust` 축소를 사용하지 않는다.
- node text의 좌우·상하 안전 여백은 화면 환산 8px 이상으로 한다.
- 720 viewBox에서는 최소 19 unit, 640 viewBox에서는 최소 17 unit을 기본 inset으로 사용한다.
- text baseline 간격은 최소 `1.25em`으로 한다.
- text bounding box와 connector 또는 box stroke 사이 간격은 최소 12 SVG unit으로 한다.
- node와 결과 card의 중심 정렬 오차는 ±1 SVG unit 이내로 한다.
- outer frame 안쪽 inset은 최소 16 SVG unit으로 한다.

### 7.3 정보 위계

```text
HTML caption      이번 그림을 보는 이유 1회
SVG group label   시스템 레이어 또는 독립 lane 1회
SVG node          actor 또는 실제 state
SVG connector     verb와 방향
HTML outcome      새로 얻은 인과 규칙 1회
```

SVG footer conclusion은 HTML caption이나 outcome과 같으면 제거한다.
실제 클래스, method, path만 원래 영문 표기를 유지하고 설명용 영문 대문자는 sentence case 또는 한국어로 바꾼다.

## 8. Implementation Priority

### P0 — 공통 구조와 확정 겹침

1. 공통 renderer의 payload, before/after, check 중복 제거
2. 390px single current-step surface 구현
3. 05, 08, 09, 12 duplicate SVG 겹침 수정
4. 02 SVG의 `Request DTO` overflow를 prototype에서 함께 수정

### P1 — 긴 문구와 복잡 구조

| Sequence | 먼저 줄일 내용 |
|---|---|
| 06 Testing | 잘못된 password의 observation/evidence/outcome 반복과 최장 164자 문구 |
| 11 Refactoring | baseline explanation/outcome, diagram/evidence 중복 |
| 12 Event Driven | 중복 방지 diagram/evidence, 120자 초과 문구 6개 |
| 04 JWT | token 없는 보호 요청의 explanation/outcome/lane 반복 |
| 05 OAuth2 + SMTP | email 검증과 LOCAL 충돌 질문의 prompt/prediction/lane 반복 |
| 08 Realtime | Origin 조건, subscription 결과와 증거 반복 |
| 09 Runtime | `.dockerignore` 실패의 observation/explanation/diagram 반복 |
| 10 CI/CD | build 실패 outcome/lane과 반복 layer label |

### P2 — 전체 정리

00, 01, 02, 03, 07의 짧은 문구도 역할이 겹치면 줄인다.
07의 condition-first 문법은 비교적 명확하므로 구조를 유지하고 반복 label만 정리한다.

## 9. Implementation Phases

### Phase 0 — Baseline and Ownership Map

1. 13개 sequence의 같은 scenario를 1440, 1024, 768, 390에서 저장한다.
2. 16개 SVG를 native 크기와 실제 308px 표시 폭으로 렌더한다.
3. 각 visible 문구를 `condition`, `route`, `change`, `evidence`, `conclusion` 중 하나로 분류한다.

검증:

- 역할이 두 개인 문장 0
- 삭제 후보와 기술적으로 유지할 문구를 sequence별로 기록

### Phase 1 — Validator First

1. `effect.subject === payload` 정규화 중복을 warning으로 검출한다.
2. 핵심 필드의 정규화된 완전 동일 문장을 warning으로 검출한다.
3. `observationTitle`, `lane.description`, caption의 길이 초과는 자동 자르지 않고 review warning으로 남긴다.
4. SVG의 308px 환산 글자 크기, viewBox 밖 text, owner box 안전 여백 계약을 검사한다.
5. 반복 layer label과 금지된 공통 filler 문구를 검사한다.

검증:

- 기존 문제를 validator가 먼저 재현
- 기술적 뉘앙스를 보존하기 위해 유사도만으로 자동 삭제하지 않음

### Phase 2 — Shared Renderer Prototype

02 DB Access 첫 scenario를 prototype으로 사용한다.

1. desktop lifeline 옆에 current inspector를 배치한다.
2. current inspector에서 actor/verb/payload 재출력을 제거한다.
3. mobile current와 detail을 한 surface로 합친다.
4. step jump를 접거나 compact index로 바꾼다.
5. evidence section은 check와 실제 source만 기본 표시한다.
6. diagram은 1099px 이하에서 현재 단계 집중 layout으로 전환하고, 900px 이하 shell·learning nav와 420px 이하 조작부 보정을 분리해 검증한다.

Prototype gate:

- 390×844에서 current actor, verb, payload, before/after, 이전·다음이 한 viewport에 보임
- 1024×900에서 내부 가로 스크롤 없이 현재 step을 읽음
- desktop message와 inspector가 같은 사실을 반복하지 않음

### Phase 3 — SVG Prototype Gate

서로 다른 topology 네 종류를 먼저 수정한다.

- 02: 수평 계층과 persistence boundary
- 07: cache state cycle
- 09: runtime nesting
- 12: producer/broker fork와 duplicate state

Prototype gate:

- text bbox가 owner box 안전 영역 안에 있음
- text와 arrow 교차 0
- mobile 환산 글자 hard fail 0
- group layer label은 연속 영역당 한 번
- footer conclusion과 HTML outcome 중복 0

### Phase 4 — Copy Reduction

1. 06, 11, 12의 긴 문구부터 줄인다.
2. 04, 05, 08, 09, 10의 실패·증거 문구를 역할별로 분리한다.
3. 00, 01, 02, 03, 07을 같은 기준으로 마무리한다.
4. 각 문장은 target theory와 실제 evidence scope를 대조한다.

기술 사실은 유지한다.

- mock 호출을 외부 전달 성공으로 확대하지 않음
- `contextLoads`를 HTTP 계약 성공으로 확대하지 않음
- in-memory idempotency를 영속 보장으로 확대하지 않음
- publisher confirm 없는 정상 반환을 broker acceptance로 확대하지 않음
- command 종료를 application health로 확대하지 않음

### Phase 5 — SVG Rollout

P0 asset을 먼저 완료한 뒤 나머지 12개 asset에 geometry contract를 적용한다.
모든 그림을 같은 카드 layout으로 바꾸지 않고 다음 고유 구조를 유지한다.

- request/tool map
- memory와 persistence boundary
- validation/auth/trust gate
- test scope
- cache cycle
- subscription fan-out
- runtime nesting
- pipeline gate
- behavior invariant lane
- event fork와 failure boundary

### Phase 6 — Browser and Repository Completion

1. 13개 sequence, 50개 scenario, 89개 lane의 첫·중간·마지막 step을 확인한다.
2. 8개 hub와 theory 왕복 link를 확인한다.
3. child repository를 각각 검증·commit·push한다.
4. 중앙 저장소에서 실제 변경된 submodule pointer와 기준 문서를 별도 commit·push한다.

## 10. Component Coverage

### 변경

- topic SVG의 text geometry, group layer label과 connector 정렬
- semantic diagram의 desktop current inspector
- mobile current-step surface
- current detail, evidence와 step jump의 중복 정보
- prediction 공개 뒤 요약
- topic visual generic caption
- scenario별 prompt, caption, evidence, outcome의 역할 분리
- 1100px과 720px responsive 집중 layout
- SVG·copy validator

### 유지

- topbar, brand mark와 repository context
- H1의 핵심 질문
- scenario 선택과 prediction gate
- Diagnostic Lifeline의 participant/time 관계
- request, response, event, failure의 방향 차이
- system layer palette와 state palette
- 이전·다음 수동 control과 progress
- theory link, code evidence, comparison, reflection, checklist와 next question
- keyboard focus, reduced motion과 forced-colors 규칙

유지 항목은 현재 학습 흐름이나 접근성에 필요한 역할이 있으며 이번 문제의 원인이 아니므로 구조를 다시 만들지 않는다.

## 11. Verification Plan

### Static

```bash
for file in */docs/visual-lab/*.js */docs/visual-lab/sequences/*/*.js; do
  node --check "$file"
done

find . -path '*/docs/visual-lab/*.html' -print0 \
  | xargs -0 xmllint --html --noout

find . -path '*/docs/visual-lab/*.svg' -print0 \
  | xargs -0 xmllint --noout

python3 scripts/validate-manifest.py
python3 scripts/verify-sequences.py
python3 scripts/validate-visual-labs.py
python3 scripts/validate-visual-lab-colors.py
git diff --check
```

### Browser

| Viewport | 확인할 것 |
|---|---|
| 1440×1000 | lifeline, current message와 inspector가 한 시선에 연결됨 |
| 1024×900 | 가로 스크롤 없는 집중 layout과 긴 actor 이름 |
| 768×1024 | current card와 detail 중복 없음 |
| 390×844 | single current-step surface, controls, 긴 한국어와 code wrap |

모든 viewport에서 다음을 확인한다.

- text overlap 0
- page horizontal overflow 0
- clipped focus outline 0
- broken image 0
- console warning/error 0
- 200% zoom overlap 0
- keyboard focus 복원
- reduced motion에서 같은 정보 유지
- informative image의 `complete`, `naturalWidth`, alt와 visible caption

### Content

- 같은 viewport에서 `verb + payload` visible 출력 1회
- 같은 viewport에서 before/after visible 출력 1회
- `step.check`는 evidence source와 함께 1회
- 같은 연속 layer의 visible label은 group당 1회
- caption, evidence와 outcome이 각각 경로·증거·결론 한 역할만 담당
- reflection은 회상 연습이므로 유지하되 outcome의 단순 복사 금지

## 12. Genericity Critique

첫 축소안이 모든 diagram을 작은 card와 짧은 문장으로만 바꾸면 일반적인 stepper UI가 된다.
또한 레이어 label을 전부 제거하면 색으로 위치를 추측해야 하고, SVG를 단순화한다는 이유로 기술 경계를 생략하면 학습 자료의 정확성이 떨어진다.

이를 다음처럼 보정한다.

- `Diagnostic Lifeline`과 topic별 topology는 유지한다.
- 정보는 삭제하기보다 유일한 소유 위치로 이동한다.
- layer는 node마다 반복하지 않지만 group rail과 현재 actor에 visible text로 남긴다.
- 문구 길이보다 기술적 증거 범위를 우선한다.
- SVG가 복잡하면 font를 줄이지 않고 구조를 두 행이나 두 lane으로 나눈다.
- 반대 조건 비교와 reflection은 반복처럼 보여도 학습 행동이 다르므로 유지한다.
- 검은 배경, accent와 icon을 제거해도 실제 경계와 상태 변화가 남아야 한다.

## 13. Applied File Scope

중앙 저장소:

```text
docs/audit/visual-lab-readability-reduction-plan.md
docs/audit/visual-lab-design-system-review.md
docs/visual-lab-design-guide.md
docs/visual-lab-content-spec.md
docs/visual-lab-implementation-plan.md
scripts/validate-visual-labs.py
SVG·copy 계약을 확장한 기존 validator
```

각 토픽 저장소:

```text
docs/visual-lab/styles.css
docs/visual-lab/visual-lab.js
docs/visual-lab/sequences/NN/visual-lab-data.js
docs/visual-lab/assets/diagrams/*.svg
docs/visual-lab/assets/SOURCE.md  # 출처 관계가 바뀌지 않아 변경하지 않음
docs/theory.md                    # 기술 사실이 어긋나지 않아 변경하지 않음
```

새 framework, dependency, external font, CDN과 장식 asset은 추가하지 않는다.

## 14. Completion Gate

- 16개 SVG의 text bbox overflow와 text/arrow 교차가 0이다.
- 308px 표시 기준으로 10.5px 미만 글자가 0이다.
- 05, 08, 09, 12 duplicate의 P0 겹침이 해결된다.
- 같은 step의 actor/verb/payload, before/after, check가 각 역할 위치에서 한 번만 보인다.
- 390×844에서 현재 step과 이전·다음 control을 한 viewport에서 읽는다.
- 1024×900에서 participant stage 때문에 내부 가로 스크롤이 생기지 않는다.
- 13개 sequence와 50개 scenario의 기술 결론과 evidence scope가 유지된다.
- 29개 Visual Lab JavaScript가 `node --check`를 통과한다.
- 모든 Visual Lab HTML·SVG가 `xmllint`를 통과한다.
- 중앙 validator, console, keyboard, 200% zoom과 reduced-motion 검수가 통과한다.
- shared JavaScript와 CSS가 8개 저장소에서 같은 checksum을 가진다.
- 각 child commit/push 뒤 중앙 submodule pointer를 별도 commit/push한다.

검증 실패나 기술 사실 확인이 남은 상태에서는 완료로 보고하지 않는다.

## 15. Implementation Result

### 15.1 적용 결과

- 8개 저장소의 공통 renderer와 CSS를 같은 checksum으로 반영했다.
- desktop은 `message = route + verb + payload`, 옆 inspector는 `before -> after + boundary + evidence scope`만 소유한다.
- 1099px 이하는 actor layer, boundary, verb, payload와 before/after를 하나의 현재 단계 surface에 합쳤다. 별도 current detail, 같은 문장의 mobile 재출력과 전체 단계 jump 목록은 제거했다.
- 공개 뒤 prediction은 선택지 문장을 되풀이하지 않고 `예상과 같음` 또는 `예상과 다름`과 판단 기준만 보여준다.
- `effect.subject`와 `payload`가 같은 데이터는 schema를 바꾸지 않고 renderer에서 중복 출력을 억제했다. 기술 데이터 계약보다 UI 소유권을 먼저 고친 결정이다.
- 50개 scenario의 역할 문구는 30,252자에서 26,045자로 13.9% 줄었고, 120자 초과 역할 문구는 0개가 됐다. step, effect, check, ID와 schema는 유지했다.
- 16개 설명 SVG 모두에 308px geometry 계약을 적용했다. 반복 layer/footer를 줄이고 text baseline, box inset과 connector 간격을 다시 맞췄으며 `<title>`과 `<desc>`는 16/16 유지했다.

### 15.2 가독성 결과

02 첫 step의 모바일 반복 영역은 약 1,533px에서 `현재 단계 surface 416px + controls 93px = 509px`로 줄었다. 전체 388 step 가운데 가장 긴 현재 단계와 controls의 합은 750px로 390x844 viewport 안에 남았다.

```text
Before
actor / verb / payload
-> 같은 actor / verb / payload
-> before / after
-> 같은 before / after
-> step jump 재출력

After
현재 actor -> verb / payload -> 다음 actor
-> before / after
-> 이전 / 다음
```

### 15.3 검증 결과

- browser: 13개 sequence, 50개 scenario, 89개 lane, 388 step을 1440x1000과 390x844에서 각각 순회해 총 776개 단계 상태를 확인했다.
- breakpoint: 02, 08, 12의 대표 복잡 경로를 1024x900과 768x1024에서 다시 확인했다.
- hub: 8개 저장소 hub를 네 viewport에서 확인해 32/32 상태가 통과했다.
- keyboard: 이전·다음 실행 뒤 desktop message 또는 mobile current card로 focus가 복원되고 3px outline과 3px offset이 유지됐다.
- motion: 로드된 CSSOM에서 `prefers-reduced-motion: reduce`, smooth scroll 제거, 0.01ms duration과 1회 iteration을 확인했다. 브라우저의 media query 강제 emulation은 제공되지 않아 정적 대체 규칙과 실제 기본 상태를 함께 확인했다.
- zoom: 별도 browser zoom 제어는 제공되지 않아 1536px 화면의 200%에 해당하는 768 CSS px와 더 좁은 390 CSS px에서 겹침·page overflow 0을 확인했다.
- console: warning과 error 0.
- static: Python validator 4종, Visual Lab JavaScript 29개, HTML 21개, SVG 272개와 중앙·8개 child `git diff --check`가 통과했다.
- shared checksum: JavaScript `c640a2b678fa2657157ef0b17131b6f93576493073713efb2edf786fb02154ba`, CSS `10a2f65671dd144fb1d21832105973eb258eb0eb99a8194c9923bce0e07ac479`.
- legacy duplicate filename: `copy`, `복사본`, 구분자와 괄호가 붙은 `2`, `3` suffix 후보 0개.

### 15.4 화면 증거와 최종 검토

새 화면 증거는 `docs/audit/screenshots/visual-lab-readability`에 저장했다.

- `hub-db-desktop-1440.png`
- `hub-db-mobile-390.png`
- `sequence-02-desktop-1440.png`
- `sequence-02-mobile-390.png`
- `sequence-08-mobile-390.png`
- `sequence-12-desktop-1440.png`

누적 최종 검토와 저장소 반영 결과는 `visual-lab-design-system-review.md`의 8.2와 9.1절에 기록한다.
