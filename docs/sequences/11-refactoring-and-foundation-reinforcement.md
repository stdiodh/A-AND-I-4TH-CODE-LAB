# 11. 리팩토링과 기초 보강

## 이 시퀀스의 목적

이번 시퀀스는 새 기능을 붙이는 단계가 아닙니다.  
이미 만든 기능을 다시 읽고, 더 설명하기 쉽고 더 바꾸기 쉬운 구조로 다듬는 단계입니다.

학생은 이번 단계에서 아래 흐름을 이해해야 합니다.

1. 지금까지 만든 코드를 다시 읽는다.
2. 책임이 섞인 지점을 찾는다.
3. 서비스 레벨 검증과 예외 응답을 보강한다.
4. 테스트를 추가해 리팩토링 안정성을 확인한다.
5. README와 문서를 다시 정리한다.

## 이전 시퀀스와의 연결

- 시작 기준: `10-answer`
- 시작 레포: `spring-boot-deployment-runtime-lab`
- 실제 11 실습 레포: `spring-boot-refactoring-foundation-lab`

10 시퀀스까지는 기능, 배포, 자동화를 하나씩 쌓았습니다.  
11 시퀀스에서는 그 결과물을 다시 읽으면서, 다음 변경이 들어와도 버티는 구조가 무엇인지 살펴봅니다.

## 기초적으로 이해해야 할 것

- 리팩토링은 기능을 바꾸지 않고 구조를 개선하는 작업입니다.
- 긴 메서드가 항상 나쁜 것은 아니지만, 여러 책임이 섞이면 변경 비용이 빠르게 커집니다.
- 검증, 예외 처리, 테스트는 따로 움직이지 않습니다. 한 부분을 바꾸면 나머지도 같이 영향을 받습니다.
- 문서 보강도 구조 개선의 일부입니다. 나중에 다시 읽기 쉬워야 다음 변경도 쉬워집니다.

## 이번 시퀀스의 실무 확장 개념

이번 시퀀스의 실무 확장 개념은 변경에 강한 코드 기준입니다.

문제 코드는 보통 이런 모습입니다.

```kotlin
fun login(request: LoginRequest): TokenResponse {
    val email = request.email.trim().lowercase()
    val user = userRepository.findByEmail(email)
        .orElseThrow { InvalidCredentialsException() }

    if (!passwordEncoder.matches(request.password, user.password)) {
        throw InvalidCredentialsException()
    }

    return TokenResponse(jwtTokenProvider.createToken(user.email))
}
```

처음에는 자연스럽지만, 입력 정리, 조회, 검증, 토큰 생성이 한 메서드에 계속 쌓이면 변경 지점을 찾기 어려워집니다.

정리된 코드는 이런 방향을 가집니다.

```kotlin
fun login(request: LoginRequest): TokenResponse {
    val email = normalizeEmail(request.email)
    val user = findUserByEmailOrThrowInvalidCredentials(email)
    verifyPassword(request.password, user.password)
    return createTokenResponse(user.email)
}
```

메서드가 짧아져서 중요한 것이 아니라, 책임 경계가 보이기 시작한 점이 중요합니다.

## 학생이 직접 구현할 순서

1. `AuthService`와 `PostService`를 다시 읽는다.
2. 한 메서드가 어떤 책임을 함께 들고 있는지 표시한다.
3. 서비스 레벨 검증 또는 예외 응답을 보강한다.
4. 테스트를 추가해 리팩토링 전후 기능이 유지되는지 확인한다.
5. README와 문서를 보강해 이번 리팩토링 목적을 남긴다.

## 학생이 직접 수정하는 핵심 파일

- `PostService.kt`
- `AuthService.kt`
- `GlobalExceptionHandler.kt`
- `README.md`
- `*Test.kt`

## 학생이 최종적으로 이해해야 하는 것

- 읽기 쉬운 구조가 왜 변경에도 강한지
- 서비스 레벨 검증이 DTO 검증과 어떻게 다른지
- 예외 응답 구조를 통일하면 무엇이 좋아지는지
- 테스트가 리팩토링의 안전장치라는 말이 왜 나오는지
- README 보강이 왜 복습 도구이자 팀 커뮤니케이션 도구인지

## 제공 전제로 두는 것

- 10 시퀀스 answer 기반 코드
- 기본 패키지 구조
- 기존 테스트 구조
- 실행 가능한 starter 환경

학생에게는 리팩토링 포인트를 직접 찾고 손으로 정리하는 경험에 집중하게 합니다.

## 이번 시퀀스의 범위

이번 시퀀스에서 다룹니다.

- `AuthService`, `PostService` 리팩토링 포인트
- 서비스 레벨 검증 또는 예외 보강 1개 이상
- 테스트 보강 1~2개 이상
- README 및 문서 보강

이번 시퀀스에서 다루지 않습니다.

- 대규모 패키지 구조 개편
- 멀티모듈 전환
- 새 아키텍처 패턴 도입
- 성능 최적화 전체

## 결과물 기준

각 브랜치는 아래 결과물을 갖춰야 합니다.

- `README.md`
- `docs/theory.md`
- `docs/implementation.md`
- `docs/answer-guide.md`
- `docs/checklist.md`
- `docs/assets.md`
- starter 코드 또는 answer 코드

브랜치 구조는 아래를 따릅니다.

- `main`: 안내 브랜치
- `11-implementation`: 학생용 starter
- `11-answer`: 정답 브랜치

## 완료 기준

이번 시퀀스는 아래가 모두 맞아야 완료입니다.

- `11-implementation`, `11-answer`, `main` 브랜치가 정리되어 있음
- starter TODO가 서비스/예외/테스트/README에 맞게 배치되어 있음
- answer 코드가 책임 분리와 테스트 보강을 보여줌
- 문서가 기초 이론, 현재 코드 흐름, 실무 확장 개념을 모두 담고 있음
- `./gradlew test` 검증이 가능함
