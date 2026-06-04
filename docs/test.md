# Test

> 메인 README로 돌아가기: [README](../README.md)

본 문서는 A&I 4기 Code Lab 중앙 허브에서 실제로 실행한 테스트와 커버리지 확인 결과를 기록합니다.
이 저장소는 직접 실행되는 애플리케이션이 아니라 시퀀스, manifest, Visual Lab 구조를 관리하는 문서 허브입니다.
따라서 이번 단계에서는 토픽 레포의 운영 코드나 테스트 코드를 변경하지 않았습니다.

## 측정 기준

| 항목 | 값 |
| :--- | :--- |
| 측정일 | 2026-06-04 |
| 기준 commit | `e4e0f1f` |
| Python | `Python 3.9.6` |
| 루트 Gradle wrapper | 없음 |
| 루트 `build.gradle.kts` | 없음 |
| coverage 도구 설정 | 확인되지 않음 |

## 실행한 테스트 명령

| 명령 | 결과 | 근거 |
| :--- | :--- | :--- |
| `python3 scripts/validate-manifest.py` | 통과 | `PASS: 4 check group(s), 0 issue(s), 0 warning group(s)` |
| `python3 scripts/validate-visual-labs.py` | 통과 | `PASS: 8 repo group(s), 0 issue(s), 0 warning group(s)` |
| `python3 -m py_compile scripts/validate-manifest.py scripts/validate-visual-labs.py` | 통과 | 출력 없음, exit code 0 |

## 테스트 개수

이 저장소에는 일반적인 unit test runner가 없습니다.
대신 GitHub Actions의 Repository Integrity workflow가 아래 검증 스크립트를 실행합니다.

- `scripts/validate-manifest.py`: manifest, sequence 문서, README 링크, 루트 금지 경로를 검증합니다.
- `scripts/validate-visual-labs.py`: 서브레포 Visual Lab 허브와 시퀀스 상세 페이지 구조를 검증합니다.

따라서 테스트 개수는 unit test case 수가 아니라 validator check group 기준으로 기록합니다.

| 검증 | check group |
| :--- | :--- |
| manifest/docs/readme/root | 4 |
| Visual Lab repo group | 8 |

## 커버리지 결과

| 항목 | Before | After | 근거 |
| :--- | :--- | :--- | :--- |
| line coverage | 미측정 | 미측정 | 루트 Gradle 프로젝트와 coverage 도구 설정이 없습니다. |
| branch coverage | 미측정 | 미측정 | `jacoco`, `kover`, coverage 관련 설정이 확인되지 않았습니다. |

이번 단계의 작업 지시서에서 `A-AND-I-4TH-CODE-LAB`은 교육 문서 레포로 분류되어 커버리지 개선과 쿼리 튜닝이 원칙적으로 제외됩니다.
커버리지를 높이기 위한 테스트를 추가하지 않았고, threshold나 exclude 패턴도 변경하지 않았습니다.

## 추가한 테스트

없습니다.

이 단계에서는 운영 코드나 테스트 코드를 변경하지 않았습니다.
중앙 허브에서 의미 있는 검증은 manifest와 Visual Lab 구조 검증이므로 기존 validator 실행 결과를 근거로 남겼습니다.

## 아직 부족한 영역

- 토픽 레포별 line/branch coverage는 각 토픽 레포의 `NN-implementation` 또는 `NN-answer` 브랜치에서 별도로 측정해야 합니다.
- 커버리지 수치를 이력서에 쓰려면 각 토픽 레포에 JaCoCo 또는 Kover 리포트 생성 설정이 필요합니다.
- 단, coverage gate는 현재 교육 레포 운영 기준에 없으므로 무리하게 추가하지 않습니다.

## 추후 측정 절차

토픽 레포에서 coverage 수치가 필요할 때는 아래 순서로 별도 작업합니다.

1. 대상 토픽 레포와 브랜치를 명확히 정합니다.
2. 기존 테스트가 통과하는지 `./gradlew test`로 확인합니다.
3. JaCoCo 또는 Kover 리포트 생성을 추가할지 별도 PR 범위로 합의합니다.
4. `build/reports/jacoco/test/jacocoTestReport.xml` 또는 Kover XML에서 line/branch coverage를 추출합니다.
5. before/after 수치와 리포트 파일 경로를 이 문서와 [Resume Evidence](./resume-evidence.md)에 연결합니다.
