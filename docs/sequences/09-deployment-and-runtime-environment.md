# 09. 배포와 실행 환경

## 목표

로컬에서 실행하던 Spring Boot 앱을 Docker와 운영 설정으로 실행 가능한 배포 단위로 묶습니다.
로컬 실행과 컨테이너 실행의 차이를 확인합니다.

## 이 시퀀스에서 배우는 것

- Spring Boot jar와 Docker image의 관계
- Dockerfile 역할
- 운영 profile과 환경변수
- Docker Compose 운영 실행
- GitHub Secrets로 민감한 값 분리
- 배포 후 로그 확인

## 시작 브랜치

```bash
git checkout 09-implementation
```

## 실습 전 확인

- 토픽 레포: `spring-boot-deployment-runtime-lab`
- 가이드 브랜치: `main`
- 시작 브랜치: `09-implementation`
- 이전 기준: `08-answer`
- Docker가 실행 가능해야 합니다.
- 실제 운영 비밀번호, JWT secret, OAuth secret, SMTP password는 코드에 쓰지 않습니다.

## 구현할 TODO

1. `Dockerfile`에서 jar 실행 단위를 확인합니다.
2. `application-prod.yaml`에서 운영 설정 자리를 확인합니다.
3. 환경변수 예시값을 안전하게 정리합니다.
4. 운영용 compose 파일을 확인합니다.
5. jar를 빌드합니다.
6. 컨테이너로 앱을 실행합니다.
7. 로그와 컨테이너 상태를 확인합니다.

## 실행 방법

```bash
docker compose up -d
./gradlew bootRun
```

컨테이너 배포 단위 확인:

```bash
./gradlew bootJar
```

## 테스트 방법

```bash
./gradlew test
```

컨테이너 실행 단위는 아래 명령으로 함께 확인합니다.

```bash
./gradlew bootJar
docker build -t aandi-runtime-lab .
docker compose up -d
```

테스트가 확인하는 것:

- `./gradlew test`로 배포 전 애플리케이션 기본 동작을 확인합니다.
- `docker build`로 jar가 컨테이너 이미지에 들어가는지 확인합니다.
- `docker compose up` 후 health check 또는 로그로 앱이 실행 가능한지 확인합니다.

실패하면 먼저 볼 것:

- test 실패와 Dockerfile 실패를 분리해서 읽습니다.
- jar 파일 경로와 Dockerfile의 `COPY` 경로가 맞는지 확인합니다.
- compose 실행 후에는 `docker compose ps`와 로그를 먼저 봅니다.

완료 기준:

- `./gradlew test`가 통과합니다.
- `docker build`가 성공합니다.
- `docker compose up` 후 health check 또는 로그로 정상 실행을 확인했습니다.

## 확인할 API 또는 화면

- `docker compose ps`
- 애플리케이션 로그
- 로컬 `bootRun` 실행 결과
- Docker image 또는 jar 빌드 결과
- 운영 profile에서 환경변수가 주입되는지 확인

## 자주 발생하는 문제

- 로컬 실행과 컨테이너 실행을 같은 것으로 봅니다. 컨테이너는 실행 환경까지 묶습니다.
- 운영 비밀값을 설정 파일에 직접 적습니다. 실제 값은 환경변수나 Secrets로 주입합니다.
- `docker compose up -d` 성공만 보고 끝냅니다. 컨테이너 상태와 로그까지 확인합니다.
- jar 빌드 실패를 배포 문제로 오해합니다. 먼저 `./gradlew test`와 `bootJar`를 확인합니다.

## 완료 기준

- jar가 빌드됩니다.
- Dockerfile이 jar 실행 단위를 설명합니다.
- 운영 설정이 환경변수 기반으로 분리됩니다.
- 컨테이너 상태와 로그를 확인했습니다.
- `./gradlew test`가 통과합니다.

## 정답과 비교하는 방법

막혔거나 실습을 마친 뒤에만 참고 정답과 비교합니다.

```bash
git diff 09-implementation..09-answer
```

## 다음 시퀀스

다음은 `10. 자동화와 운영 흐름`입니다.
수동 배포 흐름을 CI/CD workflow로 고정합니다.
