# Branch audit 2026-05-02

## 목적

전체 커리큘럼 레포를 시퀀스 운영 규칙 기준으로 점검했습니다.

이번 점검은 코드 내용 검수 전 단계입니다.  
레포별 대표 브랜치와 시퀀스별 `implementation` / `answer` 브랜치가 원격에 존재하는지 확인하는 데 집중했습니다.

## 기준

- 각 토픽 레포는 안내용 `main` 브랜치를 가진다.
- 학생용 브랜치는 `NN-implementation` 형식을 따른다.
- 정답 브랜치는 `NN-answer` 형식을 따른다.
- 루트 레포는 서브모듈 포인터를 각 토픽 레포의 안내 브랜치 기준으로 기록한다.
- 브랜치가 존재하더라도 문서와 코드 내용 정합성은 별도 라운드에서 다시 점검한다.

## 전체 결과

| Repo | Expected branch shape | Current result | Status |
| --- | --- | --- | --- |
| `aandi-prerequisite-bootcamp` | `main`, `00-implementation`, `00-answer` | `implementation`, `answer` | Needs migration |
| `spring-boot-rest-crud-lab` | `main`, `01-implementation`, `01-answer` | `implementation`, `answer` | Needs migration |
| `spring-boot-db-access-lab` | `main`, `02~06 implementation/answer` | Expected branches exist | OK |
| `spring-boot-redis-cache-lab` | `main`, `07-implementation`, `07-answer` | Expected branches exist | OK |
| `spring-boot-realtime-communication-lab` | `main`, `08-implementation`, `08-answer` | Expected branches exist | Needs content check |
| `spring-boot-deployment-runtime-lab` | `main`, `09~10 implementation/answer` | Expected branches exist | OK |
| `spring-boot-refactoring-foundation-lab` | `main`, `11-implementation`, `11-answer` | Expected branches exist | OK |
| `spring-boot-event-driven-lab` | `main`, `12-implementation`, `12-answer` | Expected branches exist | OK |

## 상세 메모

### `aandi-prerequisite-bootcamp`

현재 원격 브랜치:

- `implementation`
- `answer`

문제:

- 안내용 `main` 브랜치가 없습니다.
- `00-implementation`, `00-answer` 이름으로 분리되어 있지 않습니다.
- 원격 HEAD가 `implementation`을 보고 있습니다.

다음 작업:

- `main` 안내 브랜치를 만든다.
- 기존 `implementation`을 `00-implementation`으로 승격한다.
- 기존 `answer`를 `00-answer`로 승격한다.
- 루트 서브모듈 포인터를 새 `main` 기준으로 맞춘다.

### `spring-boot-rest-crud-lab`

현재 원격 브랜치:

- `implementation`
- `answer`

문제:

- 안내용 `main` 브랜치가 없습니다.
- `01-implementation`, `01-answer` 이름으로 분리되어 있지 않습니다.
- 원격 HEAD가 `implementation`을 보고 있습니다.

다음 작업:

- `main` 안내 브랜치를 만든다.
- 기존 `implementation`을 `01-implementation`으로 승격한다.
- 기존 `answer`를 `01-answer`로 승격한다.
- 루트 서브모듈 포인터를 새 `main` 기준으로 맞춘다.

### `spring-boot-db-access-lab`

현재 원격 브랜치:

- `main`
- `02-implementation`, `02-answer`
- `03-implementation`, `03-answer`
- `04-implementation`, `04-answer`
- `05-implementation`, `05-answer`
- `06-implementation`, `06-answer`

메모:

- 원격 기준 브랜치 구조는 기대값과 맞습니다.
- 로컬 서브모듈은 루트 포인터 기준으로 detached 상태일 수 있습니다. 루트 서브모듈에서는 자연스러운 상태입니다.

다음 작업:

- 브랜치 내용 점검 라운드에서 각 브랜치의 문서와 TODO 정합성을 확인합니다.

### `spring-boot-redis-cache-lab`

현재 원격 브랜치:

- `main`
- `07-implementation`
- `07-answer`

메모:

- 브랜치 구조는 기대값과 맞습니다.

다음 작업:

- 브랜치 내용 점검 라운드에서 Redis 캐시 문서와 코드 정합성을 확인합니다.

### `spring-boot-realtime-communication-lab`

현재 원격 브랜치:

- `main`
- `08-implementation`
- `08-answer`

메모:

- 브랜치 구조는 기대값과 맞습니다.
- `08-implementation`, `08-answer`의 최신 원격 커밋 메시지가 `feat(sequence-08): enhance realtime chat demo`입니다.
- 최근 루트 문서 정리와 같은 톤의 문서 보강이 실습 브랜치에 들어갔는지는 내용 점검이 필요합니다.

다음 작업:

- `08-implementation`, `08-answer`의 실제 `docs/*` 내용을 열어 루트 시퀀스 문서와 맞는지 확인합니다.

### `spring-boot-deployment-runtime-lab`

현재 원격 브랜치:

- `main`
- `09-implementation`, `09-answer`
- `10-implementation`, `10-answer`

메모:

- 브랜치 구조는 기대값과 맞습니다.

다음 작업:

- 브랜치 내용 점검 라운드에서 배포와 CI/CD 문서의 역할 구분을 확인합니다.

### `spring-boot-refactoring-foundation-lab`

현재 원격 브랜치:

- `main`
- `11-implementation`
- `11-answer`

메모:

- 브랜치 구조는 기대값과 맞습니다.

다음 작업:

- 브랜치 내용 점검 라운드에서 리팩토링 문서와 정답 코드 정합성을 확인합니다.

### `spring-boot-event-driven-lab`

현재 원격 브랜치:

- `main`
- `12-implementation`
- `12-answer`

메모:

- 브랜치 구조는 기대값과 맞습니다.

다음 작업:

- 브랜치 내용 점검 라운드에서 이벤트 기반 사고와 MSA 관점 설명이 코드 흐름과 맞는지 확인합니다.

## 우선순위

1. `aandi-prerequisite-bootcamp` 브랜치 구조를 `00` 규칙에 맞춘다.
2. `spring-boot-rest-crud-lab` 브랜치 구조를 `01` 규칙에 맞춘다.
3. `spring-boot-realtime-communication-lab`의 `08-implementation`, `08-answer` 내용 최신성을 확인한다.
4. 이후 레포별 내용 점검으로 넘어간다.
