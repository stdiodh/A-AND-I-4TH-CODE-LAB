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

각 시퀀스 상세 파일은 아래 필드를 가진 하나의 canonical 객체로 관리합니다. `kind: "sequence"` 데이터 안에 같은 내용을 다시 담은 `sequences` 배열을 만들지 않습니다. 아래 예시는 필드 구조를 보이기 위해 scenario 1개만 축약해 표시합니다.

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
      snippet: "핵심 5-20줄만 넣는다.",
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

모든 구현 완료 시퀀스는 top-level `workbench`를 가진다. 공통 renderer는 `workbench`를 조건 선택, `Learning Signal Trace`, 상태 snapshot, 관찰 증거와 판단으로 렌더링한다.

```js
workbench: {
  kind: "cache",
  title: "Cache State Inspector",
  instruction: "조건을 선택하고 Redis와 DB 경계를 비교합니다.",
  scenarios: [
    {
      id: "cache-miss",
      label: "첫 조회 · cache miss",
      flowId: "lookup-flow",
      tone: "signal",
      prompt: "Redis에 key가 없을 때 실제 조회 경로를 확인합니다.",
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
| `scenarios` | 필수 | 실제 이론과 흐름에 근거한 조건을 3~4개 둔다. |

`scenarios[]` 필드:

| 필드 | 필수 | 규칙 |
|---|---|---|
| `id` | 필수 | 시퀀스 안에서 고유한 kebab-case id다. |
| `label` | 필수 | 조건 선택 button에 표시할 짧은 이름이다. |
| `flowId` | 필수 | 같은 객체의 `flows[].id` 중 하나를 참조한다. |
| `tone` | 필수 | `signal`, `blocked`, `warning`, `recovered` 중 하나다. |
| `prompt` | 필수 | 현재 조건에서 관찰할 질문 또는 상황이다. |
| `route` | 필수 | 실제 actor, destination, 저장소 또는 책임 경계를 순서대로 쓴 문자열 배열이다. |
| `snapshot` | 필수 | `{ label, value, tone? }` 항목을 2개 이상 둔 배열이다. `tone`은 scenario와 같은 네 값을 사용한다. |
| `evidence` | 필수 | 로그, 응답, 테스트, 상태 또는 화면에서 확인할 실제 증거다. |
| `outcome` | 필수 | 관찰 결과로 학습자가 내려야 할 판단이다. |
| `stopAfter` | 선택 | 마지막으로 도달한 `route`의 0-based index다. 이후 node는 `도달하지 않음`으로 표시한다. |
| `fanOut` | 선택 | `realtime`에서만 사용하며 실제 메시지를 받는 대상 label 배열이다. |

작성 규칙:

- route와 snapshot에 임시 actor, 의미 없는 수치나 장식용 metric을 넣지 않는다.
- `stopAfter`는 실패 또는 차단 조건에서 실제 도달 지점이 확인될 때만 쓴다.
- `fanOut`에는 연결만 된 대상이 아니라 실제로 해당 topic을 구독해 메시지를 받는 대상만 쓴다.
- scenario를 바꾸면 `flowId`에 연결된 `flows[].steps`가 Problem, Concept, Action, Check evidence를 제공해야 한다.
- 공통 renderer는 과거 데이터의 `flows`에서 fallback trace를 만들 수 있지만, 완료된 시퀀스는 fallback을 최종 상태로 사용하지 않는다.

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
| 11 | `refactor` | Behavior Invariant Map |
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
- Learning Signal Trace 기본 동작은 route/단계 선택, 이전/다음, 진행률 표시다.
- 버튼은 기본 focus 흐름을 유지하고 키보드 접근성을 해치지 않는다.
단, 00 시퀀스는 HTTP, JSON, Postman, Git, DB 기초 수준을 넘지 않는다.

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

향후 전체 시퀀스 확장 시에는 `00`부터 `12`까지의 모든 시퀀스를 하나 이상의 카드나 흐름으로 연결한다.
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
- 버튼은 사용자가 바꾸는 조건이나 실행 결과가 드러나는 동사를 사용한다.
- 실제 학습은 연결 문서와 연결 레포로 이동하게 한다.

## 10. HTML에서 보여줘야 하는 정보

각 주제 상세 화면은 아래 정보를 표시한다.

```text
제목
영문 제목
현재 학습 질문과 goal
관찰 조건 selector
Learning Signal Trace
현재 route 상태와 snapshot
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
- 정답 브랜치명과 answer 링크
- 중앙 레포의 역할을 벗어나는 상세 구현 튜토리얼
