# Query Tuning

> 메인 README로 돌아가기: [README](../README.md)

본 문서는 A&I 4기 Code Lab 중앙 허브에서 쿼리 튜닝을 적용할 수 있는지 확인한 결과를 기록합니다.
이번 단계에서는 쿼리 튜닝을 적용하지 않았습니다.

## 대상 쿼리

| 기능 | 쿼리/조건 | 문제 후보 | 근거 |
| :--- | :--- | :--- | :--- |
| 사용자 이메일 조회 | `findByEmail(email)` | 로그인과 계정 복구 흐름에서 반복 조회됩니다. | 토픽 레포 `UserRepository` 메서드 검색 결과 |
| OAuth 사용자 조회 | `findByAuthProviderAndProviderId(provider, providerId)` | 외부 로그인 연결 흐름에서 반복 조회됩니다. | 토픽 레포 `UserRepository` 메서드 검색 결과 |
| 게시글 단건 조회 | `findById(id)` | CRUD 조회, 수정, 삭제 흐름에서 반복 조회됩니다. | 토픽 레포 service/test 검색 결과 |

위 항목은 후보일 뿐입니다.
실제 병목이라고 판단하려면 local/dev DB에서 데이터 크기를 만들고 `EXPLAIN` 또는 `EXPLAIN ANALYZE` 결과를 확인해야 합니다.

## Before

| 지표 | 값 |
| :--- | :--- |
| rows | 측정하지 않음 |
| execution time | 측정하지 않음 |
| index | 측정하지 않음 |
| 근거 | 중앙 허브에는 직접 실행할 DB와 query가 없습니다. |

## 변경 내용

없습니다.

실행 계획이나 동일 환경 before/after 측정값 없이 index를 추가하지 않았습니다.
쓰기 비용, unique 제약, migration 구조를 확인하지 않은 상태에서 튜닝을 적용하면 교육 레포의 starter/answer 흐름을 흔들 수 있습니다.

## After

| 지표 | 값 |
| :--- | :--- |
| rows | 측정하지 않음 |
| execution time | 측정하지 않음 |
| index | 변경 없음 |

## 결과 해석

이번 레포는 중앙 문서 허브이므로 쿼리 튜닝 대상에서 제외했습니다.
토픽 레포에서 튜닝이 필요하면 아래 조건을 먼저 충족해야 합니다.

- 대상 브랜치와 시퀀스를 명확히 정합니다.
- local/dev DB에 재현 가능한 데이터 크기를 준비합니다.
- `EXPLAIN` 또는 `EXPLAIN ANALYZE` 결과를 저장합니다.
- index 추가 전/후의 `rows`, `key`, `Extra`, 실행 시간을 비교합니다.
- 읽기 성능뿐 아니라 쓰기 비용과 unique 제약 영향을 문서화합니다.

## 이력서 반영 가능 여부

- [ ] 동일 환경 before/after 비교다.
- [ ] 측정 명령이 남아 있다.
- [ ] 원본 로그 또는 explain 결과가 남아 있다.
- [ ] 운영 데이터와 synthetic 데이터 차이를 구분했다.

현재는 위 조건을 충족하지 않으므로 query tuning 수치를 이력서에 반영하면 안 됩니다.
