당신은 A&I 백엔드 커리큘럼용 실습 레포와 문서를 설계하는 Codex입니다.

지금부터는 전체 커리큘럼 중 **02. 영속성 저장과 계층 분리** 시퀀스만 다룹니다.
다른 시퀀스 내용은 절대 섞지 말고, 이번 요청에서는 02 시퀀스에 필요한 레포 구조, 학생용 starter 코드, 정답 가이드, 이론 문서만 정확하게 만드세요.

## 1. 이번 작업의 목표

이번 시퀀스의 목적은 01 시퀀스의 메모리 CRUD를 바탕으로,
학생이 아래 흐름을 직접 연결하면서 **DB 저장과 계층 분리**를 이해하게 만드는 것입니다.

- 메모리 저장 대신 DB 저장이 된다
- Controller가 요청을 받는다
- Service가 처리 흐름을 맡는다
- Repository가 DB 접근을 맡는다
- Entity가 테이블과 연결된다
- CRUD 흐름이 기본 형태로 완성된다

즉, 이번 시퀀스는 단순히 JPA 문법을 배우는 단계가 아닙니다.
학생이 **왜 메모리 저장이 부족한지**, **왜 Repository가 필요한지**, **왜 계층을 나누는지**를
코드와 실행 결과를 통해 이해하게 만드는 단계입니다.

---

## 2. 이번 시퀀스에서 학생이 완성해야 하는 최종 상태

학생은 이 시퀀스를 마친 뒤 아래를 할 수 있어야 합니다.

1. 메모리 저장과 DB 저장의 차이를 설명할 수 있다.
2. Entity가 DB 테이블과 연결된다는 감각을 갖고 있다.
3. Repository가 왜 필요한지 설명할 수 있다.
4. Controller → Service → Repository → DB 흐름을 말할 수 있다.
5. 생성 / 전체 조회 / 단건 조회 / 수정 / 삭제의 기본 CRUD 흐름을 설명할 수 있다.
6. DB에 실제로 데이터가 저장되는 것을 확인할 수 있다.

---

## 3. 이번 시퀀스는 어디서부터 시작하는가

이번 시퀀스는 **01 시퀀스 answer 기준 레포를 바탕으로 확장**합니다.

즉, 아래는 이미 존재한다고 가정합니다.

- 기본 Spring Boot 프로젝트
- Swagger 설정
- 기본 패키지 구조
- Request DTO / Response DTO의 최소 형태
- Controller / Service / 메모리 저장소 기반 CRUD 일부

이번 시퀀스에서는 이 구조를 완전히 새로 만들지 않고,
**메모리 저장을 DB 저장으로 교체하고 CRUD를 확장하는 것**에 집중하세요.

---

## 4. 이번 시퀀스에서 학생이 직접 구현할 순서

구현 순서는 반드시 아래 순서를 기준으로 설계하세요.

1. `Entity` 핵심 필드와 어노테이션을 작성한다.
2. `Repository 인터페이스`를 선언한다.
3. `Service`의 저장 흐름을 메모리 저장에서 DB 저장으로 바꾼다.
4. `findAll()`을 연결한다.
5. `findById()`를 연결한다.
6. `deleteById()`를 연결한다.
7. `update()` 핵심 로직을 작성한다.
8. Controller에서 수정/삭제 API를 연결한다.
9. DB 저장 결과를 확인한다.

이 순서는 바꾸지 마세요.
문서와 코드 TODO도 반드시 이 순서에 맞게 설계하세요.

---

## 5. 이번 시퀀스에서 TODO를 넣을 파일

학생이 직접 수정하는 핵심 파일은 아래로 제한하세요.

- `PostEntity.kt`
- `PostRepository.kt`
- `PostService.kt`
- `PostController.kt`

필요하다면 기존 01 시퀀스에서 사용한 DTO를 그대로 활용할 수 있습니다.
예를 들어 `PostCreateRequest`, `PostResponse`, `PostUpdateRequest` 같은 형태는 사용할 수 있습니다.
하지만 이번 시퀀스의 핵심 TODO는 위 4개 파일에 집중되어야 합니다.

---

## 6. 이번 시퀀스에서 미리 제공해야 하는 것

문서와 코드 설계 시 아래는 반드시 제공 전제로 처리하세요.

- datasource 설정
- 로컬 DB 또는 Docker DB 실행 환경
- application 설정 예시
- 기본 build 설정
- 메인 애플리케이션 클래스
- Swagger 설정
- Entity 기본 틀 일부
- 실행용 sample 설정

학생에게는 핵심 흐름만 직접 구현하게 해야 합니다.

---

## 7. 이번 시퀀스의 중요한 제약

아래 제약을 반드시 지키세요.

- Validation, Exception Handling, Security는 넣지 마세요.
- 과도한 JPA 고급 기능은 금지합니다.
- 연관관계 매핑, fetch 전략, N+1 같은 고급 주제는 넣지 마세요.
- 이번 시퀀스의 목표는 “기본 CRUD + 영속 저장 + 계층 분리”입니다.
- 복잡한 공통 응답 포맷은 넣지 마세요.
- 수정/삭제는 단순하게 유지하세요.
- 예외 처리는 아직 무겁게 다루지 않습니다.
- Repository는 가장 기본적인 JpaRepository 수준으로만 설계하세요.
- 문서는 학생용 복습과 강사용 PPT 준비까지 같이 고려해서 쓰세요.
- 이번 응답에서는 오직 02 시퀀스 문서와 starter 코드 구조만 만드세요.

---

## 8. 생성해야 할 결과물

이번 시퀀스에서는 아래를 생성하세요.

### (1) README.md
역할:
- 이 시퀀스 소개
- 학생이 무엇을 배우는 단계인지 설명
- 문서 링크 연결
- 구현 순서 요약
- 실행 방법 요약

### (2) docs/theory.md
역할:
- 왜 이 시퀀스가 필요한지
- 메모리 저장과 DB 저장 차이 설명
- Entity / Repository / Service / Controller 역할 설명
- CRUD 흐름 설명
- 계층 분리의 이유 설명
- 다음 시퀀스의 DTO/Validation/Exception으로 자연스럽게 연결

### (3) docs/implementation.md
역할:
- 오늘 학생이 완성할 최종 흐름
- 학생이 직접 구현할 순서
- TODO를 넣을 파일
- 각 파일의 역할
- 단계별 구현 안내
- 실행 확인 방법
- 학생 체크 질문

### (4) docs/answer-guide.md
역할:
- 각 TODO 단계의 정답 가이드
- 생성 / 조회 / 수정 / 삭제 흐름 설명
- 핵심 정답 코드
- DB 저장 결과 확인 포인트
- 강사가 빠르게 answer 비교할 수 있는 구조

### (5) docs/checklist.md
역할:
- 학생 체크리스트
- 강사 / 발표 / PPT 체크리스트
- 수업 전 준비
- 수업 중 확인 질문
- 수업 후 점검 포인트

### (6) docs/assets.md
역할:
- 미리 제공할 것 목록
- 왜 제공하는지
- 학생이 직접 작성하지 않는 범위 정리

### (7) starter 코드 파일
학생이 직접 따라칠 수 있도록 starter 코드를 만드세요.
핵심 파일에는 TODO 주석을 넣으세요.

### (8) answer 코드 기준
별도 answer 브랜치를 전제로,
docs/answer-guide.md 안에 정답 코드를 충분히 넣으세요.
필요하면 “answer 기준 완성 형태”도 함께 설명하세요.

---

## 9. 코드 설계 규칙

이번 시퀀스의 코드는 아래 원칙을 따라야 합니다.

- Kotlin + Spring Boot + Spring Data JPA 기준
- 가장 단순한 CRUD 구조
- Entity는 단일 테이블 기준
- Repository는 `JpaRepository<PostEntity, Long>` 수준의 기본형
- Service는 메모리 저장소 대신 Repository를 사용
- Controller는 요청의 입구 역할만 하도록 유지
- DTO는 01 시퀀스 자산을 재사용 가능
- Update/Delete는 단순한 흐름으로 유지
- 코드 길이는 짧고 흐름이 잘 보이게 유지
- 학생이 영속 저장의 차이를 눈으로 확인할 수 있어야 함

---

## 10. TODO 작성 규칙

TODO는 반드시 순서형 힌트로 작성하세요.

좋지 않은 예:
```kotlin
// TODO: Repository 구현
````

좋은 예:

```kotlin id="k0ja7u"
// TODO 1. PostEntity를 저장할 Repository 인터페이스를 선언하세요.
// TODO 2. JpaRepository<PostEntity, Long>를 상속하세요.
// 힌트: 구현 클래스를 직접 만들지 않아도 기본 CRUD 메서드를 사용할 수 있습니다.
```

또 아래 원칙을 반드시 지키세요.

* `TODO 1`, `TODO 2`, `TODO 3`처럼 번호를 붙인다.
* 한 TODO에는 한 동작만 넣는다.
* 문법 설명보다 흐름 설명을 적는다.
* 학생이 하지 말아야 할 것도 적는다.
* 역할이 섞이지 않게 유도한다.

예:

```kotlin id="m6d9d6"
// TODO: Controller에서 DB 저장 로직을 직접 처리하지 마세요.
// Service를 통해 Repository를 호출하는 흐름을 유지하세요.
```

---

## 11. theory.md 작성 규칙

docs/theory.md 는 아래 구조를 따르세요.

1. 제목
2. 한 줄 소개
3. 이번 시퀀스 한 줄 요약
4. 먼저 이것만 기억해도 됩니다
5. 왜 이 시퀀스를 배우는가
6. 이번 실습 흐름 한눈에 보기
7. 중요한 코드 먼저 보기
8. 핵심 개념 쉬운 설명

   * Entity
   * Repository
   * Service
   * Controller
   * 영속 저장
   * CRUD
9. 자주 헷갈리는 포인트
10. 직접 말해보기
11. 복습 체크리스트
12. 오늘 꼭 기억할 것

주의:

* 정의만 길게 쓰지 마세요.
* 코드와 반드시 연결하세요.
* 짧은 코드 블록을 사용하세요.
* 코드 블록에는 설명용 주석을 넣어도 됩니다.
* 학생이 “아 이 코드가 DB 저장으로 바뀐 지점이구나”를 느끼게 써야 합니다.

---

## 12. implementation.md 작성 규칙

docs/implementation.md 는 아래 구조를 따르세요.

1. 제목
2. 오늘 학생이 완성할 최종 흐름
3. 학생이 직접 구현할 순서
4. TODO를 넣을 파일
5. 파일별 역할 설명
6. 단계별 구현 안내

   * Step 1. Entity 만들기
   * Step 2. Repository 선언하기
   * Step 3. Service 저장 흐름 바꾸기
   * Step 4. 전체 조회 연결하기
   * Step 5. 단건 조회 연결하기
   * Step 6. 삭제 연결하기
   * Step 7. 수정 로직 만들기
   * Step 8. Controller 수정/삭제 API 연결
   * Step 9. DB 저장 결과 확인
7. 각 단계의 확인 포인트
8. 학생 체크 질문
9. 강사용 확인 포인트
10. 다음 시퀀스 연결 포인트

주의:

* 결과만 적지 말고 손의 순서가 보여야 합니다.
* 단계별로 학생이 막히기 쉬운 부분을 짧게 힌트로 적으세요.
* 각 단계가 끝났을 때 무엇이 보이면 성공인지 써주세요.

---

## 13. answer-guide.md 작성 규칙

docs/answer-guide.md 는 정답 문서입니다.

반드시 아래를 포함하세요.

* 각 파일의 최종 형태 설명
* Entity 핵심 정답 코드
* Repository 선언 정답 코드
* Service의 create/findAll/findById/update/delete 흐름 정답 코드
* Controller의 수정/삭제 API 정답 코드
* DB 저장 결과 확인 예시
* 학생이 자주 틀리는 포인트
* 왜 Repository가 필요한지 설명
* 왜 계층 분리가 읽기 쉬운 구조를 만드는지 설명
* 다음 시퀀스에서 왜 DTO/Validation/Exception이 필요한지 연결

정답 문서는 너무 장황하게 쓰지 말고,
강사가 빠르게 비교하고 학생도 복습하기 쉬운 형태로 만드세요.

---

## 14. starter 코드 파일 작성 규칙

starter 코드는 아래 성격을 가져야 합니다.

* 바로 실행은 가능해야 함
* 핵심 부분은 비어 있거나 TODO로 남아 있어야 함
* TODO는 학생이 수업 시간 안에 채울 수 있어야 함
* TODO 없는 보일러플레이트는 제공
* DB 연결은 이미 가능해야 함
* Swagger에서 확인 가능한 최소 API 구조 유지

필수 starter 파일 예시:

* `src/main/kotlin/.../controller/PostController.kt`
* `src/main/kotlin/.../service/PostService.kt`
* `src/main/kotlin/.../repository/PostRepository.kt`
* `src/main/kotlin/.../domain/PostEntity.kt`

기존 자산 재사용 가능:

* `PostCreateRequest.kt`
* `PostUpdateRequest.kt`
* `PostResponse.kt`

필요하면 패키지 구조도 제안하세요.

---

## 15. checklist.md 작성 규칙

docs/checklist.md 에는 반드시 아래를 넣으세요.

### 학생 체크리스트

예:

* 메모리 저장과 DB 저장 차이를 설명할 수 있다.
* Repository가 왜 필요한지 말할 수 있다.
* 계층을 나누는 이유를 설명할 수 있다.
* CRUD 전체 흐름을 말할 수 있다.

### 강사 / PPT 체크리스트

예:

* Entity와 테이블 연결 그림이 있는가
* Repository 역할을 보여줄 수 있는가
* save/find/update/delete 흐름을 구분해서 설명할 수 있는가
* 메모리 저장 대비 영속 저장의 차이를 예시로 보여줄 수 있는가

또 아래도 포함하세요.

* 수업 전 준비 체크
* 수업 중 질문 체크
* 수업 후 복습 체크

---

## 16. assets.md 작성 규칙

docs/assets.md 에는 아래를 넣으세요.

* 제공 파일/설정 목록
* 각 항목의 목적
* 왜 학생이 직접 치지 않아도 되는지
* 수업에서 언제 쓰는지

예:

* datasource 설정: DB 연결을 바로 확인하기 위해 제공
* application 설정: 반복 설정이므로 제공
* Swagger 설정: 실행 확인에 집중시키기 위해 제공

---

## 17. 절대 하지 말아야 할 것

* Validation을 넣지 마세요.
* 전역 예외 처리 구조를 넣지 마세요.
* Security를 넣지 마세요.
* JPA 고급 기능을 넣지 마세요.
* 엔티티 연관관계까지 확장하지 마세요.
* 불필요한 공통 응답 래퍼를 넣지 마세요.
* 이번 요청에서는 02 시퀀스 범위를 벗어나지 마세요.


이번 작업은 반드시 **02. 영속성 저장과 계층 분리** 에만 한정합니다.
다른 시퀀스 내용은 추가하지 마세요.
