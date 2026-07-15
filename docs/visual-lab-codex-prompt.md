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
docs/visual-lab/assets/system-icons.svg
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
- 완성된 workbench는 책임 주체 node와 전달 edge를 분리한 semantic diagram을 primary로 사용하고 legacy route는 fallback으로 유지한다.
- node에는 icon, kind, role과 visible boundary label을 표시하고 edge에는 방향, verb, payload와 관계 kind를 표시한다.
- node icon은 직접 렌더링 가능한 로컬 `docs/visual-lab/assets/icons/{icon}.svg`를 사용한다. `system-icons.svg`는 원본 sprite와 호환 자료로 보존한다.
- 각 시퀀스는 `workbench.visual`의 `src`, `alt`, `caption`으로 주제 설명 SVG 한 개를 연결하고 `assets/SOURCE.md`, `assets/LICENSES.md`를 유지한다.
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

semantic diagram에서 actor, service, handler, repository, broker, runtime과 상태를 관찰할 resource는 node다. HTTP method, 메서드 호출과 검증 행위는 edge `verb`, request DTO, token, event, query, command와 이동 파일은 edge `payload`로 둔다. artifact는 생성·실행 상태 자체를 비교할 때만 node로 둔다.

`check`, `evidence`, `outcome`은 실제 관찰 범위를 넘지 않는다.

- Service 단위 테스트를 HTTP path/status/body 계약으로 표현하지 않는다.
- mock 발행 호출을 외부 API, mail server나 RabbitMQ의 실제 수신 성공으로 표현하지 않는다.
- `contextLoads`를 endpoint 정상 동작 증거로 사용하지 않는다.
- in-memory map을 재시작 이후에도 유지되는 영속 멱등성으로 표현하지 않는다.
- build/deploy 명령 종료를 container 상태, application log, HTTP 응답까지 정상이라는 증거로 사용하지 않는다.

DB Access 대표 흐름:

```text
Client -- 요청 · POST /posts + PostCreateRequest --> PostController
PostController -- 호출 · create(request) --> PostService
PostService -- 변환 · Request DTO → Entity --> PostService
PostService -- 저장 · save(PostEntity) --> PostRepository
PostRepository -- 영속화 · INSERT posts row --> MySQL
MySQL -- 반환 · persisted row + id --> PostRepository
PostRepository -- 반환 · PostEntity --> PostService
PostService -- 변환 · Entity → PostResponse --> PostController
PostController -- 응답 · 201 + JSON --> Client
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
- `scenario.diagram`의 caption, lanes, semantic nodes, edge verb/payload/kind와 notReached를 함께 갱신한다.
- `from`과 `to`는 `workbench.nodes` key를 참조하고 node boundary는 색상이나 배치가 아니라 text로 표시한다.
- 서로 다른 lane은 하나의 직선 timeline으로 합치지 않는다. 현재 lane만 단계 상태와 progress를 가지며 다른 lane은 `선택 가능`으로 표시한다.
- semantic edge의 code evidence는 edge 또는 node의 명시적 `codePointIds`로 연결하며 legacy flow step 위치를 상속하지 않는다.
- signal node는 passed, active, pending, blocked 상태를 label로도 전달한다.
- semantic edge가 단계 control이면 native button을 사용하고 접근 가능한 이름에 from, to, verb, payload, state를 포함한다.
- 이전/다음과 native `<progress>`를 사용한다. 자동 재생과 속도 control은 두지 않는다.
- 선택 step의 Problem, Concept, Action, Check를 code point와 context drawer에 연결한다.
- glossary와 관련 문서는 접을 수 있는 reference shelf에 둔다.
- verification은 native checkbox와 progress를 사용하고 현재 페이지 안에서만 상태를 유지한다.
- next question은 실제 same-repo 상세 경로 또는 repository journey로 연결한다.
- empty/fatal 상태는 무엇이 없고 어떤 파일을 확인할지 알려준다.
- 전체 DOM 재렌더링 뒤 `data-focus-key`로 선택 control의 focus를 복원한다.
- section observer로 learning nav의 `aria-current="location"`을 갱신한다.
- 상태 알림은 앱 재렌더링 밖에 유지되는 짧은 `role="status"` 한 곳으로 제한하고 현재 lane, from/to, verb와 payload를 알린다.
- 720px 이하에서 semantic diagram을 node -> edge -> node의 세로 방향으로 바꾸고 arrow label과 payload를 유지한다.
- `prefers-reduced-motion: reduce`에서는 transition과 smooth scroll을 제거하고 active edge의 방향·payload·상태를 정적으로 갱신한다.
- 390px에서 page-level horizontal overflow가 없어야 하며 legacy trace와 긴 code만 해당 영역에서 제한적으로 스크롤한다.

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
    visual: {
      src: "../../assets/diagrams/NN-topic.svg",
      alt: "주제의 핵심 시스템 관계",
      caption: "관찰 전에 알아야 할 경계를 한 문장으로 설명합니다."
    },
    terms: [
      { term: "Repository", meaning: "저장소 접근 방법을 Service에서 분리하는 책임" },
      { term: "Entity", meaning: "DB table과 저장 규칙에 맞춘 객체" }
    ],
    comparison: {
      label: "메모리와 DB의 데이터 수명",
      left: { title: "Process memory", body: "애플리케이션 프로세스 종료와 함께 사라집니다." },
      right: { title: "External database", body: "DB와 volume을 유지하면 새 프로세스도 같은 row를 읽습니다." }
    },
    nodes: {
      client: {
        label: "Client",
        icon: "client",
        kind: "actor",
        role: "HTTP 요청 전송",
        boundary: "Client"
      },
      controller: {
        label: "PostController",
        icon: "api",
        kind: "request handler",
        role: "요청 수신과 Service 호출",
        boundary: "Web",
        codePointIds: ["controller-entry"]
      },
      service: {
        label: "PostService",
        icon: "service",
        kind: "application service",
        role: "비즈니스 흐름 조립",
        boundary: "Application"
      },
      repository: {
        label: "PostRepository",
        icon: "repository",
        kind: "persistence port",
        role: "저장소 접근 위임",
        boundary: "Persistence"
      }
    },
    scenarios: [
      {
        id: "success",
        label: "성공 조건",
        flowId: "main-flow",
        tone: "recovered",
        prompt: "어디를 관찰해야 할까요?",
        prediction: {
          prompt: "어느 책임이 다음에 호출될까요?",
          options: [
            { id: "service", label: "Service" },
            { id: "database", label: "Database" }
          ],
          answer: "service",
          explanation: "Controller는 HTTP 요청을 Service의 애플리케이션 흐름으로 넘깁니다."
        },
        route: ["Client", "Controller", "Service", "Repository"],
        diagram: {
          caption: "PostCreateRequest가 Web과 Application 책임을 지나 Repository에 전달됩니다.",
          lanes: [
            {
              id: "create-request",
              label: "Request → Persistence",
              description: "책임 주체 사이에서 이동하는 요청 payload를 확인합니다.",
              steps: [
                {
                  from: "client",
                  to: "controller",
                  verb: "생성 요청",
                  payload: "POST /posts · PostCreateRequest",
                  kind: "request"
                },
                {
                  from: "controller",
                  to: "service",
                  verb: "처리 위임",
                  payload: "create(request)",
                  kind: "call",
                  codePointIds: ["controller-entry"]
                },
                {
                  from: "service",
                  to: "repository",
                  verb: "저장 요청",
                  payload: "PostEntity",
                  kind: "persist",
                  check: "실제 save 호출과 저장 결과를 확인합니다."
                }
              ]
            }
          ]
        },
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
- `nodes`는 id로 참조하는 keyed catalog이고 각 node에 `label`, `icon`, `kind`, `role`, `boundary`, 선택적 `codePointIds`를 둔다.
- `icon`은 로컬 sprite가 제공하는 `person`, `client`, `tool`, `api`, `service`, `repository`, `database`, `gate`, `security`, `token`, `external`, `mail`, `test`, `fixture`, `cache`, `websocket`, `broker`, `runtime`, `artifact`, `config`, `pipeline`, `host`, `refactor`, `event`, `queue`, `consumer`, `evidence`, `memory`, `handler`, `response` 중 하나다.
- `diagram.caption`은 전체 경로를 한 문장으로 읽고 `lanes`는 서로 다른 책임 흐름을 분리한다.
- lane은 `id`, `label`, `description`과 2~7개 step을 가진다.
- diagram step의 `from`, `to`는 node key를 참조하고 `verb`, `payload`, `kind`를 가진다. `kind`는 `request`, `call`, `transform`, `persist`, `response`, `failure`, `event`, `config`, `compare` 중 하나다.
- 실행되지 않은 책임은 `notReached: [{ label, reason }]`로 설명한다.
- `route`는 기존 진행 상태와 fallback을 위해 실제 actor 또는 책임·신뢰·runtime·pipeline 경계 문자열 배열로 유지한다.
- `snapshot`은 label/value와 선택적 semantic tone을 가진 항목을 2개 이상 둔다.
- blocked scenario의 `stopAfter`는 마지막 도달 route의 0-based index다.
- 실제 broadcast가 있는 realtime scenario에만 `fanOut`을 추가한다.
- `flows[].steps`는 Problem, Concept, Action, Check가 드러나는 4~6단계로 둔다.
- legacy 데이터의 fallback trace는 허용하지만 신규 또는 수정 시퀀스에는 `workbench`를 명시한다.
- `check`, `evidence`, `outcome`은 단위 테스트, mock, in-memory 상태와 명령이 실제로 보장하는 범위를 넘지 않는다.

## 10. visual-lab.js 필수 동작

- `kind: "hub"`이면 context bar, intro, journey와 empty state를 렌더링한다.
- `kind: "sequence"`이면 question, learning nav, workbench, evidence, verification, next를 렌더링한다.
- scenario 선택과 flow/step state를 일관되게 갱신한다.
- `scenario.diagram`이 있으면 semantic diagram을 primary로 렌더링하고 caption, lane, node, edge와 notReached를 semantic element로 구성한다.
- local node icon은 `<img src="../../assets/icons/{icon}.svg" alt="">`로 사용하고 visible node text를 생략하지 않는다.
- 주제 설명 SVG는 `workbench.visual`에서 읽어 `<img>`와 visible `figcaption`으로 표시하며 load error에는 text fallback을 남긴다.
- semantic edge button은 선택 step의 Problem, Concept, Action, Check와 code point를 갱신하고 재렌더링 뒤 focus를 복원한다.
- `scenario.diagram`이 없는 legacy fallback에서만 route 길이와 flow step 수를 비례해 매핑한다. semantic diagram의 edge는 각 button과 evidence step을 1:1로 연결한다.
- `stopAfter` 뒤 route는 disabled blocked 상태와 `도달하지 않음` label을 사용한다.
- step의 `codePointIds`로 code evidence를 찾고 없으면 명확한 empty state를 보여준다.
- 관련 문서 링크는 새 탭으로 열고 `rel="noreferrer"`를 사용한다.
- 첫/마지막 이동 button을 올바르게 disabled 처리한다.
- 전체 재렌더링 전 focus key를 저장하고 복원한다.
- DOM root가 없거나 data kind가 잘못돼도 JavaScript error 대신 안내 상태를 제공한다.

## 11. Shared Engine과 문서 동기화

공통 `visual-lab.js`, `styles.css`, `assets/icons/*.svg`와 `assets/system-icons.svg`는 다음 8개 토픽 레포에 같은 내용으로 로컬 복제한다.

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

공통 engine이나 icon asset을 바꾸면 8개 사본을 모두 갱신하고 hash를 비교한다.
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
shasum */docs/visual-lab/assets/system-icons.svg
find */docs/visual-lab/assets/icons -name '*.svg' -type f -print0 | sort -z | xargs -0 shasum
```

로컬 브라우저:

```bash
cd <topic-repo>
python3 -m http.server 8080 -d docs/visual-lab
```

반드시 확인할 것:

- hub journey와 모든 구현 상세 페이지
- 모든 scenario와 연결된 flow
- semantic diagram의 caption, lane, node boundary, edge verb/payload/kind, notReached와 legacy signal route fallback
- verification progress와 next question link
- keyboard focus와 재렌더링 뒤 focus 복원
- mobile semantic diagram 세로화와 arrow label/payload 유지
- reduced motion의 정적 대체 상태
- 1440x1000, 1024x900, 768x1024, 390x844
- 긴 한국어, path, command, code와 page-level overflow
- browser console error 없음
- 화면과 데이터에 secret, 정답 브랜치명, 긴 완성 구현 코드가 없음
- evidence가 테스트 종류와 runtime 관찰 범위를 넘어 통합 성공을 과장하지 않음

공통 CSS/JS를 수정했다면 00~12 전체를 desktop과 mobile에서 확인한다.
브라우저 검수나 push가 끝나지 않았다면 완료로 보고하지 않는다.
