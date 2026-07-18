# 05 OAuth2·SMTP 도메인 구조 갱신 계획

## 1. 목표

05주차의 `05-implementation`과 `05-answer`를 최신 `04-answer` 계약 위에서 다시 정렬합니다.
04주차의 인증·인가 회귀 테스트를 보존하고, OAuth2 로그인과 SMTP 계정 복구 흐름을 외부 서버 없이 검증할 수 있게 합니다.
프로덕션 코드는 기술 계층이 아니라 `common`, `user`, `auth`, `oauth`, `recovery`, `post` 기능 도메인부터 찾을 수 있는 패키지 구조로 정리합니다.

## 2. 현재 진단

- 최신 `04-answer`는 2026-07-18의 `51770df`이고 60개 테스트를 제공합니다.
- 현재 `05-implementation`과 `05-answer`는 2026-04-22의 구형 JWT 기준 `9318a93`에서 갈라졌습니다.
- 현재 테스트는 `05-implementation` 3개, `05-answer` 6개뿐이어서 OAuth2·SMTP TODO가 남아도 통과합니다.
- 05주차에는 JWT issuer/audience, 설정 fail-fast, 결정적 Validation 오류, JSON 401/403, email 정규화, 중복 가입 경쟁 처리, `.env` 보호 장치가 반영되지 않았습니다.
- SMTP 설정 이름이 중앙 문서의 `SPRING_MAIL_*`와 일치하지 않고, 테스트용 fake sender와 OAuth fake profile 경로도 없습니다.
- 기존 OAuth 사용자의 email 자동 갱신은 email 기반 JWT subject와 게시글 작성자 값을 서로 다른 시점의 신원으로 만들 수 있습니다.

## 3. 범위

변경:

- 최신 `04-answer`의 인증·인가 동작과 60개 테스트를 05주차 공통 기준으로 사용
- `05-implementation`, `05-answer`에 같은 도메인 우선 패키지 구조 적용
- OAuth2 계정 식별, 검증된 email, 계정 충돌, redirect 보안 경계 점검
- SMTP 설정, 메일 발송 위임, 계정 존재 비노출, 외부 서버 없는 테스트 점검
- README, theory, implementation, checklist의 경로와 검증 설명 동기화

변경하지 않음:

- 현재 작업 중인 `04-implementation`의 커밋되지 않은 파일
- 실제 Google 계정이나 실제 SMTP 자격 증명
- 비밀번호 재설정 토큰 저장, 만료, 일회성 사용, 실제 비밀번호 변경
- email 식별자를 user id 기반 JWT와 게시글 FK로 전환하는 후속 모델 개편
- 중앙 시퀀스 상태와 다음 06주차 범위

## 4. 가정과 결정

- 05주차의 이전 완료 기준은 중앙 시퀀스 문서대로 최신 `04-answer`입니다.
- 기존 OAuth 사용자의 provider email이 달라져도 이번 범위에서는 내부 email을 자동 변경하지 않습니다. 안정적인 user id 전환 없이 email을 바꾸면 기존 JWT와 게시글 소유권이 분리되기 때문입니다.
- OAuth2 handshake에는 기본 authorization request와 `state` 보존을 위한 임시 session이 필요할 수 있지만, 로그인 완료 뒤 API 인증은 Bearer JWT 기반 stateless 흐름을 유지합니다.
- URL fragment의 Access Token 전달은 학습용 데모로만 유지하고, 운영 환경에서는 일회용 code 또는 HttpOnly cookie를 별도 검토합니다.
- 비밀번호 재설정 API는 이번 범위에서 동일한 202 응답과 메일 발송 위임까지만 다룹니다. reset link를 실제 재설정 권한으로 설명하지 않습니다.

## 5. 목표 패키지 구조

```text
com.andi.rest_crud
├── common
│   ├── config
│   └── error
├── user
│   ├── domain
│   └── repository
├── auth
│   ├── controller
│   ├── dto
│   ├── exception
│   ├── security
│   └── service
├── oauth
│   ├── dto
│   ├── exception
│   ├── model
│   ├── security
│   └── service
├── recovery
│   ├── controller
│   ├── dto
│   ├── mail
│   └── service
└── post
    ├── controller
    ├── domain
    ├── dto
    ├── exception
    ├── repository
    └── service
```

`common`에는 여러 기능이 함께 사용하는 HTTP 오류 계약과 애플리케이션 조립 설정만 둡니다.
사용자 Entity와 Repository는 local auth, OAuth, recovery가 함께 사용하므로 독립된 `user` 도메인에 둡니다.

## 6. 실행 계획

1. 05 공통 기준 복원
   - 최신 `04-answer`의 동작을 두 05 개발 브랜치의 출발점으로 사용합니다.
   - JWT, Validation, 예외 응답, email 정규화, 중복 경쟁, 환경변수 계약을 먼저 보존합니다.
   - 확인: 기존 60개 테스트가 두 작업 트리에서 통과합니다.
2. 패키지 구조 이동
   - 공통 코드와 기능 도메인을 목표 구조로 이동하고 테스트 패키지도 같은 기준으로 맞춥니다.
   - 이동 단계에서는 기능 동작을 바꾸지 않습니다.
   - 확인: 이동 전후 테스트 수와 결과가 같고 기존 기술 계층 최상위 패키지가 남지 않습니다.
3. OAuth2 흐름 갱신
   - provider와 providerId를 외부 계정 식별자로 사용하고 검증된 email만 받습니다.
   - email을 공통 규칙으로 정규화하고 `(auth_provider, provider_id)` 저장 유일성을 보장합니다.
   - 기존 local 계정 자동 연결과 기존 OAuth 사용자의 email 자동 변경을 막습니다.
   - 성공 token은 query에 넣지 않고, 실패 redirect에는 내부 예외 내용을 노출하지 않습니다.
   - 확인: 신규/기존/충돌/검증 실패/redirect 단위 테스트가 외부 Google 연결 없이 통과합니다.
4. SMTP·계정 복구 흐름 갱신
   - `RecoveryMailSender` 포트를 통해 Service와 JavaMailSender 구현을 분리합니다.
   - `SPRING_MAIL_*` 환경변수, STARTTLS, timeout, 발신자 설정을 명시합니다.
   - 존재하지 않는 email도 같은 HTTP 응답을 반환하고 sender를 호출하지 않습니다.
   - 실제 SMTP 없이 수신자, 제목, 본문, reset link 위임을 검증합니다.
   - 확인: fake 또는 mock sender 테스트가 통과하고 테스트 중 네트워크 연결이 발생하지 않습니다.
5. 실습/정답 차이 복원
   - 두 브랜치에 같은 테스트와 구조를 두고 05 핵심 구현부만 TODO와 정답으로 나눕니다.
   - 확인: starter는 핵심 TODO 테스트에서 의도적으로 실패하고 answer는 전체 테스트가 통과합니다.
6. 문서와 설정 동기화
   - README와 표준 문서 네 개의 파일 경로, API, 환경변수, 수동/자동 검증 범위를 실제 코드와 맞춥니다.
   - 확인: 잘못된 기존 패키지 경로와 혼용된 mail 환경변수 이름이 검색되지 않습니다.

## 7. 예상 변경 파일

- 토픽 레포 `src/main/kotlin/com/andi/rest_crud/**`
- 토픽 레포 `src/test/kotlin/com/andi/rest_crud/**`
- 토픽 레포 `src/main/resources/application.yaml`
- 토픽 레포 `src/test/resources/application.yaml`
- 토픽 레포 `.env.example`, `.gitignore`, `build.gradle.kts`
- 토픽 레포 `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`
- 중앙 레포의 이 계획서

## 8. 검증

```bash
./gradlew cleanTest test
git diff --check
git status --short
```

추가 구조·보안 검색:

```bash
rg --files src/main/kotlin/com/andi/rest_crud
rg -n 'com\.andi\.rest_crud\.(controller|domain|dto|exception|repository|security|service)' src README.md docs
rg -n '\b(MAIL_HOST|MAIL_PORT|MAIL_USERNAME|MAIL_PASSWORD)\b|demo-password|demo-google-client-secret' .
```

완료 조건:

- 두 05 브랜치가 최신 04의 인증·인가 테스트 계약을 보존합니다.
- 최상위 패키지는 `common`, `user`, `auth`, `oauth`, `recovery`, `post`로 정리됩니다.
- answer는 외부 Google·SMTP 연결 없이 전체 테스트가 통과합니다.
- starter는 제공된 05 테스트가 TODO 위치를 정확히 가리키며 의도된 실패 상태입니다.
- 실제 secret, SMTP password, OAuth client secret이 저장소에 추가되지 않습니다.
