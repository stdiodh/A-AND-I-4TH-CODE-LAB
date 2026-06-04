# Performance Measurement

> 메인 README로 돌아가기: [README](../README.md)

본 문서는 A&I 4기 Code Lab 중앙 허브에서 성능 측정값을 이력서 근거로 사용할 수 있는지 확인한 결과를 기록합니다.
이 저장소는 직접 실행되는 API 서버가 아니라 교육 운영 문서와 서브레포 manifest를 관리하는 중앙 허브입니다.

## 현재 before/after 측정값 여부

현재 before/after 측정값은 없습니다.

| 항목 | 상태 | 사유 |
| :--- | :--- | :--- |
| API latency | 미측정 | 루트 저장소에 실행 대상 API 서버가 없습니다. |
| throughput | 미측정 | 루트 저장소에 부하 테스트 대상 서비스가 없습니다. |
| query latency | 미측정 | 루트 저장소에 직접 실행할 DB query가 없습니다. |
| alert detection time | 미측정 | 이 레포는 운영 모니터링 서버가 아닙니다. |

## 측정 환경 확인

| 항목 | 값 |
| :--- | :--- |
| 측정일 | 2026-06-04 |
| 기준 commit | `e4e0f1f` |
| OS | `Darwin Mac 25.4.0 arm64` |
| benchmark 도구 | `hey`, `k6`, `wrk` 명령을 찾지 못했습니다. |

확인 명령:

```bash
git rev-parse --short HEAD
uname -a
command -v hey || true
command -v k6 || true
command -v wrk || true
```

## 측정 명령

실제 성능 측정 명령은 실행하지 않았습니다.
측정 대상 서버, 데이터 크기, warm-up 조건, 동시 요청 수가 없기 때문입니다.

대신 아래 기준을 확인했습니다.

```bash
[ -f gradlew ] && echo root-gradlew-present || echo root-gradlew-missing
[ -f build.gradle.kts ] && echo root-gradle-build-present || echo root-gradle-build-missing
```

결과:

```text
root-gradlew-missing
root-gradle-build-missing
```

## API 또는 query 후보

중앙 허브 자체에는 성능 측정 대상 API가 없습니다.
실제 API와 query 후보는 각 토픽 레포에 있습니다.

| 구분 | 위치 | 상태 |
| :--- | :--- | :--- |
| REST CRUD API | `spring-boot-rest-crud-lab` | 토픽 레포에서 별도 측정 필요 |
| JPA CRUD/API | `spring-boot-db-access-lab` | 토픽 레포에서 별도 측정 필요 |
| Redis cache-aside | `spring-boot-redis-cache-lab` | 캐시 hit/miss 조건을 만든 뒤 별도 측정 필요 |
| WebSocket/STOMP | `spring-boot-realtime-communication-lab` | 메시지 송수신 기준을 정한 뒤 별도 측정 필요 |
| Docker/CI/CD | `spring-boot-deployment-runtime-lab` | GitHub Actions 또는 배포 환경 로그가 필요 |
| Event Driven | `spring-boot-event-driven-lab` | RabbitMQ local/dev 환경과 메시지 수가 필요 |

## 이력서 반영 가능 여부

- 바로 반영 가능: 문서/manifest/Visual Lab 구조 검증을 자동화했다는 정성 문장
- 반영 금지: latency, throughput, p95, query count, 성능 개선률

성능 수치를 이력서에 쓰려면 동일 환경의 before/after commit, 데이터 크기, 실행 명령, 원본 로그가 필요합니다.

## 추후 측정 절차

1. 측정할 토픽 레포와 브랜치를 정합니다.
2. 테스트 데이터 크기와 DB 종류를 기록합니다.
3. 서버 실행 명령과 warm-up 절차를 고정합니다.
4. `hey`, `k6`, `wrk` 중 하나를 설치하거나 사용 가능한 도구를 정합니다.
5. 같은 환경에서 before/after commit을 각각 측정합니다.
6. 원본 로그와 요약값을 이 문서에 연결합니다.
