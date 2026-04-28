# 10. 자동화와 운영 흐름

## 이 시퀀스의 목적

이번 시퀀스는 09에서 한 번 성공시킨 배포를
반복 가능한 자동화 흐름으로 바꾸는 단계입니다.

학생은 이번 단계에서 아래 흐름을 이해해야 합니다.

1. 코드가 변경된다.
2. build가 실행된다.
3. test가 실행된다.
4. deploy가 실행된다.
5. 마지막에 verify가 실행된다.

즉, 이번 시퀀스의 핵심은
**GitHub Actions + build/test/deploy/verify + 배포 스크립트 분리**입니다.

## 이전 시퀀스와의 연결

- 시작 기준: `09-answer`
- 시작 레포: `spring-boot-deployment-runtime-lab`
- 실제 10 실습 레포: `spring-boot-deployment-runtime-lab`

이번 시퀀스는 새 앱을 만드는 단계가 아닙니다.
이미 배포 가능한 앱 위에서 반복되는 배포 단계를 더 일관되게 만드는 데 집중합니다.

## 학생이 직접 구현할 순서

구현 순서는 반드시 아래 순서를 따릅니다.

1. workflow 파일 구조를 읽는다.
2. build step을 채운다.
3. test step을 채운다.
4. deploy step을 연결한다.
5. 배포 후 확인 단계를 점검한다.

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
