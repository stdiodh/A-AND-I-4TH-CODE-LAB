# A&I 백엔드 커리큘럼 마스터 플랜

## 문서 목적

이 문서는 A&I 백엔드 커리큘럼의 전체 운영 방향을 고정하는 중앙 기준 문서입니다.

이 문서의 역할은 아래와 같습니다.

1. 커리큘럼의 핵심 학습 흐름을 흔들리지 않게 유지합니다.
2. 도메인 순서형 문서 체계를 기준으로 실습 레포 생성 순서를 고정합니다.
3. 중앙 `docs`가 이론 저장소가 아니라 운영 문서 역할을 하도록 기준을 명확히 합니다.

중앙 `docs`는 상세 이론을 저장하는 공간이 아닙니다.
상세 이론은 각 토픽 레포 내부 문서에서 다루고, 중앙 문서는 구현 범위와 진행 순서를 고정하는 역할만 맡습니다.

---

## 중앙 문서 구조

```text
docs/
├── curriculum/
│   ├── a-and-i-backend-curriculum-master-plan.md
│   ├── a-and-i-backend-implementation-scope-plan.md
│   ├── codex-implementation-playbook.md
│   └── sequence-execution-protocol.md
│
├── guides/
│   ├── implementation-writing-guide.md
│   ├── theory-writing-guide.md
│   ├── theory-doc-template.md
│   └── checklist-writing-guide.md
│
└── sequences/
    ├── 00-prerequisite-bootcamp.md
    ├── 01-request-response-and-memory-crud.md
    ├── 02-persistence-and-layered-architecture.md
    ├── 03-safe-request-handling.md
    ├── 04-authentication-and-jwt.md
    ├── 05-external-authentication-or-email-verification.md
    ├── 06-testing-and-verification.md
    ├── 07-caching-and-redis.md
    ├── 08-realtime-communication.md
    ├── 09-deployment-and-runtime-environment.md
    ├── 10-cicd-and-operations-automation.md
    ├── 11-refactoring-and-foundation-reinforcement.md
    └── 12-message-queue-and-event-driven-thinking.md
```

---

## 핵심 운영 원칙

### 1. 초반은 백엔드 기능 흐름 이해에 집중합니다

초반부는 아래 흐름만 선명하게 잡히면 됩니다.

1. 요청이 들어온다.
2. 서비스가 처리한다.
3. 저장하거나 조회한다.
4. 응답을 돌려준다.

초반에는 운영 개념보다 기능 흐름이 먼저 와닿아야 합니다.

### 2. Swagger는 초반 실습 확인 도구로 사용합니다

Swagger는 초반부터 붙여두되, 깊게 가르치지 않습니다.

초반 Swagger의 역할은 아래와 같습니다.

- API를 직접 실행해볼 수 있게 해주기
- 요청/응답 예시를 빠르게 확인하게 해주기
- 학생이 전체 API 그림을 한 번에 보게 해주기

### 3. 환경 분리와 로그는 배포 단계에서 묶어 설명합니다

환경변수, profile, 로그는 운영 상황이 있어야 필요성이 바로 이해됩니다.

따라서 아래 개념은 `09`, `10` 도메인에서 다룹니다.

- 환경 분리
- 로그 확인
- 운영 설정
- 배포 자동화

### 4. 중앙 문서는 주차명이 아니라 도메인 순서로 봅니다

중앙 문서는 `week13`, `week14`처럼 읽지 않습니다.

아래처럼 도메인 순서로 읽습니다.

- 요청-응답과 메모리 CRUD
- 영속성 저장과 계층 분리
- 안전한 요청 처리
- 인증과 JWT
- 테스트와 검증
- 캐시와 Redis
- 실시간 통신
- 배포와 실행 환경
- 자동화와 운영 흐름
- 리팩토링과 기초 보강
- 이벤트 기반 사고 확장

### 4-1. 주제가 달라지면 레포도 분리합니다

한 시퀀스 안에서 선택형으로 보일 수 있는 주제라도,
실제 학습 흐름과 starter 구조가 크게 달라지면 별도 레포로 분리합니다.

예:

- OAuth2 로그인
- Email Verification

이 둘은 같은 "인증 확장" 범주에 있어도
학생이 따라치는 코드, 설정, 설명 구조가 달라지므로
동일 레포에서 선택형으로 오래 유지하지 않는 것을 원칙으로 합니다.

### 5. 루트 README를 작업 통제 문서로 사용합니다

Codex는 항상 루트 `README.md`를 먼저 읽고 아래를 확인합니다.

- 현재 시퀀스
- 현재 상태
- 다음 작업 대상
- 금지 사항
- 완료 조건

즉, README는 소개문이 아니라 작업 통제 문서 역할을 맡습니다.

그리고 Codex는 작업을 시작하기 전에
README에 적힌 필독 문서 순서를 먼저 확인해야 합니다.

### 6. 시퀀스별 브랜치와 문서는 함께 움직여야 합니다

각 시퀀스는 아래 브랜치 쌍으로 운영하는 것을 기본으로 합니다.

- `NN-implementation`
- `NN-answer`

그리고 브랜치가 바뀌면 아래 문서도 같이 바뀌어야 합니다.

- `README.md`
- `docs/theory.md`
- `docs/implementation.md`
- `docs/answer-guide.md`
- `docs/checklist.md`
- `docs/assets.md`

즉, `02`의 이론 문서와 `03`의 이론 문서가 같은 내용으로 남아 있으면 안 됩니다.
문서도 시퀀스 순서에 따라 계속 갱신되어야 합니다.

### 7. 서브모듈 `main` 브랜치는 대표 안내 브랜치로 둡니다

각 서브모듈 레포의 `main` 브랜치는
그 레포의 대표 안내 브랜치로 유지합니다.

`main`에는 아래가 있어야 합니다.

- 레포가 다루는 주제 요약
- 문서 목록
- 시퀀스 브랜치 목록
- 학생 시작 브랜치와 강사 비교 브랜치 안내

즉, 루트 레포의 `README`가 중앙 허브 안내 역할을 하듯,
서브모듈의 `main`도 해당 레포의 진입 안내 역할을 해야 합니다.

---

## 도메인 순서 맵

### 00. 선수지식 부트캠프

HTTP, JSON, Postman, Git/GitHub, DB 기초

### 01. 요청-응답과 메모리 CRUD

REST API + CRUD + Swagger

### 02. 영속성 저장과 계층 분리

JPA Basics + Layered Architecture + CRUD 확장

### 03. 안전한 요청 처리

DTO + Validation + Exception Handling

### 04. 인증과 JWT

Spring Security + JWT

### 05. 외부 인증 또는 이메일 인증

OAuth2 또는 Email Verification

### 06. 테스트와 검증

Testing Basics

### 07. 캐시와 Redis

Redis Caching

### 08. 실시간 통신

WebSocket

### 09. 배포와 실행 환경

Docker + AWS Deploy Basics + 환경 분리 + 로그 확인

### 10. 자동화와 운영 흐름

CI/CD + 운영 자동화

### 11. 리팩토링과 기초 보강

종합 리팩토링 + 구조 보강 + 테스트 보강

### 12. 이벤트 기반 사고 확장

Message Queue + Event-Driven Architecture + MSA 관점 소개

---

## 권장 학습 흐름

1. 00에서 선수지식을 맞춥니다.
2. 01에서 요청과 응답 흐름을 가장 단순하게 경험합니다.
3. 02에서 영속 저장과 계층 분리를 연결합니다.
4. 03에서 안전한 입력 처리와 실패 대응을 정리합니다.
5. 04와 05에서 사용자 인증 흐름을 확장합니다.
6. 06에서 이미 만든 기능을 테스트로 검증합니다.
7. 07과 08에서 통신/성능 확장 주제를 경험합니다.
8. 09와 10에서 운영 환경과 자동화를 다룹니다.
9. 11에서 전체 기본기를 다시 정리합니다.
10. 12에서 큰 구조를 가볍게 시야 확장용으로 소개합니다.

---

## 최종 기준

좋은 중앙 문서는 이론을 많이 담는 문서가 아니라,
Codex와 강사가 같은 순서와 같은 기준으로 움직이게 만드는 문서입니다.
