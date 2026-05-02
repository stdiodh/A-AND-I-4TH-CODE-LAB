# 10. 자동화와 운영 흐름

## 시퀀스 목표

이번 시퀀스의 목표는 09에서 한 번 성공시킨 배포를
반복 가능한 자동화 흐름으로 바꾸는 것입니다.

학생은 이번 단계에서 아래 흐름을 이해해야 합니다.

1. 코드가 변경된다.
2. build가 실행된다.
3. test가 실행된다.
4. deploy가 실행된다.
5. 마지막에 verify가 실행된다.

즉, 이번 시퀀스의 핵심은
GitHub Actions + build/test/deploy/verify + 배포 스크립트 분리입니다.

## 이번 시퀀스에서 다시 설명해야 하는 기초 개념

이번 10 시퀀스는 `09`까지 배포 가능한 앱과 기본 EC2 배포 흐름이 준비된 상태에서 시작합니다.
그래서 학생이 아래 기초 개념을 다시 이해해야 합니다.

- `CI`
  코드를 합치기 전에 build와 test를 반복해서 확인하는 흐름
- `CD`
  검증된 결과를 실제 실행 환경까지 전달하는 흐름
- `workflow`
  언제 어떤 순서로 작업을 실행할지 정의한 자동화 파일
- `script`
  서버에서 실제로 어떤 명령을 수행할지 담은 실행 파일
- `artifact`
  build 결과물과 배포에 필요한 파일 묶음
- `verify`
  배포 직후 상태와 응답을 다시 확인하는 단계
- `failure gate`
  앞 단계가 실패하면 다음 단계로 넘어가지 않게 막는 지점

즉, 이번 시퀀스는 "자동화가 돈다"에서 끝나지 않고
"어디서 실패를 막고 어디서 성공을 판단하는가"까지 이해하는 단계입니다.

## 현재 코드 흐름에서 어디를 봐야 하는가

이번 시퀀스는 배포를 사람이 아니라 파일과 자동화 흐름이 대신 반복하게 만드는 단계입니다.

1. `.github/workflows/ci.yml`
   build와 test를 먼저 거는 시작점
2. `.github/workflows/deploy.yml`
   artifact, 원격 전달, verify 흐름이 이어지는 파일
3. `scripts/deploy.sh`
   서버에서 실제 재배포 순서를 담당하는 스크립트
4. `scripts/check-deploy.sh`
   배포 직후 상태를 확인하는 스크립트

짧게 말하면 이번 시퀀스는

- `변경 감지 -> build -> test -> deploy -> verify`
- `workflow는 순서를 묶고, script는 실제 작업을 수행`

흐름을 함께 이해하는 단계입니다.

## 이전 시퀀스와의 연결

- 시작 기준: `09-answer`
- 시작 레포: `spring-boot-deployment-runtime-lab`
- 실제 10 실습 레포: `spring-boot-deployment-runtime-lab`

이번 시퀀스는 새 앱을 만드는 단계가 아닙니다.
이미 배포 가능한 앱 위에서 반복되는 배포 단계를 더 일관되게 만드는 데 집중합니다.

## 이번 시퀀스의 실무 확장 개념

이번 10 시퀀스의 실무 확장 개념은 아래 두 가지입니다.

- 배포 검증 단계
- 실패 차단 지점

핵심은 이렇습니다.

- 자동화는 “명령이 많다”보다 “순서가 흔들리지 않는다”가 더 중요합니다.
- build가 실패하면 test로 못 가고, test가 실패하면 deploy로 못 가야 합니다.
- deploy가 끝났어도 verify가 실패하면 “배포 성공”이라고 부르면 안 됩니다.

즉, 이번 시퀀스는 “자동 배포 버튼”을 만드는 것이 아니라
"어디서 실패를 막고 어디서 성공을 판정할지"를 정하는 단계입니다.

## 학생이 직접 구현할 순서

구현 순서는 반드시 아래 순서를 따릅니다.

1. workflow 파일 구조를 읽는다.
2. build step을 채운다.
3. test step을 채운다.
4. deploy step을 연결한다.
5. verify 단계를 점검한다.

## 문제 상황과 해결 방향을 코드로 보기

### 문제 1. test 없이 바로 deploy하면 왜 위험한가

처음에는 아래처럼 바로 배포하는 흐름이 빨라 보일 수 있습니다.

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - run: ./gradlew bootJar
      - run: bash scripts/deploy.sh
```

하지만 이 구조는 아래 문제가 있습니다.

- 테스트가 깨져도 배포로 넘어갈 수 있습니다.
- 깨진 코드를 운영 서버에서 처음 발견할 수 있습니다.

### 해결 방향 1. build와 test를 먼저 고정한다

```yaml
jobs:
  build_and_test:
    runs-on: ubuntu-latest
    steps:
      - run: ./gradlew test bootJar
```

이 흐름이면 최소한 “실행 가능하고 테스트를 통과한 결과물”만 다음 단계로 넘어갑니다.

### 문제 2. workflow 안에 모든 명령을 길게 적으면 왜 관리가 어려워지는가

```yaml
- name: Deploy
  run: |
    docker compose down || true
    docker build -t app:latest .
    docker compose up -d
    docker logs --tail 50 app
    curl --fail http://localhost:8080/
```

이 방식은 처음에는 한 파일에 다 보여서 편해 보일 수 있습니다.
하지만 실제로는 아래 문제가 생깁니다.

- 원격 서버에서 무슨 작업을 하는지 읽기 어려워집니다.
- 배포 로직만 수정하고 싶어도 workflow 전체를 건드려야 합니다.
- verify와 deploy의 책임이 섞입니다.

### 해결 방향 2. workflow와 script의 책임을 나눈다

```yaml
- name: Deploy on EC2
  run: |
    ssh ... "bash scripts/deploy.sh"

- name: Verify deployment on EC2
  run: |
    ssh ... "bash scripts/check-deploy.sh"
```

이 구조면 workflow는 순서를 묶고,
script는 서버에서 실제 작업을 담당합니다.

### 문제 3. deploy가 끝났다고 바로 성공이라고 보면 왜 위험한가

`docker compose up -d`가 끝났다고 해서
애플리케이션이 실제로 정상 동작하는 것은 아닙니다.

실제로는 아래가 그 직후에 터질 수 있습니다.

- 컨테이너는 떴지만 앱은 죽음
- DB 연결 실패
- 포트 충돌
- 루트 경로 응답 실패

### 해결 방향 3. verify를 별도 단계로 둔다

```bash
docker compose --env-file .env -f deploy/compose.prod.yaml ps
docker logs --tail 50 aandi-app
curl --fail --silent http://localhost:8080/ >/dev/null
```

이번 시퀀스에서는 verify를 “있으면 좋은 옵션”이 아니라
"배포 성공 판정의 마지막 단계"로 다뤄야 합니다.

## 학생이 직접 수정하는 핵심 파일

- `.github/workflows/ci.yml`
- `.github/workflows/deploy.yml`
- `scripts/deploy.sh`
- `scripts/check-deploy.sh`

TODO는 위 네 파일에 집중합니다.

## 학생이 최종적으로 이해해야 하는 것

- 수동 배포와 자동 배포의 차이
- CI와 CD를 입문 수준에서 구분하는 감각
- workflow와 shell script의 역할 차이
- build/test/deploy/verify가 왜 이 순서로 이어져야 하는지
- verify 단계가 왜 자동화의 일부여야 하는지

## 제공 전제로 두는 것

- 09에서 만든 배포 가능한 앱
- Dockerfile과 prod profile
- 운영용 compose 파일
- GitHub Secrets 이름 규칙
- workflow 기본 틀
- 스크립트 위치와 기본 구조

학생에게는 핵심 자동화 흐름만 직접 구현하게 합니다.

## 이번 시퀀스의 범위

이번 시퀀스에서 다룹니다.

- GitHub Actions 기본 CI 흐름
- build / test / deploy / verify 연결
- deploy 명령을 shell script로 분리하는 구조
- 배포 후 상태 확인 자동화

이번 시퀀스에서 다루지 않습니다.

- reusable workflow
- matrix build
- self-hosted runner
- Blue-Green / Canary 전략
- Kubernetes / Helm / Terraform
- 고급 운영 자동화 전체

이 부분은 이후 별도 도메인으로 다루는 것이 더 적절합니다.

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
- `10-implementation`: 학생용 starter
- `10-answer`: 정답 브랜치

## 완료 기준

이번 시퀀스는 아래가 모두 맞아야 완료입니다.

- `10-implementation`, `10-answer`, `main` 브랜치 준비
- starter TODO가 workflow와 script에 맞게 배치됨
- answer 코드가 build/test/deploy/verify 흐름을 끝까지 완성함
- `./gradlew test` 검증 완료
- shell script 문법 검증 완료
- 루트 README 상태표 갱신 완료
