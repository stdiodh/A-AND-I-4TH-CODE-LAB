# 03. 안전한 요청 처리

## 시퀀스 목적

이 시퀀스는 `02`의 DB CRUD 흐름 위에
요청 DTO, Validation, Exception Handling을 붙여
학생이 아래 흐름을 선명하게 이해하게 만드는 단계입니다.

- 요청과 응답을 Entity와 분리한다
- 잘못된 입력을 요청 초입에서 막는다
- 검증 실패와 비즈니스 예외를 구분한다
- 실패 응답도 설계 대상이라는 감각을 익힌다
- 성공 응답과 실패 응답을 같은 수준으로 읽는다

즉, 이번 시퀀스의 핵심은 어노테이션을 많이 붙이는 것이 아니라
사용자 입력을 어디까지 믿을 수 있는지, 실패를 어떤 계약으로 돌려줄지를
코드와 실행 결과로 이해하는 것입니다.

## 학생이 완성해야 하는 최종 이해

학생은 이 시퀀스를 마친 뒤 아래를 설명할 수 있어야 합니다.

1. 왜 Entity를 요청/응답 모델로 그대로 쓰면 안 되는지
2. Request DTO와 Response DTO를 왜 나누는지
3. Validation이 어디서 동작하는지
4. 검증 실패와 비즈니스 예외가 왜 다른지
5. 실패 응답을 왜 같은 구조로 통일하는지
6. 기본 검증과 커스텀 검증이 어떤 상황에서 갈리는지

## 시작 기준

이번 시퀀스는 `02-answer` 기준 레포 위에서 시작합니다.

이미 존재한다고 가정하는 것:

- Spring Boot 프로젝트
- MySQL 실행 환경
- Entity / Repository / Service / Controller 기반 기본 CRUD
- Swagger 설정
- 생성 / 조회 / 수정 / 삭제 기본 흐름

이번 단계에서는 저장 구조를 새로 만들지 않고,
입력을 더 안전하게 받고, 실패를 더 명확하게 응답하는 것에 집중합니다.

## 레포 전략

- 사용 레포: `spring-boot-db-access-lab`
- 학생 starter: `03-implementation`
- 정답 브랜치: `03-answer`
- 안내 브랜치: `main`

## 학생 구현 순서

구현 순서는 반드시 아래 순서를 따릅니다.

1. `Request DTO`와 `Response DTO`를 분리합니다.
2. Controller 입력 타입을 DTO로 바꿉니다.
3. DTO -> Entity 변환 코드를 연결합니다.
4. `@Valid`와 기본 검증을 붙입니다.
5. 검증 실패 응답 구조를 만듭니다.
6. 비즈니스 예외 1개를 만듭니다.
7. 전역 예외 핸들러를 연결합니다.
8. 성공 요청과 실패 요청을 직접 실행해봅니다.

문서와 TODO도 반드시 이 순서를 기준으로 설계합니다.

## TODO를 넣는 핵심 파일

- `PostCreateRequest.kt`
- `PostUpdateRequest.kt`
- `PostResponse.kt`
- `PostService.kt`
- `GlobalExceptionHandler.kt`
- `ErrorResponse.kt`

필요하면 아래 파일을 추가로 둘 수 있지만,
핵심 TODO는 위 파일에 집중합니다.

- `PostNotFoundException.kt`

## 미리 제공하는 것

- `02-answer` 기반 CRUD 구조
- 기본 패키지 구조
- MySQL 실행 설정
- 테스트용 H2 설정
- Swagger UI 설정
- `PostController`의 `@Valid` 연결
- 예외 클래스 기본 틀
- 응답 포맷 기본 틀
- 실행 가능한 starter 환경

학생은 입력 검증과 실패 응답의 핵심 흐름만 직접 구현합니다.

## 실무 확장 개념

이번 시퀀스의 실무 확장 개념은 아래입니다.

- 커스텀 Validation

중요한 기준은 이렇습니다.

- 이번 시퀀스의 메인 구현 흐름은 기본 `@NotBlank` + `@Valid` + 예외 응답 통일로 유지합니다.
- 대신 이론 문서에서는 기본 검증만으로 막히지 않는 문제 입력을 보여줍니다.
- 그리고 커스텀 annotation / validator 코드가 어떤 모양인지까지 같이 설명합니다.

예를 들어 문서에는 아래 흐름이 들어가야 합니다.

1. 빈 문자열은 아니지만 서비스 규칙상 막아야 하는 제목 입력
2. `@NotBlank`만으로는 이 요청이 왜 통과되는지
3. Service 안쪽 `if` 검증이 왜 뒤늦고 흐름을 지저분하게 만드는지
4. `@NoForbiddenTitleWords` 같은 커스텀 검증 코드 예시
5. 이번 시퀀스에서 어디까지 구현하고, 어디까지는 설명만 하는지

즉 `03`의 실무 확장 개념은
기본 Validation 소개가 아니라
기본 검증의 한계와 커스텀 검증의 방향까지 같이 읽는 입문 단계로 설계합니다.

## 구현 제약

- Security, JWT, 인증/인가를 넣지 않습니다.
- 테스트 확장을 본격적으로 넣지 않습니다.
- 공통 응답 래퍼를 과도하게 복잡하게 만들지 않습니다.
- 예외 계층을 실무 풀버전처럼 무겁게 만들지 않습니다.
- 커스텀 Validation을 메인 구현 범위로 과도하게 확장하지 않습니다.
- 이번 시퀀스의 목표는 `DTO 분리 + 기본 Validation + 일관된 실패 응답`입니다.
- 실무 확장 개념인 커스텀 Validation은 문서에서 상세히 다룹니다.
- 단, 문서에는 반드시 `문제 입력 -> 기본 검증의 한계 -> 해결 코드 예시`가 함께 들어가야 합니다.

## 필수 산출물

각 브랜치에는 아래 산출물이 모두 있어야 합니다.

- `README.md`
- `docs/theory.md`
- `docs/implementation.md`
- `docs/answer-guide.md`
- `docs/checklist.md`
- `docs/assets.md`
- `03-implementation` starter 코드
- `03-answer` 완성 코드

## 검증 기준

- `03-implementation`은 실행 가능한 starter여야 합니다.
- `03-answer`는 DTO, Validation, Exception 흐름이 완성되어 있어야 합니다.
- 루트 시퀀스 문서와 토픽 레포 `docs/*`가 모두 같은 시퀀스를 설명해야 합니다.
- 실무 확장 개념은 `theory.md`에만 고립되지 않고 `implementation.md`, `answer-guide.md`와도 연결되어야 합니다.
- 성공 요청 / 검증 실패 / 게시글 없음 요청을 문서 기준으로 직접 비교할 수 있어야 합니다.

## 수업 메시지

이번 단계에서 학생이 꼭 가져가야 할 문장은 아래입니다.

- CRUD가 된다고 해서 요청 처리가 안전한 것은 아닙니다.
- Request DTO와 Response DTO는 Entity와 역할이 다릅니다.
- Validation은 요청 초입에서 잘못된 값을 막는 장치입니다.
- Exception Handling은 실패 응답도 계약으로 만든다는 감각입니다.
- 기본 검증만으로는 부족한 순간이 오고, 그때 커스텀 Validation이 필요해집니다.
