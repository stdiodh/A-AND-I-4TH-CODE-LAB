# 10. 자동화와 운영 흐름

## 목표

한 번 성공한 배포 흐름을 GitHub Actions와 스크립트로 반복 가능하게 만듭니다.
workflow의 성공/실패 기준을 build, test, deploy, verify 단계로 나눠 확인합니다.

## 이 시퀀스에서 배우는 것

- CI와 CD의 차이
- workflow가 실행되는 조건
- build와 test를 먼저 고정하는 이유
- deploy script와 verify script의 역할
- 실패 차단 지점과 성공 판정 기준

## 시작 브랜치

```bash
git checkout 10-implementation
```

## 실습 전 확인

- 토픽 레포: `spring-boot-deployment-runtime-lab`
- 가이드 브랜치: `main`
- 시작 브랜치: `10-implementation`
- 이전 기준: `09-answer`
- GitHub Actions와 Secrets 설정은 실제 운영 값이 아니라 안전한 예시 이름으로 문서화합니다.

## 구현할 TODO

1. CI workflow 구조를 읽습니다.
2. build step을 채웁니다.
3. test step을 채웁니다.
4. deploy workflow에서 artifact와 배포 순서를 확인합니다.
5. `scripts/deploy.sh` 역할을 확인합니다.
6. `scripts/check-deploy.sh`로 verify 단계를 확인합니다.
7. 실패 시 다음 단계로 넘어가지 않는지 확인합니다.

## 실행 방법

```bash
./gradlew test bootJar
```

## 테스트 방법

```bash
./gradlew test
```

배포 전 검증 명령:

```bash
./gradlew test bootJar
```

테스트가 확인하는 것:

- workflow 성공 케이스에서 build, test, deploy, verify 순서가 지켜지는지 확인합니다.
- workflow 실패 케이스에서 실패한 step 이후 단계가 실행되지 않는지 확인합니다.
- 배포 전 로컬 검증 명령이 CI의 build/test 기준과 맞는지 확인합니다.

실패하면 먼저 볼 것:

- GitHub Actions 로그에서 처음 실패한 step을 먼저 엽니다.
- secret 값 자체가 아니라 secret 이름과 주입 위치가 맞는지 확인합니다.
- deploy 실패와 verify 실패를 구분해서 봅니다.

완료 기준:

- workflow 성공 케이스를 설명할 수 있습니다.
- workflow 실패 케이스와 차단 지점을 설명할 수 있습니다.
- 배포 전 검증 명령이 로컬에서 통과합니다.

## 확인할 API 또는 화면

- GitHub Actions workflow 실행 결과
- build/test job 성공 여부
- deploy job 실행 순서
- verify job 또는 verify script 결과
- 실패한 step에서 workflow가 멈추는지 확인

## 자주 발생하는 문제

- test 없이 deploy로 바로 넘어갑니다. 배포 전 검증이 먼저 와야 합니다.
- workflow 안에 모든 배포 명령을 길게 넣습니다. 반복 로직은 script로 분리합니다.
- deploy가 끝나면 성공이라고 판단합니다. verify 단계에서 컨테이너 상태, 로그, HTTP 응답을 확인합니다.
- GitHub Secrets 값을 workflow 파일에 직접 적습니다. secret 이름만 참조합니다.

## 완료 기준

- build와 test가 deploy보다 먼저 실행됩니다.
- deploy script와 verify script의 역할이 분리되어 있습니다.
- workflow 실패 시 다음 단계로 넘어가지 않습니다.
- verify 단계가 배포 성공 판정에 포함됩니다.
- `./gradlew test`가 통과합니다.

## 정답과 비교하는 방법

막혔거나 실습을 마친 뒤에만 참고 정답과 비교합니다.

```bash
git diff 10-implementation..10-answer
```

## 다음 시퀀스

다음은 `11. 리팩토링과 기초 보강`입니다.
동작을 보존하면서 구조를 읽기 쉽게 다듬습니다.
