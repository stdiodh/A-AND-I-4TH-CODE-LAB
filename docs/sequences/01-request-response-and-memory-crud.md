# 01. 요청/응답과 메모리 CRUD

## 목표

Spring Boot에서 요청이 들어오고 응답이 나가는 가장 기본 흐름을 구현합니다.
DB 없이 메모리 저장소를 사용해 CRUD와 HTTP 흐름에 집중합니다.

## 이 시퀀스에서 배우는 것

- Controller가 요청을 받는 방식
- Service가 처리 흐름을 맡는 이유
- Repository가 임시 메모리 저장소를 다루는 방식
- Request DTO와 Response DTO의 역할
- Swagger에서 API를 실행하고 응답을 확인하는 방법

## 시작 브랜치

```bash
git checkout 01-implementation
```

## 실습 전 확인

- 토픽 레포: `spring-boot-rest-crud-lab`
- 가이드 브랜치: `main`
- 시작 브랜치: `01-implementation`
- Java와 Gradle 실행 환경이 준비되어 있어야 합니다.
- 이번 시퀀스에서는 DB, JPA, Security, Validation을 다루지 않습니다.

## 구현할 TODO

1. `PostCreateRequest`를 작성합니다.
2. `PostResponse`를 작성합니다.
3. 메모리에 저장할 `Post` 모델을 확인합니다.
4. `PostMemoryRepository` 저장/조회 흐름을 구현합니다.
5. `PostService.create()`를 구현합니다.
6. `PostService.getAll()`과 `getById()`를 구현합니다.
7. `PostController`에서 POST/GET API를 연결합니다.
8. Swagger에서 생성, 전체 조회, 단건 조회를 실행합니다.

## 실행 방법

```bash
./gradlew bootRun
```

## 테스트 방법

```bash
./gradlew test
```

테스트가 확인하는 것:

- Controller smoke test로 Spring MVC 요청 경로가 연결되는지 확인합니다.
- 게시글 생성, 전체 조회, 단건 조회의 기본 성공 케이스가 통과하는지 확인합니다.
- 메모리 Repository가 요청 흐름 안에서 값을 저장하고 다시 반환하는지 확인합니다.

실패하면 먼저 볼 것:

- 실패한 테스트 이름에서 어떤 API가 깨졌는지 먼저 읽습니다.
- Controller mapping 경로, HTTP method, DTO 필드 이름이 테스트 요청과 같은지 확인합니다.
- 메모리 저장소는 서버 재시작 후 비어 있는 것이 정상입니다.

완료 기준:

- Controller smoke test가 통과합니다.
- CRUD API 기본 성공 케이스가 통과합니다.
- 실패 메시지를 보고 Controller, Service, Repository 중 어디를 볼지 설명할 수 있습니다.

## 확인할 API 또는 화면

- Swagger: `http://localhost:8080/swagger`
- `POST /posts`
- `GET /posts`
- `GET /posts/{id}`

## 자주 발생하는 문제

- Controller에서 직접 저장하려고 합니다. Controller는 Service를 호출하는 입구 역할만 합니다.
- 서버 재시작 후 데이터가 사라집니다. 메모리 저장소라서 정상입니다.
- DTO와 내부 모델을 같은 것으로 생각합니다. 요청/응답 모양과 내부 저장 모양은 분리합니다.
- Swagger 경로가 열리지 않으면 서버가 정상 기동했는지 로그를 먼저 확인합니다.

## 완료 기준

- POST 요청으로 게시글을 생성할 수 있습니다.
- 전체 조회와 단건 조회가 동작합니다.
- Controller -> Service -> Repository 흐름을 설명할 수 있습니다.
- 서버 재시작 시 메모리 데이터가 사라지는 이유를 설명할 수 있습니다.
- `./gradlew test`가 통과합니다.

## 정답과 비교하는 방법

막혔거나 실습을 마친 뒤에만 참고 정답과 비교합니다.

```bash
git diff 01-implementation..01-answer
```

## 다음 시퀀스

다음은 `02. 영속성 저장과 계층 분리`입니다.
메모리 저장소를 MySQL/JPA 기반 저장소로 바꿉니다.
