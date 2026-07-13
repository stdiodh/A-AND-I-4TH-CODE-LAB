# 05. 외부 인증과 SMTP 계정 복구 입문

## 목표

기존 JWT 인증 흐름 위에 OAuth2 로그인, SMTP 메일 발송, 계정 복구 유스케이스를 작은 단계로 붙입니다.
한 번에 깊게 구현하기보다 외부 연동 결과를 우리 서비스 사용자와 안전하게 연결하는 흐름에 집중합니다.

## 이 시퀀스에서 배우는 것

- Google OAuth2 리다이렉트 흐름
- provider와 providerId로 외부 사용자를 식별하는 방법
- LOCAL 사용자와 OAUTH 사용자의 차이
- 메일 발송 책임을 인터페이스와 구현체로 나누는 방법
- 계정 복구 요청에서 민감한 정보 노출을 피하는 방법
- 외부 계정이 어려울 때 mock 또는 local profile로 흐름을 확인하는 방법

## 시작 브랜치

```bash
git checkout 05-implementation
```

## 실습 전 확인

- 토픽 레포: `spring-boot-db-access-lab`
- 가이드 브랜치: `main`
- 시작 브랜치: `05-implementation`
- 이전 기준: `04-answer`
- 실제 Google client secret, SMTP password는 코드와 문서에 쓰지 않습니다.
- 외부 계정 준비가 어렵다면 mock 또는 local profile 대안으로 흐름을 먼저 확인합니다.

## 단계 구성

05는 하나의 시퀀스지만 내부를 세 단계로 나눕니다.

```text
05-A OAuth2 로그인 흐름
05-B SMTP 메일 발송 흐름
05-C 계정 복구 유스케이스
```

## 05-A. OAuth2 로그인 흐름

### 목표

Google OAuth2 로그인 성공 결과에서 provider, providerId, email을 읽고 우리 서비스 사용자와 연결합니다.
외부 로그인 성공 후에도 우리 서비스 기준의 JWT 또는 사용자 정보 응답이 필요하다는 점을 확인합니다.

### 사전 준비

- `04-answer`의 회원가입, 로그인, JWT 흐름을 이해합니다.
- Google OAuth2 설정값은 환경변수 또는 local profile로 주입합니다.
- 외부 계정 준비가 어렵다면 OAuth 사용자 정보를 mock으로 제공하는 테스트 또는 local profile을 사용합니다.

### 구현할 TODO

1. OAuth2 로그인 시작 URL과 redirect 흐름을 확인합니다.
2. Google 사용자 정보에서 `email`과 provider id를 읽습니다.
3. provider 이름과 providerId를 내부 사용자 식별 기준으로 저장합니다.
4. LOCAL 사용자와 OAUTH 사용자의 차이를 코드에서 드러냅니다.
5. provider가 검증한 이메일인지 확인하고, 기존 로컬 계정의 자동 연결 위험을 설명합니다.
6. OAuth2 성공 후 자체 JWT를 URL query가 아닌 fragment로 전달하는 데모 흐름을 확인합니다.

### 실행 확인 방법

- 브라우저에서 OAuth2 로그인 시작 URL로 이동합니다.
- 성공 후 redirect URL에 필요한 결과가 붙는지 확인합니다.
- 외부 계정이 없다면 mock profile로 `OAuthAccountService` 흐름을 먼저 확인합니다.

### 실패 케이스

- OAuth 응답에 email이 없습니다.
- providerId를 읽지 못합니다.
- 이미 같은 email을 가진 LOCAL 사용자가 있습니다.
- OAuth2 성공은 했지만 우리 서비스 JWT가 발급되지 않습니다.
- JWT를 query parameter에 넣어 서버 로그, 방문 기록, referrer에 남깁니다. 데모는 fragment를 사용하고 운영에서는 일회용 code 또는 HttpOnly cookie를 검토합니다.
- 검증되지 않은 이메일이나 명시적 동의 없이 기존 로컬 계정을 자동 연결합니다.

### 테스트 방법

```bash
./gradlew test
```

테스트에서는 외부 Google 서버에 직접 의존하지 않습니다.
OAuth profile 값을 fake 객체나 service 단위 테스트로 넣어 내부 사용자 연결 흐름을 확인합니다.

### 자주 발생하는 문제

- 외부 로그인 성공만으로 우리 서비스 인증이 끝났다고 생각합니다.
- providerId 대신 email만으로 외부 사용자를 구분하려고 합니다.
- 실제 client secret을 코드, README, 테스트에 적습니다.
- OAuth2 설정 실패와 우리 서비스 사용자 연결 실패를 같은 문제로 봅니다.

### 완료 기준

- provider와 providerId가 왜 필요한지 설명할 수 있습니다.
- LOCAL 사용자와 OAUTH 사용자의 차이를 설명할 수 있습니다.
- OAuth2 성공 후 우리 서비스 JWT 또는 사용자 정보 흐름으로 이어집니다.
- 외부 계정 없이도 service 단위 흐름을 테스트할 수 있습니다.

## 05-B. SMTP 메일 발송 흐름

### 목표

계정 복구에서 메일 발송 책임을 분리합니다.
비즈니스 흐름은 `RecoveryMailSender` 인터페이스에 의존하고, 실제 SMTP 발송은 `SmtpRecoveryMailSender` 구현체가 담당하게 합니다.

### 사전 준비

- 메일 발송에 필요한 host, port, username, password를 환경변수로 준비합니다.
- 실제 SMTP password는 코드와 문서에 쓰지 않습니다.
- 실습 중에는 local profile 또는 fake sender로 발송 흐름만 확인할 수 있습니다.

### 구현할 TODO

1. `RecoveryMailSender` 인터페이스를 확인합니다.
2. `SmtpRecoveryMailSender` 구현체에서 메일 제목, 본문, 수신자를 구성합니다.
3. SMTP 설정을 환경변수 기반으로 연결합니다.
4. 실제 비밀번호가 로그나 응답에 노출되지 않도록 확인합니다.
5. 외부 SMTP가 어렵다면 fake sender로 service 테스트를 먼저 작성합니다.

### 실행 확인 방법

- local profile에서 fake sender 또는 테스트 SMTP 값을 사용합니다.
- 실제 SMTP를 사용할 때는 환경변수만 설정하고 코드는 바꾸지 않습니다.
- 로그에는 발송 성공/실패 흐름만 남기고 password는 남기지 않습니다.

### 실패 케이스

- SMTP 인증 실패
- host 또는 port 설정 오류
- 수신자 email 형식 오류
- 메일 발송 예외가 계정 복구 API 응답을 과도하게 노출함

### 테스트 방법

```bash
./gradlew test
```

테스트에서는 SMTP 서버에 직접 의존하지 않습니다.
`RecoveryMailSender`를 fake 또는 mock으로 대체해 service가 어떤 메일 발송 요청을 만드는지 확인합니다.

### 자주 발생하는 문제

- `AccountRecoveryService`에서 JavaMailSender를 직접 사용합니다.
- SMTP password를 application.yaml이나 문서에 평문으로 적습니다.
- 메일 발송 실패를 사용자에게 너무 자세히 알려줍니다.
- 외부 SMTP 연결이 안 된 것을 계정 복구 로직 실패로 오해합니다.

### 완료 기준

- 메일 발송 책임이 인터페이스와 구현체로 분리되었습니다.
- SMTP 설정은 환경변수 기반입니다.
- 테스트는 실제 SMTP 서버 없이 통과합니다.
- 민감정보가 코드, 문서, 로그에 노출되지 않습니다.

## 05-C. 계정 복구 유스케이스

### 목표

비밀번호 재설정 요청에서 임시 식별자를 포함한 reset link를 만들고 메일 발송 책임으로 넘기는 흐름을 작게 설계합니다.
토큰 저장, 만료 검증, 실제 비밀번호 변경, 재사용 차단은 이번 답안에 포함되지 않은 후속 보안 구현으로 구분합니다.

### 사전 준비

- 05-B의 `RecoveryMailSender` 흐름이 분리되어 있어야 합니다.
- 복구 링크 base URL은 환경변수로 주입합니다.
- 존재하지 않는 email 요청도 안전하게 응답해야 합니다.

### 구현할 TODO

1. 비밀번호 재설정 요청 DTO를 확인합니다.
2. 요청 email로 사용자를 조회합니다.
3. 존재하지 않는 email이어도 계정 존재 여부를 노출하지 않습니다.
4. 복구 토큰을 생성합니다.
5. 임시 식별자를 포함한 reset link를 만들고 메일 발송 요청으로 넘깁니다.
6. 현재 구현만으로는 재설정을 완료할 수 없는 이유를 설명합니다.
7. 후속 구현에 필요한 토큰 저장, 만료, 일회성 사용 기준을 정리합니다.

### 실행 확인 방법

- 비밀번호 재설정 요청 API를 호출합니다.
- 존재하는 email과 존재하지 않는 email이 같은 형태의 응답을 주는지 확인합니다.
- 테스트 또는 local profile로 reset link 생성 결과를 확인합니다.

### 실패 케이스

- 존재하지 않는 email 요청
- 만료된 토큰, 이미 사용한 토큰, token/email 불일치, 새 password validation은 후속 구현에서 다룰 실패 케이스입니다.

### 테스트 방법

```bash
./gradlew test
```

현재 테스트는 애플리케이션 context를 확인합니다. reset link와 sender 호출은 local fake sender 또는 후속 단위 테스트로 확인할 수 있습니다.
외부 SMTP나 실제 Google 계정은 테스트 필수 조건이 아닙니다.

### 자주 발생하는 문제

- 존재하지 않는 email을 바로 알려줍니다.
- 임시 UUID가 URL에 있다는 이유만으로 안전한 reset token 저장소가 완성됐다고 생각합니다.
- token, email, password 같은 민감한 값을 로그에 남깁니다.
- 계정 복구와 로그인 인증을 같은 책임으로 섞습니다.

### 완료 기준

- 복구 요청 API가 계정 존재 여부를 노출하지 않습니다.
- 현재 reset link 생성 범위와 후속 토큰 저장·만료·재사용 차단 범위를 구분합니다.
- 메일 발송은 `RecoveryMailSender`를 통해 요청됩니다.
- `./gradlew test`가 통과합니다.

## 필요한 환경변수

실제 값은 로컬 환경이나 GitHub Secrets에만 둡니다.
문서와 코드에는 아래 이름만 사용합니다.

```text
GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET
SPRING_MAIL_HOST
SPRING_MAIL_PORT
SPRING_MAIL_USERNAME
SPRING_MAIL_PASSWORD
APP_FRONTEND_URL
APP_PASSWORD_RESET_URL
JWT_SECRET
```

## 실행 방법

```bash
docker compose up -d
./gradlew bootRun
```

외부 계정 설정이 준비되지 않았다면 `./gradlew test`와 local profile 대안으로 내부 흐름을 먼저 확인합니다.

## 테스트 방법

```bash
./gradlew test
```

테스트가 확인하는 것:

- 현재 자동 테스트는 애플리케이션 context를 확인합니다.
- OAuth service, 메일 발송 위임, 토큰 만료와 재사용 차단은 구현을 확장할 때 별도 단위 테스트가 필요합니다.
- 실제 OAuth와 SMTP 흐름은 외부 계정 또는 명시적인 test double 없이 검증됐다고 판단하지 않습니다.

실패하면 먼저 볼 것:

- 실제 Google client secret이나 SMTP password가 테스트에 필요하도록 만들지 않았는지 확인합니다.
- mock/local profile이 활성화되어 외부 네트워크 없이 테스트가 실행되는지 봅니다.
- 토큰 만료를 구현한다면 현재 시간 기준과 만료 시간 계산을 먼저 확인합니다.

완료 기준:

- context 테스트가 외부 연동 없이 통과합니다.
- OAuth, SMTP, reset link는 자동 테스트와 수동 확인 범위를 구분해 설명할 수 있습니다.

## 확인할 API 또는 화면

- Swagger: `http://localhost:8080/swagger`
- OAuth2 로그인 시작 URL
- OAuth2 성공 후 URL fragment 기반 JWT 데모 흐름과 운영 환경의 안전한 교환 방식 차이
- 비밀번호 재설정 메일 요청 API
- reset link 생성 흐름
- 메일 발송 성공/실패 로그

## 완료 기준

- 05-A OAuth2 사용자 연결 흐름을 설명할 수 있습니다.
- 05-B 메일 발송 책임이 분리되었습니다.
- 05-C reset link 생성 범위와 아직 구현하지 않은 토큰 저장, 만료, 실제 재설정 범위를 설명할 수 있습니다.
- 외부 계정 없이도 mock/local profile로 핵심 흐름을 확인할 수 있습니다.
- 민감한 값이 코드나 문서에 직접 노출되지 않았습니다.
- `./gradlew test`가 통과합니다.

## 정답과 비교하는 방법

막혔거나 실습을 마친 뒤에만 참고 정답과 비교합니다.

```bash
git diff 05-implementation..05-answer
```

## 다음 시퀀스

다음은 `06. 테스트와 검증`입니다.
기존 Service 흐름을 테스트로 검증합니다.
