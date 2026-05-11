# 02. 영속성 저장과 계층 분리

## 목표

메모리 저장소를 MySQL/JPA 저장소로 바꾸고, Controller, Service, Repository, Entity 계층을 분리합니다.
데이터가 서버 재시작 후에도 DB에 남는 흐름을 확인합니다.

## 이 시퀀스에서 배우는 것

- 메모리 저장과 DB 저장의 차이
- Entity와 테이블의 연결
- Repository가 DB 접근을 맡는 이유
- `Controller -> Service -> Repository -> DB` 흐름
- MySQL에서 실제 저장 결과를 확인하는 방법

## 시작 브랜치

```bash
git checkout 02-implementation
```

## 실습 전 확인

- 토픽 레포: `spring-boot-db-access-lab`
- 가이드 브랜치: `main`
- 시작 브랜치: `02-implementation`
- 이전 기준: `01-answer`
- Docker로 MySQL을 실행할 수 있어야 합니다.

## 구현할 TODO

1. `PostEntity`의 핵심 필드와 JPA 어노테이션을 작성합니다.
2. `PostRepository`를 선언합니다.
3. Service 저장 흐름을 DB 저장으로 바꿉니다.
4. 전체 조회와 단건 조회를 Repository에 연결합니다.
5. 수정과 삭제 흐름을 연결합니다.
6. Controller에서 수정/삭제 API를 연결합니다.
7. MySQL 저장 결과를 확인합니다.

## 실행 방법

```bash
docker compose up -d
./gradlew bootRun
```

## 테스트 방법

```bash
./gradlew test
```

테스트가 확인하는 것:

- Repository integration test로 JPA Repository와 테스트 DB 연결을 확인합니다.
- 게시글 저장, 조회, 수정, 삭제가 DB 기준으로 동작하는지 확인합니다.
- Entity와 DTO를 섞지 않고 Service가 Repository를 통해 DB에 접근하는지 확인합니다.

실패하면 먼저 볼 것:

- 테스트 DB 설정과 런타임 MySQL 설정을 혼동하지 않았는지 확인합니다.
- Entity 필드, Repository 메서드, Service 트랜잭션 흐름을 순서대로 봅니다.
- 저장 후 조회가 실패하면 id 생성과 flush 시점을 확인합니다.

완료 기준:

- Repository integration test가 통과합니다.
- DB 저장/조회/수정/삭제 테스트가 통과합니다.
- 메모리 저장과 DB 저장의 차이를 테스트 결과로 설명할 수 있습니다.

## 확인할 API 또는 화면

- Swagger: `http://localhost:8080/swagger`
- `POST /posts`
- `GET /posts`
- `GET /posts/{id}`
- `PUT /posts/{id}`
- `DELETE /posts/{id}`
- MySQL 테이블 데이터

## 자주 발생하는 문제

- MySQL을 켜지 않고 서버를 실행합니다. 먼저 `docker compose up -d`를 실행합니다.
- Entity와 DTO를 섞습니다. Entity는 DB 저장 모양, DTO는 요청/응답 모양입니다.
- `findById()` 결과가 없을 때를 처리하지 않습니다. 없는 데이터 조회 흐름을 확인합니다.
- 테스트는 H2 기반으로 실행될 수 있으므로 런타임 DB와 테스트 DB 설정을 구분합니다.

## 완료 기준

- CRUD 요청이 DB에 저장되고 조회됩니다.
- 서버 재시작 후에도 데이터가 남는 것을 확인했습니다.
- Entity, Repository, Service 역할을 설명할 수 있습니다.
- `./gradlew test`가 통과합니다.

## 정답과 비교하는 방법

막혔거나 실습을 마친 뒤에만 참고 정답과 비교합니다.

```bash
git diff 02-implementation..02-answer
```

## 다음 시퀀스

다음은 `03. 안전한 요청 처리`입니다.
요청 검증과 에러 응답을 추가합니다.
