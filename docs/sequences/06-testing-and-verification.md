# 06. 테스트와 검증

## 목표

최신 `05-answer`의 기능, 보안 계약과 자동 테스트를 그대로 보존한 채 Service 단위 테스트 네 개를 추가합니다.
이미 제공된 104개 회귀 테스트와 학생이 새로 완성할 네 테스트의 역할을 구분하고, fixture·mock·assertion으로 Service의 판단을 격리해 검증합니다.

## 이 시퀀스에서 배우는 것

- Given, When, Then으로 한 동작을 검증하는 방법
- fixture로 반복 준비를 줄이되 판단에 중요한 값은 테스트 본문에 드러내는 기준
- Repository, `PasswordEncoder`, `JwtTokenProvider`를 mock으로 분리하는 기준
- 정상 반환, 기대 예외, 저장 인자와 collaborator 호출을 검증하는 방법
- Service 단위 테스트와 HTTP 통합 테스트가 제공하는 증거의 차이

## 시작 브랜치

```bash
git checkout 06-implementation
```

## 실습 전 확인

- 토픽 레포: `spring-boot-db-access-lab`
- 가이드 브랜치: `main`
- 시작 브랜치: `06-implementation`
- 이전 기준: 최신 `05-answer`
- production 코드, 설정과 기존 104개 테스트는 수정하지 않습니다.
- Google·SMTP credential 없이 자동 테스트를 실행할 수 있습니다.

## 이번에 다루는 파일

```text
src/test/kotlin/com/andi/rest_crud/
├── auth/service/AuthServiceTest.kt
├── post/service/PostAuthorizationServiceTest.kt
├── post/service/PostServiceTest.kt
└── support/TestFixtureFactory.kt
```

`TestFixtureFactory`와 기존 `PostAuthorizationServiceTest`, `AuthServiceTest`의 signup 테스트 네 개는 완성된 상태로 제공됩니다.
fixture를 새로 만드는 것이 아니라 다음 네 test body를 완성하는 것이 이번 과제입니다.

| 대상 | 정상 흐름 | 실패 흐름 |
|---|---|---|
| `PostService` | 생성 입력과 principal email이 저장값과 응답에 보존됨 | 없는 id 조회가 `PostNotFoundException`을 발생시킴 |
| `AuthService` | email 정규화 뒤 token과 만료 정보를 반환함 | 비밀번호 불일치가 JWT 생성 전에 중단됨 |

## 구현 순서

1. 제공된 `TestFixtureFactory`의 기본값과 override 지점을 읽습니다.
2. `PostService.create`의 저장 인자와 응답 mapping을 검증합니다.
3. `PostService.getById`의 조회 실패 예외를 검증합니다.
4. `AuthService.login` 성공 시 email 정규화, password 비교, token과 expiry를 검증합니다.
5. 비밀번호 불일치 시 `InvalidCredentialsException`과 JWT 미호출을 검증합니다.
6. 대상 테스트를 먼저 실행한 뒤 전체 회귀 suite를 반복 실행합니다.

## starter 상태 확인

`06-implementation`은 test source가 컴파일되지만 신규 네 body의 명시적인 `TODO()` 때문에 전체 테스트가 실패합니다.

```bash
./gradlew testClasses
./gradlew test
```

첫 명령은 통과해야 합니다. 두 번째 명령은 신규 네 테스트만 `NotImplementedError`로 실패해야 합니다.
기존 테스트, Spring context나 dependency 실패는 정상적인 starter 상태가 아닙니다.

## 답안 검증 순서

네 body를 완성한 뒤 좁은 범위부터 확인합니다.

```bash
./gradlew test \
  --tests '*AuthServiceTest' \
  --tests '*PostServiceTest'

./gradlew test
./gradlew test --rerun-tasks
git diff --check
```

답안은 기존 104개와 신규 4개, 최소 108개의 `@Test` 선언을 보존해야 하며 완성된 두 test file에 `TODO()`가 없어야 합니다.

## 기존 HTTP 검증과의 경계

신규 네 Service 테스트는 실제 DB, BCrypt 계산, JWT 서명과 HTTP filter chain을 실행하지 않습니다.
최신 05에는 다음 HTTP·보안 증거가 이미 통합 테스트로 제공됩니다.

- `auth/controller/AuthIntegrationTest.kt`: validation 400과 인증 흐름
- `post/controller/PostAuthorizationIntegrationTest.kt`: 인증 실패 401과 인가 실패 403
- `common/config/SecurityErrorHandlerTest.kt`: 보안 오류 응답 계약

신규 Service 테스트가 이 증거를 대신하지 않으며, 기존 통합 테스트도 삭제하거나 약화하지 않습니다.

## Visual Lab

fixture, mock, Service, assertion과 테스트별 보장 범위를 화면에서 비교할 수 있습니다.

- [06 테스트와 검증 Visual Lab](../../spring-boot-db-access-lab/docs/visual-lab/sequences/06/index.html)

로컬 확인:

```bash
python3 -m http.server 8081 -d spring-boot-db-access-lab/docs/visual-lab
```

```text
http://localhost:8081/sequences/06/
```

## 완료 기준

- 최신 05의 production, 설정과 기존 104개 테스트를 보존했습니다.
- 제공 fixture를 사용해 `PostService` 2개, `AuthService` 2개 test body를 완성했습니다.
- 생성 성공에서 저장 인자와 응답을 모두 검증했습니다.
- 로그인 성공에서 정규화와 collaborator 협력을, 실패에서 JWT 미호출을 검증했습니다.
- 대상 테스트, 전체 테스트와 `--rerun-tasks` 실행이 통과합니다.
- 신규 Service 테스트와 기존 400·401·403 통합 테스트의 증거 범위를 설명할 수 있습니다.
- Google·SMTP credential 없이 자동 테스트를 완료했습니다.

## 정답과 비교하는 방법

막혔거나 실습을 마친 뒤에만 참고 정답과 비교합니다.

```bash
git diff 06-implementation..06-answer
```

두 브랜치의 학습 diff는 `AuthServiceTest.kt`, `PostServiceTest.kt`의 test body로 제한됩니다.

## 다음 시퀀스

다음은 `07. 캐시와 Redis`입니다.
조회 성능을 위해 Redis 캐시를 도입합니다.
