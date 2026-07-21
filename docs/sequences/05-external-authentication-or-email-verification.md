# 05. 외부 인증과 SMTP 계정 복구

## 목표

최신 `04-answer`의 JWT 인증·인가 흐름 위에 Google OAuth2 로그인과 SMTP 기반 비밀번호 재설정을 연결합니다.
학생은 외부 profile을 내부 계정과 안전하게 연결하고, reset token의 수명 주기와 트랜잭션 이후 비동기 메일 발송 경계를 테스트로 확인합니다.

## 브랜치와 문서

- 토픽 레포: `spring-boot-db-access-lab`
- 가이드: `main`
- 학생 시작점: `05-implementation`
- 참고 정답: `05-answer`
- 토픽 상세 문서: `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`

```bash
git checkout 05-implementation
```

실제 Google client secret과 SMTP password는 저장소에 기록하지 않고 로컬 `.env`에만 둡니다.

## 직접 구현할 범위

`05-implementation`에서 수정할 범위는 **5개 파일의 TODO 6개**입니다.
표에 없는 production 파일은 제공된 연결 계약이므로 먼저 테스트와 호출 흐름만 확인합니다.

| 순서 | 파일 | 메서드 | 확인할 흐름 |
|---:|---|---|---|
| 1 | `oauth/security/CustomOAuthUserService.kt` | `normalizePrincipal` | 검증된 OAuth profile 정규화 |
| 2 | `oauth/service/OAuthAccountService.kt` | `handleOAuthLogin` | 내부 계정 연결과 JWT 발급 |
| 3 | `oauth/security/OAuthLoginHandlers.kt` | `onAuthenticationSuccess` | 안전한 성공 redirect |
| 4-A | `recovery/service/AccountRecoveryService.kt` | `requestPasswordReset` | reset token 발급·회전·cooldown |
| 4-B | `recovery/service/AccountRecoveryService.kt` | `confirmPasswordReset` | token 확정·비밀번호 변경·단일 사용 |
| 5 | `recovery/mail/SmtpRecoveryMailSender.kt` | `sendPasswordResetMail` | SMTP 메시지 조립·발송 |

실습은 다음 순서를 유지합니다.

```text
OAuth profile -> account -> redirect
-> recovery request -> recovery confirm
-> AFTER_COMMIT -> bounded async executor -> SMTP
```

`PasswordResetTokenCodec`, token entity·repository, controller, `RecoveryMailDispatch`, Security 설정과 HTML 화면은 제공된 scaffold입니다.
TODO 구현 중 기대 입력·출력과 실행 순서를 확인하는 용도로 읽습니다.

## 구현 계약

### OAuth2

- Google의 `email_verified=true`인 profile만 받습니다.
- 외부 사용자는 `provider + providerId`로 식별합니다.
- 같은 email의 LOCAL 계정이나 다른 외부 계정을 자동 연결하지 않습니다.
- 성공 redirect의 JWT는 query가 아니라 fragment로 전달하고, HTML 실습 화면이 메모리로 읽은 즉시 URL에서 제거합니다.
- 실패 응답에는 token, email, provider 원문 오류 같은 내부 정보를 노출하지 않습니다.

### 계정 복구

- 요청: `POST /account-recovery/password-reset`
- 확정: `POST /account-recovery/password-reset/confirm`
- raw token은 `SecureRandom` 32-byte를 Base64URL without padding으로 인코딩합니다.
- DB에는 raw token이 아니라 SHA-256 hash만 저장합니다.
- 사용자당 token 행 하나를 회전하므로 재발급하면 이전 token이 무효가 됩니다.
- 기본 TTL은 15분, LOCAL 사용자별 재요청 cooldown은 1분입니다.
- 확정 시 BCrypt 비밀번호 변경과 token의 `usedAt` 기록을 같은 트랜잭션에서 처리합니다.
- 요청은 계정 존재, OAuth 계정, SMTP 결과를 구분하지 않고 유효한 형식이면 `Cache-Control: no-store`와 202를 반환합니다.
- 확정 성공은 `Cache-Control: no-store`와 204입니다. 만료·재사용·회전·존재하지 않는 token은 같은 400 `INVALID_PASSWORD_RESET_TOKEN`으로 처리합니다.

### 메일 발송

- token 저장 트랜잭션이 commit된 뒤 `AFTER_COMMIT` event가 실행됩니다.
- `RecoveryMailDispatch`는 크기가 제한된 executor에서 SMTP를 비동기로 호출하므로 HTTP 요청은 발송 완료를 기다리지 않습니다.
- recipient, raw token, reset link, SMTP 내부 오류를 공개 응답이나 로그에 남기지 않습니다.

## 로컬 실행

`.env.example`을 복사하고 로컬 값만 수정합니다.

```bash
test -f .env || cp .env.example .env
docker compose config --quiet
docker compose up -d --wait --wait-timeout 120
./gradlew bootRun
```

기본 compose는 MySQL과 Mailpit을 실행합니다.
SMTP는 `localhost:1025`, Mailpit 화면은 `http://localhost:8025`이며 인증과 TLS 없이 로컬 메일·reset link를 확인할 수 있습니다.

주요 환경변수:

- OAuth: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`
- redirect: `APP_FRONTEND_URL`, `APP_PASSWORD_RESET_URL`
- reset 정책: `APP_PASSWORD_RESET_TOKEN_TTL=PT15M`, `APP_PASSWORD_RESET_RESEND_COOLDOWN=PT1M`
- 발신자: `APP_RECOVERY_MAIL_FROM`
- SMTP: `SPRING_MAIL_HOST`, `SPRING_MAIL_PORT`, `SPRING_MAIL_USERNAME`, `SPRING_MAIL_PASSWORD`
- SMTP 옵션: `SPRING_MAIL_PROPERTIES_MAIL_SMTP_*`
- 기존 설정: `DB_*`, `JWT_*`

확인 위치:

- 인증 실습 화면: `http://localhost:8080/auth-practice/`
- OAuth 시작: `http://localhost:8080/oauth2/authorization/google`
- Google callback: `http://localhost:8080/login/oauth2/code/google`
- Mailpit: `http://localhost:8025`
- Swagger: `http://localhost:8080/swagger`

## 자동 테스트와 증거

자동 테스트는 Google과 SMTP 외부 네트워크를 사용하지 않습니다.
OAuth profile, mail sender와 JavaMailSender 경계는 mock 또는 fake로 대체하고 내부 정책과 최신 04 회귀를 확인합니다.

제공된 scaffold gate는 TODO 구현 전에도 통과해야 합니다.

```bash
./gradlew test \
  --tests '*PasswordResetTokenCodecTest' \
  --tests '*PasswordResetTokenRepositoryTest' \
  --tests '*RecoveryMailDispatchTest' \
  --tests '*RecoveryMailEventIntegrationTest' \
  --tests '*AccountRecoveryController*Test' \
  --tests '*AuthPracticePageIntegrationTest'
```

초기 `05-implementation`에서 전체 테스트를 실행하면 104개 중 TODO와 연결된 24개 실패가 정상입니다.
설정·컴파일 실패나 그 밖의 실패를 의도된 starter 상태로 취급하면 안 됩니다.

모든 TODO를 완성한 starter와 `05-answer`의 완료 gate:

```bash
rg -n 'TODO\(' src/main/kotlin
./gradlew test
node --check src/main/resources/static/auth-practice/app.js
git diff --check
```

- TODO 검색: 0건
- 전체 테스트: 104/104 통과
- JavaScript 문법과 diff 검사: 통과

자동 테스트의 증거 범위는 profile 검증·계정 연결·redirect, recovery 202/204, token hash·회전·TTL·단일 사용, cooldown, AFTER_COMMIT bounded async와 SMTP 메시지 조립입니다.

## 실제 외부 연동 확인

실제 Google consent·callback과 Gmail 인증·수신은 자동 테스트와 별도의 수동 E2E입니다.

1. Google console에 `http://localhost:8080/login/oauth2/code/google`을 callback URI로 등록합니다.
2. 유효한 Google credential을 로컬 `.env`에 넣고 로그인·redirect·`/auth/me` 흐름을 확인합니다.
3. Gmail을 사용할 때는 SMTP app password, TLS와 허용된 발신자를 로컬 환경변수로 override합니다.
4. 복구 요청이 즉시 202를 반환하고 메일이 비동기로 도착하는지 확인합니다.
5. reset 성공 204, 같은 token 재사용과 만료·회전 token의 동일한 공개 실패를 확인합니다.
6. credential, email, token, reset link와 SMTP 내부 오류가 로그에 남지 않는지 확인합니다.

외부 credential이 없을 때는 Mailpit과 자동 테스트까지가 로컬 실습 증거이며, 실제 Google·Gmail 성공으로 기록하지 않습니다.

## 완료 기준

- 5개 파일의 TODO 6개를 정해진 순서로 구현했습니다.
- OAuth identity와 자동 연결 금지, 안전한 redirect 경계를 설명할 수 있습니다.
- raw token과 DB hash, 15분 TTL, 사용자별 회전, 1분 cooldown과 단일 사용을 확인했습니다.
- BCrypt 변경과 `usedAt` 처리가 같은 트랜잭션에 있습니다.
- recovery 202/204와 일반화된 실패 응답을 확인했습니다.
- AFTER_COMMIT·bounded async SMTP가 HTTP 응답과 분리되어 있습니다.
- scaffold gate와 최종 104/104 테스트 결과를 구분합니다.
- 실제 Google·Gmail 수동 E2E 여부를 자동 테스트와 구분해 기록합니다.

## 정답과 비교

실습을 마친 뒤에만 참고 정답과 비교합니다.

```bash
git diff 05-implementation..05-answer
```

## 다음 시퀀스

다음은 `06. 테스트와 검증`입니다.
05에서 만든 정상·실패 계약을 더 작은 테스트 단위와 회귀 증거로 정리합니다.
