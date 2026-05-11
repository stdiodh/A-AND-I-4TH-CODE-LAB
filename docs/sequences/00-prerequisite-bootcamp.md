# 00. 선수지식 부트캠프

## 목표

Spring Boot 실습 전에 HTTP, JSON, Postman, Git, DB 기본 용어를 맞춥니다.
이 시퀀스는 서버 코드를 구현하는 단계가 아니라 이후 실습을 따라가기 위한 환경 준비 단계입니다.

## 이 시퀀스에서 배우는 것

- HTTP 메서드와 상태 코드 읽기
- JSON 요청/응답 구조 이해
- Postman으로 GET/POST 요청 보내기
- Git clone, branch, add, commit 흐름
- table, row, column, PK 같은 DB 기본 용어

## 시작 브랜치

```bash
git checkout 00-implementation
```

## 실습 전 확인

- 토픽 레포: `aandi-prerequisite-bootcamp`
- 가이드 브랜치: `main`
- 시작 브랜치: `00-implementation`
- Postman 또는 HTTP 요청 도구가 준비되어 있어야 합니다.
- Git 명령을 실행할 터미널이 준비되어 있어야 합니다.

## 구현할 TODO

코드 TODO는 없습니다.
대신 아래 손동작을 직접 진행합니다.

1. Postman으로 GET 요청을 보냅니다.
2. Postman으로 POST 요청을 보냅니다.
3. JSON body 값을 바꿔봅니다.
4. Git clone을 해봅니다.
5. 새 branch를 만들어봅니다.
6. add와 commit을 해봅니다.
7. DB 기본 용어를 표 예시로 설명합니다.

## 실행 방법

해당 없음.
서버 실행이 없는 준비 시퀀스입니다.

## 테스트 방법

자동화 테스트는 없습니다.
대신 개발 환경과 기본 도구 실행을 직접 확인합니다.

```bash
java -version
git --version
```

Gradle wrapper가 있는 토픽 레포에서는 아래 명령까지 확인합니다.

```bash
./gradlew --version
```

테스트가 확인하는 것:

- Java, Git, Gradle 명령을 터미널에서 실행할 수 있습니다.
- Postman 또는 HTTP 요청 도구로 GET/POST 요청을 보낼 수 있습니다.
- JSON body와 HTTP 상태 코드를 함께 읽을 수 있습니다.

실패하면 먼저 볼 것:

- Java가 설치되어 있고 터미널 PATH에 잡혀 있는지 확인합니다.
- Gradle wrapper 명령은 중앙 레포가 아니라 Gradle 프로젝트가 있는 토픽 레포에서 실행합니다.
- 요청 도구에서 URL, method, body 형식이 맞는지 먼저 확인합니다.

완료 기준:

- 개발 환경 확인 명령이 실행됩니다.
- GET/POST 요청과 Git 기본 명령을 직접 실행했습니다.
- 다음 시퀀스의 `./gradlew bootRun`과 `./gradlew test`를 실행할 준비가 되었습니다.

## 확인할 API 또는 화면

- Postman 요청/응답 화면
- HTTP 상태 코드
- JSON request body와 response body
- Git branch 목록
- DB 용어 그림 또는 표 자료

## 자주 발생하는 문제

- 중앙 레포에서 명령을 실행합니다. 이 시퀀스는 토픽 레포에서 진행합니다.
- HTTP 응답 본문만 보고 상태 코드를 놓칩니다. 상태 코드와 body를 함께 봅니다.
- JSON의 key와 value를 구분하지 못합니다. key는 이름, value는 값으로 읽습니다.
- branch를 만든 뒤 현재 branch를 확인하지 않습니다. `git branch --show-current`로 확인합니다.

## 완료 기준

- GET/POST 요청을 보내고 응답을 읽을 수 있습니다.
- JSON body 값을 바꿔 요청할 수 있습니다.
- Git 기본 흐름을 직접 실행해봤습니다.
- table, row, column, PK를 예시로 설명할 수 있습니다.
- 다음 Spring Boot 실습에서 사용할 최소 용어를 이해했습니다.

## 정답과 비교하는 방법

막혔거나 실습을 마친 뒤에만 참고 자료와 비교합니다.

```bash
git diff 00-implementation..00-answer
```

## 다음 시퀀스

다음은 `01. 요청/응답과 메모리 CRUD`입니다.
Spring Boot에서 HTTP 요청이 Controller, Service, 메모리 저장소를 거쳐 응답으로 돌아오는 흐름을 구현합니다.
