# A&I 4기 Code Lab Central Hub

이 저장소는 A&I 백엔드 커리큘럼 전체를 운영하기 위한 중앙 허브입니다.
실제 실습 산출물을 한 저장소에 계속 누적하는 본체가 아니라, 시퀀스 순서와 생성 기준을 고정하는 통제 레포로 사용합니다.

## 이 레포의 목적

- 커리큘럼 전체 방향을 흔들리지 않게 유지합니다.
- `docs/sequences`의 순서를 기준으로 토픽 레포 생성 순서를 고정합니다.
- Codex가 먼저 읽어야 할 중앙 문서와 가이드를 고정합니다.
- 각 시퀀스의 구현 범위와 산출물 기준을 중앙에서 관리합니다.
- 현재 작업 상태와 다음 작업 대상을 기록합니다.
- 시퀀스별 진행 단위를 `1 sequence = 1 branch = 1 PR`로 유지합니다.

중앙 `docs`는 상세 이론 저장소가 아닙니다.
상세 이론과 실습 문서는 각 토픽 레포 안에서 작성하고, 이 저장소는 운영 기준과 생성 순서를 관리합니다.

## 작업 공간 기준

- 로컬 작업 기준 루트: 이 저장소의 루트 디렉터리
- 중앙 운영 문서 위치: `./docs`
- 시퀀스 기준 문서 위치: `./docs/sequences`
- 가이드 문서 위치: `./docs/guides`
- 커리큘럼 기준 문서 위치: `./docs/curriculum`

Codex는 항상 이 저장소 루트를 현재 작업 기준점으로 보고 문서를 읽어야 합니다.

## Source Of Truth

아래 세 가지가 중앙 기준입니다.

1. `README.md`
2. `docs/curriculum/*`
3. `docs/sequences/*`

특히 시퀀스 순서와 범위 판단의 최종 기준은 `docs/sequences`입니다.
중앙 문서에 없는 범위를 Codex가 임의로 추가하면 안 됩니다.

## 작업 전 필독 문서

Codex는 작업 전에 아래 문서를 반드시 읽어야 합니다.
이 순서를 건너뛰면 안 됩니다.

1. `README.md`
2. `docs/curriculum/a-and-i-backend-curriculum-master-plan.md`
3. `docs/curriculum/a-and-i-backend-implementation-scope-plan.md`
4. `docs/curriculum/codex-implementation-playbook.md`
5. `docs/curriculum/sequence-execution-protocol.md`
6. `docs/guides/implementation-writing-guide.md`
7. `docs/guides/theory-writing-guide.md`
8. `docs/guides/theory-doc-template.md`
9. `docs/guides/checklist-writing-guide.md`
10. 현재 작업 대상인 `docs/sequences/0X-...md`
11. 해당 토픽 레포의 `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, starter 코드

문서 종류별 강제 기준은 아래와 같습니다.

- `theory.md`: `docs/guides/theory-doc-template.md`, `docs/guides/theory-writing-guide.md`를 반드시 따릅니다.
- `implementation.md`: `docs/guides/implementation-writing-guide.md`를 반드시 따릅니다.
- `checklist.md`: `docs/guides/checklist-writing-guide.md`를 반드시 따릅니다.
- 전체 구조와 범위 판단: `docs/curriculum/*`, `docs/sequences/*`를 반드시 따릅니다.
- 시퀀스 실행 순서와 브랜치/레포 규칙: `docs/curriculum/sequence-execution-protocol.md`를 반드시 따릅니다.
- 서브모듈 대표 브랜치 운영 규칙: 각 서브모듈의 `main` 브랜치는 레포 요약/문서 안내 브랜치로 유지합니다.

## Codex 작업 원칙

Codex는 아래 원칙을 반드시 지켜야 합니다.

1. 작업 시작 전에 루트 `README.md`와 중앙 `docs`를 먼저 읽습니다.
2. 한 번에 하나의 시퀀스만 작업합니다.
3. 현재 시퀀스 문서 외 다른 시퀀스는 무시합니다.
4. 다음 시퀀스는 사용자 승인 전 절대 진행하지 않습니다.
5. 과한 범위 확장, 선행 구현, 예고 생성 작업을 하지 않습니다.
6. 생성 전에 현재 상태와 목표 산출물을 먼저 요약합니다.
7. 구현 문서는 `docs/guides/implementation-writing-guide.md`를 따릅니다.
8. 이론 문서는 `docs/guides/theory-writing-guide.md`와 `docs/guides/theory-doc-template.md`를 따릅니다.
9. 체크리스트는 `docs/guides/checklist-writing-guide.md`를 따릅니다.
10. 상세 이론은 중앙 `docs`에 다시 쓰지 않고 각 토픽 레포 내부 문서에서만 작성합니다.
11. 생성 후에는 README 링크, 진행 상태, 체크리스트 반영 여부를 다시 점검합니다.
12. 문서 기준이 모호하거나 사용자 의도를 정확히 이해하지 못하면 추측하지 말고 질문합니다.
13. 작업 범위가 크거나 여러 단계로 나뉘면, 실행 전에 계획서를 먼저 보여줍니다.
14. 학습 주제가 분명히 갈라지면 같은 레포에서 선택형으로 섞지 않고 별도 레포로 분리합니다.
15. 현재 시퀀스 문서에서 벗어나는 구현, 문서, 예시를 임의로 추가하지 않습니다.
16. 각 서브모듈 레포의 `main` 브랜치에는 레포 소개, 문서 안내, 브랜치 안내가 있어야 합니다.

## 문서 참조 순서

Codex는 아래 순서로만 중앙 문서를 읽고 작업합니다.

1. `docs/curriculum/a-and-i-backend-curriculum-master-plan.md`
2. `docs/curriculum/a-and-i-backend-implementation-scope-plan.md`
3. `docs/curriculum/codex-implementation-playbook.md`
4. `docs/curriculum/sequence-execution-protocol.md`
5. `docs/guides/implementation-writing-guide.md`
6. `docs/guides/theory-writing-guide.md`
7. `docs/guides/theory-doc-template.md`
8. `docs/guides/checklist-writing-guide.md`
9. `docs/sequences/0X-...md`
10. 해당 토픽 레포의 `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, starter 코드

추가 규칙도 함께 고정합니다.

- `implementation.md`를 쓸 때는 결과보다 순서를 먼저 보여줘야 합니다.
- `theory.md`를 쓸 때는 정의보다 문제 상황과 코드 연결을 먼저 보여줘야 합니다.
- `checklist.md`를 쓸 때는 학생용과 강사용을 반드시 분리해야 합니다.
- 문서 작성 중 범위 판단이 흔들리면 시퀀스 문서로 다시 돌아갑니다.
- 큰 작업은 바로 구현에 들어가지 않고 계획서부터 사용자에게 보여줘야 합니다.
- Codex가 사용자 요청을 제대로 이해하지 못했다고 판단되면 먼저 질문해야 합니다.
- 시퀀스 작업 순서는 `docs/curriculum/sequence-execution-protocol.md`를 기준으로 고정합니다.
- 각 브랜치의 `docs/*`는 반드시 그 시퀀스 주제에 맞게 바뀌어야 하며, 이전 시퀀스 문서를 그대로 재사용하면 안 됩니다.
- 각 서브모듈의 `main` 브랜치는 실습 브랜치가 아니라 안내 브랜치이며, 학생/강사가 들어와도 어떤 브랜치로 가야 하는지 바로 알 수 있어야 합니다.

## 현재 작업 상태

- Current sequence: `12-message-queue-and-event-driven-thinking`
- Status: `DONE`
- Last completed sequence: `12-message-queue-and-event-driven-thinking`
- Next sequence: `-`

| Sequence | Status | Repo | Docs Ready | Code Ready | Review |
| --- | --- | --- | --- | --- | --- |
| 00 | DONE | `aandi-prerequisite-bootcamp` | Y | Y | Y |
| 01 | DONE | `spring-boot-rest-crud-lab` | Y | Y | Y |
| 02 | DONE | `spring-boot-db-access-lab` | Y | Y | Y |
| 03 | DONE | `spring-boot-db-access-lab` | Y | Y | Y |
| 04 | DONE | `spring-boot-db-access-lab` | Y | Y | Y |
| 05 | DONE | `spring-boot-db-access-lab` | Y | Y | Y |
| 06 | DONE | `spring-boot-db-access-lab` | Y | Y | Y |
| 07 | DONE | `spring-boot-redis-cache-lab` | Y | Y | Y |
| 08 | DONE | `spring-boot-realtime-communication-lab` | Y | Y | Y |
| 09 | DONE | `spring-boot-deployment-runtime-lab` | Y | Y | Y |
| 10 | DONE | `spring-boot-deployment-runtime-lab` | Y | Y | Y |
| 11 | DONE | `spring-boot-refactoring-foundation-lab` | Y | Y | Y |
| 12 | DONE | `spring-boot-event-driven-lab` | Y | Y | Y |

상태 값은 아래 의미로 사용합니다.

- `READY`: 현재 시퀀스를 시작할 수 있는 상태
- `IN_PROGRESS`: 현재 시퀀스 레포 생성 또는 보정 작업 중
- `REVIEW`: 문서/코드 산출물이 나왔고 검토 대기 중
- `DONE`: 완료 조건을 모두 충족했고 다음 시퀀스로 넘어갈 수 있는 상태
- `BLOCKED`: 앞선 시퀀스 승인 전에는 시작하지 않는 상태

## 시퀀스 완료 조건

각 시퀀스는 아래 항목이 모두 준비되어야 `DONE`으로 표시합니다.

- `README.md`
- `docs/theory.md`
- `docs/implementation.md`
- `docs/answer-guide.md`
- `docs/checklist.md`
- `docs/assets.md`
- starter 코드
- answer 기준 검토 완료
- README 링크 정리 완료

필수 산출물이 하나라도 빠지면 `DONE`으로 올리지 않습니다.

## 작업 단위 규칙

큰 작업일수록 단위를 잘라서 운영합니다.

- 시퀀스 1개당 Codex 작업 1회
- 시퀀스 1개당 브랜치 1개
- 시퀀스 1개당 PR 1개

권장 브랜치 이름 예시는 아래와 같습니다.

- `sequence/00-prerequisite-bootcamp`
- `sequence/01-request-response-and-memory-crud`
- `sequence/02-persistence-and-layered-architecture`

각 토픽 레포는 시퀀스별로 아래 브랜치 구조를 유지합니다.

- `main`
- `NN-implementation`
- `NN-answer`

예:

- `main`
- `02-implementation`, `02-answer`
- `03-implementation`, `03-answer`

여기서 `main`은 아래 역할을 맡습니다.

- 이 레포가 어떤 시퀀스를 담는지 요약
- 어떤 문서가 있는지 안내
- 학생이 시작할 브랜치와 강사가 비교할 브랜치 안내
- 시퀀스 맵 또는 브랜치 맵 제공

## 토픽 레포 운영 전략

토픽 레포는 시퀀스별로 무조건 새로 만드는 것이 아니라, 도메인 기준으로 관리합니다.

### 레포 이름 규칙

레포 이름은 주차명이 아니라 도메인이 바로 보이게 짓습니다.

- `spring-boot-rest-crud-lab`
- `spring-boot-db-access-lab`
- `spring-boot-safe-request-handling-lab`
- `spring-boot-auth-jwt-lab`

### 새 레포를 만드는 경우

아래 조건이면 새 토픽 레포를 만드는 편이 좋습니다.

- 학습 도메인이 분명히 달라질 때
- 선택형 주제가 아니라 별도 트랙으로 운영해야 할 때
- starter 구조와 answer 구조가 크게 달라질 때
- 독립 실습으로 운영하는 편이 더 자연스러울 때

### 기존 레포를 재사용하는 경우

아래 조건이면 기존 토픽 레포를 재사용합니다.

- 주제가 이어지는 연속 실습일 때
- 같은 도메인 안에서 구현 범위만 확장될 때
- answer 비교 기준을 한 레포 안에서 유지하는 편이 더 쉬울 때

이 경우에는 새 레포를 만들기보다 브랜치와 PR 단위로 분리합니다.

- 기능 단위 브랜치
- 시퀀스 단위 브랜치
- PR 단위 검토 기록

### GitHub 반영 순서

토픽 레포 작업은 아래 순서로 진행합니다.

1. 로컬에서 토픽 레포를 정비합니다.
2. GitHub 원격 레포를 생성하거나 기존 레포를 확인합니다.
3. `main` 브랜치에 레포 요약과 브랜치 안내를 구성합니다.
4. `NN-implementation` / `NN-answer` 브랜치를 푸시합니다.
5. 중앙 허브 루트에 같은 이름의 디렉터리로 서브모듈을 연결합니다.
6. 중앙 README 상태 표에 연결 결과를 반영합니다.

즉, 중앙 허브는 토픽 레포의 소유자이자 연결 지점이고, 실제 실습 산출물은 각 토픽 레포가 맡습니다.

현재 연결된 토픽 레포:

- `aandi-prerequisite-bootcamp`: 시퀀스 00 선수지식 부트캠프 레포
- `spring-boot-rest-crud-lab`: 시퀀스 01 실습 레포
- `spring-boot-db-access-lab`: 시퀀스 02~06 실습 레포, `main` 안내 브랜치와 `02~06` 시퀀스 브랜치 운영
- `spring-boot-redis-cache-lab`: 시퀀스 07 실습 레포, Redis cache-aside 시퀀스 전용 레포
- `spring-boot-realtime-communication-lab`: 시퀀스 08 실습 레포, WebSocket/STOMP 실시간 통신 전용 레포
- `spring-boot-deployment-runtime-lab`: 시퀀스 09~10 실습 레포, Docker/배포/CI-CD 시퀀스 레포
- `spring-boot-refactoring-foundation-lab`: 시퀀스 11 실습 레포, 리팩토링과 기초 보강 전용 레포
- `spring-boot-event-driven-lab`: 시퀀스 12 실습 레포, RabbitMQ 기반 이벤트 발행/소비 전용 레포

## 표준 작업 프로토콜

매 시퀀스 작업은 아래 순서로 진행합니다.

1. 루트 `README.md`에서 현재 시퀀스를 확인합니다.
2. `docs/curriculum/sequence-execution-protocol.md`를 다시 확인합니다.
3. 해당 시퀀스 문서를 읽고 이번 범위를 확정합니다.
4. 이번 작업 범위와 목표 산출물을 짧게 요약합니다.
5. `NN-implementation`, `NN-answer` 브랜치 전략을 확정합니다.
6. 문서를 생성하거나 교체합니다.
7. starter 코드를 생성하거나 보정합니다.
8. answer 기준을 검토합니다.
9. 루트 `README.md`의 상태를 갱신합니다.
10. 작업을 멈추고 사용자 승인 대기를 합니다.

다음 시퀀스로 자동 진행하면 안 됩니다.

## 토픽 레포 필수 산출물

각 시퀀스 토픽 레포는 아래 구조를 반드시 갖춰야 합니다.

- `README.md`
- `docs/theory.md`
- `docs/implementation.md`
- `docs/answer-guide.md`
- `docs/checklist.md`
- `docs/assets.md`
- starter 코드
- answer 기준 설명 또는 비교 기준

작성 기준은 아래와 같습니다.

- 구현 문서는 손의 순서를 보여줘야 합니다.
- 이론 문서는 기억 복구와 코드 연결을 먼저 도와야 합니다.
- README는 실습 안내와 진입 흐름 중심으로 씁니다.
- TODO는 결과 나열이 아니라 순서형 힌트여야 합니다.

## 금지 사항

아래 항목은 중앙 허브 운영 규칙상 금지합니다.

- 여러 시퀀스를 한 번에 생성하지 않습니다.
- 다음 시퀀스를 미리 만들지 않습니다.
- 중앙 문서를 무시하고 바로 코드부터 만들지 않습니다.
- 시퀀스 문서 범위를 벗어난 기능을 추가하지 않습니다.
- 상세 이론을 중앙 `docs`에 다시 쓰지 않습니다.
- 이론 문서와 구현 문서를 서로 섞지 않습니다.
- 민감한 실제 값이나 비밀 정보를 하드코딩하지 않습니다.
- 상태 갱신 없이 다음 단계로 넘어가지 않습니다.

README에 아래 문장을 운영 규칙으로 고정합니다.

- Codex는 현재 시퀀스 외 문서를 생성하지 않는다.
- Codex는 다음 시퀀스를 미리 작업하지 않는다.
- Codex는 중앙 docs에 없는 범위를 추가하지 않는다.
- Codex는 이론 문서와 구현 문서를 서로 섞지 않는다.
- Codex는 상세 이론을 중앙 docs에 다시 쓰지 않는다.
- Codex는 생성 전에 현재 상태와 목표 산출물을 먼저 요약한다.

## 중앙 운영 문서 링크

- [커리큘럼 마스터 플랜](./docs/curriculum/a-and-i-backend-curriculum-master-plan.md)
- [구현 범위 계획서](./docs/curriculum/a-and-i-backend-implementation-scope-plan.md)
- [Codex Implementation Playbook](./docs/curriculum/codex-implementation-playbook.md)
- [구현 문서 작성 가이드](./docs/guides/implementation-writing-guide.md)
- [이론 문서 작성 가이드](./docs/guides/theory-writing-guide.md)
- [이론 문서 템플릿](./docs/guides/theory-doc-template.md)
- [체크리스트 작성 가이드](./docs/guides/checklist-writing-guide.md)

## 시퀀스 문서 링크

- [00. 선수지식 부트캠프](./docs/sequences/00-prerequisite-bootcamp.md)
- [01. 요청-응답과 메모리 CRUD](./docs/sequences/01-request-response-and-memory-crud.md)
- [02. 영속성 저장과 계층 분리](./docs/sequences/02-persistence-and-layered-architecture.md)
- [03. 안전한 요청 처리](./docs/sequences/03-safe-request-handling.md)
- [04. 인증과 JWT](./docs/sequences/04-authentication-and-jwt.md)
- [05. 외부 인증 또는 이메일 인증](./docs/sequences/05-external-authentication-or-email-verification.md)
- [06. 테스트와 검증](./docs/sequences/06-testing-and-verification.md)
- [07. 캐시와 Redis](./docs/sequences/07-caching-and-redis.md)
- [08. 실시간 통신](./docs/sequences/08-realtime-communication.md)
- [09. 배포와 실행 환경](./docs/sequences/09-deployment-and-runtime-environment.md)
- [10. 자동화와 운영 흐름](./docs/sequences/10-cicd-and-operations-automation.md)
- [11. 리팩토링과 기초 보강](./docs/sequences/11-refactoring-and-foundation-reinforcement.md)
- [12. 이벤트 기반 사고 확장](./docs/sequences/12-message-queue-and-event-driven-thinking.md)

## 다음 작업 시작점

현재 중앙 허브 기준 `00 ~ 12` 시퀀스 정리가 완료된 상태입니다.
새 트랙을 추가하거나 기존 시퀀스를 다시 손보기 전에는 반드시 이 README와 중앙 `docs`를 다시 읽고,
이번 턴의 목표 산출물 목록을 먼저 요약한 뒤 진행합니다.
