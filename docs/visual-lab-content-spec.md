# A&I Backend Visual Lab Content Spec

## 1. 문서 목적

이 문서는 A&I Backend Visual Lab에서 보여줄 학습 콘텐츠의 범위와 데이터 구조를 정의한다.

Visual Lab은 상세 이론 문서를 대체하지 않는다.
각 시퀀스와 토픽 레포의 이론 문서, 구현 문서, 체크리스트로 이동하기 위한 시각적 진입점이다.
정답 브랜치는 작성자가 흐름을 검증할 때 참고할 수 있지만 화면과 데이터에는 직접 노출하지 않는다.

## 2. 모든 시퀀스 공통 브랜치 기준

Visual Lab은 특정 시퀀스 하나만 설명하는 페이지가 아니다.
모든 시퀀스는 아래 브랜치 규칙을 기준으로 시각화한다.

```text
NN-implementation
-> 학생 실습용 starter 브랜치
-> TODO와 순서형 힌트가 들어 있는 구현 시작점
-> Visual Lab에서는 "학생이 직접 따라갈 흐름"으로 연결한다.

NN-answer
-> 강사용 비교/정답 브랜치
-> 완성된 코드와 정답 문서가 있는 기준점
-> Visual Lab 작성자는 검수 때 참고하되 화면과 데이터에는 브랜치명을 노출하지 않는다.
```

`NN`은 `docs/sequences`의 번호와 같아야 한다.

예:

```text
00-implementation / 00-answer
01-implementation / 01-answer
02-implementation / 02-answer
...
12-implementation / 12-answer
```

Visual Lab 콘텐츠를 만들 때는 각 시퀀스마다 아래 순서를 따른다.

1. 중앙 `docs/sequences/NN-...md`에서 학습 범위를 확인한다.
2. 해당 토픽 레포의 `NN-answer` 브랜치에서 실제 완성 흐름을 검수한다.
3. 해당 토픽 레포의 `NN-implementation` 브랜치에서 학생이 따라갈 구현 순서를 확인한다.
4. HTML에는 상세 이론이나 정답 코드 전체를 복붙하지 않는다.
5. 핵심 실행 흐름과 확인 지점만 보여주고 정답 브랜치명은 숨긴다.

## 3. 모든 시퀀스 데이터 정의 규칙

토픽 레포의 `docs/visual-lab/index.html`은 허브로 사용한다.
허브 데이터는 `kind: "hub"`와 시퀀스 목록을 가진다.
각 시퀀스 상세 데이터는 `docs/visual-lab/sequences/NN/visual-lab-data.js`에 둔다.

허브 데이터 예:

```js
window.visualLabData = {
  kind: "hub",
  title: "DB Access Lab Visual Lab",
  description: "이 레포는 02-06 시퀀스를 다룹니다.",
  sequences: [
    {
      sequence: "02",
      title: "DB Access",
      topic: "Persistence and layered architecture",
      href: "./sequences/02/index.html",
      summary: "Controller에서 MySQL까지 저장 흐름을 봅니다."
    }
  ]
};
```

각 시퀀스 상세 파일은 아래 필드를 가진 하나의 canonical 객체로 관리합니다. `kind: "sequence"` 데이터 안에 같은 내용을 다시 담은 `sequences` 배열을 만들지 않습니다. 아래 예시는 기존 canonical 필드를 보이기 위해 scenario 1개만 축약한 것이며 필수 `nodes`와 `diagram` 계약은 3.1.1의 완성 예시를 따릅니다.

```js
window.visualLabData = {
  kind: "sequence",
  sequence: "NN",
  title: "한국어 주제명",
  goal: "한 줄 목표",
  problem: "이 시퀀스가 해결하는 문제",
  workbench: {
    kind: "persistence",
    title: "Persistence Boundary",
    instruction: "저장 조건을 선택하고 객체가 MySQL까지 이동하는 경로와 증거를 확인합니다.",
    scenarios: [
      {
        id: "create-to-mysql",
        label: "DB 저장 성공",
        flowId: "main-flow",
        tone: "recovered",
        prompt: "POST 요청이 계층을 지나 영속 저장되는 경로를 관찰합니다.",
        route: ["Client", "Controller", "Service", "Repository", "MySQL"],
        snapshot: [
          { label: "저장 위치", value: "MySQL", tone: "recovered" }
        ],
        evidence: "저장 후 생성 id와 조회 결과를 확인합니다.",
        outcome: "서버가 다시 시작되어도 DB row가 남습니다."
      }
    ]
  },
  actors: [
    { id: "client", label: "Client", kind: "client" },
    { id: "server", label: "Server", kind: "server" },
    { id: "db", label: "DB", kind: "db" }
  ],
  flows: [
    {
      id: "main-flow",
      title: "핵심 요청 흐름",
      steps: [
        {
          id: "step-1",
          from: "client",
          to: "server",
          messageKind: "request",
          problem: "왜 이 단계가 필요한가",
          concept: "어떤 개념을 보는가",
          action: "무엇을 구현하거나 확인하는가",
          check: "무엇으로 확인하는가",
          codePointIds: ["controller-create"]
        }
      ]
    }
  ],
  codePoints: [
    {
      id: "controller-create",
      title: "Controller 요청 진입",
      file: "src/main/kotlin/.../PostController.kt",
      language: "kotlin",
      snippet: "실제 핵심 코드 3-12줄만 넣는다.",
      explanation: "요청 입구만 설명한다.",
      check: "요청 경로와 메서드가 맞는지 확인한다."
    }
  ],
  flow: [
    {
      id: "step-1",
      label: "단계 이름",
      problem: "왜 이 단계가 필요한가",
      concept: "어떤 개념을 보는가",
      action: "무엇을 구현하거나 확인하는가",
      check: "무엇으로 확인하는가"
    }
  ],
  concepts: [],
  practice: [],
  mentorHints: []
}
```

필드 작성 규칙:

- 상세 데이터의 `kind`, `sequence`, `title`, `goal`, `problem`, `workbench`, `actors`, `flows`, `codePoints`는 필수 필드다.
- 기존 소비자 호환을 위해 `flow`도 유지할 수 있다.
- 각 `flows[].steps`는 4~6개 정도의 학습 흐름으로 제한한다.
- 각 시퀀스는 최소 2개 이상의 `codePoints`를 가진다.
- Visual Lab 데이터에는 `answerBranch`, `sourceAnswerBranch`, `NN-answer` 문자열을 넣지 않는다.
- 긴 이론, 정답 코드, 완성 구현 코드는 넣지 않는다.

## 3.1 Workbench 데이터 규칙

모든 구현 완료 시퀀스는 top-level `workbench`를 가진다. 공통 renderer는 `workbench`를 입력 조건 선택, 경로 예측, 단계별 책임 이동, 상태 변화, 관찰 근거와 회고 순서로 렌더링한다. 아래 축약 예시는 호환용 route와 snapshot을 설명하며 완성된 workbench는 3.1.1의 `nodes`와 `diagram`도 함께 제공한다.

```js
workbench: {
  kind: "cache",
  title: "Cache State Inspector",
  instruction: "조건을 선택하고 Redis와 DB 경계를 비교합니다.",
  visual: {
    src: "../../assets/diagrams/07-cache-state-cycle.svg",
    alt: "MySQL 원본과 Redis 파생 복사본의 조회·만료·무효화 흐름",
    caption: "Redis 값은 TTL이 있는 파생 복사본이며 key가 없을 때 MySQL 원본을 다시 읽습니다."
  },
  scenarios: [
    {
      id: "cache-miss",
      label: "post:1 key 없음",
      flowId: "lookup-flow",
      tone: "signal",
      prompt: "결과를 열기 전에 DB 조회와 Redis 저장이 일어날지 예측합니다.",
      observationTitle: "비어 있는 key를 조회하면 어느 저장소를 먼저 읽을까?",
      theoryRef: "../../../theory.md#seq-07",
      reflection: {
        prompt: "MISS 뒤에 원본을 읽고 cache를 채우는 이유를 한 문장으로 써 보세요.",
        hint: "원본 저장소와 파생 복사본의 수명을 구분합니다."
      },
      route: ["Client", "PostQueryService", "Redis miss", "Repository", "DB"],
      snapshot: [
        { label: "Cache lookup", value: "miss", tone: "warning" },
        { label: "DB lookup", value: "findById(id)", tone: "signal" }
      ],
      evidence: "cache miss 뒤 Repository 조회가 이어지는지 확인합니다.",
      outcome: "DB 원본을 반환하고 다음 조회를 위해 캐시를 채웁니다."
    }
  ]
}
```

`workbench` 필드:

| 필드 | 필수 | 규칙 |
|---|---|---|
| `kind` | 필수 | 아래 13개 시퀀스 kind 중 하나를 사용한다. |
| `title` | 필수 | 주차별 primary workbench 이름을 짧게 쓴다. |
| `instruction` | 필수 | 학습자가 무엇을 선택하고 관찰할지 능동형 문장으로 쓴다. |
| `visual` | 필수 | `{ src, alt, caption }`으로 시퀀스의 기본 주제 설명 SVG와 대체 설명을 연결한다. |
| `terms` | 필수 | 예측 전에 필요한 용어를 `{ term, meaning }` 2개 이상으로 짧게 설명한다. 화면에서는 기본 닫힌 `details`로 제공해 모르는 학생이 먼저 확인하되 첫 행동을 밀어내지 않는다. |
| `comparison` | 필수 | `{ label, left, right }`로 관찰 뒤 구분할 두 조건의 인과 차이를 설명한다. |
| `nodes` | 필수 | scenario diagram이 참조할 책임 주체와 관찰 resource를 id로 관리하는 keyed catalog다. |
| `scenarios` | 필수 | 실제 이론과 흐름에 근거한 조건을 3~4개 둔다. |

`scenarios[]` 필드:

| 필드 | 필수 | 규칙 |
|---|---|---|
| `id` | 필수 | 시퀀스 안에서 고유한 kebab-case id다. |
| `label` | 필수 | 조건 선택 button에 표시할 짧은 이름이다. |
| `flowId` | 필수 | 같은 객체의 `flows[].id` 중 하나를 참조한다. |
| `tone` | 필수 | `signal`, `blocked`, `warning`, `recovered` 중 하나다. |
| `prompt` | 필수 | 현재 조건에서 관찰할 질문 또는 상황이다. |
| `observationTitle` | 필수 | 예측 뒤 실제 경로에서 확인할 한 가지 질문을 자연스러운 한국어로 쓴다. |
| `prediction` | 필수 | `{ prompt, options, answer, explanation }`으로 관찰 전 판단과 관찰 뒤 설명을 연결한다. |
| `visual` | 선택 | 기본 구조와 다른 조건만 `{ src, alt, caption }`으로 scenario 전용 SVG를 연결한다. 생략하면 `workbench.visual`을 사용한다. |
| `theoryRef` | 필수 | `../../../theory.md#seq-NN`처럼 현재 조건을 설명하는 이론 절을 명시적 anchor까지 연결한다. |
| `reflection` | 필수 | `{ prompt, hint }`로 관찰한 인과 규칙을 학습자가 자기 말로 다시 쓰게 한다. 입력 내용은 현재 화면 상태에만 두고 전송하지 않는다. |
| `route` | 필수 | 실제 actor, destination, 저장소 또는 책임 경계를 순서대로 쓴 문자열 배열이다. |
| `snapshot` | 필수 | `{ label, value, tone? }` 항목을 2개 이상 둔 배열이다. `tone`은 scenario와 같은 네 값을 사용한다. |
| `evidence` | 필수 | 로그, 응답, 테스트, 상태 또는 화면에서 확인할 실제 증거다. |
| `outcome` | 필수 | 관찰 결과로 학습자가 내려야 할 판단이다. |
| `diagram` | 필수 | 한 문장 `caption`, 책임별 `lanes`, 동사와 payload를 가진 `steps`, 선택적 `notReached`를 제공한다. |
| `stopAfter` | 선택 | 마지막으로 도달한 `route`의 0-based index다. 이후 node는 `도달하지 않음`으로 표시한다. |
| `fanOut` | 선택 | `realtime`에서만 사용하며 실제 메시지를 받는 대상 label 배열이다. |

작성 규칙:

- scenario `label`은 `hit`, `miss`, `blocked`, 성공/실패처럼 관찰 결과를 미리 공개하지 않고 입력 조건만 말한다.
- `prompt`는 현재 주어진 상태, `prediction.prompt`는 학생이 내려야 할 판단 하나만 맡는다. 입력 조건 전체를 예측 질문에서 다시 쓰지 않는다.
- `prediction.explanation`은 선택이 갈린 기준, `diagram.caption`은 실제 전체 경로, `evidence`는 증거의 종류·범위·한계, `outcome`은 관찰 뒤 남길 인과 규칙 하나만 맡는다.
- `observationTitle`은 20~35자 안팎의 관찰 대상, lane `description`은 다른 lane과 구분되는 책임을 설명한다. caption의 축약본이나 scenario 전체 경로를 반복하지 않는다.
- route와 snapshot에 임시 actor, 의미 없는 수치나 장식용 metric을 넣지 않는다.
- `stopAfter`는 실패 또는 차단 조건에서 실제 도달 지점이 확인될 때만 쓴다.
- `fanOut`에는 연결만 된 대상이 아니라 실제로 해당 topic을 구독해 메시지를 받는 대상만 쓴다.
- scenario를 바꾸면 `flowId`에 연결된 `flows[].steps`가 Problem, Concept, Action, Check evidence를 제공해야 한다.
- 공통 renderer는 과거 데이터의 `flows`에서 fallback trace를 만들 수 있지만, 완료된 시퀀스는 fallback을 최종 상태로 사용하지 않는다.
- `theoryRef`가 가리키는 절에는 같은 id의 명시적 HTML anchor를 둔다. 자동 생성 heading anchor에만 의존하지 않는다.
- 해당 theory 절 끝에는 `[Visual Lab에서 입력 조건을 보고 경로 예측하기](./visual-lab/sequences/NN/)` 링크를 두어 왕복할 수 있게 한다.
- `reflection.prompt`는 정답 문장을 요구하지 않는다. “어느 경계에서 무엇이 바뀌었는가”처럼 실제로 관찰한 관계를 다시 쓰게 한다.
- reflection은 회상 행동이므로 유지하되 `outcome`을 단순히 의문형으로 복사하지 않는다.

### 3.1.1 Semantic diagram 데이터 계약

`nodes`와 `diagram`은 책임 주체와 이동하는 payload를 분리한다. 아래 예시는 validation 실패 조건을 축약한 것이다.

```js
workbench: {
  kind: "gate",
  title: "Failure Gate",
  instruction: "잘못된 요청이 어느 책임 경계에서 멈추는지 확인합니다.",
  nodes: {
    client: {
      label: "Client",
      icon: "client",
      kind: "actor",
      role: "HTTP 요청 전송",
      boundary: "Client",
      systemLayer: "outside"
    },
    validation: {
      label: "Spring MVC · Bean Validation",
      icon: "gate",
      kind: "validation gate",
      role: "argument binding 뒤 Controller method 전에 입력 조건 판단",
      boundary: "HTTP argument resolution",
      systemLayer: "interface",
      codePointIds: ["controller-create"]
    },
    handler: {
      label: "GlobalExceptionHandler",
      icon: "handler",
      kind: "exception handler",
      role: "검증 예외를 HTTP 오류 응답으로 변환",
      boundary: "Error response mapping",
      systemLayer: "interface"
    },
    controller: {
      label: "PostController",
      icon: "api",
      kind: "request handler",
      role: "검증을 통과한 요청만 수신",
      boundary: "Web",
      systemLayer: "interface"
    },
    service: {
      label: "PostService",
      icon: "service",
      kind: "application service",
      role: "유효한 요청의 처리 흐름 조립",
      boundary: "Application",
      systemLayer: "application"
    }
  },
  scenarios: [
    {
      id: "invalid-request",
      label: "입력 검증 실패",
      flowId: "validation-flow",
      tone: "blocked",
      prompt: "잘못된 title이 Service 전에 멈추는지 확인합니다.",
      observationTitle: "잘못된 요청은 어느 책임에서 멈출까?",
      theoryRef: "../../../theory.md#seq-03",
      reflection: {
        prompt: "왜 Service가 호출되지 않았는지 경계 이름을 넣어 써 보세요.",
        hint: "argument binding 뒤 Controller method 앞을 봅니다."
      },
      route: ["Client", "Spring MVC · Bean Validation", "GlobalExceptionHandler", "Client"],
      diagram: {
        caption: "PostCreateRequest가 validation gate에서 거부되어 Service는 호출되지 않습니다.",
        lanes: [
          {
            id: "request-validation",
            label: "Request → Validation",
            description: "요청 payload와 실패 증거가 생기는 책임 경계를 봅니다.",
            steps: [
              {
                from: "client",
                to: "validation",
                verb: "요청 · 바인딩",
                payload: "POST /posts · JSON → PostCreateRequest",
                kind: "request",
                effect: {
                  kind: "transform",
                  subject: "요청 본문",
                  before: "JSON 문자열",
                  after: "PostCreateRequest 객체"
                },
                evidenceScope: "runtime"
              },
              {
                from: "validation",
                to: "handler",
                verb: "검증 실패",
                payload: "MethodArgumentNotValidException",
                kind: "failure",
                effect: {
                  kind: "gate",
                  subject: "요청 실행 경로",
                  before: "Controller 진입 대기",
                  after: "validation gate에서 중단"
                },
                evidenceScope: "runtime",
                concept: "Service 이전 validation gate",
                codePointIds: ["controller-create"]
              },
              {
                from: "handler",
                to: "client",
                verb: "오류 응답",
                payload: "400 ErrorResponse · field errors",
                kind: "response",
                effect: {
                  kind: "return",
                  subject: "HTTP 응답",
                  before: "검증 예외",
                  after: "400 ErrorResponse"
                },
                evidenceScope: "runtime",
                check: "실제 error response의 field와 message를 확인합니다."
              }
            ]
          }
        ],
        notReached: [
          {
            label: "PostController method body · PostService",
            reason: "argument validation이 실패해 Controller method와 application service를 호출하지 않습니다."
          }
        ]
      },
      snapshot: [
        { label: "실패 경계", value: "Bean Validation", tone: "blocked" },
        { label: "Service 호출", value: "도달하지 않음", tone: "blocked" }
      ],
      evidence: "실제 validation error response를 확인합니다.",
      outcome: "잘못된 입력은 Service 책임으로 넘어가지 않습니다."
    }
  ]
}
```

`nodes` 작성 규칙:

- key는 scenario 안에서 안정적으로 재사용할 kebab-case 또는 camelCase id다.
- 각 node는 `label`, `icon`, `kind`, `role`, `boundary`, `systemLayer`를 모두 가진다. 실제 코드와 연결할 때만 `codePointIds`를 추가한다.
- node는 actor, service, handler, repository, storage, broker, runtime 또는 상태 자체를 관찰할 artifact/resource다.
- method, command, HTTP verb, 검증 행위처럼 두 책임 사이에서 일어나는 동작은 node가 아니라 edge `verb`다.
- request DTO, token, event, query, command와 전달 파일은 기본적으로 edge `payload`다. artifact의 생성·실행 상태를 비교할 때만 별도 node로 둔다.
- `boundary`는 화면에 표시되는 책임 경계 이름이며 색상이나 위치만으로 대신하지 않는다.
- `systemLayer`는 `outside`, `interface`, `application`, `resource`, `integration`, `runtime` 중 하나다. 호출자, 입구·출구, 서비스·정책, 상태·데이터, 연동·메시징, 실행·배포라는 시스템 위치를 뜻하며 진행 상태를 뜻하지 않는다.
- `icon`은 `person`, `client`, `tool`, `api`, `service`, `repository`, `database`, `gate`, `security`, `token`, `external`, `mail`, `test`, `fixture`, `cache`, `websocket`, `broker`, `runtime`, `artifact`, `config`, `pipeline`, `host`, `refactor`, `event`, `queue`, `consumer`, `evidence`, `memory`, `handler`, `response` 중 하나다.
- icon은 각 토픽 레포의 직접 렌더링 가능한 `docs/visual-lab/assets/icons/{icon}.svg`에 연결한다. `system-icons.svg`는 원본 sprite와 호환 자료로만 보존한다.
- `workbench.visual`과 선택적 `scenario.visual`의 `src`는 `docs/visual-lab/assets` 안의 로컬 SVG를 가리킨다. 두 visual은 모두 비어 있지 않은 `alt`, visible `caption`, `viewBox`를 가지며 외부 URL, script와 font를 포함하지 않는다.
- `assets/SOURCE.md`와 `assets/LICENSES.md`에 생성·파생 관계와 사용 조건을 기록한다. 외부 CDN, emoji와 network asset을 사용하지 않는다.

`diagram` 작성 규칙:

- `caption`은 선택한 조건의 전체 흐름과 핵심 판단을 한 문장으로 쓴다.
- `lanes`는 request/response와 event, build와 verify, Before와 After처럼 책임이 다른 흐름을 분리한다.
- 각 lane은 고유 `id`, 짧은 `label`, 읽는 목적을 설명하는 `description`, 2~7개의 `steps`를 가진다.
- 각 step의 `from`과 `to`는 `workbench.nodes` key를 참조하고 `verb`, `payload`, `kind`를 반드시 가진다.
- 각 step은 `effect: { kind, subject, before, after }`를 가진다. `kind`는 `transfer`, `transform`, `persist`, `gate`, `return`, `fanout`, `verify`, `preserve` 중 하나이며 화살표 전후의 차이를 비교할 수 있게 쓴다.
- `effect.subject`는 데이터 계약상 `payload`와 같을 수 있다. renderer는 두 값이 정규화 기준으로 같으면 subject 제목을 다시 보여주지 않고 before와 after만 표시한다.
- `payload 변환 전 → payload 변환 완료`, `호출 전 책임 → 호출 후 책임`, `반환 대기 → 호출자 보유`, `evidence가 아직 관찰되지 않음 → 상태가 판정됨`처럼 어느 주제에도 붙일 수 있는 틀 문장은 쓰지 않는다. 실제 key/value, collection 또는 row의 존재, 인증 주체, 연결·구독 대상, 최초 실패 gate, assertion 결과가 어떻게 달라졌는지 적는다.
- 각 step은 `evidenceScope`를 가진다. 값은 `code`, `test`, `runtime`, `manual`, `concept` 중 실제 확인 범위 하나다.
- edge `kind`는 `request`, `call`, `transform`, `persist`, `response`, `failure`, `event`, `config`, `compare` 중 하나다.
- `concept`, `check`, `codePointIds`는 해당 edge에서 실제 근거가 있을 때만 추가한다.
- `notReached`는 실행되지 않은 node 또는 책임 label과 그 이유를 함께 제공한다. 단순 opacity나 빈 node로 대신하지 않는다.
- `route`, `snapshot`, `evidence`, `outcome`, `flowId`는 기존 진행 상태와 evidence 연결을 위해 함께 유지한다.
- lane은 독립 비교 경로일 수 있으므로 전체 `lanes[].steps`를 하나의 시간축으로 해석하지 않는다. 현재 lane만 단계 진행 상태를 가지며 다른 lane은 선택 가능한 경로다.
- actor 표시 순서를 고정해야 할 때 `diagram.participants`에 `workbench.nodes` key를 중복 없이 쓴다. 이 값은 전체 비교 경로의 정렬 기준이며, active lane 화면에는 현재 lane step의 `from`과 `to`에 등장하는 node만 남긴다.
- 특정 lane의 participant 순서를 따로 고정할 때만 `lane.participants`에 현재 lane의 node key를 중복 없이 쓴다. 이 배열은 해당 lane의 모든 step `from`/`to`를 포함해야 하며 관련 없는 node를 추가하지 않는다.
- 한 lane을 본 뒤 비교할 경로가 정해져 있을 때만 `lane.nextLaneIds`에 같은 diagram의 lane id를 쓴다.
- progress는 현재 lane 범위만 사용한다. 학생이 수동으로 lane을 넘을 때는 `다음 경로`라고 표시한다.
- semantic edge의 code evidence는 edge의 `codePointIds`, 도착 node, 출발 node 순서의 명시적 연결만 사용한다. legacy flow step의 배열 위치를 상속하지 않는다.
- desktop message는 `from`, `to`, `verb`, `payload`를 맡고 current inspector는 `before → after`, 출발·도착 boundary와 `evidenceScope`를 맡는다. `check`와 실제 source는 아래 evidence section에서 한 번만 보여준다.
- 모바일 세로 흐름은 route, `verb`, `payload`, `kind`, boundary, `systemLayer`, state label과 `before → after`를 한 current-step surface에 합친다. 바로 뒤에 같은 current detail을 다시 만들지 않는다.
- edge가 단계 선택 control이면 keyboard focus와 접근 가능한 이름에 `from`, `to`, `verb`, `payload`, state가 모두 포함되어야 한다.
- reduced motion은 전달 애니메이션만 제거하며 caption, 방향, payload와 notReached 이유는 정적으로 유지한다.

코드 근거는 파일 경로 badge를 먼저 보여주지 않는다. 화면과 이론 문서 모두 다음 순서를 따른다.

```text
이 단계에서 확인할 한 문장
→ 실제 핵심 코드 3~12줄
→ 이 코드가 바꾸는 상태 또는 다음 책임 한 문장
```

- 첫 문장은 학생에게 필요한 맥락이며, 코드 안에 넣을 때는 해당 언어의 올바른 주석 문법을 사용한다.
- 코드 조각은 현재 저장소의 실제 코드를 사용한다. 긴 완성 답안이나 임시 코드는 넣지 않는다.
- 전체 코드 위치가 꼭 필요하면 주 근거 아래의 접힌 참고 영역에서 한 번만 연결한다.

13개 시퀀스의 kind 매핑:

| Sequence | kind | Workbench |
|---|---|---|
| 00 | `request` | Request Workbench |
| 01 | `request-trace` | Request Packet Trace |
| 02 | `persistence` | Persistence Boundary |
| 03 | `gate` | Failure Gate |
| 04 | `auth` | Auth Boundary |
| 05 | `trust` | Trust & Recovery Map |
| 06 | `test` | Test Harness |
| 07 | `cache` | Cache State Inspector |
| 08 | `realtime` | Connection & Broadcast Console |
| 09 | `runtime` | Runtime Boundary |
| 10 | `pipeline` | Pipeline Gate |
| 11 | `refactor` | Behavior Change Ledger: 유지된 계약과 의도적 변경을 별도 lane으로 비교 |
| 12 | `event` | Event Delivery Trace |

## 3.2 핵심 흐름 데이터 규칙

각 시퀀스의 canonical 핵심 흐름은 `window.visualLabData.flows`에 둔다. `flow`는 기존 소비자 호환이 필요할 때만 유지하는 축약 필드다.
Flow는 정답 비교가 아니라 학생이 따라갈 문제 해결 순서다.
각 `flows[].steps` 단계는 Problem, Concept, Action, Check를 모두 가져야 한다.

```js
{
  id: "step-1",
  label: "요청 시작",
  problem: "요청이 어느 코드로 들어오는지 확인해야 합니다.",
  concept: "Controller는 HTTP 입구입니다.",
  action: "`POST /posts` 요청을 Controller 메서드와 연결합니다.",
  check: "Swagger 또는 테스트로 요청 경로를 확인합니다."
}
```

- 한 단계에는 긴 이론이나 정답 코드 전체를 넣지 않는다.
- Diagnostic Lifeline 기본 동작은 lane/message 선택, 이전/다음, 현재 단계와 상태 변화 표시다.
- 버튼은 기본 focus 흐름을 유지하고 키보드 접근성을 해치지 않는다.
단, 00 시퀀스는 HTTP, JSON, Postman, Git, DB 기초 수준을 넘지 않는다.

## 3.3 증거 표현의 상한

`check`, `evidence`, `outcome`은 실제로 관찰한 범위까지만 주장한다. 실행 경로를 설명하는 diagram과 그 경로가 성공했다는 증거를 구분한다.

| 확인한 증거 | 표현할 수 있는 판단 | 금지하는 과장 |
|---|---|---|
| Service 단위 테스트의 반환값과 예외 | 해당 Service 단위 동작 | HTTP path, status, response body 계약 전체 |
| mock 또는 spy의 메서드 호출 | 발행자나 adapter가 호출됨 | 외부 API, mail server, RabbitMQ가 실제 수신·처리함 |
| publisher confirm 없는 `convertAndSend` 반환·예외 | publisher 호출의 반환 또는 중단 | broker acceptance·routing 성공이나 확정적인 미전송 |
| `contextLoads` | Spring context가 로드됨 | endpoint 요청·응답과 전체 기능이 정상임 |
| `ConcurrentHashMap.putIfAbsent` | 현재 process 안의 중복 기록 방지 | 재시작·다중 instance에서도 유지되는 영속 멱등성 |
| build/deploy 명령 종료 | 해당 명령 또는 job이 끝남 | container process, application log, HTTP 응답까지 정상임 |

- integration 성공을 말하려면 실제 boundary를 통과한 로그, 응답, 상태 또는 integration test가 필요하다.
- `notReached` 대상은 실행됐다고 추정하지 않고 확인되지 않은 이유를 그대로 쓴다.
- outbox, retry, rollback, exactly-once, 영속 저장처럼 현재 범위를 벗어난 보장은 구현된 것처럼 쓰지 않는다.

## 4. 반드시 참조해야 할 대표 백엔드 문서

### 4.1 DB Access Lab 이론 문서

참조 URL:

```text
https://github.com/stdiodh/spring-boot-db-access-lab/blob/02-answer/docs/theory.md
```

이 문서는 Visual Lab의 DB / Repository / Entity / Service 흐름 콘텐츠를 만들 때 첫 기준으로 사용한다.

반드시 반영할 핵심 흐름:

```text
POST /posts
-> PostController
-> PostCreateRequest
-> PostService
-> PostEntity
-> PostRepository
-> MySQL
-> PostResponse
-> JSON Response
```

이론 문서에서 강조하는 핵심 개념:

- 메모리 저장은 서버 재시작 시 사라진다.
- DB 저장은 애플리케이션이 꺼져도 데이터가 남는다.
- Entity는 DB 테이블과 연결되는 서버 내부 데이터다.
- Repository는 DB 접근을 맡는다.
- Service는 요청 DTO를 Entity로 바꾸고 Repository를 호출한 뒤 Response DTO로 바꾼다.
- Controller는 요청을 받고 Service를 호출하는 입구다.
- JPA는 CRUD를 편하게 해주지만 관계 매핑과 N+1 문제는 따로 이해해야 한다.

### 4.2 DB Access Lab 구현 문서

참조 URL:

```text
https://github.com/stdiodh/spring-boot-db-access-lab/blob/02-answer/docs/implementation.md
```

반드시 반영할 구현 순서:

```text
1. PostEntity 작성
2. PostRepository 선언
3. PostService에서 메모리 저장 대신 Repository 사용
4. findAll 연결
5. findById 연결
6. deleteById 연결
7. update 로직 작성
8. Controller에서 수정/삭제 API 연결
9. MySQL 저장 결과 확인
```

파일별 역할:

```text
PostEntity.kt
-> DB 테이블과 연결되는 핵심 데이터 구조

PostRepository.kt
-> DB 접근을 맡는 기본 JPA Repository

PostService.kt
-> Entity 생성, 조회, 수정, 삭제 흐름을 조립하는 곳

PostController.kt
-> 요청을 받아 Service에 전달하고 응답을 돌려주는 입구

PostCreateRequest.kt
-> 글 생성 요청 값

PostUpdateRequest.kt
-> 글 수정 요청 값

PostResponse.kt
-> 바깥으로 내보낼 응답 모양
```

### 4.3 DB Access Lab 정답 브랜치 README

참조 URL:

```text
https://github.com/stdiodh/spring-boot-db-access-lab/tree/02-answer
```

반드시 반영할 브랜치 맥락:

- `02-implementation`: 학생 실습용 starter 브랜치
- `02-answer`: 비교용 정답 브랜치
- Visual Lab 작성자는 정답 브랜치의 흐름을 검수 기준으로 참고한다.
- 학생이 직접 구현할 코드를 대신 작성해주는 페이지가 아니다.
- 코드 실행 흐름을 이해하게 만드는 페이지다.

## 5. 반드시 참조해야 할 중요 코드

아래 코드는 DB Access Lab의 실제 정답 브랜치 코드를 기준으로 한다.

### 5.1 Controller

참조 URL:

```text
https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/controller/PostController.kt
```

시각화해야 할 포인트:

- `@RestController`
- `@RequestMapping("/posts")`
- `GET /posts`
- `GET /posts/{id}`
- `POST /posts`
- `PUT /posts/{id}`
- `DELETE /posts/{id}`
- Controller는 Repository를 직접 호출하지 않는다.
- Controller는 Service를 호출한다.

Visual Lab 표현:

```text
HTTP Request
-> PostController
-> PostService
```

### 5.2 DTO

참조 URL:

```text
https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/dto/PostCreateRequest.kt
https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/dto/PostUpdateRequest.kt
https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/dto/PostResponse.kt
```

시각화해야 할 포인트:

- `PostCreateRequest`는 생성 요청 데이터다.
- `PostUpdateRequest`는 수정 요청 데이터다.
- `PostResponse`는 클라이언트로 나가는 응답 데이터다.
- Entity를 그대로 응답하지 않고 Response DTO로 바꾼다.
- `PostResponse.from(entity)` 변환 흐름을 보여준다.

Visual Lab 표현:

```text
JSON Request
-> PostCreateRequest
-> PostEntity
-> PostResponse
-> JSON Response
```

### 5.3 Entity

참조 URL:

```text
https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/domain/PostEntity.kt
```

시각화해야 할 포인트:

- `@Entity`
- `@Table(name = "posts")`
- `@Id`
- `@GeneratedValue(strategy = GenerationType.IDENTITY)`
- `title`
- `content`
- `author`
- Entity는 DB 테이블과 연결되는 객체다.

Visual Lab 표현:

```text
PostEntity
-> posts table
```

### 5.4 Repository

참조 URL:

```text
https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/repository/PostRepository.kt
```

시각화해야 할 포인트:

- `PostRepository`
- `JpaRepository<PostEntity, Long>`
- 직접 SQL 구현 없이 기본 CRUD 메서드 사용
- `save`
- `findAll`
- `findById`
- `deleteById`

Visual Lab 표현:

```text
PostService
-> PostRepository
-> JpaRepository
-> MySQL
```

### 5.5 Service

참조 URL:

```text
https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/service/PostService.kt
```

시각화해야 할 포인트:

- `create(request)`
- 요청 DTO를 Entity로 변환
- `postRepository.save(...)`
- 저장된 Entity를 `PostResponse.from(...)`으로 변환
- `getAll()`
- `findById(id)`
- `update(id, request)`
- `delete(id)`
- Service는 전체 처리 흐름을 조립하는 계층이다.

Visual Lab 표현:

```text
PostCreateRequest
-> PostEntity 생성
-> postRepository.save(entity)
-> savedPost
-> PostResponse.from(savedPost)
```

## 6. Visual Lab에 포함할 대표 주제

최소 아래 주제를 포함한다.

```text
1. HTTP 요청/응답
2. Controller
3. DTO
4. Service
5. Entity
6. Repository
7. Database
8. CRUD
9. 영속성 저장
10. 계층 분리
11. 수정 흐름
12. 삭제 흐름
13. JPA 기본 CRUD
14. N+1 문제 입문
15. 관계 매핑 입문
```

현재 `00`부터 `12`까지의 모든 시퀀스는 하나 이상의 실제 카드나 흐름으로 연결한다.
단, 각 시퀀스의 상세 이론은 HTML에 복제하지 않고 해당 토픽 레포 링크로 연결한다.

## 7. 주제 데이터 구조 예시

각 시퀀스 서브모듈의 `docs/visual-lab/sequences/NN/visual-lab-data.js`에는 아래 계층의 데이터를 사용한다. 상세 필드 계약은 3절을 따른다.

```js
window.visualLabData = {
  kind: "sequence",
  sequence: "02",
  title: "DB 접근 흐름",
  goal: "메모리 저장 대신 DB에 저장하는 계층 흐름을 이해한다.",
  problem: "서버 재시작 후에도 데이터가 남으려면 메모리 밖의 저장소가 필요합니다.",
  workbench: {
    kind: "persistence",
    title: "Persistence Boundary",
    instruction: "저장 조건을 선택하고 실제 영속성 경계를 확인합니다.",
    scenarios: [
      /* 실제 theory와 flows에 연결된 scenario 3~4개 */
    ]
  },
  actors: [
    /* 실제 요청과 저장 경계 actor */
  ],
  flows: [
    {
      id: "create-flow",
      title: "게시글 저장 흐름",
      steps: [
        /* Problem, Concept, Action, Check와 codePointIds */
      ]
    }
  ],
  codePoints: [
    /* 실제 파일의 핵심 위치와 확인 지점 */
  ],
  concepts: [
    {
      title: "Repository",
      body: "저장소 접근 역할을 맡습니다."
    }
  ],
  checks: [],
  next: {}
};
```

## 8. 각 주제별 내용 정의

### 8.1 HTTP 요청/응답

짧은 설명:

```text
클라이언트가 서버에 요청을 보내고 JSON 응답을 받는 기본 흐름입니다.
```

흐름:

```text
Client
-> HTTP Request
-> Controller
-> Service
-> Response DTO
-> JSON Response
```

핵심 포인트:

- HTTP Method
- URL
- Request Body
- Status Code
- Response Body

### 8.2 Controller

짧은 설명:

```text
Controller는 HTTP 요청이 처음 도착하는 백엔드 진입점입니다.
```

흐름:

```text
POST /posts
-> PostController.create()
-> PostService.create()
```

코드 포인트:

- `@RestController`
- `@RequestMapping("/posts")`
- `@PostMapping`
- `@GetMapping`
- `@PutMapping`
- `@DeleteMapping`

주의:

```text
Controller가 Repository를 직접 호출하는 흐름으로 설명하지 않는다.
```

### 8.3 DTO

짧은 설명:

```text
DTO는 외부 요청/응답 데이터와 내부 Entity를 분리하기 위한 객체입니다.
```

흐름:

```text
JSON Request
-> PostCreateRequest
-> PostEntity
-> PostResponse
-> JSON Response
```

코드 포인트:

- `PostCreateRequest`
- `PostUpdateRequest`
- `PostResponse`
- `PostResponse.from(entity)`

### 8.4 Service

짧은 설명:

```text
Service는 요청 DTO를 Entity로 바꾸고 Repository를 호출한 뒤 응답 DTO를 만드는 흐름을 조립합니다.
```

흐름:

```text
PostCreateRequest
-> PostEntity 생성
-> postRepository.save(...)
-> PostResponse.from(...)
```

코드 포인트:

- `create(request)`
- `getAll()`
- `getById(id)`
- `update(id, request)`
- `delete(id)`

### 8.5 Entity

짧은 설명:

```text
Entity는 DB 테이블과 연결되는 서버 내부 데이터 객체입니다.
```

흐름:

```text
PostEntity
-> posts table
```

코드 포인트:

- `@Entity`
- `@Table(name = "posts")`
- `@Id`
- `@GeneratedValue`

### 8.6 Repository

짧은 설명:

```text
Repository는 DB 접근을 담당하고, Service가 DB 세부 구현에 직접 의존하지 않게 분리합니다.
```

흐름:

```text
PostService
-> PostRepository
-> JpaRepository
-> MySQL
```

코드 포인트:

- `JpaRepository<PostEntity, Long>`
- `save`
- `findAll`
- `findById`
- `deleteById`

### 8.7 Database

짧은 설명:

```text
Database는 서버가 꺼져도 데이터를 보관하는 영속 저장소입니다.
```

흐름:

```text
PostEntity
-> INSERT INTO posts
-> MySQL Row
```

핵심 포인트:

- 메모리 저장과 DB 저장 차이
- 영속성
- 테이블
- Row
- Primary Key

### 8.8 CRUD

짧은 설명:

```text
CRUD는 생성, 조회, 수정, 삭제라는 백엔드 기본 데이터 처리 흐름입니다.
```

흐름:

```text
Create
-> Read
-> Update
-> Delete
```

연결 API:

```text
POST /posts
GET /posts
GET /posts/{id}
PUT /posts/{id}
DELETE /posts/{id}
```

### 8.9 수정 흐름

흐름:

```text
PUT /posts/{id}
-> findById(id)
-> Entity 값 변경
-> save(post)
-> PostResponse
```

핵심 포인트:

- 먼저 기존 Entity를 찾는다.
- 값을 바꾼다.
- 저장한다.
- 응답 DTO로 변환한다.

### 8.10 삭제 흐름

흐름:

```text
DELETE /posts/{id}
-> PostController.delete()
-> PostService.delete()
-> postRepository.deleteById(id)
-> 204 No Content
```

### 8.11 N+1 문제 입문

짧은 설명:

```text
N+1은 코드에서는 한 번 조회처럼 보이지만, 연관 데이터 접근 때문에 DB 쿼리가 반복되는 문제입니다.
```

흐름:

```text
findAll()
-> posts 1번 조회
-> post.comments 접근
-> comments N번 추가 조회
```

주의:

- 이번 HTML에서는 N+1을 깊게 구현하지 않는다.
- 실무 확장 개념으로 짧게 소개한다.
- 상세 설명은 theory.md로 연결한다.

## 9. 콘텐츠 작성 원칙

- 설명은 짧게 쓴다.
- 상세 이론을 HTML에 길게 복붙하지 않는다.
- 각 주제는 "현재 질문 -> 조건 선택 -> 시스템 경로 -> 관찰 증거 -> 판단 -> 검증 -> 다음 질문" 순서로 구성한다.
- 코드 원문 전체를 HTML에 길게 넣지 않는다.
- 중요한 코드 위치와 흐름만 보여준다.
- route, 상태, 번호와 label은 실제 actor, 경계, 테스트 또는 응답을 표현해야 한다.
- semantic node와 edge는 책임 주체, 동작, payload와 boundary를 서로 다른 필드로 표현해야 한다.
- evidence는 단위 테스트, mock, in-memory 상태나 명령 종료가 실제로 보장하는 범위를 넘지 않아야 한다.
- 버튼은 사용자가 바꾸는 조건이나 실행 결과가 드러나는 동사를 사용한다.
- 실제 학습은 연결 문서와 연결 레포로 이동하게 한다.

## 10. HTML에서 보여줘야 하는 정보

각 주제 상세 화면은 아래 정보를 표시한다.

```text
제목
영문 제목
현재 학습 질문과 goal
관찰 조건 selector
participant header와 수직 lifeline
현재 message와 before → after
관찰 증거와 판단
현재 단계의 Problem, Concept, Action, Check
연결된 코드 포인트와 책임 경계
session-local 검증 질문
다음 질문
관련 문서 링크
관련 코드 링크
```

## 11. HTML에서 피해야 하는 정보

- 긴 이론 문단
- 정답 코드 전체 복붙
- 너무 많은 API 설명
- 강의 자료 전체 복제
- 실제 흐름과 연결되지 않은 임시 수치, metric, actor 또는 장식용 terminal
- 동사와 payload 없이 이어진 장식용 화살표와 의미 없는 icon
- 테스트 종류나 runtime 경계를 무시한 과장된 성공 증거
- 정답 브랜치명과 answer 링크
- 중앙 레포의 역할을 벗어나는 상세 구현 튜토리얼
