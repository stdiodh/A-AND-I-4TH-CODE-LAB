# 이 코스 사용법

이 중앙 레포는 수업 순서와 토픽 레포를 안내하는 허브입니다.
학생은 중앙 레포를 서브모듈까지 clone하지 않아도 됩니다.
오늘 수업에 해당하는 토픽 레포만 clone해서 실습합니다.

## 중앙 레포와 토픽 레포

- 중앙 레포: 시퀀스 순서, 레포 위치, 브랜치 규칙을 확인하는 곳
- 토픽 레포: 실제 실습 코드와 학습 문서가 있는 곳

코스 구조는 [manifest](../manifest/sequences.yml)에서 한눈에 볼 수 있습니다.

## 오늘의 시퀀스 찾기

1. 수업 안내에서 시퀀스 번호를 확인합니다.
2. [learning path](./learning-path.md)에서 해당 시퀀스의 토픽 레포를 찾습니다.
3. 토픽 레포 README를 열고 시작 명령을 따라갑니다.

## 실습 시작

항상 `NN-implementation` 브랜치에서 시작합니다.
GitHub 원격 default branch 상태가 실습 시작 기준과 다를 수 있으므로 clone 뒤에는 시퀀스 번호가 붙은 implementation 브랜치를 명시적으로 checkout합니다.

```bash
git clone <repo-url>
cd <repo-name>
git checkout NN-implementation
```

예를 들어 시퀀스 01은 아래처럼 시작합니다.

```bash
git clone https://github.com/stdiodh/spring-boot-rest-crud-lab.git
cd spring-boot-rest-crud-lab
git checkout 01-implementation
```

## 실행과 테스트

각 토픽 레포 README의 `실행 방법`과 `테스트 방법`을 먼저 따릅니다.
보통 Spring Boot 실습은 아래 명령을 사용합니다.

```bash
./gradlew bootRun
./gradlew test
```

MySQL, Redis, RabbitMQ가 필요한 시퀀스는 먼저 아래 명령을 실행할 수 있습니다.

```bash
docker compose up -d
```

테스트는 단순히 "돌려보기"가 아니라 오늘 배운 개념이 동작하는지 확인하는 기준입니다.
각 시퀀스 문서의 `테스트가 확인하는 것`, `실패하면 먼저 볼 것`, `완료 기준`을 함께 읽습니다.

테스트가 실패하면 먼저 실패한 테스트 클래스와 메서드 이름을 봅니다.
그다음 expected/actual 값을 비교하고, 요청 body, 인증 헤더, DB/Redis/RabbitMQ 준비 상태를 확인합니다.
외부 OAuth2, SMTP 같은 서비스가 필요한 흐름은 mock 또는 local profile 대안으로 먼저 확인합니다.

## Visual Lab 보기

Visual Lab이 있는 레포에서는 아래처럼 확인합니다.
`docs/visual-lab/index.html`은 토픽 레포의 허브이고,
시퀀스별 상세 화면은 `docs/visual-lab/sequences/NN/index.html`에서 열 수 있습니다.

```bash
python3 -m http.server 8080 -d docs/visual-lab
```

브라우저에서 엽니다.

```text
http://localhost:8080
```

## 정답과 비교하기

처음부터 정답 브랜치를 보지 않습니다.
막혔거나 실습을 마친 뒤에만 같은 번호의 `NN-answer`와 비교합니다.

```bash
git fetch origin
git diff NN-implementation..NN-answer
```
