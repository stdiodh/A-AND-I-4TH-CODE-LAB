좋아요.
이번에는 **04. 인증과 JWT** 시퀀스 전용 Codex 프롬프트입니다.

이 시퀀스의 목표는 **회원가입과 로그인 최소 흐름을 만들고, JWT로 보호된 API 접근을 경험하게 하는 것**입니다. 학생은 `User 핵심 필드 확인 → 회원가입 Request DTO 작성 → 회원가입 Service에서 비밀번호 인코딩 연결 → 로그인 Request DTO 작성 → 로그인 Service에서 사용자 조회와 비밀번호 확인 → JWT 발급 메서드 연결 → 인증이 필요한 API 지정 → 토큰에서 사용자 정보 읽기 → 토큰 유무 비교 확인` 순서로 구현해야 하고, TODO를 넣을 핵심 파일은 `UserSignUpRequest.kt`, `LoginRequest.kt`, `AuthService.kt`, `SecurityConfig.kt`, `JwtTokenProvider.kt`, `AuthController.kt`입니다. 또 Security 설정 뼈대, PasswordEncoder Bean, JWT 유틸 초안, 인증 실패 처리 일부는 미리 제공하는 전제로 가야 합니다. 

````text id="fx1vkr"
당신은 A&I 백엔드 커리큘럼용 실습 레포와 문서를 설계하는 Codex입니다.

지금부터는 전체 커리큘럼 중 **04. 인증과 JWT** 시퀀스만 다룹니다.
다른 시퀀스 내용은 절대 섞지 말고, 이번 요청에서는 04 시퀀스에 필요한 레포 구조, 학생용 starter 코드, 정답 가이드, 이론 문서만 정확하게 만드세요.

## 1. 이번 작업의 목표

이번 시퀀스의 목적은 이전 시퀀스에서 만든 안전한 요청 처리 흐름 위에,
학생이 아래 흐름을 직접 연결하면서 **인증과 JWT의 가장 기본적인 구조**를 이해하게 만드는 것입니다.

- 회원가입 요청을 받는다
- 비밀번호를 안전하게 저장한다
- 로그인 요청을 처리한다
- 사용자를 확인한다
- JWT를 발급한다
- 보호된 API는 토큰이 있어야 접근할 수 있다
- 토큰에서 현재 사용자 정보를 읽을 수 있다

즉, 이번 시퀀스는 Spring Security 전체를 깊게 배우는 단계가 아닙니다.
학생이 **인증은 누구인지 확인하는 것**, **인가/보호는 접근 가능 여부를 나누는 것**,
**JWT는 로그인 이후 요청을 구분하기 위한 수단 중 하나**라는 감각을 갖게 만드는 단계입니다.

---

## 2. 이번 시퀀스에서 학생이 완성해야 하는 최종 상태

학생은 이 시퀀스를 마친 뒤 아래를 할 수 있어야 합니다.

1. 인증과 인가의 차이를 설명할 수 있다.
2. 회원가입과 로그인 최소 흐름을 설명할 수 있다.
3. 비밀번호를 그냥 저장하면 안 되는 이유를 말할 수 있다.
4. 로그인 후 JWT를 발급받을 수 있다.
5. 보호된 API에서 토큰 유무에 따라 결과가 달라지는 것을 확인할 수 있다.
6. JWT가 왜 필요한지 입문 수준에서 설명할 수 있다.

---

## 3. 이번 시퀀스는 어디서부터 시작하는가

이번 시퀀스는 **03 시퀀스 answer 기준 레포를 바탕으로 확장**합니다.

즉, 아래는 이미 존재한다고 가정합니다.

- Spring Boot 프로젝트
- Swagger 설정
- DB 연결
- Entity / Repository / Service / Controller 기반 CRUD
- DTO 분리
- Validation
- 기본 예외 처리

이번 시퀀스에서는 이 구조를 완전히 새로 만들지 않고,
**사용자를 식별하고 로그인 이후 요청을 구분하는 흐름**을 추가하는 데 집중하세요.

---

## 4. 이번 시퀀스에서 학생이 직접 구현할 순서

구현 순서는 반드시 아래 순서를 기준으로 설계하세요.

1. `User` 핵심 필드를 확인한다.
2. 회원가입 `Request DTO`를 만든다.
3. 회원가입 Service에서 비밀번호 인코딩을 연결한다.
4. 로그인 `Request DTO`를 만든다.
5. 로그인 Service에서 사용자 조회와 비밀번호 확인을 연결한다.
6. JWT 발급 메서드를 연결한다.
7. 인증이 필요한 API를 지정한다.
8. 토큰에서 사용자 정보를 읽는 흐름을 연결한다.
9. 토큰 유무에 따른 결과 차이를 확인한다.

이 순서는 바꾸지 마세요.
문서와 코드 TODO도 반드시 이 순서에 맞게 설계하세요.

---

## 5. 이번 시퀀스에서 TODO를 넣을 파일

학생이 직접 수정하는 핵심 파일은 아래로 제한하세요.

- `UserSignUpRequest.kt`
- `LoginRequest.kt`
- `AuthService.kt`
- `SecurityConfig.kt`
- `JwtTokenProvider.kt`
- `AuthController.kt`

필요하면 아래 같은 파일을 추가로 둘 수는 있지만,
핵심 TODO는 위 파일에 집중되어야 합니다.

- `User.kt`
- `UserRepository.kt`
- `TokenResponse.kt`
- `JwtAuthenticationFilter.kt`

단, Security 전체를 과하게 확장하지 말고 최소 흐름만 보이게 하세요.

---

## 6. 이번 시퀀스에서 미리 제공해야 하는 것

문서와 코드 설계 시 아래는 반드시 제공 전제로 처리하세요.

- Security 설정 뼈대
- PasswordEncoder Bean
- JWT 유틸 초안
- 인증 실패 처리 일부
- 기존 03 시퀀스 answer 기반 프로젝트
- 기본 패키지 구조
- Swagger 설정
- build 설정
- application 설정
- 실행 가능한 starter 환경

학생에게는 핵심 흐름만 직접 구현하게 해야 합니다.

---

## 7. 이번 시퀀스의 중요한 제약

아래 제약을 반드시 지키세요.

- OAuth2를 넣지 마세요.
- Email Verification을 넣지 마세요.
- refresh token까지 확장하지 마세요.
- 권한(Role) 체계를 복잡하게 만들지 마세요.
- 테스트를 본격적으로 넣지 마세요.
- Security 설정을 실무 풀버전처럼 길게 만들지 마세요.
- JWT 구조를 너무 깊게 설명하지 마세요.
- 세션/쿠키/JWT 비교를 길게 하지 말고 이번 실습 맥락에만 맞게 설명하세요.
- 이번 시퀀스의 핵심은 “회원가입 → 로그인 → 토큰 발급 → 보호된 API 접근”입니다.
- 인증과 인가를 구분해서 설명하되, 인가를 복잡하게 확장하지는 마세요.
- 문서는 학생용 복습과 강사용 PPT 준비까지 같이 고려해서 쓰세요.
- 이번 응답에서는 오직 04 시퀀스 문서와 starter 코드 구조만 만드세요.

---

## 8. 생성해야 할 결과물

이번 시퀀스에서는 아래를 생성하세요.

### (1) README.md
역할:
- 이 시퀀스 소개
- 학생이 무엇을 배우는 단계인지 설명
- 문서 링크 연결
- 구현 순서 요약
- 실행 방법 요약

### (2) docs/theory.md
역할:
- 왜 이 시퀀스가 필요한지
- 인증과 인가 차이 설명
- 회원가입 / 로그인 흐름 설명
- PasswordEncoder가 왜 필요한지 설명
- JWT가 왜 필요한지 설명
- 보호된 API 흐름 설명
- 다음 시퀀스의 OAuth2 또는 Email Verification으로 자연스럽게 연결

### (3) docs/implementation.md
역할:
- 오늘 학생이 완성할 최종 흐름
- 학생이 직접 구현할 순서
- TODO를 넣을 파일
- 각 파일의 역할
- 단계별 구현 안내
- 실행 확인 방법
- 학생 체크 질문

### (4) docs/answer-guide.md
역할:
- 각 TODO 단계의 정답 가이드
- 회원가입 흐름 정답
- 로그인 흐름 정답
- 비밀번호 인코딩 정답
- JWT 발급 정답
- 보호된 API 접근 정답
- 강사가 빠르게 answer 비교할 수 있는 구조

### (5) docs/checklist.md
역할:
- 학생 체크리스트
- 강사 / 발표 / PPT 체크리스트
- 수업 전 준비
- 수업 중 확인 질문
- 수업 후 점검 포인트

### (6) docs/assets.md
역할:
- 미리 제공할 것 목록
- 왜 제공하는지
- 학생이 직접 작성하지 않는 범위 정리

### (7) starter 코드 파일
학생이 직접 따라칠 수 있도록 starter 코드를 만드세요.
핵심 파일에는 TODO 주석을 넣으세요.

### (8) answer 코드 기준
별도 answer 브랜치를 전제로,
docs/answer-guide.md 안에 정답 코드를 충분히 넣으세요.
필요하면 “answer 기준 완성 형태”도 함께 설명하세요.

---

## 9. 코드 설계 규칙

이번 시퀀스의 코드는 아래 원칙을 따라야 합니다.

- Kotlin + Spring Boot + Spring Security 기준
- JWT 기반 최소 인증 흐름
- 회원가입, 로그인, 보호된 API 1개 정도로 최소 구성
- User는 가장 기본적인 필드만 사용
  - 예: id, email, password
- 비밀번호는 반드시 PasswordEncoder로 처리
- 로그인 성공 시 access token 1개만 발급하는 단순 구조
- 보호된 API는 `me` 조회 또는 간단한 사용자 정보 조회 정도로 충분
- SecurityConfig는 최소한으로 유지
- JWT 유틸은 토큰 생성과 사용자 식별 정도만 보여주면 충분
- 코드 길이는 짧고 역할이 잘 보이게 유지

---

## 10. TODO 작성 규칙

TODO는 반드시 순서형 힌트로 작성하세요.

좋지 않은 예:
```kotlin
// TODO: 로그인 구현
````

좋은 예:

```kotlin
// TODO 1. email로 사용자를 찾으세요.
// TODO 2. passwordEncoder.matches(...)로 비밀번호를 확인하세요.
// TODO 3. 검증이 끝나면 JWT를 발급하세요.
// TODO 4. 토큰을 응답 DTO에 담아 반환하세요.
```

또 아래 원칙을 반드시 지키세요.

* `TODO 1`, `TODO 2`, `TODO 3`처럼 번호를 붙인다.
* 한 TODO에는 한 동작만 넣는다.
* 문법 설명보다 흐름 설명을 적는다.
* 학생이 하지 말아야 할 것도 적는다.
* 역할이 섞이지 않게 유도한다.

예:

```kotlin
// TODO: 비밀번호를 원문 그대로 저장하지 마세요.
// 회원가입 시 PasswordEncoder를 통해 인코딩한 뒤 저장하세요.
```

또는

```kotlin
// TODO: Controller에서 인증 로직을 직접 처리하지 마세요.
// Service가 회원가입/로그인 흐름을 맡도록 유지하세요.
```

---

## 11. theory.md 작성 규칙

docs/theory.md 는 아래 구조를 따르세요.

1. 제목
2. 한 줄 소개
3. 이번 시퀀스 한 줄 요약
4. 먼저 이것만 기억해도 됩니다
5. 왜 이 시퀀스를 배우는가
6. 이번 실습 흐름 한눈에 보기
7. 중요한 코드 먼저 보기
8. 핵심 개념 쉬운 설명

   * 인증
   * 인가
   * 회원가입
   * 로그인
   * PasswordEncoder
   * JWT
   * 보호된 API
9. 자주 헷갈리는 포인트
10. 직접 말해보기
11. 복습 체크리스트
12. 오늘 꼭 기억할 것

주의:

* 정의만 길게 쓰지 마세요.
* 코드와 반드시 연결하세요.
* 짧은 코드 블록을 사용하세요.
* 코드 블록에는 설명용 주석을 넣어도 됩니다.
* 학생이 “아, 로그인 이후 요청을 구분하는 흐름이 JWT였구나”를 느끼게 써야 합니다.

---

## 12. implementation.md 작성 규칙

docs/implementation.md 는 아래 구조를 따르세요.

1. 제목
2. 오늘 학생이 완성할 최종 흐름
3. 학생이 직접 구현할 순서
4. TODO를 넣을 파일
5. 파일별 역할 설명
6. 단계별 구현 안내

   * Step 1. User 핵심 필드 확인
   * Step 2. 회원가입 DTO 만들기
   * Step 3. 회원가입 Service 연결
   * Step 4. 로그인 DTO 만들기
   * Step 5. 로그인 Service 연결
   * Step 6. JWT 발급 연결
   * Step 7. 보호된 API 지정
   * Step 8. 토큰에서 사용자 정보 읽기
   * Step 9. 토큰 유무 비교 확인
7. 각 단계의 확인 포인트
8. 학생 체크 질문
9. 강사용 확인 포인트
10. 다음 시퀀스 연결 포인트

주의:

* 결과만 적지 말고 손의 순서가 보여야 합니다.
* 단계별로 학생이 막히기 쉬운 부분을 짧게 힌트로 적으세요.
* 각 단계가 끝났을 때 무엇이 보이면 성공인지 써주세요.

---

## 13. answer-guide.md 작성 규칙

docs/answer-guide.md 는 정답 문서입니다.

반드시 아래를 포함하세요.

* 각 파일의 최종 형태 설명
* 회원가입 DTO 정답 코드
* 로그인 DTO 정답 코드
* AuthService 핵심 정답 코드
* PasswordEncoder 사용 정답 코드
* JwtTokenProvider 핵심 정답 코드
* SecurityConfig 핵심 정답 코드
* 보호된 API 예시
* 회원가입 요청 예시
* 로그인 요청 예시
* 토큰 응답 예시
* 토큰 없이 접근했을 때 예시
* 학생이 자주 틀리는 포인트
* 왜 비밀번호를 인코딩해야 하는지 설명
* 왜 JWT가 필요한지 설명
* 다음 시퀀스에서 왜 OAuth2 또는 Email Verification으로 확장하는지 연결

정답 문서는 너무 장황하게 쓰지 말고,
강사가 빠르게 비교하고 학생도 복습하기 쉬운 형태로 만드세요.

---

## 14. starter 코드 파일 작성 규칙

starter 코드는 아래 성격을 가져야 합니다.

* 바로 실행은 가능해야 함
* 핵심 부분은 비어 있거나 TODO로 남아 있어야 함
* TODO는 학생이 수업 시간 안에 채울 수 있어야 함
* TODO 없는 보일러플레이트는 제공
* Swagger 또는 최소한의 API 실행 확인이 가능해야 함
* 회원가입 / 로그인 / 보호된 API 흐름이 모두 있어야 함

필수 starter 파일 예시:

* `src/main/kotlin/.../dto/UserSignUpRequest.kt`
* `src/main/kotlin/.../dto/LoginRequest.kt`
* `src/main/kotlin/.../dto/TokenResponse.kt`
* `src/main/kotlin/.../service/AuthService.kt`
* `src/main/kotlin/.../security/SecurityConfig.kt`
* `src/main/kotlin/.../security/JwtTokenProvider.kt`
* `src/main/kotlin/.../controller/AuthController.kt`

필요하면 추가 가능:

* `User.kt`
* `UserRepository.kt`
* `JwtAuthenticationFilter.kt`

단, Security 전체를 과하게 확장하지 말고 최소 흐름만 보이게 하세요.

---

## 15. checklist.md 작성 규칙

docs/checklist.md 에는 반드시 아래를 넣으세요.

### 학생 체크리스트

예:

* 인증과 인가 차이를 설명할 수 있다.
* JWT가 왜 필요한지 말할 수 있다.
* 로그인 후 토큰을 받아봤다.
* 보호된 API에서 토큰 유무 차이를 확인했다.

### 강사 / PPT 체크리스트

예:

* 인증과 인가 차이를 한 장으로 설명할 수 있는가
* 로그인 흐름 그림이 있는가
* JWT 구조를 너무 깊지 않게 설명할 수 있는가
* 보호된 API 예시가 있는가

또 아래도 포함하세요.

* 수업 전 준비 체크
* 수업 중 질문 체크
* 수업 후 복습 체크

---

## 16. assets.md 작성 규칙

docs/assets.md 에는 아래를 넣으세요.

* 제공 파일/설정 목록
* 각 항목의 목적
* 왜 학생이 직접 치지 않아도 되는지
* 수업에서 언제 쓰는지

예:

* Security 설정 뼈대: 학생이 인증 흐름에 집중할 수 있도록 제공
* PasswordEncoder Bean: 반복 설정이므로 제공
* JWT 유틸 초안: 토큰 전체 구현보다 흐름 이해에 집중시키기 위해 제공

---

## 17. 절대 하지 말아야 할 것

* OAuth2를 넣지 마세요.
* Email Verification을 넣지 마세요.
* refresh token을 넣지 마세요.
* 권한 체계를 복잡하게 만들지 마세요.
* 테스트를 본격적으로 넣지 마세요.
* Security 고급 설정을 넣지 마세요.
* 이번 요청에서는 04 시퀀스 범위를 벗어나지 마세요.

이번 작업은 반드시 **04. 인증과 JWT** 에만 한정합니다.
다른 시퀀스 내용은 추가하지 마세요.
