# A&I Backend Visual Lab Design Guide

## 1. 문서 목적

이 문서는 A&I Backend Visual Lab의 디자인 시스템을 정의한다.

A&I Backend Visual Lab은 A&I 4기 백엔드 커리큘럼을 글이 아닌 시각적 흐름으로 이해하기 위한 정적 HTML 학습 페이지다.

이 페이지는 다음을 목표로 한다.

- 학습자가 현재 질문에 맞는 조건을 선택하고 실제 시스템 경로를 관찰하게 한다.
- 요청, 객체, 토큰, 캐시, 테스트, 실행 산출물, 이벤트가 책임 경계를 지나는 흐름을 시각화한다.
- 선택한 경로의 개념, 코드, 확인 증거를 같은 맥락에서 연결한다.
- A&I 공식 사이트의 밝고 깔끔한 브랜드 톤을 유지한다.
- 문서 요약 카드가 아니라 주차별 백엔드 워크벤치로 동작한다.

## 2. 반드시 참조해야 할 디자인 자료

### 2.1 A&I 공식 사이트

참조 URL:

```text
https://aandiclub.com/
```

사용 목적:

- A&I 브랜드 톤 참고
- 밝은 배경
- 깔끔한 동아리/학습 커뮤니티 분위기
- 과하지 않은 색상 사용
- 친근하지만 가벼워 보이지 않는 개발자 학습 페이지 느낌

주의:

- 사이트를 그대로 복제하지 않는다.
- 브랜드 톤만 참고한다.
- Visual Lab 자체는 첨부된 교육용 인포그래픽 스타일에 더 가깝게 만든다.

### 2.2 첨부된 스타일 가이드 MD

참조 파일:

```text
stitch_ai_datastructure_image_style_guide.md
```

이 파일은 밝은 교육 자료의 톤과 도식 가독성을 참고하는 자료다.
현재 Visual Lab의 구조, 컴포넌트와 접근성 규칙은 이 문서와 실제 공통 CSS/JavaScript 구현을 우선한다.

핵심 규칙:

- 개발자 학습용 슬라이드 느낌
- 깔끔한 벡터형 인포그래픽
- 한국어 제목 중심 레이아웃
- 자료구조 개념을 한눈에 이해할 수 있는 시각화
- 시리즈 간 폰트/레이아웃 일관성 유지
- 한 화면에서 질문과 관찰 대상을 파악할 수 있는 교육용 작업면
- 네이비 / 로열블루 / 청록 중심 팔레트
- 흰색 또는 회백색 배경
- 얇은 파란색 계열 테두리
- 실제 경계와 전달 순서를 표현하는 도식
- 번호는 시퀀스와 실제 단계 순서에만 사용

## 3. 디자인 콘셉트

A&I Backend Visual Lab은 일반 문서 페이지가 아니다.

구체적인 Subject는 다음과 같다.

```text
실행 중인 백엔드 요청, 객체, 상태, 경계와 전달 단위를 직접 추적하며 이론을 확인하는 정적 학습 환경
```

주요 Audience는 Spring Boot 기초부터 DB, 검증, 인증, 외부 연동, 테스트, 캐시, 실시간 통신, 배포, 리팩토링과 이벤트 기반 사고를 순서대로 학습하는 A&I 백엔드 학습자다.

화면의 Single Job은 다음과 같다.

```text
학습자가 이번 시퀀스에서 조작할 조건, 관찰할 시스템 변화, 설명해야 할 다음 판단을 첫 화면에서 놓치지 않게 한다.
```

모든 상세 화면은 아래 학습 문법을 따른다.

```text
현재 질문
-> 조작 가능한 입력 또는 상태
-> 관찰한 시스템 경로
-> 개념 또는 책임 경계
-> 실패나 대안 비교
-> 검증 증거
-> 다음 질문
```

피해야 할 느낌:

- 일반 블로그 글
- 무거운 관리자 페이지
- 동일한 카드만 반복하는 학습 대시보드
- 큰 마케팅 Hero와 기능 소개 grid
- 다크모드 개발자 콘솔
- 3D 그래픽 사이트
- 네온 사이버펑크
- 지나치게 귀여운 교육 사이트

## 4. 디자인 토큰

기존 `--color-*` 팔레트 토큰은 호환을 위해 유지한다. 새 컴포넌트는 색상값을 직접 쓰지 않고 아래 semantic token을 먼저 사용한다.

```css
:root {
  --color-correct: #176F72;
  --color-boundary-strong: #6F82B8;

  --surface-canvas: var(--color-bg-base);
  --surface-primary: var(--color-card-white);
  --surface-secondary: var(--color-summary-bg);
  --surface-evidence: var(--color-correct-bg);
  --surface-warning: var(--color-panel-blue-tint);
  --surface-danger: var(--color-incorrect-bg);
  --surface-diagram: var(--color-bg-base);
  --surface-node: var(--color-card-white);

  --ink-primary: var(--color-body-navy);
  --ink-secondary: var(--color-subtext);
  --ink-quiet: var(--color-subtext);

  --signal-active: var(--color-accent-blue);
  --signal-muted: var(--color-summary-border);
  --evidence: var(--color-accent-teal);
  --evidence-ink: var(--color-title-navy);
  --hypothesis: var(--color-subtext);
  --decision: var(--color-title-navy);

  --danger: var(--color-incorrect);
  --warning: var(--color-subtext);
  --recovered: var(--color-correct);
  --blocked: var(--color-subtext);
  --edge-request: var(--color-accent-blue);
  --edge-response: var(--color-accent-teal);
  --edge-persist: var(--color-title-navy);
  --edge-failure: var(--color-incorrect);

  --border-strong: var(--color-boundary-strong);
  --border-soft: var(--color-outline-soft);
  --focus-ring: var(--color-accent-blue);
}
```

핵심 palette의 역할은 다음과 같다.

| 이름 | HEX | 역할 |
|---|---|---|
| Lab Paper | `#F8F9FB` | 전체 canvas |
| System Ink | `#111B3F` | 본문과 코드 외 시스템 구조 |
| A&I Navy | `#0C2691` | 현재 질문과 판단 제목 |
| Signal Blue | `#2955E4` | 선택한 조건과 active path |
| Evidence Teal | `#3F8996` | 관찰 결과와 확인 증거 |
| Boundary Line | `#C9D6F3` | 계층, trust, runtime, pipeline 경계 |

`#176F72`는 작은 회복 상태 text의 대비를 위한 semantic support color, `#6F82B8`는 흰 작업면에서 3:1 이상의 비텍스트 경계 대비를 위한 support color다. 둘은 core accent로 반복하지 않고 각각 `--color-correct`, `--color-boundary-strong`을 통해서만 사용한다.

공통 spacing, radius, elevation과 motion도 토큰으로만 확장한다.

```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;

  --radius-small: 8px;
  --radius-medium: 14px;
  --radius-large: 20px;
  --shadow-panel: 0 18px 50px rgba(17, 27, 63, 0.08);

  --motion-duration: 240ms;
  --motion-easing: cubic-bezier(0.2, 0.8, 0.2, 1);
}
```

## 5. 색상 사용 규칙

### 5.1 현재 질문과 판단

- 질문과 판단 제목은 `--decision`을 사용한다.
- 선택한 조건과 현재 경로는 `--signal-active`를 사용한다.
- 관찰 증거와 회복 결과의 선·면은 `--evidence` 또는 `--recovered`를 사용한다.
- 작은 evidence text는 `--evidence-ink`를 사용해 일반 텍스트 4.5:1 대비를 유지한다.
- 일반 본문에는 accent를 사용하지 않는다.

### 5.2 표면

- 기본 작업면은 `--surface-primary`와 `--border-strong`을 사용한다.
- 보조 설명과 비활성 상태는 `--surface-secondary`를 사용한다.
- evidence drawer와 다음 질문은 `--surface-evidence`를 사용한다.
- shadow는 주 작업면처럼 시각적 층위가 필요한 곳에만 쓴다.

### 5.3 상태 표현

상태 tone은 `signal`, `blocked`, `warning`, `recovered` 네 가지다.

- 색상만으로 상태를 전달하지 않고 `진행 중`, `여기서 차단`, `주의 필요`, `확인 완료` label을 함께 표시한다.
- blocked node는 점선 경계와 `도달하지 않음` 텍스트를 함께 쓴다.
- 선택 상태는 `aria-pressed`, 현재 단계는 `aria-current="step"`으로도 표현한다.
- 전체 panel을 진한 색으로 뒤집지 않는다.
- 빨강·주황·노랑을 장식 accent로 추가하지 않는다.

## 6. 타이포그래피

외부 폰트를 import하지 않고 세 역할을 구분한다.

```css
:root {
  --font-display: Pretendard, SUIT, "Noto Sans KR", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  --font-body: Pretendard, SUIT, "Noto Sans KR", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  --font-utility: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
}
```

| 역할 | 크기와 굵기 | 행간·자간 | 사용 위치 | 사용 금지 위치 |
|---|---|---|---|---|
| Display | `clamp(2rem, 4.8vw, 4.65rem)`, 800~900 | 1.04~1.15, `-0.035em`~-`0.05em` | 현재 질문, 주요 판단 제목 | 긴 설명, control label |
| Body | 0.95~1.18rem, 400~700 | 1.55~1.75, `-0.01em` | 한국어 설명, 개념, 검증 질문 | 경로와 코드 정렬 |
| Utility / Data | 0.68~0.95rem, 500~900 | 1.4~1.65, `0`~`0.08em` | HTTP, 상태, 경로, 명령, 파일, progress | 긴 한국어 본문과 질문 |

Display는 마케팅 문구가 아니라 이번 시퀀스의 실제 질문에만 사용한다. Hero를 크게 보이게 만들기 위해 본문까지 Display로 확장하지 않는다.

## 7. 배경 장식

배경은 `--surface-canvas` 위에 낮은 대비의 32px 시스템 grid를 한 번만 사용한다. 모바일에서는 24px로 줄인다.

```css
body::before {
  content: "";
  position: fixed;
  inset: 0;
  background-image:
    linear-gradient(rgba(41, 85, 228, 0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(41, 85, 228, 0.035) 1px, transparent 1px);
  background-size: 32px 32px;
  z-index: -1;
  pointer-events: none;
}
```

큰 원, 사선, 점 패턴은 필수 장식이 아니다. 추가 장식은 actor, boundary, route 또는 상태를 설명할 때만 허용하며 콘텐츠 뒤에 독립적으로 떠 있는 장식은 추가하지 않는다.

## 8. 구조 표면과 컴포넌트

모든 내용을 같은 카드로 나누지 않는다. 컴포넌트의 표면은 정보 역할에 따라 구분한다.

- `journey-list`: 허브에서 시퀀스 선후 관계를 표현하는 ordered list다.
- `sequence-hero`: 기존 class 이름은 유지하지만, 화면을 채우는 Hero가 아니라 시퀀스 identity와 현재 질문을 담는 compact header다.
- `scenario-selector`: 학습자가 바꾸는 실제 입력 또는 상태다.
- `workbench`: 선택한 경로, 상태 snapshot, 관찰 증거와 판단을 묶는 primary surface다.
- `semantic-diagram`: actor와 책임 주체, 전달 관계와 경계를 함께 읽는 primary system figure다.
- `diagram-lane`: request/response, producer/broker/consumer, build/runtime처럼 서로 다른 책임 흐름을 분리한다.
- `semantic-node`: 실제 책임 주체나 관찰할 resource를 icon, kind, role, boundary와 함께 표시한다.
- `semantic-edge`: 두 node 사이의 방향, 동사, payload와 관계 kind를 표시하는 단계 control이다.
- `lifeline-sequence`: 책임 주체를 한 번만 놓고 위에서 아래로 실행 시간을 읽는 주 다이어그램이다.
- `active-effect`: 현재 화살표가 바꾸는 대상의 before와 after를 나란히 보여주는 기록이다.
- `not-reached`: 선택한 조건에서 실행되지 않은 대상과 이유를 별도 목록으로 설명한다.
- `evidence-layout`: 현재 단계의 Problem, Concept, Action, Check와 책임·개념을 연결한다.
- `reference-shelf`: 용어, 범위와 문서 링크를 secondary `details`로 둔다.
- `verification-list`: 현재 session에서만 유지하는 확인 질문이다.
- `next-question`: 다음 시퀀스로 이어지는 실제 질문과 링크다.

radius는 small 8px, medium 14px, large 20px 안에서만 사용한다. hover에서 transform으로 위치를 이동하지 않는다.

## 9. Diagnostic Lifeline과 주차별 Workbench

`Diagnostic Lifeline`은 전체 Visual Lab의 하나뿐인 signature element다. 장식용 선이 아니라 누가 어떤 데이터를 넘겼고 그 순간 무엇이 바뀌었는지를 시간 순서대로 기록한다.

```text
책임 주체 header: Client | Controller | Service | Repository | DB
                              │          │           │
시간 ↓      Client ── JSON ─>│          │           │
                              │── DTO ──>│           │
                              │          │── Entity >│
                              │          │           │── row ─> DB

현재 변화: JSON 문자열 → PostCreateRequest 객체
확인 근거: 실제 응답·로그·테스트·코드 중 이 단계가 보장하는 범위
```

### 9.1 의미 기반 시스템 다이어그램 문법

완성된 workbench는 이름만 나열한 `route` 선이나 actor 카드와 transition 카드의 분리된 grid로 끝내지 않는다. 책임 주체 header와 수직 lifeline을 한 번 배치하고 message를 위에서 아래로 읽는 semantic sequence를 우선 표시한다. `route`는 호환용 진행 상태로 유지할 수 있다.
책임 주체 catalog는 `workbench.nodes`, 관계는 각 scenario의 `diagram.lanes[].steps`로 관리한다.

```text
[책임 주체 또는 시스템 resource]
  -- 동사 · payload · 관계 kind -->
[다음 책임 주체]
  책임 경계 · Boundary label
```

- node는 실제로 책임을 수행하는 actor, service, handler, repository, broker, runtime이나 상태와 생명주기를 관찰할 artifact/resource다.
- HTTP method, 메서드 호출, 검증 행위와 같은 동작은 독립 node로 만들지 않고 edge의 `verb`와 `payload`로 표현한다.
- request DTO, token, event, command, artifact가 단순히 이동하는 값이면 edge의 `payload`다. image처럼 생성·실행 상태 자체를 비교하는 대상일 때만 node로 승격한다.
- edge는 방향과 함께 `verb`, `payload`, `kind`를 항상 표시한다. `kind`는 `request`, `call`, `transform`, `persist`, `response`, `failure`, `event`, `config`, `compare` 중 하나다.
- 현재 edge는 `effect.subject`, `effect.before`, `effect.after`를 함께 보여준다. 단순 이동이면 위치 또는 소유 책임이 바뀌고, 변환·저장·검증이면 객체나 시스템 상태가 바뀐다.
- `호출 전 책임`, `반환 대기`, `판정 입력`, `evidence가 아직 관찰되지 않음`처럼 payload만 바꿔 끼울 수 있는 틀 문장은 상태 변화로 인정하지 않는다. 학생이 실행 전후를 비교할 수 있도록 실제 값, 저장 위치, 인증 주체, 연결 대상, 실패 gate 또는 assertion 결과를 쓴다.
- `evidenceScope`는 `code`, `test`, `runtime`, `manual`, `concept` 중 하나를 text로 표시해 코드 한 조각이 실제 실행 전체를 보장하는 것처럼 보이지 않게 한다.
- `from === to`는 같은 lifeline을 되돌아오는 self-call loop로, `response`는 역방향 화살표로, `event`는 점선 message로, `failure`는 중단 표식과 도달하지 않은 책임으로 구분한다.
- 코드 근거는 파일 경로 badge가 아니라 학생이 확인할 한 문장으로 시작한다. 바로 아래에 저장소의 실제 핵심 코드 3~12줄을 놓고, 끝에 이 코드가 바꾸는 상태나 다음 책임을 한 문장으로 적는다. 전체 파일 위치는 꼭 필요할 때만 접힌 참고 영역에 둔다.
- node의 `boundary`는 `Controller`, `Persistence`, `Trust`, `Build time`, `Runtime`, `Broker`처럼 판단이나 책임이 실제로 바뀌는 위치를 visible text로 표시한다.
- 서로 다른 lane을 하나의 실행 시간축으로 합치지 않는다. 현재 lane 안에서만 `지남`, `현재 관찰`, `다음`을 사용하고 다른 lane은 `선택 가능`으로 표시한다.
- progress는 전체 edge 합계가 아니라 현재 lane 이름과 `현재 단계 / lane 단계 수`를 보여준다. lane 끝의 이동은 `다음 경로`로 명시하고 학생이 수동으로 이동한다.
- semantic edge와 evidence는 edge/node의 명시적 `codePointIds`로 연결하며 legacy flow step의 위치를 비례 상속하지 않는다.
- `lane`은 동시에 존재하지만 성격이 다른 흐름을 분리한다. 주문 응답과 비동기 event 전달, build와 verify, Before와 After를 하나의 직선으로 합치지 않는다.
- `caption`은 선택한 조건의 전체 경로를 한 문장으로 읽어준다.
- `notReached`는 opacity로 숨기지 않고 실행되지 않은 대상과 이유를 함께 표시한다.

`system-icons.svg`는 공통 outline 원본과 하위 호환 자료로 보존한다. 실제 participant header는 직접 렌더링 가능한 `docs/visual-lab/assets/icons/{icon}.svg`를 `<img>`로 사용한다. icon은 책임을 빠르게 찾는 보조 수단이며 alt를 비워 장식으로 처리하고 label, role, boundary를 visible text로 유지한다. load error에서도 기술 역할 label이 남아야 한다. hub와 sequence entry의 favicon은 같은 저장소 로컬 `assets/visual-lab-mark.svg`를 사용한다.

각 시퀀스는 주제에서 직접 나온 설명 SVG 한 개를 `workbench.visual`의 `src`, `alt`, `caption`으로 연결한다. 설명 SVG는 memory와 DB 생명주기, cache 상태, subscription fan-out처럼 학생이 먼저 알아야 할 관계만 보여주고 interactive path나 text를 대체하지 않는다. desktop에서는 원본 비율을 유지하되 높이를 360px 이내로 제한하고, mobile에서는 그림 영역의 전체 폭을 사용한다. 390px 화면의 약 320px 그림 영역에서도 가장 작은 visible text가 10.5px 아래로 축소되지 않도록 관계 수, viewBox 폭과 SVG 내부 font-size를 함께 조정한다. `assets/SOURCE.md`와 `assets/LICENSES.md`에 출처와 사용 조건을 기록한다. 외부 icon CDN, emoji, 외부 font, script와 network URL은 사용하지 않는다.

다이어그램의 `check`와 evidence는 실제 증거보다 넓은 보장을 주장하지 않는다. mock 호출은 외부 시스템 통합 성공, `contextLoads`는 HTTP 계약, in-memory map은 영속 멱등성, 배포 명령 종료는 서비스 정상 응답의 증거가 아니다. publisher confirm이 없으면 `convertAndSend` 정상 반환도 broker acceptance·routing을 보장하지 않고, 모호한 전송 예외도 미전송을 확정하지 않는다.

단계 번호는 실제 lane의 시간 순서를 뜻한다. 각 message는 `지남`, `현재 관찰`, `다음`, `도달하지 않음` 상태를 text와 함께 표시한다. `stopAfter` 이후 책임은 단순히 흐리게 하지 않고 도달하지 않은 이유를 적는다.

기본 trace를 모든 주차에 똑같이 보이게 만드는 것으로 끝내지 않는다. `workbench.kind`에 따라 실제 판단 구조를 다음처럼 구분한다.

| Sequence | kind | Primary workbench |
|---|---|---|
| 00 | `request` | method, URL, JSON, status를 읽는 Request Workbench |
| 01 | `request-trace` | 요청·응답 객체의 계층 이동을 보는 Request Packet Trace |
| 02 | `persistence` | memory/MySQL과 DTO/Entity를 비교하는 Persistence Boundary |
| 03 | `gate` | invalid input이 멈추는 위치를 보는 Failure Gate |
| 04 | `auth` | 발급·검증과 401/403을 구분하는 Auth Boundary |
| 05 | `trust` | 외부 identity, 계정 충돌, reset mail의 Trust Map |
| 06 | `test` | fixture, mock, assertion, 보장 범위를 보는 Test Harness |
| 07 | `cache` | empty, warm, expired, evicted, refill을 보는 Cache State Inspector |
| 08 | `realtime` | connect, subscribe, send, broadcast와 fan-out을 보는 Connection Console |
| 09 | `runtime` | jar, build context, image, container, environment의 Runtime Boundary |
| 10 | `pipeline` | 최초 실패와 이후 blocked 단계를 보는 Pipeline Gate |
| 11 | `refactor` | 유지된 계약과 의도적으로 바뀐 동작을 분리하는 Behavior Change Ledger |
| 12 | `event` | direct/broker path와 consumer 상태를 보는 Event Delivery Trace |

gate, auth, trust, pipeline은 차단 경계를 강조한다. cache, runtime, test, refactor는 snapshot 비교를 우선한다. realtime과 event는 전달 경로와 실제 수신 대상을 우선하며, `fanOut`은 실제 수신 대상이 있을 때만 표시한다.

기존 `actors`, `flows`, `codePoints`는 trace의 단계와 evidence를 제공한다. explicit workbench가 없는 과거 데이터는 `flows`에서 기본 trace를 만들 수 있지만, 완성된 시퀀스의 primary 디자인은 명시적 `workbench`를 사용한다.

## 10. 레이아웃

### 10.1 토픽 레포 허브

허브는 카드 grid 대신 시퀀스 journey를 primary로 사용한다.

```text
Repository context
-> 시퀀스 identity와 실제 질문
-> 학습 시작 link
-> 다음 시퀀스
```

### 10.2 시퀀스 상세

```text
┌──────────────────────────────────────────────────────────┐
│ Context bar                                              │
├───────────────┬──────────────────────────────────────────┤
│ 이번 질문 · 꼭 알아야 할 전제                           │
├──────────────────────────────────────────────────────────┤
│ 결과를 숨긴 조건 -> 내 예측                             │
├──────────────────────────────────────────────────────────┤
│ participant header와 수직 lifeline                      │
│ 위→아래 message · 현재 before → after                   │
│ 짧은 주석 → 실제 핵심 코드 → 확인 가능한 범위          │
├──────────────────────────────────────────────────────────┤
│ 반대 조건 비교 -> 인과 규칙 정리 -> 다음 질문          │
└──────────────────────────────────────────────────────────┘
```

첫 viewport에는 현재 질문, 필수 전제, 첫 등장 용어, 입력 조건과 첫 행동이 보여야 한다. 모든 scenario는 `prediction`을 제공하고 선택 전에는 path, snapshot, outcome을 공개하지 않는다. participant는 header에 한 번만 배치하고 message는 위에서 아래로 쌓는다. 한 lane은 최대 7개 message이며 현재 message 하나만 before/after와 코드 근거를 확장한다. 긴 이론, glossary와 전체 파일 위치는 primary workbench 아래의 접을 수 있는 shelf로 둔다.

## 11. 반응형·접근성·모션

### 11.1 반응형

- desktop은 최대 1320px 작업면과 2열 evidence layout을 사용할 수 있다.
- 980px 이하에서는 header, workbench header와 evidence를 1열로 바꾼다.
- 720px 이하에서는 learning nav를 가로 이동 가능한 대체 nav로 두고 scenario control과 결과를 세로로 재배치한다.
- 390px에서 page-level horizontal overflow가 없어야 한다.
- 720px 이하에서는 전체 participant 카드를 먼저 쌓지 않는다. 현재 message를 `출발 책임 → 도착 책임`, payload, before → after 순서의 압축 lifeline으로 먼저 보여주고 이전·다음 단계는 수동 control로 이동한다.
- legacy Signal Trace와 긴 code만 해당 영역 안에서 제한적인 가로 스크롤을 허용하며 semantic diagram 이해를 가로 스크롤에 의존시키지 않는다.
- 긴 한국어, 파일 경로, 명령과 상태 label은 잘리거나 겹치지 않아야 한다.

### 11.2 키보드와 상태

- 본문 건너뛰기 링크를 제공한다.
- 모든 button, link, input, summary에 3px `:focus-visible` outline과 3px offset을 유지한다.
- 주요 control은 가능한 한 44px 이상 touch target을 확보한다.
- `semantic-edge`가 단계 control이면 native `button`을 사용하고 `from`, `to`, `verb`, `payload`, before, after, 현재 상태가 접근 가능한 이름에 포함되어야 한다.
- icon과 화살표 모양은 보조 표현이며 node label, boundary, edge kind와 state를 text로도 유지한다.
- scenario 변경과 route/step 이동 뒤 `data-focus-key`로 trigger focus를 복원한다.
- 진행률은 semantic `progress`, 선택은 `aria-pressed`, 현재 위치는 `aria-current`로 표현한다.
- 넓고 자주 바뀌는 영역 전체에 `aria-live`를 붙이지 않는다. 선택 결과의 짧은 status만 `polite`로 알린다.

### 11.3 단일 모션 시스템

모션은 scenario 또는 step 변경 시 현재 message와 active-effect가 다음 책임으로 이동하는 한 순간에만 사용한다.

- duration: `240ms`
- easing: `cubic-bezier(0.2, 0.8, 0.2, 1)`
- 자동 반복: 없음
- 자동 재생과 속도 control: 사용하지 않음. 학생이 이전/다음으로 관찰 속도를 결정
- `prefers-reduced-motion: reduce`: smooth scroll과 transition을 제거하고 같은 상태를 즉시 표시
- reduced motion에서도 active edge, 방향, payload와 `도달하지 않음` 이유를 정적인 상태로 모두 읽을 수 있어야 한다.

## 12. 금지 사항

사용하지 말 것:

- 외부 JS 라이브러리
- React, Vue, Next.js
- Bootstrap
- Tailwind CDN
- 외부 폰트 import
- 실사 이미지
- 3D 렌더링
- 다크모드
- 네온 효과
- 복잡한 배경
- 필수 장식처럼 반복되는 큰 원, glow, blanket gradient
- 큰 마케팅 Hero와 동일 카드 grid 중심 구성
- 주차별 시스템 차이를 지우는 범용 dashboard template
- 실제 actor, 상태, 경계, 확인 증거와 연결되지 않은 번호·badge·metric
- 책임 주체와 전달 payload를 구분하지 않은 동일한 node 나열
- 동사와 payload label이 없는 장식용 연결선 또는 화살표
- icon만으로 actor, 경계나 상태를 전달하는 표현
- 단위 테스트, mock, in-memory 상태나 명령 종료를 더 넓은 통합 성공으로 과장하는 evidence
- hover transform으로 발생하는 layout 이동
- 여러 컴포넌트에 흩어진 반복 animation
- 빨강/주황/노랑 중심 팔레트
- 손글씨체
- 명조체
- 과하게 귀여운 둥근 폰트
