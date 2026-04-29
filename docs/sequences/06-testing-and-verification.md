# 06. 테스트와 검증

## 시퀀스 목표

이번 시퀀스의 목표는 학생이 이미 만든 Service 흐름을 테스트로 다시 확인하면서,
테스트가 왜 필요한지 현실적으로 이해하도록 만드는 것입니다.

학생은 이번 시퀀스를 마친 뒤 아래를 할 수 있어야 합니다.

1. 테스트가 왜 필요한지 설명할 수 있다.
2. 정상 케이스와 실패 케이스를 구분해서 테스트할 수 있다.
3. Service 단위 테스트를 작성할 수 있다.
4. fixture, mock, given-when-then 흐름을 설명할 수 있다.
5. 변경 이후에도 기존 기능을 다시 신뢰할 수 있다는 점을 이해할 수 있다.

## 이번 시퀀스에서 다시 설명해야 하는 기초 개념

이번 06 시퀀스는 `05`까지 기능이 늘어난 상태에서 시작합니다.
그래서 학생이 아래 기초 개념을 다시 이해해야 합니다.

- `test`
  코드가 기대한 결과를 내는지 확인하는 실행 가능한 검증
- `service test`
  controller나 DB 전체가 아니라 service 로직 흐름에 집중하는 테스트
- `fixture`
  반복해서 쓸 입력값과 객체를 정리해두는 준비 코드
- `mock`
  실제 의존성 대신 원하는 상황만 흉내 내는 테스트 더블
- `regression`
  수정 후 원래 되던 기능이 깨지는 상황

즉, 이전 시퀀스에서 기능을 많이 만들었다면
이번 시퀀스에서는 "이 기능을 어떻게 다시 믿을 것인가"라는 관점을 다시 잡아야 합니다.

## 현재 코드 흐름에서 어디를 봐야 하는가

이번 시퀀스는 기능을 새로 만드는 단계가 아니라,
이미 있는 service 흐름을 테스트 코드에서 다시 따라가는 단계입니다.

1. `PostService.kt`
   게시글 생성과 조회 예외 흐름의 테스트 대상
2. `AuthService.kt`
   로그인 성공과 실패 흐름의 테스트 대상
3. `TestFixtureFactory.kt`
   테스트 입력과 fixture를 모아두는 지점
4. `PostServiceTest.kt`
   CRUD service 테스트의 가장 작은 예시
5. `AuthServiceTest.kt`
   인증 흐름도 service 테스트 대상이 될 수 있음을 보여주는 예시

짧게 말하면 이번 시퀀스는

- `fixture 준비 -> Service 호출 -> 결과 검증`
- `정상 케이스 -> 실패 케이스 -> 다시 실행`

흐름을 반복하며 신뢰를 쌓는 단계입니다.

## 시작 기준

- 시작 레포: `spring-boot-db-access-lab`
- 시작 기준 브랜치: `05-answer`
- 작업 브랜치:
  - `06-implementation`
  - `06-answer`
  - `main` 안내 브랜치 갱신

이번 시퀀스는 같은 도메인 위의 연속 실습이므로 새 레포를 만들지 않습니다.

## 이번 시퀀스에서 다루는 범위

- `PostService` 정상 케이스 테스트
- `PostService` 예외 케이스 테스트
- `AuthService` 인증 성공 테스트
- `AuthService` 인증 실패 테스트
- fixture와 mock 사용
- `./gradlew test`로 결과 검증

## 이번 시퀀스의 실무 확장 개념

이번 06 시퀀스의 실무 확장 개념은 아래 두 가지입니다.

- `테스트 범위 구분`
- `테스트 더블 사용 기준`

핵심은 이렇습니다.

- 모든 테스트를 같은 방식으로 작성하지 않는다.
- 지금은 `service test`에 집중하고, controller/integration/e2e는 의도적으로 범위 밖에 둔다.
- mock은 편리하지만, "무조건 쓰는 도구"가 아니라 "이번에는 service 로직만 보고 싶다"는 선택이다.

즉, 이번 시퀀스는 테스트 문법만 배우는 시간이 아니라
"왜 지금은 이 범위의 테스트를 하는가"를 같이 이해하는 단계입니다.

## 이번 시퀀스에서 다루지 않는 범위

- controller 테스트
- repository 테스트
- 통합 테스트
- e2e 테스트
- TDD 이론 심화

## 학생 구현 순서

구현 순서는 반드시 아래를 따릅니다.

1. 테스트 대상 Service를 확인한다.
2. fixture 또는 given 데이터를 준비한다.
3. 정상 케이스 테스트를 작성한다.
4. 예외 케이스 테스트를 작성한다.
5. 인증 흐름 테스트를 추가한다.
6. 테스트를 다시 실행하며 결과를 확인한다.

## 문제 상황과 해결 방향을 코드로 보기

### 문제 1. 서비스 테스트인데 실제 DB까지 같이 띄우면 무엇이 흐려지는가

테스트를 처음 쓸 때는 "진짜처럼 다 확인해야 안전하지 않을까?"라고 생각하기 쉽습니다.
하지만 이번 시퀀스는 service 로직 하나를 확인하는 단계이므로,
DB까지 같이 끌어오면 오히려 무엇을 검증하는지 흐려질 수 있습니다.

### 문제 코드

```kotlin
val context = SpringApplication.run(App::class.java)
val postService = context.getBean(PostService::class.java)
val result = postService.create(request)
```

이런 방식은 실행 자체는 가능해도,

- 지금 실패가 service 로직 때문인지
- DB 설정 때문인지
- 다른 bean wiring 때문인지

구분하기 어려워집니다.

### 해결 방향 1. 지금은 service 와 의존성만 분리해서 본다

```kotlin
val postRepository = mock(PostRepository::class.java)
val postService = PostService(postRepository)

`when`(postRepository.save(any(PostEntity::class.java))).thenReturn(savedPost)

val result = postService.create(request)
assertEquals(request.title, result.title)
```

이 흐름이면 "이번 테스트는 PostService.create 로직을 본다"는 범위가 분명해집니다.

### 문제 2. 테스트마다 입력값을 전부 새로 만들면 무엇이 어려워지는가

```kotlin
val request = PostCreateRequest(
    title = "테스트 제목",
    content = "테스트 내용",
    author = "tester"
)
```

이렇게 매 테스트마다 값을 다시 만들면,
테스트가 늘어날수록 본문이 준비 코드로 길어집니다.

### 해결 방향 2. fixture 로 반복 입력을 정리한다

```kotlin
val request = TestFixtureFactory.postCreateRequest()
val user = TestFixtureFactory.user(email = request.email, password = encodedPassword)
```

이 방식이면

- 테스트 본문이 짧아지고
- "무엇을 검증하는지"가 더 또렷해지고
- 값이 바뀌어도 수정 지점이 줄어듭니다

## 문서에 반드시 남겨야 하는 것

이번 시퀀스 문서에는 아래가 함께 들어가야 합니다.

1. 기초 개념 설명
2. 현재 코드 흐름
3. 왜 지금은 service test 에 집중하는지
4. mock 과 fixture 를 왜 쓰는지
5. controller / integration / e2e 를 왜 이번 범위에서 제외하는지
6. 이번 시퀀스에서 실제 구현 범위와 설명-only 범위

## 핵심 TODO 파일

- `src/test/kotlin/com/andi/rest_crud/support/TestFixtureFactory.kt`
- `src/test/kotlin/com/andi/rest_crud/service/PostServiceTest.kt`
- `src/test/kotlin/com/andi/rest_crud/service/AuthServiceTest.kt`

핵심 TODO는 위 파일에 집중되어야 합니다.

## 필수 산출물

각 브랜치에는 아래 산출물이 모두 있어야 합니다.

- `README.md`
- `docs/theory.md`
- `docs/implementation.md`
- `docs/answer-guide.md`
- `docs/checklist.md`
- `docs/assets.md`
- starter 테스트 코드
- answer 테스트 코드

## 문서 작성 기준

- `theory.md`: 왜 지금 테스트가 필요한지, 정상/실패 흐름 차이, fixture/mock/given-when-then 설명
- `implementation.md`: 학생이 손으로 칠 순서와 TODO 파일 설명
- `answer-guide.md`: 강사가 빠르게 비교할 수 있는 정답 흐름
- `checklist.md`: 학생 체크리스트와 강사/PPT 체크리스트 분리
- `assets.md`: 미리 제공하는 것과 학생이 직접 작성하지 않는 범위 정리

## 운영 메모

- `06-implementation`은 학생용 starter 브랜치입니다.
- `06-answer`는 비교용 완성 브랜치입니다.
- 서브모듈 `main`은 실습 브랜치가 아니라 안내 브랜치이며, 06까지의 브랜치 구조와 문서 구조를 보여줘야 합니다.
- 완료 후 루트 `README.md`에는 06 완료 상태와 다음 시퀀스를 반영해야 합니다.
