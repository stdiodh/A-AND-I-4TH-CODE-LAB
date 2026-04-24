# 시퀀스 실행 프로토콜

## 문서 목적

이 문서는 A&I 백엔드 커리큘럼에서
각 시퀀스를 어떤 순서로 작업해야 하는지 고정하는 실행 프로토콜입니다.

핵심 목표는 아래와 같습니다.

1. 시퀀스마다 같은 순서로 작업하게 합니다.
2. 브랜치 구조와 레포 분리 기준이 흔들리지 않게 합니다.
3. 학생용 starter와 정답용 answer가 항상 분리되게 합니다.
4. 각 브랜치의 문서가 반드시 그 시퀀스 내용만 설명하게 합니다.
5. 각 서브모듈의 `main` 브랜치가 안내 브랜치 역할을 하게 합니다.

---

## 가장 중요한 원칙

### 1. 시퀀스마다 `NN-implementation`, `NN-answer` 브랜치를 만듭니다

예:

- `02-implementation`
- `02-answer`
- `03-implementation`
- `03-answer`

학생은 `NN-implementation`에서 시작하고,
강사는 `NN-answer`를 비교 기준으로 사용합니다.

### 1-1. 각 서브모듈 레포는 `main` 브랜치를 안내 브랜치로 둡니다

서브모듈 레포의 `main` 브랜치는 실습 starter 브랜치가 아닙니다.
이 브랜치는 그 레포의 대표 안내 브랜치로 사용합니다.

`main`에는 아래가 있어야 합니다.

- 이 레포가 다루는 주제 요약
- 어떤 문서가 있는지 안내
- 어떤 시퀀스 브랜치가 있는지 안내
- 학생이 시작할 브랜치와 정답 비교 브랜치 안내
- 필요하면 `docs/branch-guide.md` 또는 `docs/sequence-map.md`

즉, 사용자는 서브모듈 레포의 `main`에 들어오면
"이 레포는 무엇을 다루고, 어디로 가야 하는가"를 바로 이해할 수 있어야 합니다.

### 2. 주제가 달라지면 다른 Git 레포를 만듭니다

같은 레포 안에서 확장하기보다,
학습 주제가 분명히 달라지면 별도 토픽 레포를 만듭니다.

예:

- `spring-boot-db-access-lab`
- `spring-boot-safe-request-handling-lab`
- `spring-boot-auth-jwt-lab`

또는 현재처럼 연속 실습을 위해 한 레포를 유지하더라도,
주제가 완전히 갈라지면 같은 레포 안의 선택형 구조로 오래 끌고 가지 않습니다.

### 3. `implementation`에는 TODO를 넣고, `answer`에는 완성본을 둡니다

- `NN-implementation`
  - 학생이 직접 따라칠 수 있는 starter
  - 중요한 코드에 순서형 TODO 포함
- `NN-answer`
  - 완성된 정답 코드
  - 강사용 비교 기준

### 4. 각 브랜치의 docs는 반드시 그 시퀀스에 맞게 바뀌어야 합니다

가장 중요한 금지 규칙은 아래입니다.

- `02`의 이론 문서와 `03`의 이론 문서가 같은 내용이면 안 됩니다.
- `03-implementation`의 `docs/theory.md`가 `02` 설명을 담으면 안 됩니다.
- `NN-answer`도 `NN-implementation`과 같은 시퀀스 주제를 설명해야 합니다.

즉, 브랜치가 바뀌면 `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, `docs/answer-guide.md`, `docs/assets.md`도 함께 바뀌어야 합니다.

---

## 시퀀스 작업 고정 순서

아래 순서는 모든 시퀀스에서 공통으로 지킵니다.

### Step 1. 현재 시퀀스를 확정합니다

먼저 아래를 읽습니다.

1. 루트 `README.md`
2. `docs/curriculum/*`
3. `docs/guides/*`
4. 현재 시퀀스의 `docs/sequences/0X-...md`

현재 시퀀스 외 작업은 하지 않습니다.

### Step 2. 기존 레포를 재사용할지, 새 레포를 만들지 결정합니다

판단 기준:

- 이전 시퀀스와 같은 도메인 흐름이면 기존 레포 재사용
- 주제가 달라지면 새 레포 생성

이 단계에서 애매하면 바로 질문하고,
추측으로 레포 구조를 정하지 않습니다.

### Step 3. 시퀀스 브랜치를 만듭니다

각 토픽 레포에는 아래 두 브랜치를 만듭니다.

- `main`
- `NN-implementation`
- `NN-answer`

그리고 `NN+1-implementation`은 반드시 `NN-answer` 기준에서 시작합니다.

### Step 4. 학생용 starter 구조를 만듭니다

`NN-implementation`에서는 아래를 만듭니다.

- `README.md`
- `docs/theory.md`
- `docs/implementation.md`
- `docs/answer-guide.md`
- `docs/checklist.md`
- `docs/assets.md`
- starter 코드

starter 코드는 실행 가능해야 하고,
핵심 코드에는 학생이 따라칠 수 있는 TODO가 있어야 합니다.

### Step 4-1. `main` 브랜치에 안내 문서를 맞춥니다

각 토픽 레포의 `main` 브랜치에는 아래가 있어야 합니다.

- `README.md`
- 필요 시 `docs/branch-guide.md`
- 필요 시 `docs/sequence-map.md`

그리고 아래를 반드시 설명해야 합니다.

- 이 레포가 다루는 시퀀스 범위
- 문서 목록
- `NN-implementation`, `NN-answer` 브랜치 사용법
- 학생 시작 브랜치와 강사 비교 브랜치

### Step 5. 정답 구조를 만듭니다

`NN-answer`에서는 아래를 맞춥니다.

- 같은 시퀀스를 설명하는 `README.md`
- 같은 시퀀스를 설명하는 `docs/*`
- 완성된 answer 코드

문서는 starter와 같은 시퀀스를 설명해야 하며,
정답 코드만 달라져야 합니다.

### Step 6. 문서가 진짜 그 시퀀스를 설명하는지 검증합니다

아래를 반드시 확인합니다.

- `README.md`가 이전 시퀀스 설명을 끌고 오지 않는가
- `docs/theory.md`가 현재 시퀀스 핵심 개념을 설명하는가
- `docs/implementation.md`가 학생 손의 순서를 보여주는가
- `docs/checklist.md`가 학생용/강사용으로 분리되어 있는가
- `docs/answer-guide.md`가 현재 시퀀스 정답만 설명하는가

### Step 7. 코드와 문서가 함께 맞는지 검증합니다

아래를 확인합니다.

- starter TODO 위치가 문서 설명과 맞는가
- answer 코드가 answer-guide와 맞는가
- 실행 기준이 문서와 맞는가
- 테스트나 부팅 확인이 가능한가

### Step 8. 루트 README 상태를 갱신합니다

시퀀스 완료 후에는 루트 `README.md`에 아래를 반영합니다.

- 현재 완료한 시퀀스
- 다음 시퀀스
- 상태표의 `Docs Ready`, `Code Ready`, `Review`
- 연결된 토픽 레포 상태

즉, 작업 완료 사실은 반드시 루트 README에 남겨야 합니다.

### Step 9. 토픽 레포는 서브모듈로 루트에 남깁니다

다른 레포에서 작업했더라도,
중앙 허브에는 서브모듈로 연결 상태를 남깁니다.

즉, 중앙 허브는 아래를 기억해야 합니다.

- 어떤 시퀀스가 어떤 토픽 레포를 쓰는지
- 어떤 서브모듈 경로로 연결되어 있는지
- 어떤 브랜치를 기준으로 보는지
- 해당 토픽 레포의 `main`이 안내 브랜치로 준비되어 있는지

### Step 10. 다음 시퀀스로 자동 진행하지 않습니다

시퀀스 하나가 끝나면 멈추고,
사용자 승인 후 다음 시퀀스로 갑니다.

---

## 문서 작성 규칙

### `theory.md`

- 반드시 `docs/guides/theory-doc-template.md`
- 반드시 `docs/guides/theory-writing-guide.md`

를 따릅니다.

### `implementation.md`

- 반드시 `docs/guides/implementation-writing-guide.md`

를 따릅니다.

### `checklist.md`

- 반드시 `docs/guides/checklist-writing-guide.md`

를 따릅니다.

---

## TODO 규칙

좋은 TODO는 아래 조건을 만족해야 합니다.

- 순서가 보인다
- 중요한 코드에만 있다
- 학생이 다음 손동작을 바로 알 수 있다
- 문법 설명보다 흐름 설명이 먼저 나온다

예:

```kotlin
// TODO 1. 요청 DTO의 title 값이 비어 있는지 검증하세요.
// TODO 2. 비어 있다면 요청 초입에서 막히게 하세요.
// TODO 3. 검증 실패 응답이 어디서 만들어지는지도 함께 확인하세요.
```

---

## 완료 기준

한 시퀀스는 아래가 모두 준비되어야 완료로 봅니다.

- `NN-implementation` 브랜치 준비
- `NN-answer` 브랜치 준비
- `main` 브랜치의 레포 요약/브랜치 안내 준비
- 각 브랜치의 `README.md`와 `docs/*`가 현재 시퀀스 내용으로 교체됨
- starter TODO 준비
- answer 코드 준비
- 실행 또는 테스트 검증 완료
- 루트 `README.md` 상태 갱신 완료
- 필요 시 서브모듈 연결 상태 반영 완료

---

## 최종 기준

시퀀스 작업은 "코드를 만든다"에서 끝나지 않습니다.
레포 분리, 브랜치 분리, TODO starter, answer, 시퀀스별 docs 교체, 루트 README 기록, 서브모듈 연결까지 모두 포함되어야 완료입니다.
