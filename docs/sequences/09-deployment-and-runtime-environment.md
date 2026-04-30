# 09. 배포와 실행 환경

## 이 시퀀스의 목적

이번 시퀀스는 이전까지 만든 Spring Boot 애플리케이션을
로컬 개발 환경 밖으로 옮겨보는 첫 배포 실습입니다.

학생은 이번 단계에서 아래 흐름을 이해해야 합니다.

1. 실행 가능한 앱을 하나의 배포 단위로 묶는다.
2. 운영 환경 설정을 코드 밖으로 분리한다.
3. GitHub Actions와 Secrets를 이용해 EC2로 전달한다.
4. 배포 후 로그로 실제 기동 상태를 확인한다.

즉, 이번 시퀀스의 핵심은
Docker + prod profile + GitHub Actions 기본 배포 + Secrets + 로그 확인입니다.

## 이전 시퀀스와의 연결

- 시작 기준: `08-answer`
- 시작 레포: `spring-boot-realtime-communication-lab`
- 실제 09 실습 레포: `spring-boot-deployment-runtime-lab`

이번 시퀀스는 08에서 완성한 앱을 다시 구현하는 단계가 아닙니다.
이미 동작하는 앱을 운영 환경으로 옮기는 흐름에만 집중합니다.

## 학생이 직접 구현할 순서

구현 순서는 반드시 아래 순서를 따릅니다.

1. `Dockerfile` 핵심 줄을 채운다.
2. `application-prod.yaml`로 운영 설정을 분리한다.
3. `compose.prod.yaml`로 운영 실행 구성을 확인한다.
4. `deploy.yml`에서 GitHub Actions 배포 흐름을 완성한다.
5. GitHub Secrets를 연결하고, 배포 후 로그를 확인한다.

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
