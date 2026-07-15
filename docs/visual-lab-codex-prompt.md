# A&I Backend Visual Lab Codex Prompt

## 1. 역할

너는 A&I 4기 Code Lab Central Hub 저장소에서 작업하는 구현 도우미다.

이번 작업은 중앙 레포의 기준 문서를 읽고, 대상 시퀀스 서브모듈 안의 `A&I Backend Visual Lab`을 실제 시스템 흐름을 추적하는 정적 학습 워크스페이스로 구현하거나 검수하는 것이다.

중앙 레포는 구현물을 직접 보관하지 않는다.
중앙 레포는 기준 문서, validator, 검수 기록과 submodule pointer만 관리한다.

## 2. 작업 전 반드시 읽을 문서

작업 전 아래 문서를 읽어라.

```text
AGENTS.md
README.md
.agents/skills/aandi-visual-lab-design/SKILL.md
docs/visual-lab-sequence-workflow.md
docs/visual-lab-design-guide.md
docs/visual-lab-content-spec.md
docs/visual-lab-implementation-plan.md
docs/audit/visual-lab-design-system-plan.md
docs/sequences/NN-*.md
```

대상 토픽 레포의 아래 문서와 현재 구현도 읽어라.

```text
README.md
docs/theory.md
docs/implementation.md
docs/checklist.md
docs/visual-lab/index.html
docs/visual-lab/styles.css
docs/visual-lab/visual-lab-data.js
docs/visual-lab/visual-lab.js
docs/visual-lab/sequences/NN/index.html
docs/visual-lab/sequences/NN/visual-lab-data.js
```

DB Access Lab 흐름을 반영할 때는 아래 문서를 검수 자료로 참고할 수 있다.

```text
https://github.com/stdiodh/spring-boot-db-access-lab/blob/02-answer/docs/theory.md
https://github.com/stdiodh/spring-boot-db-access-lab/blob/02-answer/docs/implementation.md
https://github.com/stdiodh/spring-boot-db-access-lab/tree/02-answer
```

## 3. 모든 시퀀스 브랜치 기준

Visual Lab은 한 시퀀스만 설명하는 페이지가 아니다.
모든 시퀀스는 아래 브랜치 기준으로 확장한다.

```text
NN-implementation
-> 학생 실습용 starter 브랜치
-> TODO와 순서형 힌트를 확인하는 기준

NN-answer
-> 완성 흐름을 검수하는 참고 브랜치
-> 화면과 데이터에는 브랜치명이나 완성 구현 코드를 직접 노출하지 않음
```

`NN`은 중앙 `docs/sequences` 번호와 같아야 한다.
학생용 또는 비교용 브랜치의 커리큘럼 범위를 임의로 변경하지 않는다.

## 4. 매우 중요한 작업 원칙

- `docs/visual-lab` 또는 중앙 Visual Lab 디자인 문서를 바꾸는 작업은 `$aandi-visual-lab-design`을 사용한다.
- 구현 전 design plan과 genericity critique를 작성한다.
- 중앙 레포는 상세 이론 또는 Visual Lab 구현 저장소가 아니다.
- 구현 파일은 대상 서브모듈의 `docs/visual-lab` 아래에만 둔다.
- 루트 레포에 `docs/index.html` 또는 `docs/visualizer/*` 구현 파일을 만들지 않는다.
- 기존 커리큘럼, 시퀀스 순서, 기술 사실과 데이터 계약을 근거 없이 바꾸지 않는다.
- 정답 브랜치명, secret, 긴 이론과 완성 구현 코드를 화면 데이터에 넣지 않는다.
- 기존 canonical `flows`, `codePoints`, `checks`, `next`를 보존하고 topic workbench를 연결한다.
- 공통 CSS/JS는 CDN이나 다른 서브모듈 경로로 공유하지 않고 8개 토픽 레포에 동일하게 로컬 복제한다.
- 각 토픽 레포를 검수하고 commit/push한 뒤 중앙 submodule pointer를 별도로 commit/push한다.

## 5. 구현 목표

대상 시퀀스 서브모듈 안에서 아래 파일을 생성 또는 수정한다.

```text
docs/visual-lab/index.html
docs/visual-lab/styles.css
docs/visual-lab/visual-lab-data.js
docs/visual-lab/visual-lab.js
docs/visual-lab/sequences/NN/index.html
docs/visual-lab/sequences/NN/visual-lab-data.js
```

`docs/visual-lab/index.html`은 sequence journey 허브다.
상세 페이지는 현재 질문, topic workbench, evidence, verification, next question을 하나의 학습 흐름으로 렌더링한다.

공통 경험 문법:

```text
현재 질문
-> 조작할 입력 또는 상태
-> 관찰한 시스템 경로
-> 개념 또는 책임 경계
-> 실패 또는 대안 비교
-> 검증 증거
-> 다음 질문
```

## 6. 디자인 요구사항

반드시 `docs/visual-lab-design-guide.md`와 `docs/audit/visual-lab-design-system-plan.md`를 따른다.

핵심 방향:

- A&I의 밝은 교육용 identity를 유지한다.
- 배경은 `#F8F9FB`, 본문은 `#111B3F`, 핵심 질문은 `#0C2691`을 사용한다.
- 선택 신호는 `#2955E4`, 관찰 증거는 `#3F8996`을 semantic token으로 사용한다.
- Display, Body, Utility/Data typography 역할을 system font 안에서 분리한다.
- 외부 font import를 추가하지 않는다.
- `Learning Signal Trace` 하나만 signature element로 사용한다.
- Hero는 marketing 문구가 아니라 현재 학습 질문과 goal을 보여주는 question header다.
- 범용 카드 grid보다 hub journey와 한 개의 primary workbench를 먼저 보여준다.
- 번호는 실제 sequence와 실제 경로 순서에만 사용한다.
- terminal, metric, status, divider는 실제 명령·상태·경계를 전달할 때만 사용한다.
- 다크 관리자 dashboard, 네온, glow, blanket gradient, hover 이동을 사용하지 않는다.

주제별 workbench 예:

```text
00 Request Workbench
01 Request Packet Trace
02 Persistence Boundary
03 Failure Gate
04 Auth Boundary
05 Trust & Recovery Map
06 Test Harness
07 Cache State Inspector
08 Connection Console
09 Runtime Boundary
10 Pipeline Gate
11 Behavior Invariant Map
12 Event Delivery Trace
```

## 7. 콘텐츠 요구사항

반드시 중앙 sequence 문서와 대상 토픽 레포의 theory, implementation, checklist, 실제 code point를 근거로 작성한다.

각 구조 요소는 다음 중 하나와 연결되어야 한다.

```text
실제 요청 또는 입력
실제 actor와 책임 경계
실제 객체·token·cache·artifact·test·event 상태
실제 실패 또는 대안
실제 응답·로그·명령·테스트·코드 증거
실제 다음 질문
```

DB Access 대표 흐름:

```text
Client
-> PostController
-> PostCreateRequest
-> PostService
-> PostEntity
-> PostRepository
-> MySQL
-> PostResponse
-> JSON Response
```

실제 콘텐츠 대신 lorem ipsum, 임시 metric, 임시 chart, 임시 시스템 actor를 추가하지 않는다.
UI copy는 학습자가 선택하고 확인할 대상을 먼저 말하며 기술적으로 정확한 기존 내용을 마케팅 문구로 바꾸지 않는다.

## 8. 구현 요구사항

- HTML/CSS/Vanilla JavaScript와 상대 경로만 사용한다.
- hub와 상세 HTML은 `#app.app-shell`, `noscript`, data script, shared engine만 연결한다.
- compact context bar에서 repository와 현재 sequence를 표시한다.
- hub는 semantic `ol` 기반 sequence journey로 렌더링한다.
- 상세 화면은 question header와 5단계 learning nav를 제공한다.
- scenario selector는 `fieldset`, `legend`, button과 `aria-pressed`를 사용한다.
- 선택 scenario는 실제 `flowId`와 연결되고 flow의 첫 단계로 초기화된다.
- topic workbench는 signal trace, state snapshot, 관찰 증거, 판단을 함께 갱신한다.
- signal node는 passed, active, pending, blocked 상태를 label로도 전달한다.
- 이전/다음, 재생/일시정지, 속도와 native `<progress>`를 사용한다.
- 선택 step의 Problem, Concept, Action, Check를 code point와 context drawer에 연결한다.
- glossary와 관련 문서는 접을 수 있는 reference shelf에 둔다.
- verification은 native checkbox와 progress를 사용하고 현재 페이지 안에서만 상태를 유지한다.
- next question은 실제 same-repo 상세 경로 또는 repository journey로 연결한다.
- empty/fatal 상태는 무엇이 없고 어떤 파일을 확인할지 알려준다.
- 전체 DOM 재렌더링 뒤 `data-focus-key`로 선택 control의 focus를 복원한다.
- section observer로 learning nav의 `aria-current="location"`을 갱신한다.
- 상태 알림은 짧은 `role="status"` 한 곳으로 제한한다.
- `prefers-reduced-motion: reduce`에서는 자동 재생과 속도 control을 비활성화하고 정보를 즉시 갱신한다.
- 390px에서 page-level horizontal overflow가 없어야 하며 긴 trace와 code만 해당 영역에서 스크롤한다.

## 9. visual-lab-data.js 데이터 필수 구조

허브 데이터:

```js
window.visualLabData = {
  kind: "hub",
  title: "Topic Visual Lab",
  description: "이 레포의 학습 경로",
  sequences: [
    {
      sequence: "NN",
      title: "주제",
      topic: "영문 범위",
      href: "./sequences/NN/index.html",
      summary: "학습 질문"
    }
  ]
};
```

상세 데이터:

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
          problem: "관찰할 문제",
          concept: "책임 또는 개념",
          action: "이동 또는 판단",
          check: "검증 증거",
          codePointIds: ["controller-entry"]
        }
      ]
    }
  ],
  workbench: {
    kind: "request-trace",
    title: "주제별 워크벤치",
    instruction: "조건을 선택하고 경로를 관찰하세요.",
    scenarios: [
      {
        id: "success",
        label: "성공 조건",
        flowId: "main-flow",
        tone: "recovered",
        prompt: "어디를 관찰해야 할까요?",
        route: ["Client", "Controller", "Service", "Repository"],
        snapshot: [
          { label: "요청", value: "실제 요청" },
          { label: "결과", value: "실제 결과", tone: "recovered" }
        ],
        evidence: "실제 확인 지점",
        outcome: "증거로 내릴 판단"
      }
    ]
  },
  codePoints: [],
  concepts: [],
  responsibilities: [],
  checks: [],
  next: { id: "NN", title: "다음 주제", reason: "다음 질문" }
};
```

데이터 규칙:

- 각 시퀀스는 3~4개의 실제 scenario를 제공한다.
- `flowId`는 같은 객체의 `flows[].id`와 일치해야 한다.
- `tone`은 `signal`, `blocked`, `warning`, `recovered` 중 하나다.
- `route`는 실제 actor 또는 책임·신뢰·runtime·pipeline 경계 문자열 배열이다.
- `snapshot`은 label/value와 선택적 semantic tone을 가진 항목을 2개 이상 둔다.
- blocked scenario의 `stopAfter`는 마지막 도달 route의 0-based index다.
- 실제 broadcast가 있는 realtime scenario에만 `fanOut`을 추가한다.
- `flows[].steps`는 Problem, Concept, Action, Check가 드러나는 4~6단계로 둔다.
- legacy 데이터의 fallback trace는 허용하지만 신규 또는 수정 시퀀스에는 `workbench`를 명시한다.

## 10. visual-lab.js 필수 동작

- `kind: "hub"`이면 context bar, intro, journey와 empty state를 렌더링한다.
- `kind: "sequence"`이면 question, learning nav, workbench, evidence, verification, next를 렌더링한다.
- scenario 선택과 flow/step state를 일관되게 갱신한다.
- route 길이와 step 수가 달라도 현재 step을 전체 route에 비례해 매핑한다.
- `stopAfter` 뒤 route는 disabled blocked 상태와 `도달하지 않음` label을 사용한다.
- step의 `codePointIds`로 code evidence를 찾고 없으면 명확한 empty state를 보여준다.
- 관련 문서 링크는 새 탭으로 열고 `rel="noreferrer"`를 사용한다.
- 첫/마지막 이동 button과 reduced-motion playback button을 올바르게 disabled 처리한다.
- 전체 재렌더링 전 timer를 해제하고 focus key를 복원한다.
- DOM root가 없거나 data kind가 잘못돼도 JavaScript error 대신 안내 상태를 제공한다.

## 11. Shared Engine과 문서 동기화

공통 `visual-lab.js`와 `styles.css`는 다음 8개 토픽 레포에 같은 내용으로 로컬 복제한다.

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

공통 engine을 바꾸면 8개 사본을 모두 갱신하고 hash를 비교한다.
한 레포를 다른 서브모듈의 runtime dependency로 만들거나 CDN, symlink, 새 package를 추가하지 않는다.

핵심 data field, token, component state 또는 검증 방식이 바뀌면 중앙 design guide, content spec, implementation plan, review prompt와 validator를 실제 코드에 맞게 동기화한다.
README 전체를 재작성하지 말고 Visual Lab 위치나 실행 방법이 실제와 다를 때만 필요한 부분을 수정한다.

## 12. 완료 후 검수

정적 검사:

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

shasum */docs/visual-lab/visual-lab.js
shasum */docs/visual-lab/styles.css
```

로컬 브라우저:

```bash
cd <topic-repo>
python3 -m http.server 8080 -d docs/visual-lab
```

반드시 확인할 것:

- hub journey와 모든 구현 상세 페이지
- 모든 scenario와 연결된 flow
- signal route, snapshot, evidence, code/context drawer
- verification progress와 next question link
- keyboard focus와 재렌더링 뒤 focus 복원
- reduced motion의 정적 대체 상태
- 1440x1000, 1024x900, 768x1024, 390x844
- 긴 한국어, path, command, code와 page-level overflow
- browser console error 없음
- 화면과 데이터에 secret, 정답 브랜치명, 긴 완성 구현 코드가 없음

공통 CSS/JS를 수정했다면 00~12 전체를 desktop과 mobile에서 확인한다.
브라우저 검수나 push가 끝나지 않았다면 완료로 보고하지 않는다.
