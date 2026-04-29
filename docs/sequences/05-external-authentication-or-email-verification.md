# 05. 외부 인증과 SMTP 계정 복구 입문

## 시퀀스 목적

이번 시퀀스는 `04-answer`의 자체 로그인 + JWT 흐름 위에
아래 두 확장을 함께 붙이는 단계입니다.

1. `Google OAuth2` 로그인
2. `SMTP` 기반 비밀번호 재설정 메일 요청

핵심은 기술을 깊게 파는 것이 아니라,
"인증은 로그인에서 끝나지 않고 외부 로그인과 계정 복구로 확장된다"는 감각을
학생이 코드와 문서로 함께 잡게 만드는 것입니다.

## 시작 기준

이번 시퀀스는 반드시 `04-answer`를 기준으로 시작합니다.

이미 존재한다고 가정하는 것:

- 회원가입
- 로그인
- JWT 발급
- `/auth/me`
- 기본 Validation / 예외 응답

## 이번 시퀀스에서 다시 설명해야 하는 기초 개념

이번 05 시퀀스는 `04` 위에서 이어지지만,
학생이 반드시 다시 이해해야 하는 기초 개념이 있습니다.

- `OAuth2`
  외부 제공자가 인증을 대신 처리하는 로그인 흐름
- `provider`
  어떤 외부 로그인 제공자인지 구분하는 값
- `providerId`
  외부 제공자가 사용자를 식별하는 고유 값
- `SMTP`
  메일을 전송할 때 쓰는 프로토콜
- `password reset link`
  사용자가 메일을 통해 비밀번호 재설정 흐름으로 들어가게 하는 링크
- `JWT 연결`
  외부 로그인 성공 이후에도 우리 서비스는 결국 자체 토큰으로 다음 요청을 구분한다는 점

즉, `04`에서 JWT를 배웠더라도,
`05`에서는 "외부 로그인 성공 후에도 왜 우리 서비스 토큰이 다시 필요한가"를 다시 짚어야 합니다.

## 현재 코드 흐름에서 어디를 봐야 하는가

이번 시퀀스는 기술 이름만 이해하면 충분하지 않습니다.
현재 레포에서 어떤 파일이 어떤 역할을 하는지 같이 봐야 합니다.

1. `CustomOAuthUserService.kt`
   Google 응답에서 `email`, `sub`를 읽는 시작점
2. `OAuthLoginSuccessHandler.kt`
   외부 로그인 성공 후 우리 서비스 흐름으로 다시 연결하는 지점
3. `OAuthAccountService.kt`
   기존 사용자 연결 / 신규 사용자 생성 정책이 모이는 핵심 서비스
4. `AccountRecoveryService.kt`
   비밀번호 재설정 메일 요청을 받아 reset 링크를 만드는 서비스
5. `SmtpRecoveryMailSender.kt`
   실제 SMTP 발송을 담당하는 구현체

짧게 말하면 이번 시퀀스는

- `외부 로그인 성공 -> 우리 사용자 연결 -> 우리 JWT 발급`
- `비밀번호 재설정 요청 -> reset 링크 생성 -> SMTP 메일 발송`

두 줄기의 흐름을 같이 보는 단계입니다.

## 학생이 완성해야 하는 최종 상태

학생은 이 시퀀스를 마친 뒤 아래를 할 수 있어야 합니다.

### OAuth2 파트

1. 자체 로그인과 Google 로그인 차이를 설명할 수 있다.
2. Google 사용자 정보를 읽는 흐름을 설명할 수 있다.
3. 기존 사용자 / 신규 사용자 분기를 설명할 수 있다.
4. 외부 로그인 결과를 우리 서비스 사용자와 연결할 수 있다.
5. Google이 인증을 대신 해줘도 왜 우리 서비스 JWT가 다시 필요한지 설명할 수 있다.

### SMTP 파트

1. SMTP가 왜 계정 복구 메일 발송에 쓰이는지 설명할 수 있다.
2. email 기준 비밀번호 재설정 메일 요청 흐름을 설명할 수 있다.
3. reset 링크를 왜 만들어 메일에 넣는지 설명할 수 있다.
4. reset 링크 안의 token이 왜 민감한 값인지 설명할 수 있다.
5. 이번 시퀀스가 실제 비밀번호 변경 완료까지는 다루지 않는다는 점을 설명할 수 있다.

## 왜 이번 시퀀스에서 둘 다 다루는가

원래 외부 인증과 이메일 인증은 분리해서 다루기 좋은 주제입니다.
하지만 현재 실습 목적상,

- `Google OAuth2`는 외부 로그인 확장 흐름
- `SMTP`는 계정 복구 메일 발송 흐름

을 한 번에 묶어 보면 "인증 관련 확장 기능"을 한 장에서 보기 좋습니다.

다만 범위는 반드시 작게 유지합니다.

이번 시퀀스의 핵심은 기술 자체를 많이 붙이는 것이 아니라,
아래 두 질문에 답할 수 있게 만드는 것입니다.

1. 외부 로그인 사용자를 우리 DB 사용자와 어떻게 안전하게 연결할 것인가
2. 계정 복구 메일 요청은 왜 보안 관점에서 조심해야 하는가

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

## 이번 시퀀스의 실무 확장 개념

### 1. 계정 연결 정책

Google 로그인은 성공했지만, 우리 서비스 입장에서는
"이 사용자를 기존 사용자와 연결할 것인가, 신규 사용자로 볼 것인가"를 다시 판단해야 합니다.

같은 email의 로컬 계정이 이미 있는데도 무조건 신규 사용자를 만들면,
한 사람에게 계정이 여러 개 생길 수 있습니다.

이번 시퀀스 문서와 코드는 반드시 아래 분기를 설명해야 합니다.

1. 이미 같은 `provider + providerId` 사용자가 있는가
2. 그건 없지만 같은 `email` 사용자가 있는가
3. 둘 다 없으면 신규 사용자로 볼 수 있는가

### 2. 계정 복구 보안 관점

비밀번호 재설정 메일 요청은 단순 편의 기능처럼 보여도,
아래 보안 포인트가 같이 붙습니다.

- 존재하지 않는 email에 대해 응답을 다르게 주면 계정 존재 여부가 노출될 수 있다.
- reset 링크에 들어가는 token은 민감한 값이다.
- reset 링크를 로그, 화면, 예외 메시지에 쉽게 노출하면 안 된다.

이번 시퀀스는 전체 복구 시스템을 완성하지 않더라도,
이 보안 감각은 문서에 반드시 같이 남깁니다.

## 문제 상황과 해결 방향을 코드로 보기

### 문제 1. OAuth 로그인 성공 때마다 새 사용자를 만들면 어떤 문제가 생기는가

```kotlin
fun handleOAuthLogin(profile: OAuthUserProfile): OAuthLoginResponse {
    val newUser = userRepository.save(
        User(
            email = profile.email,
            password = passwordEncoder.encode(UUID.randomUUID().toString()),
            authProvider = profile.provider,
            providerId = profile.providerId
        )
    )

    return createSuccessResponse(newUser, true)
}
```

이 코드는 OAuth 로그인 자체는 성공시킬 수 있습니다.
하지만 기존 Google 사용자 재로그인, 기존 로컬 계정 연결, 신규 사용자 생성을 구분하지 못합니다.

### 해결 방향 1. provider 기준과 email 기준을 둘 다 본다

```kotlin
val existingOAuthUser = userRepository.findByAuthProviderAndProviderId(provider, profile.providerId)
    .orElse(null)

if (existingOAuthUser != null) {
    return OAuthLinkResult(userRepository.save(existingOAuthUser), false)
}

val existingEmailUser = userRepository.findByEmail(profile.email).orElse(null)
if (existingEmailUser != null) {
    existingEmailUser.authProvider = provider
    existingEmailUser.providerId = profile.providerId
    return OAuthLinkResult(userRepository.save(existingEmailUser), false)
}
```

이 흐름이면

- 같은 `provider + providerId` 사용자는 재사용하고
- 같은 email의 로컬 사용자는 OAuth 계정으로 연결하고
- 둘 다 없을 때만 신규 생성

이라는 정책을 코드로 설명할 수 있습니다.

### 문제 2. 비밀번호 재설정 요청에서 존재하지 않는 email을 바로 알려주면 어떤 문제가 생기는가

```kotlin
fun requestPasswordReset(email: String) {
    val user = userRepository.findByEmail(email)
        .orElseThrow { IllegalArgumentException("존재하지 않는 사용자입니다.") }

    val resetLink = createResetLink(user.email)
    recoveryMailSender.sendPasswordResetMail(user.email, resetLink)
}
```

이 코드는 개발 중에는 편하지만,
실무에서는 공격자에게 "이 email이 가입돼 있는지"를 알려줄 수 있습니다.

### 해결 방향 2. 존재하지 않는 email은 조용히 종료한다

```kotlin
fun requestPasswordReset(email: String) {
    val user = userRepository.findByEmail(email).orElse(null) ?: return
    val resetLink = createResetLink(user.email)
    recoveryMailSender.sendPasswordResetMail(user.email, resetLink)
}
```

이번 시퀀스는 여기까지만 다룹니다.
실무에서는 여기에 token 저장, 만료, 재사용 방지, 링크 검증까지 추가됩니다.

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

## 구현 제약

- OAuth2와 SMTP는 넣되, 둘 다 깊게 확장하지 않는다.
- Google provider 하나만 사용한다.
- SMTP는 비밀번호 재설정 메일 요청까지만 다룬다.
- 실제 비밀번호 변경 완료까지는 가지 않는다.
- refresh token, 계정 연결 고급 정책, SMTP 고급 보안 정책까지 확장하지 않는다.
- 테스트는 본격 확장이 아니라 실행 가능 검증 수준으로 유지한다.

## 문서에 반드시 남겨야 하는 것

이번 시퀀스 문서에는 아래가 함께 들어가야 합니다.

1. 기초 개념 설명
2. 현재 코드 흐름
3. 문제 상황
4. 문제 코드
5. 왜 운영상 위험한지
6. 해결 코드 예시
7. 이번 시퀀스에서 실제 구현 범위와 설명-only 범위
