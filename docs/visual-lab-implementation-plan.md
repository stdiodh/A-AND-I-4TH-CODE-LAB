# A&I Backend Visual Lab Implementation Plan

## 1. 구현 목적

A&I Backend Visual Lab은 각 시퀀스 서브모듈 안에서 정적 HTML, CSS, Vanilla JavaScript만으로 구현한다.

목표는 A&I 백엔드 커리큘럼과 토픽 레포의 이론/코드 흐름을 하나의 학습 워크스페이스에서 직접 선택하고 추적하는 것이다.

이 페이지는 실제 Spring Boot 서버를 실행하지 않는다.
대신 문서와 코드에서 정의된 요청, 객체, token, cache, artifact, test, event 흐름을 시각화한다.

공통 학습 문법은 아래와 같다.

```text
현재 질문
-> 조작할 입력 또는 상태
-> 관찰한 시스템 경로
-> 개념 또는 책임 경계
-> 실패 또는 대안 비교
-> 검증 증거
-> 다음 질문
```

## 2. 구현 범위

각 토픽 레포 안에서 관리할 파일:

```text
<topic-repo>/docs/visual-lab/index.html
<topic-repo>/docs/visual-lab/styles.css
<topic-repo>/docs/visual-lab/visual-lab-data.js
<topic-repo>/docs/visual-lab/visual-lab.js
<topic-repo>/docs/visual-lab/sequences/NN/index.html
<topic-repo>/docs/visual-lab/sequences/NN/visual-lab-data.js
```

루트 레포에는 위 구현 파일을 만들지 않는다.
루트 레포는 기준 문서, validator, 검수 기록과 submodule pointer만 관리한다.

기준 문서:

```text
docs/visual-lab-design-guide.md
docs/visual-lab-content-spec.md
docs/visual-lab-implementation-plan.md
docs/visual-lab-codex-prompt.md
docs/audit/visual-lab-design-system-plan.md
```

## 3. 구현 전 반드시 읽을 문서

Codex는 작업 전 아래 문서를 읽어야 한다.

```text
AGENTS.md
README.md
.agents/skills/aandi-visual-lab-design/SKILL.md
docs/visual-lab-sequence-workflow.md
docs/visual-lab-design-guide.md
docs/visual-lab-content-spec.md
docs/visual-lab-implementation-plan.md
docs/visual-lab-codex-prompt.md
docs/audit/visual-lab-design-system-plan.md
docs/sequences/NN-*.md
```

대상 토픽 레포에서는 `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, 현재 `docs/visual-lab` 파일을 함께 읽는다.

DB Access Lab 콘텐츠를 만들 때 아래 외부 문서를 검수 자료로 참고할 수 있다.

```text
https://github.com/stdiodh/spring-boot-db-access-lab/blob/02-answer/docs/theory.md
https://github.com/stdiodh/spring-boot-db-access-lab/blob/02-answer/docs/implementation.md
https://github.com/stdiodh/spring-boot-db-access-lab/tree/02-answer
```

구현 전에 대상 시퀀스의 subject, audience, single job, palette, typography, layout, signature, motion을 짧게 계획하고 generic dashboard 패턴이 남아 있는지 비판한 뒤 수정한다.

## 4. 모든 시퀀스 확장 원칙

Visual Lab은 `02-answer`만을 위한 페이지가 아니다.
`00`부터 `12`까지 각 시퀀스의 실제 학습 질문과 시스템 경로를 같은 시각 문법으로 연결한다.

모든 시퀀스는 아래 브랜치 규칙을 유지한다.

```text
NN-implementation
-> 학생이 실습을 시작하는 브랜치
-> TODO와 구현 순서를 확인하는 기준

NN-answer
-> 완성 흐름을 검수하는 참고 브랜치
-> 화면과 데이터에는 브랜치명이나 완성 구현 코드를 직접 노출하지 않음
```

시퀀스별 콘텐츠 확장 순서:

1. 중앙 `docs/sequences/NN-...md`에서 학습 범위를 확정한다.
2. 토픽 레포의 theory, implementation, checklist와 실제 코드 경로를 확인한다.
3. `flows`, `codePoints`, `checks`, `next`의 기존 기술 내용을 보존한다.
4. `docs/visual-lab/sequences/NN/visual-lab-data.js`에 주제별 `workbench`를 추가한다.
5. 시나리오의 `flowId`, `route`, `snapshot`, `evidence`, `outcome`을 실제 흐름과 연결한다.
6. 긴 이론, secret, 정답 브랜치명, 완성 코드 전체를 화면 데이터에 넣지 않는다.

## 5. 서브모듈 작업 완료 흐름

각 서브모듈 구현은 아래 단위를 모두 끝내야 완료된다.

```text
1. 대상 서브모듈의 docs/visual-lab 구현
2. 대상 서브모듈의 정적·브라우저 검수
3. 대상 서브모듈 commit/push
4. 루트 레포에서 submodule pointer 변경 확인
5. 루트 기준 문서 또는 validator 변경이 있으면 함께 검수
6. 루트 레포 commit/push
```

루트 push가 인증 문제로 실패하면 다음 작업 전에 미완료 상태를 보고한다.
학생용 `NN-implementation`과 비교용 브랜치의 범위는 임의로 변경하지 않는다.

## 6. 구현 원칙

- 외부 라이브러리, React, Vue, Next.js, Bootstrap, Tailwind CDN을 사용하지 않는다.
- HTML/CSS/Vanilla JavaScript와 상대 경로만 사용한다.
- 상세 HTML은 정적인 섹션을 반복하지 않고 `#app` shell과 데이터/engine 연결만 둔다.
- `Learning Signal Trace`를 유일한 signature element로 사용한다.
- 각 시퀀스의 primary surface는 실제 주제에서 나온 workbench여야 한다.
- 시나리오 상태는 색상뿐 아니라 label, route state, evidence, outcome으로 전달한다.
- 기존 커리큘럼, 시퀀스 순서, 기술 사실과 데이터 스키마를 근거 없이 변경하지 않는다.
- 외부 font import와 CDN 의존성을 추가하지 않는다.
- hover 이동, 장식용 glow, 반복 gradient, 흩어진 animation을 사용하지 않는다.
- 공통 CSS/JS는 외부 공용 경로에 의존하지 않고 8개 토픽 레포에 같은 내용으로 로컬 복제한다.

## 7. 파일별 구현 계획

### 7.1 docs/visual-lab/index.html과 sequences/NN/index.html

역할:

- `docs/visual-lab/index.html`: 토픽 레포의 sequence journey 허브
- `docs/visual-lab/sequences/NN/index.html`: 한 시퀀스의 질문과 workbench 진입점
- 실제 화면 구조는 shared engine이 데이터의 `kind`에 따라 렌더링

허브 HTML 연결:

```html
<link rel="stylesheet" href="./styles.css" />
<div id="app" class="app-shell">
  <noscript>Visual Lab을 보려면 JavaScript를 활성화해주세요.</noscript>
</div>
<script src="./visual-lab-data.js"></script>
<script src="./visual-lab.js"></script>
```

상세 HTML 연결:

```html
<link rel="stylesheet" href="../../styles.css" />
<div id="app" class="app-shell">
  <noscript>Visual Lab을 보려면 JavaScript를 활성화해주세요.</noscript>
</div>
<script src="./visual-lab-data.js"></script>
<script src="../../visual-lab.js"></script>
```

정적 HTML에 설명 섹션이나 컴포넌트별 빈 container를 반복해서 만들지 않는다.
`lang="ko"`, charset, viewport, title과 `noscript` 안내를 유지한다.

### 7.2 docs/visual-lab/styles.css

역할:

- A&I light identity와 semantic token 정의
- Display, Body, Utility/Data typography 역할 분리
- hub, sequence, workbench, evidence, verification, next question 레이아웃
- focus, mobile, reduced motion, forced colors 처리

핵심 semantic token:

```text
surface-canvas
surface-primary
surface-secondary
surface-evidence
signal-active
signal-muted
evidence
hypothesis
decision
danger
warning
recovered
blocked
focus-ring
motion-duration
motion-easing
```

공통 화면 문법:

```text
context-bar
hub-intro + journey-list
sequence-hero + sequence-thesis
learning-nav
scenario-selector
workbench + signal-trace
state-snapshot + outcome-panel
trace-controls + progress
evidence-layout + context-drawer + code-evidence
reference-shelf
verification-section
next-question
empty-state / fatal-state
```

컴포넌트마다 색상, 간격, radius, motion 값을 다시 하드코딩하지 않는다.
390px에서는 page-level horizontal overflow가 없어야 하며, signal trace와 긴 code만 해당 영역 안에서 스크롤할 수 있다.

### 7.3 docs/visual-lab/visual-lab-data.js

역할:

- 토픽 레포 hub 데이터 정의
- `kind: "hub"`와 시퀀스 journey 제공

```js
window.visualLabData = {
  kind: "hub",
  title: "DB Access Lab Visual Lab",
  description: "이 레포의 학습 흐름을 선택합니다.",
  sequences: [
    {
      sequence: "02",
      title: "DB Access",
      topic: "Persistence and layered architecture",
      href: "./sequences/02/index.html",
      summary: "요청이 영속 저장으로 이어지는 경계를 확인합니다."
    }
  ]
};
```

허브는 범용 카드 grid가 아니라 순서와 다음 이동이 드러나는 `ol.journey-list`로 렌더링한다.

### 7.4 docs/visual-lab/sequences/NN/visual-lab-data.js

역할:

- 시퀀스의 canonical 학습 데이터 정의
- 실제 actor, flow, code point, verification, next question 제공
- topic-specific `workbench`와 3~4개 실제 시나리오 제공

필수 구조:

```js
window.visualLabData = {
  kind: "sequence",
  sequence: "NN",
  title: "한국어 주제명",
  subtitle: "학습 범위",
  goal: "한 줄 목표",
  problem: "현재 질문의 배경",
  actors: [],
  flows: [
    {
      id: "main-flow",
      title: "핵심 흐름",
      steps: [
        {
          id: "main-flow-step-1",
          from: "Client",
          to: "Controller",
          problem: "무엇을 관찰하는가",
          concept: "어떤 책임인가",
          action: "무엇이 이동하거나 판단되는가",
          check: "무엇으로 확인하는가",
          codePointIds: ["controller-entry"]
        }
      ]
    }
  ],
  workbench: {
    kind: "request-trace",
    title: "주제별 워크벤치 이름",
    instruction: "조건을 바꾸며 무엇을 확인할지 안내합니다.",
    scenarios: [
      {
        id: "create-success",
        label: "생성 성공",
        flowId: "main-flow",
        tone: "recovered",
        prompt: "이 조건에서 어디를 관찰해야 할까요?",
        route: ["Client", "Controller", "Service", "Repository", "DB"],
        snapshot: [
          { label: "요청", value: "POST /posts" },
          { label: "저장", value: "row 확인", tone: "recovered" }
        ],
        evidence: "실제 확인 명령, 화면 또는 코드 지점",
        outcome: "이 증거로 내릴 판단"
      }
    ]
  },
  codePoints: [],
  concepts: [],
  responsibilities: [],
  checks: [],
  next: { id: "NN", title: "다음 주제", reason: "이어지는 질문" }
};
```

`workbench` 작성 규칙:

- `kind`는 시퀀스 주제에 맞는 request, request-trace, persistence, gate, auth, trust, test, cache, realtime, runtime, pipeline, refactor, event 중 하나를 사용한다.
- 각 시퀀스는 실제 콘텐츠에 근거한 3~4개 scenario를 둔다.
- `flowId`는 같은 객체의 `flows[].id`와 반드시 일치해야 한다.
- `tone`은 `signal`, `blocked`, `warning`, `recovered` 중 하나다.
- `route`에는 실제 actor와 책임·신뢰·runtime·pipeline 경계만 순서대로 쓴다.
- `snapshot`은 label/value를 가진 항목을 2개 이상 두며 필요한 항목에 같은 semantic tone을 넣을 수 있다.
- `evidence`는 실제 요청, 응답, 상태, 로그, 명령, 테스트 또는 코드 지점을 가리킨다.
- `outcome`은 학습자가 증거를 보고 내릴 판단을 쓴다.
- blocked scenario의 `stopAfter`는 마지막으로 도달한 route의 0-based index다.
- realtime broadcast처럼 실제 수신자 분기가 있을 때만 `fanOut`을 추가한다.
- `flows[].steps`는 Problem, Concept, Action, Check가 드러나는 4~6단계로 제한한다.
- `workbench`가 없는 legacy 데이터는 engine이 `flows`에서 trace를 만들 수 있지만 신규·수정 시퀀스는 명시적인 `workbench`를 제공한다.

### 7.5 docs/visual-lab/visual-lab.js

역할:

- `window.visualLabData.kind`에 따라 hub 또는 sequence 경험 렌더링
- 기존 canonical flow와 topic workbench 연결
- 모든 state 변경 후 키보드 focus와 진행 의미 보존

Hub 렌더링:

- compact context bar
- repository title, description, single job
- 시퀀스 순서를 나타내는 semantic journey list
- 빈 sequences 데이터의 안내 상태

Sequence 렌더링:

```text
compact context bar
-> current question header
-> learning nav
-> scenario selector
-> topic workbench / Learning Signal Trace
-> snapshot + evidence/outcome
-> selected code/context drawer
-> verification
-> next question
```

필수 동작:

- scenario 선택 시 `aria-pressed`를 갱신하고 연결된 `flowId`의 첫 단계로 이동한다.
- signal node는 passed, active, pending, blocked 상태를 label과 함께 제공한다.
- 이전/다음, 재생/일시정지, 속도와 native `<progress>`로 단계 진행을 제공한다.
- scenario, route, control을 선택해 전체 DOM이 다시 렌더링돼도 `data-focus-key`로 focus를 복원한다.
- 선택 step의 Problem, Concept, Action, Check와 `codePointIds`를 evidence 영역에 연결한다.
- responsibility와 concept는 context drawer에, glossary와 문서는 접을 수 있는 reference shelf에 둔다.
- verification checkbox는 현재 페이지 session에만 유지하고 native `<progress>`와 완료 수를 갱신한다.
- same-repo 다음 시퀀스가 있으면 상세 페이지로, 없으면 해당 repository journey로 연결한다.
- data가 없거나 잘못된 경우 원인과 확인 파일을 알려주는 empty/fatal state를 렌더링한다.
- section observer는 learning nav의 현재 위치를 `aria-current="location"`으로 표현한다.
- 상태 변경 알림은 workbench의 짧은 `role="status"` 한 곳으로 제한한다.
- reduced motion에서는 자동 재생과 속도 조절을 비활성화하고 같은 정보를 정적으로 제공한다.

### 7.6 Shared Engine 로컬 복제

공통 `visual-lab.js`와 `styles.css`는 다음 8개 토픽 레포에 같은 내용으로 둔다.

```text
aandi-prerequisite-bootcamp
spring-boot-rest-crud-lab
spring-boot-db-access-lab
spring-boot-redis-cache-lab
spring-boot-realtime-communication-lab
spring-boot-deployment-runtime-lab
spring-boot-refactoring-foundation-lab
spring-boot-event-driven-lab
```

한 레포의 파일을 다른 서브모듈에서 runtime import하지 않는다.
CDN, symlink, 새 package 대신 동일한 engine을 각 레포에 로컬 복제해 GitHub Pages 상대 경로를 유지한다.

공통 engine을 변경하면 8개 사본을 모두 동기화하고 hash가 같은지 확인한다.
시퀀스 고유 구조는 공통 engine을 fork하지 않고 `workbench.kind`와 canonical 데이터로 표현한다.

## 8. 구현 단계

### Step 1. 기준과 현재 상태 확인

- repository, remote, branch, status, submodule 관계 확인
- `$aandi-visual-lab-design`과 중앙 기준 문서 확인
- 대상 theory, implementation, checklist, sequence data 확인
- 기존 hub와 상세 페이지의 before 화면 확인

### Step 2. 디자인 계획과 genericity critique

- subject, audience, single job 정의
- palette와 typography 역할 확인
- 두 레이아웃을 비교하고 Learning Signal Trace 방향 선택
- 범용 dashboard, 카드 나열, 장식 terminal, 의미 없는 metric이 남는지 비판

### Step 3. 데이터 계약 확정

- 실제 `flows`, actor, code point, check, next question 확인
- 주제별 `workbench.kind`와 3~4개 scenario 작성
- blocked, warning, recovered 상태와 evidence를 색상 외 정보로 작성

### Step 4. HTML shell과 shared style 동기화

- hub와 sequence의 최소 `#app` shell 확인
- semantic token, context bar, journey, question header, workbench, evidence, verification, next 레이아웃 반영
- 8개 토픽 레포의 공통 CSS를 같은 내용으로 동기화

### Step 5. Shared engine 동기화

- hub/sequence 분기 렌더링
- scenario와 flow state 연결
- signal trace, snapshot, evidence/context drawer 렌더링
- focus restore, progress semantics, empty/fatal state 처리
- 8개 토픽 레포의 공통 JS를 같은 내용으로 동기화

### Step 6. 시퀀스별 콘텐츠 연결

- 모든 구현된 시퀀스의 시나리오를 직접 전환
- hub 또는 상세 데이터가 비어 있거나 잘못된 상태를 원인과 확인 대상으로 안내
- 긴 이론과 완성 구현을 복제하지 않고 실제 문서와 코드 위치로 연결

### Step 7. 정적 검증

```bash
for repo in \
  aandi-prerequisite-bootcamp \
  spring-boot-rest-crud-lab \
  spring-boot-db-access-lab \
  spring-boot-redis-cache-lab \
  spring-boot-realtime-communication-lab \
  spring-boot-deployment-runtime-lab \
  spring-boot-refactoring-foundation-lab \
  spring-boot-event-driven-lab
do
  find "$repo/docs/visual-lab" -name '*.js' -print0 | xargs -0 -n1 node --check
done

python3 scripts/validate-manifest.py
python3 scripts/validate-visual-labs.py
git diff --check
```

공통 파일 hash도 확인한다.

```bash
shasum */docs/visual-lab/visual-lab.js
shasum */docs/visual-lab/styles.css
```

### Step 8. 브라우저 검수

대상 토픽 레포에서 실행한다.

```bash
python3 -m http.server 8080 -d docs/visual-lab
```

hub, 모든 상세 시퀀스, 모든 scenario, signal route, controls, evidence, verification, next link를 확인한다.

화면 크기:

```text
1440x1000
1024x900
768x1024
390x844
```

### Step 9. 저장소 완료 처리

- 각 토픽 레포의 변경과 검증 결과 확인
- 서브모듈별 commit/push
- 중앙 저장소에서 변경된 submodule pointer와 기준 문서만 commit/push
- 남은 브라우저 또는 외부 환경 검증이 있으면 완료로 숨기지 않고 기록

## 9. 검수 기준

### 9.1 기능 검수

- hub journey가 올바른 상세 페이지로 이동한다.
- 첫 scenario가 기본 선택되고 `aria-pressed="true"`를 가진다.
- scenario 변경 시 연결 flow, route, snapshot, evidence, outcome이 함께 바뀐다.
- signal node와 이전/다음 control이 같은 단계 상태를 가리킨다.
- 재생, 일시정지, 속도 변경과 마지막 단계 정지가 동작한다.
- native progress가 현재 단계와 verification 완료 수를 정확히 표현한다.
- code point, responsibility, concept, reference가 현재 step과 연결된다.
- verification checkbox는 페이지 내에서 동작하고 다음 질문 링크가 실제 경로로 이동한다.
- empty/fatal 상태가 원인과 확인 대상을 알려준다.

### 9.2 디자인 검수

- A&I light palette와 Display/Body/Utility 역할이 유지된다.
- 첫 화면에서 현재 질문과 조작할 조건이 설명 카드보다 먼저 보인다.
- Learning Signal Trace가 실제 시스템 경로를 표현한다.
- 주차별 workbench가 같은 카드 layout을 이름만 바꾼 결과가 아니다.
- 상태는 label, route state, snapshot, evidence를 통해 색상 없이도 구분된다.
- 다크 관리자 dashboard, 장식 terminal, glow, blanket gradient 느낌이 없다.

### 9.3 접근성과 반응형 검수

- skip link, semantic heading, nav, fieldset/legend, button, list, progress가 올바르게 동작한다.
- 모든 interactive element에 visible `:focus-visible`이 있다.
- scenario와 control 재렌더링 뒤 focus가 선택한 요소로 돌아온다.
- reduced motion에서 smooth scroll, transition, 자동 재생이 제거된다.
- 390px에서 page-level horizontal overflow, 잘린 focus, 겹친 한국어 문장이 없다.
- 긴 path와 code는 해당 영역 안에서만 스크롤된다.
- touch target은 가능한 한 44px 이상이다.

### 9.4 회귀 검수

- 모든 Visual Lab JavaScript가 `node --check`를 통과한다.
- central manifest와 Visual Lab validator가 통과한다.
- 8개 레포의 shared JS/CSS hash가 각각 일치한다.
- browser console error가 없다.
- 모든 구현 시퀀스의 실제 기술 내용과 `flowId` 연결이 유지된다.
- 화면과 데이터에 secret, 정답 브랜치명, 긴 완성 구현 코드가 노출되지 않는다.
- 공통 CSS/JS를 변경한 경우 00~12 전체를 desktop과 mobile에서 회귀 확인한다.
