# SEQ 06 Testing 기준선 재정렬 및 테스트 리팩터링 계획

작성일: 2026-07-22 KST

상태: 06 원격 전환 완료, Visual Lab·중앙 draft PR 검토 대기

대상 저장소: `spring-boot-db-access-lab`

## 1. Goal

최신 `05-answer`의 기능, 보안 계약, 설정과 104개 회귀 테스트를 보존한 상태에서 `06-implementation`, `06-answer`를 다시 구성한다.

06의 신규 학습 범위는 아래 네 Service 단위 테스트로 제한한다.

1. `PostService.create` 정상 흐름
2. `PostService.getById` 조회 실패 흐름
3. `AuthService.login` 성공 흐름
4. `AuthService.login` 비밀번호 불일치 흐름

이번 리팩터링은 production package나 도메인 구조를 바꾸는 작업이 아니다. 최신 05 production 코드를 불변 기준으로 두고 fixture, mock 경계, assertion과 starter 실패 계약을 정리하는 테스트 코드 리팩터링이다.

## 2. Scope

변경 범위:

- 최신 `origin/05-answer`에서 두 06 후보를 다시 분기한다.
- 06의 표준 문서 네 개를 현재 feature package와 테스트 범위에 맞춘다.
- 기존 104개 테스트를 보존하고 Service 단위 테스트 네 개를 추가한다.
- 신규 테스트용 `TestFixtureFactory` 완성본을 제공한다.
- starter의 네 body는 명시적 `TODO()`로 실패하고 answer는 같은 네 body만 완성한다.
- 06 Visual Lab의 오래된 경로와 증거 설명만 현재 테스트에 맞춘다.
- 중앙의 이 시퀀스 문서와 audit 기록을 실제 실행 기준에 맞춘다.

변경하지 않는 범위:

- `src/main/**`, build와 runtime 설정
- 최신 05의 기존 test method와 test 설정
- Visual Lab 공용 CSS, renderer, layout과 interaction 구조
- 중앙 manifest의 시퀀스 상태
- 07과 이후 시퀀스
- 원격 official ref는 검증과 exact lease gate를 통과한 후보로만 전환한다.

## 3. 기준선 감사

2026-07-22 전환 결과와 복구 기준:

| Ref | Commit | 판단 |
|---|---|---|
| `origin/05-answer` | `db45c976ef8fa28ae67a7f93a21bb421f2cbb421` | 새 06이 보존할 최신 기준 |
| `origin/06-implementation` | `20a059f917b73fd5411a5abcfef615cbb5f4a5ff` | 전환·원격 검증 완료 |
| `origin/06-answer` | `7670ab9cf027c342314b6daa26b812d69b84f2ed` | 전환·원격 검증 완료 |
| `archive/06-implementation-pre-refresh-20260722` | `c6c65e4b9bc49ce436bbad88108cba8cc089ebd6` | 전환 전 starter 보존 |
| `archive/06-answer-pre-refresh-20260722` | `a316e9e17e7bbbe64be11c78815e7d6c615e91de` | 전환 전 answer 보존 |

기존 06은 최신 05를 조상으로 두지 않아 feature package, 계정 복구, JWT·OAuth·인가, Visual Lab과 테스트가 예전 기준으로 역행했다. 정적 `@Test` 선언도 최신 05의 104개에서 10개로 줄어 있었다. 이 차이는 06의 정상 학습 diff가 아니므로 과거 production patch는 재적용하지 않았다.

## 4. 구현 결과

### 4.1 표준 문서와 legacy 문서

두 후보에는 아래 표준 문서만 사용한다.

```text
README.md
docs/theory.md
docs/implementation.md
docs/checklist.md
```

최신 기준선에는 과거 `docs/answer-guide.md`, `docs/assets.md`, `docs/branch-guide.md` 같은 legacy 문서가 이미 존재하지 않았다. 삭제를 위한 빈 변경을 만들거나 파일을 다시 생성하지 않았다. 현재 코드와 일치하는 fixture·mock·검증 안내와 멘토 리뷰 포인트는 표준 네 문서에 통합했다.

### 4.2 Fixture

제공 경로:

```text
src/test/kotlin/com/andi/rest_crud/support/TestFixtureFactory.kt
```

제공 함수는 `postCreateRequest`, `postEntity`, `loginRequest`, `user` 네 개다. fixture는 starter와 answer에서 동일한 완성본이며 기존 104개 테스트를 일괄 치환하지 않는다.

### 4.3 신규 테스트

| 파일 | 보존/추가 범위 |
|---|---|
| `auth/service/AuthServiceTest.kt` | signup 4개 보존, login 성공·비밀번호 불일치 2개 추가 |
| `post/service/PostAuthorizationServiceTest.kt` | 기존 테스트 보존 |
| `post/service/PostServiceTest.kt` | create 성공·getById 조회 실패 2개 추가 |

로그인 테스트는 실제 BCrypt와 JWT를 생성하지 않고 `PasswordEncoder`, `JwtTokenProvider`의 협력을 mock으로 검증한다. 게시글 생성 테스트는 response뿐 아니라 repository에 전달된 entity의 title, content, author를 함께 검증한다.

### 4.4 Starter failure contract

`06-implementation`은 `./gradlew testClasses`가 통과한다. 전체 테스트에서는 신규 네 test method만 `NotImplementedError`로 실패하며, 빈 body나 assertion 없는 거짓 green은 없다.

`06-answer`는 같은 네 위치만 완성하고 test source에 `TODO()`를 남기지 않는다.

### 4.5 기존 HTTP 증거

validation 400, 인증 실패 401과 인가 실패 403은 다음 최신 05 테스트가 이미 검증한다.

- `auth/controller/AuthIntegrationTest.kt`
- `post/controller/PostAuthorizationIntegrationTest.kt`
- `common/config/SecurityErrorHandlerTest.kt`

신규 Service 테스트는 이 통합 증거를 대신하지 않으며, Google·SMTP credential 없이 실행된다.

## 5. 후보와 official 브랜치

| 역할 | Local branch | Candidate SHA | 상태 |
|---|---|---|---|
| 공통 준비 | `develop/06-refresh-common` | `0e112944cf05043241ead5204b48c6490469e968` | 구현 완료 |
| starter 후보 | `develop/06-refresh-implementation` | `20a059f917b73fd5411a5abcfef615cbb5f4a5ff` | official `06-implementation` 전환 완료 |
| answer 후보 | `develop/06-refresh-answer` | `7670ab9cf027c342314b6daa26b812d69b84f2ed` | official `06-answer` 전환 완료 |
| Visual Lab main 후보 | `develop/06-visual-evidence-refresh` | `27acade05047a1a719657cd641c6c9bf06161303` | draft PR #18 검토 대기 |
| 중앙 반영 후보 | `agent/06-testing-refresh` | `7479ae0b720328db4688e28555297e99439a176e` | draft PR #9 검토 대기 |

두 공식 06 원격 브랜치는 atomic push와 exact lease로 위 후보에 전환됐고 fetch 뒤 SHA와 최신 05 ancestry를 확인했다. Visual Lab main 후보는 [draft PR #18](https://github.com/stdiodh/spring-boot-db-access-lab/pull/18), 중앙 문서와 submodule pointer는 [draft PR #9](https://github.com/stdiodh/A-AND-I-4TH-CODE-LAB/pull/9)로 분리했다. 두 PR은 아직 각 저장소의 `main`에는 합치지 않았다.

## 6. 검증 결과

| Gate | 결과 |
|---|---|
| Lineage | 두 후보 모두 최신 `05-answer`를 조상으로 가짐 |
| Production invariant | `src/main`, build와 runtime 설정 diff 0 |
| Regression preservation | 기존 104개 `@Test` 선언과 test source 삭제 0 |
| New learning tests | answer의 `@Test` 선언 108개, 신규 Auth 2개·Post 2개 |
| Starter compile | `./gradlew testClasses --no-daemon` 통과 |
| Starter red | 전체 108개 중 신규 네 test만 `NotImplementedError`로 실패 |
| Answer targeted | `AuthServiceTest`, `PostServiceTest` 통과 |
| Answer full | `./gradlew test` 통과 |
| Answer rerun | `./gradlew test --rerun-tasks` 통과 |
| Branch diff | implementation과 answer 차이는 두 Service test file뿐 |
| Docs/fixture | 두 후보에서 동일 |
| Static | answer TODO 0, `git diff --check`와 Visual Lab data syntax 통과 |
| External dependency | Google·SMTP credential 없이 완료 |
| Central validation | manifest 4개 check group, Visual Lab 8개 repo group 모두 통과 |

핵심 재현 명령:

```bash
./gradlew testClasses
./gradlew test

./gradlew test \
  --tests '*AuthServiceTest' \
  --tests '*PostServiceTest'
./gradlew test --rerun-tasks
```

## 7. Visual Lab 정합성 보정

초기 계획은 Visual Lab tree를 불변으로 두었지만 실제 검토에서 06 데이터가 과거 flat package와 실제 BCrypt/JWT 사용을 설명하고 있었다. `$aandi-visual-lab-design` 절차에 따라 범위를 아래 사실 보정으로 제한했다.

- code point를 현재 `auth/service`, `post/service` test 경로로 수정
- `PasswordEncoder`, `JwtTokenProvider`를 mock collaborator로 설명
- 게시글 생성의 save 인자와 response 증거를 함께 표시
- 400·401·403을 미래 후보가 아니라 기존 05 통합 테스트 증거로 표시

공용 CSS, JavaScript renderer, component, palette, typography와 motion은 변경하지 않았다. 데스크톱·모바일, keyboard focus, 긴 한글, console error, reduced-motion rule을 브라우저에서 확인했다.

## 8. 원격 전환 결과와 후속 Gate

06 official ref 전환은 다음 순서로 완료했다.

1. `origin/06-implementation`, `origin/06-answer`가 old SHA와 같은지 재확인했다.
2. 기존 tip을 archive tag로 보존했다.
3. candidate SHA를 명시한 atomic push와 exact `--force-with-lease`를 사용했다.
4. fetch 뒤 official ref SHA와 최신 05 ancestry를 재확인했다.

생성·확인한 archive tag:

```text
archive/06-implementation-pre-refresh-20260722
archive/06-answer-pre-refresh-20260722
```

중앙 후보는 submodule pointer를 `27acade05047a1a719657cd641c6c9bf06161303`으로 갱신했고 전체 submodule을 초기화한 격리 worktree에서 manifest와 Visual Lab validator를 통과했다. 병합은 Visual Lab [draft PR #18](https://github.com/stdiodh/spring-boot-db-access-lab/pull/18)을 먼저 처리한 뒤 중앙 [draft PR #9](https://github.com/stdiodh/A-AND-I-4TH-CODE-LAB/pull/9)을 처리한다.

## 9. Acceptance Gates

| Gate | 완료 기준 |
|---|---|
| Lineage | 최신 `05-answer`가 두 official 06 ref의 조상이다. |
| Production invariant | `05-answer..06-answer`의 production, build, runtime 설정 diff가 0이다. |
| Regression preservation | 기존 104개 테스트와 test source 삭제가 0이다. |
| New learning tests | answer에 Auth 2개, Post 2개를 더해 최소 108개 테스트가 있다. |
| Starter red | 신규 네 test만 명시적 TODO 이유로 실패한다. |
| Answer green | targeted, 전체, `--rerun-tasks`가 통과한다. |
| Branch diff | implementation과 answer 차이는 두 Service test body뿐이다. |
| Docs | 표준 네 문서가 실제 package, TODO와 명령에 일치하며 legacy 파일을 재생성하지 않는다. |
| Visual Lab | 06 사실 보정만 있고 공용 디자인·renderer 변경과 파일 삭제가 없다. |
| External dependency | Google·SMTP credential 없이 테스트가 끝난다. |
| Central validation | `validate-manifest.py`, `validate-visual-labs.py`가 통과한다. |

## 10. 남은 작업과 Definition Of Done

구현, official 06 ref 전환, 중앙 validator와 두 draft PR 게시까지 완료했다. 남은 작업은 아래 병합 순서뿐이다.

1. Visual Lab draft PR #18을 검토·병합한다.
2. 중앙 draft PR #9가 병합된 submodule commit을 가리키는지 확인한 뒤 검토·병합한다.

두 PR이 병합되고 07과 다른 시퀀스에 변경이 없음을 다시 확인하면 상태를 `완료`로 바꾼다.
