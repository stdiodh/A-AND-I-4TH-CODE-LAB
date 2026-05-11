# 06. 테스트와 검증

## 목표

이미 만든 Service 흐름과 인증/인가 흐름을 테스트로 다시 확인합니다.
테스트 종류를 모두 넓히기보다 Service 단위 테스트와 핵심 HTTP 정책 테스트의 실행 기준을 명확히 잡습니다.

## 이 시퀀스에서 배우는 것

- 테스트가 필요한 이유
- Service 단위 테스트 범위
- 정상 케이스와 실패 케이스 구분
- fixture로 테스트 입력 정리
- mock으로 의존성 분리
- validation 400, 인증 실패 401, 인가 실패 403 확인

## 시작 브랜치

```bash
git checkout 06-implementation
```

## 실습 전 확인

- 토픽 레포: `spring-boot-db-access-lab`
- 가이드 브랜치: `main`
- 시작 브랜치: `06-implementation`
- 이전 기준: `05-answer`
- 이번 시퀀스는 전체 E2E보다 Service 단위 테스트와 최소 HTTP 정책 테스트에 집중합니다.

## 구현할 TODO

1. 테스트 대상 Service를 확인합니다.
2. 테스트 fixture를 준비합니다.
3. `PostService` 정상 케이스와 작성자 인가 실패 케이스를 테스트합니다.
4. `PostService` 실패 케이스를 테스트합니다.
5. `AuthService` 인증 성공 케이스를 테스트합니다.
6. `AuthService` 인증 실패 케이스를 테스트합니다.
7. 공개 API, 보호 API, 작성자 전용 API의 HTTP 상태 코드를 테스트합니다.
8. 테스트를 반복 실행하며 결과를 확인합니다.

## 실행 방법

```bash
docker compose up -d
./gradlew bootRun
```

애플리케이션 실행이 꼭 필요하지 않은 테스트 실습은 테스트 명령을 먼저 실행해도 됩니다.

## 테스트 방법

```bash
./gradlew test
```

테스트가 확인하는 것:

- unit test는 Service의 비즈니스 판단을 빠르게 확인합니다.
- slice test는 Controller, Repository처럼 한 계층의 Spring 연결을 좁게 확인합니다.
- integration test는 인증/인가, DB 저장, HTTP 상태 코드처럼 여러 계층이 이어진 흐름을 확인합니다.
- validation 400, 인증 실패 401, 인가 실패 403을 테스트 이름과 결과로 구분합니다.

권장 실행 순서:

1. 실패하는 단위 테스트 하나를 먼저 읽습니다.
2. 관련 fixture와 mock 설정을 확인합니다.
3. 전체 `./gradlew test`를 다시 실행합니다.
4. 통합 테스트 실패는 요청 body, 인증 헤더, DB 준비 데이터를 함께 확인합니다.

실패하면 먼저 볼 것:

- 테스트 이름이 given/when/then 의도를 드러내는지 확인합니다.
- 실패 메시지의 expected/actual 값을 비교합니다.
- 외부 서비스가 필요한 테스트라면 mock 또는 local profile 대안을 사용합니다.

완료 기준:

- unit, slice, integration test의 차이를 설명할 수 있습니다.
- 테스트 실행 순서와 실패 메시지 읽는 법을 설명할 수 있습니다.
- 전체 테스트가 통과하고, 각 테스트가 어떤 동작을 보장하는지 말할 수 있습니다.

## 확인할 API 또는 화면

- 테스트 실행 결과
- `PostServiceTest`
- `AuthServiceTest`
- `PostAuthorizationIntegrationTest`
- validation 실패 400
- 인증 없는 보호 API 접근 401
- 다른 사용자 수정/삭제 403
- 실패 테스트가 실패 이유를 정확히 보여주는지 확인

## 자주 발생하는 문제

- 모든 테스트를 실제 DB 기반으로 만들려고 합니다. Service 단위 테스트는 mock으로 책임을 분리하고, HTTP 정책은 작은 통합 테스트로 확인합니다.
- 정상 케이스만 테스트합니다. 실패 케이스도 하나 이상 작성합니다.
- 테스트마다 입력값을 길게 반복합니다. fixture로 반복 입력을 줄입니다.
- 테스트 이름이 무엇을 검증하는지 드러나지 않습니다.
- 401과 403을 같은 실패로 봅니다. 인증 실패와 인가 실패는 다른 상태 코드로 확인합니다.

## 완료 기준

- Service 정상/실패 테스트가 작성되었습니다.
- fixture 또는 테스트 helper로 반복 입력이 정리되었습니다.
- 인증 성공/실패 흐름을 테스트로 확인했습니다.
- 공개 조회 API는 인증 없이 성공합니다.
- 보호 쓰기 API는 인증 없이는 401, 작성자가 아니면 403으로 실패합니다.
- `./gradlew test`가 통과합니다.
- 어떤 테스트가 어떤 동작을 보장하는지 설명할 수 있습니다.

## 정답과 비교하는 방법

막혔거나 실습을 마친 뒤에만 참고 정답과 비교합니다.

```bash
git diff 06-implementation..06-answer
```

## 다음 시퀀스

다음은 `07. 캐시와 Redis`입니다.
조회 성능을 위해 Redis 캐시를 도입합니다.
