# Troubleshooting

막혔을 때는 아래 순서로 확인합니다.

## 1. 브랜치 확인

```bash
git branch --show-current
```

현재 수업 번호와 같은 `NN-implementation`인지 확인합니다.

## 2. 실행 위치 확인

명령은 중앙 레포가 아니라 토픽 레포 안에서 실행합니다.

```bash
pwd
ls
```

`build.gradle.kts`가 보이면 Spring Boot 실습 레포 안에 있는 것입니다.

## 3. 의존 서비스 확인

DB, Redis, RabbitMQ가 필요한 시퀀스는 먼저 실행합니다.

```bash
docker compose up -d
```

## 4. 테스트 먼저 실행

```bash
./gradlew test
```

테스트 실패 메시지에서 파일 이름과 함수 이름을 먼저 봅니다.

## 5. 서버 실행

```bash
./gradlew bootRun
```

Swagger가 있는 시퀀스는 브라우저에서 확인합니다.

```text
http://localhost:8080/swagger
```

## 6. 문서 다시 보기

토픽 레포에서 아래 순서로 다시 읽습니다.

1. `README.md`
2. `docs/theory.md`
3. `docs/implementation.md`
4. `docs/checklist.md`

## 7. 마지막에 정답과 비교

정답 브랜치는 처음부터 보는 자료가 아니라 비교용입니다.

```bash
git fetch origin
git diff NN-implementation..NN-answer
```
