# 05. 외부 인증과 SMTP 계정 복구 입문

## 시퀀스 목적

이번 시퀀스는 `04-answer`의 자체 로그인 + JWT 흐름 위에
아래 두 확장을 함께 붙이는 단계입니다.

1. `Google OAuth2` 로그인
2. `SMTP` 기반 비밀번호 재설정 메일 요청

핵심은 기술을 깊게 파는 것이 아니라,
"인증은 로그인에서 끝나지 않고 외부 로그인과 계정 복구로 확장된다"는 감각을 학생이 잡게 만드는 것입니다.

## 왜 이번 시퀀스에서 둘 다 다루는가

원래 외부 인증과 이메일 인증은 분리해서 다루기 좋은 주제입니다.
하지만 현재 실습 목적상,

- `Google OAuth2`는 외부 로그인 확장 흐름
- `SMTP`는 계정 복구 메일 발송 흐름

을 한 번에 묶어 보면 "인증 관련 확장 기능"을 한 장에서 보기 좋습니다.

다만 범위는 반드시 작게 유지합니다.

## 시작 기준

이번 시퀀스는 반드시 `04-answer`를 기준으로 시작합니다.

이미 존재한다고 가정하는 것:

- 회원가입
- 로그인
- JWT 발급
- `/auth/me`
- 기본 Validation / 예외 응답

## 학생이 완성해야 하는 최종 상태

학생은 이 시퀀스를 마친 뒤 아래를 할 수 있어야 합니다.

### OAuth2 파트

1. 자체 로그인과 Google 로그인 차이를 설명할 수 있다.
2. Google 사용자 정보를 읽는 흐름을 설명할 수 있다.
3. 기존 사용자 / 신규 사용자 분기를 설명할 수 있다.
4. 외부 로그인 결과를 우리 서비스 사용자와 연결할 수 있다.

### SMTP 파트

1. SMTP가 왜 계정 복구 메일 발송에 쓰이는지 설명할 수 있다.
2. email 기준 비밀번호 재설정 메일 요청 흐름을 설명할 수 있다.
3. reset 링크를 왜 만들어 메일에 넣는지 설명할 수 있다.
4. 이번 시퀀스가 실제 비밀번호 변경 완료까지는 다루지 않는다는 점을 설명할 수 있다.

## 현재 도메인에서의 SMTP 범위

현재 레포는 로그인 아이디가 곧 `email`입니다.
그래서 이번 시퀀스의 SMTP 파트는 `아이디 찾기`보다
`비밀번호 재설정 메일 요청`을 대표 흐름으로 다룹니다.

즉 이번 범위는 아래입니다.

- email 입력
- 사용자 확인
- reset 링크 생성
- SMTP 메일 발송

아래는 이번에 다루지 않습니다.

- 실제 비밀번호 변경 완료
- reset token 저장소
- 토큰 만료 / 재전송 정책
- 아이디 찾기 전용 추가 도메인

## 학생 구현 순서

이번 시퀀스의 구현 순서는 아래로 고정합니다.

1. Google provider 설정을 확인한다.
2. 로그인 성공 후 Google 사용자 정보를 읽는다.
3. 기존 OAuth 사용자 / 기존 로컬 사용자 / 신규 사용자를 분기한다.
4. 우리 서비스 사용자와 연결한다.
5. OAuth 성공 응답을 정리한다.
6. SMTP 설정을 확인한다.
7. 비밀번호 재설정 메일 요청 API를 연결한다.
8. reset 링크를 만들고 메일 발송 Service를 연결한다.

## TODO를 넣을 파일

OAuth2 핵심 TODO:

- `CustomOAuthUserService.kt`
- `OAuthLoginSuccessHandler.kt`
- `OAuthAccountService.kt`

SMTP 핵심 TODO:

- `AccountRecoveryService.kt`
- `SmtpRecoveryMailSender.kt`

## 미리 제공하는 것

- `04-answer` 기반 로그인/JWT 구조
- Google OAuth2 client 설정 자리
- SMTP 설정 자리
- `User.authProvider`, `User.providerId`
- `AccountRecoveryController`
- `PasswordResetMailRequest`
- `auth-demo.html`

학생은 핵심 흐름만 직접 구현합니다.

## 문서와 브랜치 기준

이번 시퀀스는 아래 브랜치 구조를 유지합니다.

- `05-implementation`
- `05-answer`
- 서브모듈 `main`

각 브랜치의 `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/answer-guide.md`, `docs/checklist.md`, `docs/assets.md`는
반드시 이번 05 시퀀스 내용으로 교체되어야 합니다.

## 구현 제약

- OAuth2와 SMTP는 넣되, 둘 다 깊게 확장하지 않는다.
- Google provider 하나만 사용한다.
- SMTP는 비밀번호 재설정 메일 요청까지만 다룬다.
- 실제 비밀번호 변경 완료까지는 가지 않는다.
- refresh token, 계정 연결 고급 정책, SMTP 고급 보안 정책까지 확장하지 않는다.
- 테스트는 본격 확장이 아니라 실행 가능 검증 수준으로 유지한다.

## 산출물

- `README.md`
- `docs/theory.md`
- `docs/implementation.md`
- `docs/answer-guide.md`
- `docs/checklist.md`
- `docs/assets.md`
- `05-implementation` starter 코드
- `05-answer` 정답 코드
- 서브모듈 `main` 안내 문서 업데이트
- 루트 `README.md` 상태 반영
