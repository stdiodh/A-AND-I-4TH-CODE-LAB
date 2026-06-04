# Docs

> 메인 README로 돌아가기: [README](../README.md)

이 디렉터리는 A&I 4기 Code Lab 중앙 허브의 운영 근거를 정리합니다.
중앙 허브는 상세 이론 저장소가 아니라, 커리큘럼 순서와 토픽 레포 운영 기준을 고정하는 문서 시스템입니다.

## 문서 깊이

| Depth | 문서 | 역할 |
| :--- | :--- | :--- |
| 0 | [README](../README.md) | 코드랩 중앙 허브의 목적, 시작 흐름, 현재 상태 |
| 1 | [Docs README](./README.md) | 상세 문서 목차와 증빙 연결 |
| 2 | [Resume Evidence](./resume-evidence.md) | 이력서 문장과 실제 근거 연결 |
| 2 | [Branch Strategy](./branch-strategy.md) | `NN-implementation` / `NN-answer` 학습 흐름 |
| 2 | [Documentation Structure](./documentation-structure.md) | `theory`, `implementation`, `checklist`, `visual-lab` 산출물 기준 |
| 2 | [Curriculum](./curriculum.md) | 시퀀스별 목표, 결과물, 리뷰 포인트 요약 |

## 운영 문서

- [Session Operation](./session-operation.md): 세션 전, 중, 후 운영 흐름
- [Mentor Guide](./mentor-guide.md): 멘토가 준비하고 질문에 대응하는 기준
- [Review Guide](./review-guide.md): 과제 리뷰 우선순위와 diff 기반 피드백 기준
- [Demo Capture](./demo-capture.md): 이미지/GIF 증빙 상태와 수동 촬영 기준

## 테스트와 측정 문서

- [Test](./test.md): 중앙 manifest와 Visual Lab 구조 검증 결과, coverage 미측정 사유
- [Performance Measurement](./performance-measurement.md): 성능 before/after 측정값 여부와 추후 측정 절차
- [Query Tuning](./query-tuning.md): 쿼리 튜닝 후보, 미적용 사유, 추후 `EXPLAIN` 기준

## API 흐름과 실행 증거

이 중앙 허브는 직접 실행되는 API 서버가 아니라 시퀀스와 토픽 레포를 관리하는 문서 허브입니다.
따라서 루트 `docs/api-flows`에는 상세 API 표를 새로 만들지 않았습니다.
API 실행 흐름은 각 토픽 레포의 `README.md`, `docs/implementation.md`, Swagger 경로, 테스트 코드에서 확인합니다.
토픽별 실행 명령과 테스트 명령은 [manifest](./manifest/sequences.yml)의 `runCommand`, `testCommand`, `swaggerPath`를 기준으로 봅니다.

## 기존 기준 문서

- [manifest](./manifest/sequences.yml): 시퀀스별 레포, 브랜치, 실행 명령, 테스트 명령, Visual Lab 위치
- [커리큘럼 마스터 플랜](./curriculum/a-and-i-backend-curriculum-master-plan.md)
- [구현 범위 계획서](./curriculum/a-and-i-backend-implementation-scope-plan.md)
- [시퀀스 실행 프로토콜](./curriculum/sequence-execution-protocol.md)
- [학생 사용법](./student/how-to-use-this-course.md)
- [강사 체크리스트](./instructor/checklist.md)
- [에이전트 작업 규칙](./agent/codex-behavior-guide.md)

## 이 중앙 허브에서 보이는 증거

- 00부터 12까지의 시퀀스를 중앙 manifest와 `docs/sequences`에서 관리합니다.
- 각 토픽 레포는 `main` 안내 브랜치와 `NN-implementation`, `NN-answer` 브랜치 쌍으로 운영합니다.
- 학생은 starter 브랜치에서 구현하고, 완료 후 answer 브랜치와 diff로 비교합니다.
- 문서 산출물은 `README`, `theory`, `implementation`, `checklist`, `visual-lab` 구조로 반복됩니다.
- Repository Integrity workflow가 manifest, README 링크, Visual Lab 구조를 검증합니다.
