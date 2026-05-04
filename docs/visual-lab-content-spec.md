# A&I Backend Visual Lab Content Spec

## 1. 문서 목적

이 문서는 A&I Backend Visual Lab에서 보여줄 학습 콘텐츠의 범위와 데이터 구조를 정의한다.

Visual Lab은 상세 이론 문서를 대체하지 않는다.
각 시퀀스와 토픽 레포의 이론 문서, 구현 문서, 체크리스트, 정답 브랜치를 시각적으로 연결하는 진입점이다.

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
-> Visual Lab에서는 "실행 흐름을 시각화할 기준 코드"로 연결한다.
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
2. 해당 토픽 레포의 `NN-answer` 브랜치에서 실제 완성 흐름을 확인한다.
3. 해당 토픽 레포의 `NN-implementation` 브랜치에서 학생이 따라갈 구현 순서를 확인한다.
4. HTML에는 상세 이론이나 정답 코드 전체를 복붙하지 않는다.
5. 핵심 실행 흐름, 데이터 변환, 관련 문서/코드 링크만 보여준다.

## 3. 모든 시퀀스 데이터 정의 규칙

각 시퀀스 주제는 해당 시퀀스 서브모듈의 `docs/visual-lab/sequences.js`에서 아래 필드를 가져야 한다.

```js
{
  id: "sequence-topic-id",
  sequence: "NN",
  title: "한국어 주제명",
  englishTitle: "English Topic Name",
  category: "Category",
  shortDescription: "학습 진입점 수준의 짧은 설명",
  whyItMatters: "왜 이 흐름을 이해해야 하는지",
  sourceRepo: "topic-repo-name",
  sourceImplementationBranch: "NN-implementation",
  sourceAnswerBranch: "NN-answer",
  sourceDocs: [],
  sourceCode: [],
  flow: [],
  transform: [],
  points: [],
  exampleRequest: {},
  exampleResponse: {}
}
```

필드 작성 규칙:

- `sourceImplementationBranch`는 학생 실습 시작 브랜치를 가리킨다.
- `sourceAnswerBranch`는 Visual Lab이 흐름을 검증할 기준 브랜치를 가리킨다.
- `sourceDocs`는 이론/구현/체크리스트/정답 가이드 링크를 담는다.
- `sourceCode`는 핵심 코드 파일 링크만 담는다.
- `flow`는 한 화면에서 볼 수 있는 실행 흐름이어야 한다.
- `transform`은 JSON, DTO, Entity, DB Row, Response DTO 변환만 짧게 보여준다.
- `points`는 3~6개 이내의 핵심 포인트로 제한한다.

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
-> PostService
-> PostCreateRequest
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
- Visual Lab은 정답 브랜치의 흐름을 학습용으로 시각화한다.
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

각 시퀀스 서브모듈의 `docs/visual-lab/sequences.js`에는 아래 구조의 데이터를 사용한다.

```js
const visualLabTopics = [
  {
    id: "db-access-flow",
    sequence: "02",
    title: "DB 접근 흐름",
    englishTitle: "DB Access Flow",
    category: "Persistence",
    shortDescription: "메모리 저장 대신 MySQL에 데이터를 저장하는 계층 흐름입니다.",
    whyItMatters: "백엔드에서는 요청 데이터가 단순히 메모리에 머무르지 않고 DB에 영속적으로 저장되어야 합니다.",
    sourceRepo: "spring-boot-db-access-lab",
    sourceImplementationBranch: "02-implementation",
    sourceAnswerBranch: "02-answer",
    sourceDocs: [
      {
        label: "이론 문서",
        url: "https://github.com/stdiodh/spring-boot-db-access-lab/blob/02-answer/docs/theory.md"
      },
      {
        label: "구현 문서",
        url: "https://github.com/stdiodh/spring-boot-db-access-lab/blob/02-answer/docs/implementation.md"
      }
    ],
    sourceCode: [
      {
        label: "PostController.kt",
        url: "https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/controller/PostController.kt"
      },
      {
        label: "PostService.kt",
        url: "https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/service/PostService.kt"
      },
      {
        label: "PostEntity.kt",
        url: "https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/domain/PostEntity.kt"
      },
      {
        label: "PostRepository.kt",
        url: "https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/repository/PostRepository.kt"
      }
    ],
    flow: [
      "Client",
      "POST /posts",
      "PostController",
      "PostCreateRequest",
      "PostService",
      "PostEntity",
      "PostRepository",
      "MySQL",
      "PostResponse",
      "JSON Response"
    ],
    transform: [
      {
        from: "JSON Request",
        to: "PostCreateRequest",
        description: "클라이언트가 보낸 JSON 요청이 생성 DTO로 매핑됩니다."
      },
      {
        from: "PostCreateRequest",
        to: "PostEntity",
        description: "Service에서 요청 DTO를 DB 저장용 Entity로 변환합니다."
      },
      {
        from: "PostEntity",
        to: "posts table",
        description: "Repository가 Entity를 MySQL 테이블에 저장합니다."
      },
      {
        from: "saved PostEntity",
        to: "PostResponse",
        description: "저장 결과를 클라이언트 응답 DTO로 변환합니다."
      }
    ],
    points: [
      "Controller는 요청의 입구입니다.",
      "Service는 처리 흐름을 조립합니다.",
      "Repository는 DB 접근을 담당합니다.",
      "Entity는 DB 테이블과 연결됩니다.",
      "Response DTO는 Entity를 그대로 노출하지 않기 위해 사용합니다."
    ],
    exampleRequest: {
      method: "POST",
      path: "/posts",
      body: {
        title: "A&I Backend",
        content: "DB 저장 흐름을 학습합니다.",
        author: "student"
      }
    },
    exampleResponse: {
      id: 1,
      title: "A&I Backend",
      content: "DB 저장 흐름을 학습합니다.",
      author: "student"
    }
  }
];
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
- 각 주제는 "개념 -> 흐름 -> 코드 포인트 -> 관련 문서" 순서로 구성한다.
- 코드 원문 전체를 HTML에 길게 넣지 않는다.
- 중요한 코드 위치와 흐름만 보여준다.
- 실제 학습은 연결 문서와 연결 레포로 이동하게 한다.

## 10. HTML에서 보여줘야 하는 정보

각 주제 상세 화면은 아래 정보를 표시한다.

```text
제목
영문 제목
카테고리
짧은 설명
왜 중요한가
실행 흐름
데이터 변환 흐름
핵심 포인트
예시 요청
예시 응답
관련 문서 링크
관련 코드 링크
implementation/answer 브랜치 링크
```

## 11. HTML에서 피해야 하는 정보

- 긴 이론 문단
- 정답 코드 전체 복붙
- 너무 많은 API 설명
- 강의 자료 전체 복제
- 중앙 레포의 역할을 벗어나는 상세 구현 튜토리얼
