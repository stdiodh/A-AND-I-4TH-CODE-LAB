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
  --surface-canvas: var(--color-bg-base);
  --surface-primary: var(--color-card-white);
  --surface-secondary: var(--color-summary-bg);
  --surface-evidence: var(--color-correct-bg);
  --surface-warning: var(--color-panel-blue-tint);
  --surface-danger: var(--color-incorrect-bg);

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

  --border-strong: var(--color-line-blue-light);
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
- `evidence-layout`: 현재 단계의 Problem, Concept, Action, Check와 책임·개념을 연결한다.
- `reference-shelf`: 용어, 범위와 문서 링크를 secondary `details`로 둔다.
- `verification-list`: 현재 session에서만 유지하는 확인 질문이다.
- `next-question`: 다음 시퀀스로 이어지는 실제 질문과 링크다.

radius는 small 8px, medium 14px, large 20px 안에서만 사용한다. hover에서 transform으로 위치를 이동하지 않는다.

## 9. Learning Signal Trace와 주차별 Workbench

`Learning Signal Trace`는 전체 Visual Lab의 하나뿐인 signature element다.

```text
선택한 입력 또는 상태
-> 실제 request/object/token/cache/artifact/test/event 경로
-> 현재 책임 경계
-> 관찰 증거
-> 판단
```

trace의 번호는 실제 route 순서를 뜻한다. 각 node는 `지남`, `현재 관찰`, `다음`, `도달하지 않음` 상태를 text와 함께 표시한다. `stopAfter` 이후 node는 blocked로 표시하고 비활성화한다.

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
| 09 | `runtime` | jar, image, container, environment의 Runtime Boundary |
| 10 | `pipeline` | 최초 실패와 이후 blocked 단계를 보는 Pipeline Gate |
| 11 | `refactor` | 구조 변경 전후 계약을 비교하는 Behavior Invariant Map |
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
│ Sequence      │ 현재 학습 질문과 goal                   │
├──────────────────────────────────────────────────────────┤
│ 질문 -> 관찰 -> 개념·코드 -> 검증 -> 다음 질문         │
├──────────────────────────────────────────────────────────┤
│ 조건 선택                                                │
│ Learning Signal Trace                                   │
│ snapshot | 관찰 증거 | 판단 | 단계 control             │
├──────────────────────────────┬───────────────────────────┤
│ 현재 단계 Problem/Concept/   │ 책임·개념 context         │
│ Action/Check + code evidence │                           │
├──────────────────────────────────────────────────────────┤
│ Verification -> Next question                           │
└──────────────────────────────────────────────────────────┘
```

첫 viewport에는 현재 질문과 관찰 조건이 우선 보여야 한다. 긴 이론, glossary와 reference는 primary workbench 아래의 evidence 또는 접을 수 있는 shelf로 둔다.

## 11. 반응형·접근성·모션

### 11.1 반응형

- desktop은 최대 1320px 작업면과 2열 evidence layout을 사용할 수 있다.
- 980px 이하에서는 header, workbench header와 evidence를 1열로 바꾼다.
- 720px 이하에서는 learning nav를 가로 이동 가능한 대체 nav로 두고 scenario control과 결과를 세로로 재배치한다.
- 390px에서 page-level horizontal overflow가 없어야 한다.
- Signal Trace와 긴 code만 해당 영역 안에서 가로 스크롤을 허용한다.
- 긴 한국어, 파일 경로, 명령과 상태 label은 잘리거나 겹치지 않아야 한다.

### 11.2 키보드와 상태

- 본문 건너뛰기 링크를 제공한다.
- 모든 button, link, input, summary에 3px `:focus-visible` outline과 3px offset을 유지한다.
- 주요 control은 가능한 한 44px 이상 touch target을 확보한다.
- scenario 변경과 route/step 이동 뒤 `data-focus-key`로 trigger focus를 복원한다.
- 진행률은 semantic `progress`, 선택은 `aria-pressed`, 현재 위치는 `aria-current`로 표현한다.
- 넓고 자주 바뀌는 영역 전체에 `aria-live`를 붙이지 않는다. 선택 결과의 짧은 status만 `polite`로 알린다.

### 11.3 단일 모션 시스템

모션은 scenario 또는 step 변경 시 Signal Trace의 active path가 이동하는 한 순간에만 사용한다.

- duration: `240ms`
- easing: `cubic-bezier(0.2, 0.8, 0.2, 1)`
- 자동 반복: 없음
- 자동 재생: 학습자가 명시적으로 시작했을 때만 사용
- `prefers-reduced-motion: reduce`: smooth scroll과 transition을 제거하고 재생·속도 control을 비활성화한 뒤 같은 상태를 즉시 표시

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
- hover transform으로 발생하는 layout 이동
- 여러 컴포넌트에 흩어진 반복 animation
- 빨강/주황/노랑 중심 팔레트
- 손글씨체
- 명조체
- 과하게 귀여운 둥근 폰트
