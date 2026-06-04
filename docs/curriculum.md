# Curriculum

> 메인 README로 돌아가기: [README](../README.md)

이 문서는 포트폴리오 관점에서 4기 Code Lab 커리큘럼 구조를 요약합니다.
상세 범위 판단은 [커리큘럼 마스터 플랜](./curriculum/a-and-i-backend-curriculum-master-plan.md), [구현 범위 계획서](./curriculum/a-and-i-backend-implementation-scope-plan.md), [manifest](./manifest/sequences.yml)를 기준으로 합니다.

## 운영 목표

- 백엔드 입문자가 요청, 처리, 저장, 검증, 인증, 운영 흐름을 순서대로 경험하게 합니다.
- 각 시퀀스는 독립 실습이면서 이전 시퀀스의 개념을 이어받습니다.
- 실습 레포는 `NN-implementation` starter와 `NN-answer` 비교 브랜치로 분리합니다.
- 중앙 허브는 상세 이론보다 시퀀스 순서, 브랜치 규칙, 문서 산출물 기준을 관리합니다.

## 시퀀스 요약

| Sequence | 주제 | 토픽 레포 | 실습 결과물 | 리뷰 포인트 |
| :--- | :--- | :--- | :--- | :--- |
| 00 | 선수지식 부트캠프 | `aandi-prerequisite-bootcamp` | HTTP, JSON, Postman, Git, DB 기본 흐름 | 기본 도구와 요청/응답 용어를 설명할 수 있는가 |
| 01 | 요청/응답과 메모리 CRUD | `spring-boot-rest-crud-lab` | Spring Boot REST CRUD starter/answer | Controller, Service, Repository 흐름을 구분하는가 |
| 02 | 영속성 저장과 계층 분리 | `spring-boot-db-access-lab` | MySQL/JPA 기반 CRUD | 메모리 저장과 DB 저장 차이를 설명하는가 |
| 03 | 안전한 요청 처리 | `spring-boot-db-access-lab` | DTO, Validation, 예외 응답 | 실패 요청을 안전하게 막고 응답하는가 |
| 04 | 인증과 JWT | `spring-boot-db-access-lab` | 회원가입, 로그인, JWT 인증 | 공개 API와 보호 API 차이를 설명하는가 |
| 05 | 외부 인증과 계정 복구 | `spring-boot-db-access-lab` | OAuth2/SMTP 계정 복구 흐름 | 민감정보를 노출하지 않고 외부 연동을 설명하는가 |
| 06 | 테스트와 검증 | `spring-boot-db-access-lab` | 정상/실패 케이스 테스트 | 테스트가 무엇을 검증하는지 말할 수 있는가 |
| 07 | 캐시와 Redis | `spring-boot-redis-cache-lab` | cache-aside 조회 흐름 | DB와 캐시 역할, TTL, 무효화를 구분하는가 |
| 08 | 실시간 통신 | `spring-boot-realtime-communication-lab` | WebSocket/STOMP 흐름 | 연결, 구독, 메시지 발행 흐름을 설명하는가 |
| 09 | 배포와 실행 환경 | `spring-boot-deployment-runtime-lab` | Docker, AWS 배포 기본 | 환경 분리와 로그 확인 흐름을 이해하는가 |
| 10 | 자동화와 운영 흐름 | `spring-boot-deployment-runtime-lab` | CI/CD와 배포 스크립트 | 자동화가 어떤 반복 작업을 줄이는지 설명하는가 |
| 11 | 리팩토링과 기초 보강 | `spring-boot-refactoring-foundation-lab` | 구조 정리와 테스트 보강 | 기능 유지와 구조 개선을 분리해 리뷰하는가 |
| 12 | 메시지 큐와 이벤트 기반 사고 | `spring-boot-event-driven-lab` | RabbitMQ 기반 발행/소비 흐름 | 동기 처리와 비동기 이벤트 흐름 차이를 설명하는가 |

## 필수 개념 묶음

- 요청 흐름: HTTP, JSON, Controller, Service, Response
- 데이터 흐름: Entity, Repository, JPA, DB, DTO
- 안전성: Validation, Exception Handling, 인증, 민감정보 관리
- 검증: 단위 테스트, 실패 케이스, 실행 명령, CI 검증
- 운영: Docker, 배포 환경, 로그, 자동화, 메시지 큐

## 실습 결과물 기준

각 시퀀스는 아래 산출물을 기본 기준으로 봅니다.

- 학생 시작용 `NN-implementation` 브랜치
- 강사용 비교용 `NN-answer` 브랜치
- 학생이 먼저 읽는 `README.md`
- 개념과 코드 흐름을 연결하는 `docs/theory.md`
- 손으로 구현할 순서를 보여주는 `docs/implementation.md`
- 학생/강사용 확인 항목을 나누는 `docs/checklist.md`
- 흐름을 시각화하는 `docs/visual-lab/*`
