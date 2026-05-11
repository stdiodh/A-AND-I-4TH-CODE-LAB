# 03. 안전한 요청 처리

## 목표

잘못된 요청을 DTO 단계에서 검증하고, 실패 응답을 일관된 형태로 돌려줍니다.
성공 흐름뿐 아니라 실패 흐름도 API 설계의 일부로 다룹니다.

## 이 시퀀스에서 배우는 것

- Request DTO와 Entity 분리
- non-null Request DTO와 Bean Validation 책임
- Validation 어노테이션 사용
- 전역 예외 처리
- 에러 응답 형식 통일
- 성공 요청과 실패 요청을 함께 확인하는 방법

## 시작 브랜치

```bash
git checkout 03-implementation
```

## 실습 전 확인

- 토픽 레포: `spring-boot-db-access-lab`
- 가이드 브랜치: `main`
- 시작 브랜치: `03-implementation`
- 이전 기준: `02-answer`
- MySQL 실행 환경과 Swagger 확인 경로를 준비합니다.

## 구현할 TODO

1. Request DTO에 검증 규칙을 추가합니다.
2. Controller에서 `@Valid`를 연결합니다.
3. Service에서 `requireNotNull`로 요청값을 다시 검증하지 않도록 책임을 나눕니다.
4. 잘못된 요청의 실패 응답을 확인합니다.
5. 도메인 예외를 추가합니다.
6. `GlobalExceptionHandler`에서 예외를 응답으로 바꿉니다.
7. 성공 요청과 실패 요청을 Swagger에서 모두 실행합니다.

## 실행 방법

```bash
docker compose up -d
./gradlew bootRun
```

## 테스트 방법

```bash
./gradlew test
```

테스트가 확인하는 것:

- 잘못된 요청이 400으로 실패하는지 확인합니다.
- Validation 실패 응답이 정해진 에러 응답 형식을 따르는지 확인합니다.
- DTO validation과 Service 비즈니스 예외가 각각 알맞은 응답으로 변환되는지 확인합니다.

실패하면 먼저 볼 것:

- Controller 요청 DTO에 `@Valid`가 연결되어 있는지 확인합니다.
- Request DTO의 Bean Validation 어노테이션과 non-null 타입이 의도와 맞는지 봅니다.
- 실패 응답 body의 필드 이름이 테스트 기대값과 같은지 확인합니다.

완료 기준:

- 잘못된 요청 시 400 테스트가 통과합니다.
- 에러 응답 형식 테스트가 통과합니다.
- 실패 메시지를 읽고 DTO 검증 문제와 예외 처리 문제를 구분할 수 있습니다.

## 확인할 API 또는 화면

- Swagger: `http://localhost:8080/swagger`
- 정상 생성 요청
- 빈 title, 빈 content 같은 실패 요청
- 없는 게시글 조회 또는 수정 요청
- 에러 응답 JSON

## 자주 발생하는 문제

- DTO가 아니라 Entity에 요청 검증을 몰아넣습니다. 외부 요청 검증은 Request DTO에서 시작합니다.
- `@Valid`를 Controller에 연결하지 않아 검증이 실행되지 않습니다.
- Service에서 null 입력 검증까지 처리하려고 합니다. Service는 검증을 통과한 요청으로 비즈니스 규칙을 판단합니다.
- 에러 응답 메시지가 요청마다 제각각입니다. 공통 응답 형식을 맞춥니다.
- 실패 케이스를 Swagger에서 직접 실행하지 않고 넘어갑니다.

## 완료 기준

- 잘못된 요청이 저장 로직까지 들어가지 않습니다.
- Validation 실패가 일관된 에러 응답으로 내려옵니다.
- DTO validation과 Service 비즈니스 규칙 검증의 차이를 설명할 수 있습니다.
- 없는 데이터 요청도 예외 응답으로 처리됩니다.
- 정상/실패 요청 흐름을 모두 설명할 수 있습니다.
- `./gradlew test`가 통과합니다.

## 정답과 비교하는 방법

막혔거나 실습을 마친 뒤에만 참고 정답과 비교합니다.

```bash
git diff 03-implementation..03-answer
```

## 다음 시퀀스

다음은 `04. 인증과 JWT`입니다.
회원가입, 로그인, JWT 발급과 보호 API 흐름을 다룹니다.
