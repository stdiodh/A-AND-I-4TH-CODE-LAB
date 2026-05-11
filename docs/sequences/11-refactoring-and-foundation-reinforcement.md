# 11. 리팩토링과 기초 보강

## 목표

이미 만든 기능의 동작을 보존하면서 layer-based 패키지 구조를 feature-based 구조로 전환합니다.
새 기능을 크게 추가하는 단계가 아니라 책임 분리, 구조 개선, 테스트 기반 검증에 집중합니다.

## 이 시퀀스에서 배우는 것

- 리팩토링은 동작을 바꾸지 않고 구조를 개선하는 작업이라는 점
- layer-based 구조와 feature-based 구조의 차이
- 패키지 이동 단계와 책임 분리 단계 구분
- `post`, `auth`, `account/recovery`, `common` 책임 경계
- common 패키지가 쓰레기통이 되지 않게 관리하는 기준
- 테스트로 동작 보존 확인

## 시작 브랜치

```bash
git checkout 11-implementation
```

## 실습 전 확인

- 토픽 레포: `spring-boot-refactoring-foundation-lab`
- 가이드 브랜치: `main`
- 시작 브랜치: `11-implementation`
- 이전 기준: `10-answer`
- 리팩토링 전 `./gradlew test` 결과를 먼저 확인합니다.

## 구현할 TODO

1. 리팩토링 전 `./gradlew test`를 실행해 현재 동작을 고정합니다.
2. `post` 기능을 `post/api`, `post/application`, `post/domain`, `post/persistence`로 이동합니다.
3. `auth` 기능을 `auth/api`, `auth/application`, `auth/domain`, `auth/persistence`, `auth/security`로 이동합니다.
4. 계정 복구 기능을 `account/recovery/api`, `account/recovery/application`, `account/recovery/mail`로 이동합니다.
5. 공통 예외, validation helper, config를 `common/error`, `common/validation`, `common/config`로 이동합니다.
6. import와 package 경로를 정리합니다.
7. 테스트를 다시 실행해 API 동작이 유지되는지 확인합니다.
8. 테스트가 통과한 뒤 작은 책임 분리를 수행합니다.

## 실행 방법

```bash
docker compose up -d
./gradlew bootRun
```

## 테스트 방법

```bash
./gradlew test
```

리팩토링 전후에 같은 명령을 각각 실행합니다.

테스트가 확인하는 것:

- 리팩토링 전 현재 API 동작을 고정합니다.
- 패키지 구조 변경 후에도 같은 테스트가 통과하는지 확인합니다.
- Controller, Service, Repository 이동이 외부 API 동작을 바꾸지 않았는지 확인합니다.

실패하면 먼저 볼 것:

- 패키지 이동 직후라면 import, package 선언, component scan 범위를 먼저 확인합니다.
- 책임 분리 후 실패했다면 변경 전후 테스트 이름과 실패 케이스를 비교합니다.
- 새 구조를 만들면서 API path, response body, status code를 바꾸지 않았는지 봅니다.

완료 기준:

- 리팩토링 전 `./gradlew test`가 통과합니다.
- 리팩토링 후 `./gradlew test`가 다시 통과합니다.
- API 동작 보존과 패키지 구조 변경을 테스트 결과로 설명할 수 있습니다.

## 확인할 API 또는 화면

- 리팩토링 전후 테스트 결과
- 변경 전 layer-based 구조와 변경 후 feature-based 구조
- `post`, `auth`, `account/recovery`, `common` 패키지
- `common`에 들어간 파일이 정말 공통 책임인지 확인

## 자주 발생하는 문제

- 리팩토링 중 기능을 함께 바꿉니다. 이번 목표는 동작 보존입니다.
- 패키지 이동과 책임 분리를 한 번에 섞습니다. 먼저 이동, 다음 테스트, 그 뒤 작은 책임 분리 순서로 갑니다.
- `common` 패키지에 애매한 파일을 모두 넣습니다. 공통 책임이 분명한 파일만 둡니다.
- 테스트 없이 구조를 바꿉니다. 변경 전후 테스트 결과를 비교합니다.
- 과도한 구조 용어를 외우는 데 집중합니다. 핵심은 변경할 때 볼 파일을 가까이 모으는 것입니다.

## 완료 기준

- 리팩토링 전후 주요 기능 동작이 유지됩니다.
- 패키지 구조가 feature 중심으로 변경되었습니다.
- 순환 의존성이 생기지 않았습니다.
- `common` 패키지가 공통 책임만 담고 있습니다.
- 테스트가 리팩토링 안전망 역할을 합니다.
- `./gradlew test`가 통과합니다.

## 정답과 비교하는 방법

막혔거나 실습을 마친 뒤에만 참고 정답과 비교합니다.

```bash
git diff 11-implementation..11-answer
```

## 다음 시퀀스

다음은 `12. 메시지 큐와 이벤트 기반 사고`입니다.
요청/응답 흐름 위에 이벤트 발행과 처리를 붙입니다.
