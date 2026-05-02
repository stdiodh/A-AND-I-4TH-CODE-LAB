# 09. 배포와 실행 환경

## 시퀀스 목표

이번 시퀀스의 목표는 이전까지 만든 Spring Boot 애플리케이션을
로컬 개발 환경 밖으로 옮겨보는 첫 배포 흐름을 이해하는 것입니다.

학생은 이번 단계에서 아래 흐름을 이해해야 합니다.

1. 실행 가능한 앱을 하나의 배포 단위로 묶는다.
2. 운영 환경 설정을 코드 밖으로 분리한다.
3. GitHub Actions와 Secrets를 이용해 EC2로 전달한다.
4. 배포 후 로그로 실제 기동 상태를 확인한다.

즉, 이번 시퀀스의 핵심은
Docker + prod profile + GitHub Actions 기본 배포 + Secrets + 로그 확인입니다.

## 이번 시퀀스에서 다시 설명해야 하는 기초 개념

이번 09 시퀀스는 `08`까지 기능 구현을 마친 뒤 시작합니다.
그래서 학생이 아래 기초 개념을 다시 이해해야 합니다.

- `jar`
  Spring Boot 앱을 실행 가능한 결과물로 묶은 파일
- `Dockerfile`
  그 결과물을 어떤 환경에서 어떻게 실행할지 적어두는 파일
- `profile`
  로컬과 운영처럼 환경마다 다른 설정 묶음을 적용하는 방식
- `environment variable`
  코드 밖에서 주입하는 실행 환경 값
- `GitHub Secrets`
  workflow에서만 꺼내 쓸 수 있는 비밀값 저장소
- `release bundle`
  서버에 올릴 jar와 배포 파일 묶음
- `runtime log`
  서버에서 앱이 실제로 어떻게 올라갔는지 보여주는 기록

즉, 이번 시퀀스는 "코드를 서버에 올린다"가 아니라
"실행 결과물과 운영 설정을 분리해서 안전하게 전달한다"는 관점으로 보는 단계입니다.

## 현재 코드 흐름에서 어디를 봐야 하는가

이번 시퀀스는 이미 동작하는 앱을 운영 환경으로 옮기는 단계입니다.

1. `Dockerfile`
   jar가 어떤 실행 단위로 바뀌는지 보여주는 시작점
2. `src/main/resources/application-prod.yaml`
   운영 환경 전용 설정 자리
3. `deploy/compose.prod.yaml`
   앱, MySQL, Redis가 어떻게 함께 뜨는지 보여주는 파일
4. `.github/workflows/deploy.yml`
   build, 전달, 재기동, 로그 확인 순서가 모이는 파일
5. `.env.example`
   어떤 환경변수가 필요한지 보여주는 힌트 파일

짧게 말하면 이번 시퀀스는

- `코드 -> jar -> Docker image -> EC2 실행`
- `설정 자리 정의 -> 실제 값은 환경변수/Secrets로 주입`

흐름을 함께 이해하는 단계입니다.

## 이전 시퀀스와의 연결

- 시작 기준: `08-answer`
- 시작 레포: `spring-boot-realtime-communication-lab`
- 실제 09 실습 레포: `spring-boot-deployment-runtime-lab`

이번 시퀀스는 08에서 완성한 앱을 다시 구현하는 단계가 아닙니다.
이미 동작하는 앱을 운영 환경으로 옮기는 흐름에만 집중합니다.

## 이번 시퀀스의 실무 확장 개념

이번 09 시퀀스의 실무 확장 개념은 아래 두 가지입니다.

- 환경변수 우선순위
- 시크릿 관리

핵심은 이렇습니다.

- 운영 환경에서는 값이 로컬과 다를 수밖에 없습니다.
- 그래서 설정 파일은 값을 “보관”하기보다 값을 “받아올 자리”를 정의해야 합니다.
- DB 비밀번호, JWT 시크릿, SMTP 계정, OAuth 시크릿, EC2 pem key는 코드에 넣으면 안 됩니다.

즉, 이번 시퀀스는 “배포 파일을 만든다”에서 끝나지 않고
"어떤 값은 어디에 두고, 어떤 값은 절대 코드에 두지 말아야 하는가"까지 이해하는 단계입니다.

## 학생이 직접 구현할 순서

구현 순서는 반드시 아래 순서를 따릅니다.

1. `Dockerfile` 핵심 줄을 채운다.
2. `application-prod.yaml`로 운영 설정을 분리한다.
3. `compose.prod.yaml`로 운영 실행 구성을 확인한다.
4. `deploy.yml`에서 GitHub Actions 배포 흐름을 완성한다.
5. GitHub Secrets를 연결하고, 배포 후 로그를 확인한다.

## 문제 상황과 해결 방향을 코드로 보기

### 문제 1. 운영 비밀번호를 설정 파일에 직접 적으면 왜 위험한가

처음에는 아래 코드가 가장 편해 보일 수 있습니다.

```yaml
spring:
  datasource:
    url: jdbc:mysql://prod-db:3306/aandi
    username: root
    password: super-secret-password

jwt:
  secret: hard-coded-jwt-secret
```

이렇게 두면 로컬에서는 빨리 실행될 수 있습니다.
하지만 실제로는 아래 문제가 같이 생깁니다.

- Git에 비밀값이 그대로 남습니다.
- 개발자와 운영자가 같은 비밀값을 보게 됩니다.
- 환경이 바뀔 때마다 파일을 직접 수정해야 합니다.

### 해결 방향 1. 설정 파일에는 자리만 두고 값은 밖에서 넣는다

```yaml
spring:
  datasource:
    url: ${DB_URL:}
    username: ${DB_USERNAME:}
    password: ${DB_PASSWORD:}

jwt:
  secret: ${JWT_SECRET:}
```

이 흐름이면 어떤 값이 필요한지는 파일이 알려주고,
실제 값은 `.env`나 GitHub Secrets 같은 실행 환경에서 넣을 수 있습니다.

### 문제 2. 배포 workflow 안에 pem key를 직접 적으면 왜 위험한가

```yaml
- name: Deploy
  run: |
    cat <<'EOF' > ~/.ssh/aandi.pem
    -----BEGIN PRIVATE KEY-----
    ...
    EOF
```

이 방식은 예시로는 보일 수 있어도,
실제 운영에서는 비밀키가 workflow 코드와 히스토리에 남기 때문에 매우 위험합니다.

### 해결 방향 2. Secrets에서 꺼내고 실행 시점에만 임시 파일로 만든다

```yaml
- name: Write SSH key
  run: |
    printf '%s' "${{ secrets.EC2_SSH_KEY }}" > ~/.ssh/aandi-ec2.pem
    chmod 600 ~/.ssh/aandi-ec2.pem
```

이 방식이면 키를 코드에 남기지 않고,
배포 실행 시점에만 잠깐 복원해서 쓸 수 있습니다.

### 문제 3. 배포가 끝났다고 바로 성공이라고 보면 왜 위험한가

`docker compose up -d`가 끝났다고 해서 앱이 정상 기동한 것은 아닙니다.
실제로는 아래 문제가 그 뒤에 바로 드러날 수 있습니다.

- DB 연결 실패
- Redis 연결 실패
- OAuth 시크릿 누락
- 포트 충돌

### 해결 방향 3. 마지막 확인은 항상 로그까지 본다

```bash
docker compose ps
docker logs --tail 50 aandi-app
```

이번 시퀀스에서는 배포 완료의 마지막 기준을 “명령 성공”이 아니라
"로그에서 실제 기동 상태를 확인했는가"로 잡아야 합니다.

## 학생이 직접 수정하는 핵심 파일

- `Dockerfile`
- `src/main/resources/application-prod.yaml`
- `deploy/compose.prod.yaml`
- `.github/workflows/deploy.yml`

보조 파일은 추가할 수 있지만,
TODO는 위 네 파일에 집중합니다.

## 학생이 최종적으로 이해해야 하는 것

- Dockerfile이 jar를 어떻게 실행 단위로 바꾸는가
- prod profile이 왜 필요한가
- 운영 비밀값을 왜 Secrets로 분리해야 하는가
- EC2 pem key나 계정 정보를 왜 코드에 넣으면 안 되는가
- 배포 후 왜 로그를 먼저 확인해야 하는가

## 제공 전제로 두는 것

- 기존 애플리케이션 코드
- 로컬 실행 가능한 기본 환경
- EC2 준비 가이드
- GitHub Secrets에 넣을 값 목록
- 로컬 의존 서비스용 compose
- 운영용 파일 기본 골격

학생에게는 핵심 배포 흐름만 직접 구현하게 합니다.

## 이번 시퀀스의 범위

이번 시퀀스에서 다룹니다.

- Dockerfile
- Spring Boot jar 패키징
- 운영 profile
- Docker Compose 운영 실행
- GitHub Actions 기본 배포 흐름
- GitHub Secrets
- EC2 로그 확인

이번 시퀀스에서 다루지 않습니다.

- Kubernetes
- ECS
- Terraform
- Nginx / SSL / 도메인
- 고급 운영 자동화 전체
- 고급 배포 전략

이 부분은 다음 시퀀스 `10-cicd-and-operations-automation`에서 더 깊게 다룹니다.

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
- `09-implementation`: 학생용 starter
- `09-answer`: 정답 브랜치

## 완료 기준

이번 시퀀스는 아래가 모두 맞아야 완료입니다.

- 새 토픽 레포 생성 및 루트 서브모듈 연결
- `main`, `09-implementation`, `09-answer` 브랜치 준비
- starter TODO가 배포 흐름에 맞게 배치됨
- answer 코드가 배포 흐름을 끝까지 완성함
- `./gradlew test`와 `bootJar` 검증 완료
- 루트 README 상태표 갱신 완료
