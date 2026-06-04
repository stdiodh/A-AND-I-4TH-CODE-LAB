# Resume Evidence

> 메인 README로 돌아가기: [README](../README.md)

이 문서는 이력서 문장과 저장소 안에서 확인 가능한 근거를 연결합니다.
확인되지 않은 수강생 수, 완주율, 만족도, 성능 개선률은 작성하지 않습니다.

## 이력서 연결 요약

| 이력서 문장 | README 위치 | 상세 근거 | 검증 상태 |
| :--- | :--- | :--- | :--- |
| 4기 백엔드 코드랩을 중앙 허브, 시퀀스 문서, manifest 기준으로 운영 가능하게 구조화했습니다. | [포트폴리오 관점 요약](../README.md#포트폴리오-관점-요약) | [manifest](./manifest/sequences.yml), [curriculum](./curriculum.md) | 문서와 파일 기준 확인 |
| 학생은 `NN-implementation`에서 실습하고 `NN-answer`와 diff로 비교하는 학습 흐름을 구성했습니다. | [학생 실습 시작 흐름](../README.md#학생-실습-시작-흐름) | [branch strategy](./branch-strategy.md), [branch policy](./instructor/branch-policy.md) | 문서 기준 확인 |
| `theory`, `implementation`, `checklist`, `visual-lab` 구조로 실습 자료 산출물을 표준화했습니다. | [Minimal Sequence Documentation Rule](../README.md#minimal-sequence-documentation-rule) | [documentation structure](./documentation-structure.md), [visual lab rules](./agent/visual-lab-rules.md) | 문서 기준 확인 |
| 다음 기수도 재사용할 수 있도록 세션 운영, 멘토 대응, 리뷰 기준을 문서화했습니다. | [문서 입구](../README.md#문서-입구) | [session operation](./session-operation.md), [mentor guide](./mentor-guide.md), [review guide](./review-guide.md) | 문서 기준 확인 |
| Repository Integrity workflow로 manifest와 Visual Lab 구조 검증을 자동화했습니다. | [Source Of Truth](../README.md#source-of-truth) | [.github/workflows/repository-integrity.yml](../.github/workflows/repository-integrity.yml), [agent repository rules](./agent/repository-rules.md) | workflow 파일 기준 확인 |

## 바로 사용할 수 있는 문장

- A&I 4기 백엔드 코드랩 중앙 허브를 구성해 00~12 시퀀스, 토픽 레포, 브랜치 전략, 문서 산출물 기준을 한 저장소에서 관리했습니다.
- 학생이 `NN-implementation` 브랜치에서 실습하고 `NN-answer` 브랜치와 diff로 비교하는 학습 흐름을 설계했습니다.
- `theory`, `implementation`, `checklist`, `visual-lab` 문서 구조를 표준화해 다음 기수도 재사용할 수 있는 교육 운영 기준을 남겼습니다.
- manifest와 Repository Integrity workflow를 사용해 시퀀스 문서, 브랜치명 규칙, Visual Lab 구조를 검증하는 운영 체계를 만들었습니다.

## 수치 검증 후 사용할 문장

- [ ] 수강생 수: [확인 필요]
- [ ] 완주율: [확인 필요]
- [ ] 만족도: [확인 필요]
- [ ] 온보딩 시간 변화: [측정 필요]
- [ ] line coverage: [측정 필요]
- [ ] branch coverage: [측정 필요]
- [ ] p95 latency before/after: [측정 필요]
- [ ] query count before/after: [측정 필요]
- [ ] alert detection time before/after: [측정 필요]

현재 before/after 측정값은 없습니다.
이 저장소와 토픽 레포의 `build.gradle.kts`, workflow, scripts에서 coverage 도구 설정은 확인되지 않았습니다.

## 아직 쓰면 안 되는 표현

- 수강생 수를 확인된 근거 없이 작성한 문장
- 완주율을 확인된 근거 없이 작성한 문장
- 만족도를 확인된 근거 없이 작성한 문장
- 온보딩 시간 단축률을 측정 없이 작성한 문장
- 커버리지 수치를 리포트 없이 작성한 문장
- 성능 개선률을 before/after 측정 없이 작성한 문장
- 장애 대응 시간 단축률을 기록 없이 작성한 문장
- 처리량 개선 배수를 측정 없이 작성한 문장

## 근거 링크

| 구분 | 위치 | 설명 |
| :--- | :--- | :--- |
| 코드 | [토픽 레포 목록](../README.md#토픽-레포-운영-전략) | 실제 실습 코드는 중앙 허브가 아니라 토픽 레포에 있습니다. |
| 테스트 | [manifest](./manifest/sequences.yml) | 각 시퀀스의 `testCommand`를 관리합니다. |
| 테스트 실행 결과 | [Test](./test.md) | 중앙 manifest와 Visual Lab 구조 검증 결과를 기록합니다. |
| CI | [Repository Integrity workflow](../.github/workflows/repository-integrity.yml) | manifest, README 링크, Visual Lab 구조 검증을 실행합니다. |
| 문서 | [Docs README](./README.md) | 포트폴리오 증빙 문서 목차입니다. |
| 브랜치 | [Branch Strategy](./branch-strategy.md) | `NN-implementation` / `NN-answer` 운영 기준입니다. |
| 성능 측정 | [Performance Measurement](./performance-measurement.md) | 현재 before/after 측정값이 없으며 추후 측정 조건을 기록합니다. |
| 쿼리 튜닝 | [Query Tuning](./query-tuning.md) | 실행 계획 없는 index/쿼리 변경을 하지 않은 근거를 기록합니다. |
| 커밋/PR | [현재 작업 상태](../README.md#현재-작업-상태) | 시퀀스별 완료 상태를 중앙 README에서 관리합니다. |

## 제한 사항

- 이 저장소에는 수강생 수, 완주율, 만족도 수치가 없습니다.
- 이번 문서 정리는 백엔드 교육 운영 시스템 증빙이므로 성능 측정값이나 커버리지 수치를 새로 만들지 않았습니다.
- 중앙 허브 자체의 런타임 API가 없어 `docs/api-flows` 상세 API 문서는 만들지 않았습니다. API 흐름은 각 토픽 레포의 `README.md`, `docs/implementation.md`, Swagger 경로, 테스트 코드에서 확인해야 합니다.
- 이 레포는 교육 문서 허브이므로 커버리지 개선과 쿼리 튜닝은 원칙적으로 제외했습니다. 실제 수치가 필요하면 각 토픽 레포에서 별도 리포트와 실행 계획을 만들어야 합니다.
- 실제 수업 운영 수치가 필요하면 별도 출석/설문/평가 자료와 연결한 뒤 이 문서를 갱신해야 합니다.
