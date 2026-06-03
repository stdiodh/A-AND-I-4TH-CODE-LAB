# A&I 4기 Code Lab Repository Quality Sweep

## 1. 작업 시작 상태

- 기준 루트: `AandI_4rdPeriod_code_lab`
- 기준 문서: `docs/manifest/sequences.yml`, `docs/sequences/*`
- 사전 감사 문서: `docs/audit/prework-repository-inventory.md`
- 이번 작업 원칙: 커리큘럼 순서 유지, 문서 수 증가 금지, Visual Lab 4파일 스펙 유지, implementation 브랜치 정답 노출 금지

초기 검증과 동기화에서 확인한 내용:

- `git submodule update --init --recursive` 실행
- `git submodule foreach 'git fetch --all --prune'` 실행
- `python3 scripts/validate-manifest.py` 통과
- `python3 scripts/validate-visual-labs.py` 통과
- SEQ 01 `spring-boot-rest-crud-lab` main Visual Lab/legacy 문서 정리 후 `./gradlew test` 통과
- SEQ 01 `01-implementation` 문서 정답 노출 제거 후 `./gradlew test` 통과

현재까지 생성하고 원격에 반영한 커밋:

| 위치 | 브랜치 | 커밋 | 내용 |
|---|---|---|---|
| `spring-boot-rest-crud-lab` | `main` | `405e1d1` | SEQ 01 legacy 문서 축소와 Visual Lab 4파일 스펙 정리 |
| `spring-boot-rest-crud-lab-01-implementation-worktree` | `01-implementation` | `f7edadc` | starter 문서의 answer 브랜치명/정답 안내 노출 제거 |
| `spring-boot-event-driven-lab` | `main` | `809df6a` | SEQ 12 Visual Lab 스펙 정리와 main legacy 정답 가이드 축소 |
| `spring-boot-refactoring-foundation-lab` | `main` | `4cc498d` | SEQ 11 main 문서 범위 복구와 Visual Lab 스펙 정리 |
| `spring-boot-redis-cache-lab` | `main` | `6d306f0` | SEQ 07 main Visual Lab 스펙 정리와 guide 문서 보정 |

## 2. 전체 시퀀스 상태 표

| Seq | Title | Repo | Impl Branch | Answer Branch | Docs | Visual Lab | Risk | Priority |
|---|---|---|---|---|---|---|---|---|
| 00 | Prerequisite | `aandi-prerequisite-bootcamp` | `00-implementation` | `00-answer` | 확인 필요 | 확인 필요 | legacy `implementation`/`answer` 가능성 | 6 |
| 01 | REST CRUD | `spring-boot-rest-crud-lab` | `01-implementation` | `01-answer` | main/implementation 정리 완료, answer 추가 점검 필요 | main 4파일 스펙 정리 완료 | 원격 default branch와 legacy branch 수동 조치 필요 | 1 |
| 02 | DB Access | `spring-boot-db-access-lab` | `02-implementation` | `02-answer` | 확인 필요 | 공통 Visual Lab 확인 필요 | 공통 레포라 02~06 변경 영향 큼 | 5 |
| 03 | Validation | `spring-boot-db-access-lab` | `03-implementation` | `03-answer` | 확인 필요 | 공통 Visual Lab 확인 필요 | 공통 레포라 02~06 변경 영향 큼 | 5 |
| 04 | JWT | `spring-boot-db-access-lab` | `04-implementation` | `04-answer` | 확인 필요 | 공통 Visual Lab 확인 필요 | 공통 레포라 02~06 변경 영향 큼 | 5 |
| 05 | OAuth2 + SMTP | `spring-boot-db-access-lab` | `05-implementation` | `05-answer` | 확인 필요 | 공통 Visual Lab 확인 필요 | 공통 레포라 02~06 변경 영향 큼 | 5 |
| 06 | Testing | `spring-boot-db-access-lab` | `06-implementation` | `06-answer` | 확인 필요 | 공통 Visual Lab 확인 필요 | 공통 레포라 02~06 변경 영향 큼 | 5 |
| 07 | Redis Cache | `spring-boot-redis-cache-lab` | `07-implementation` | `07-answer` | main guide 보정 완료, implementation/answer 추가 점검 필요 | main 4파일 스펙 정리 완료 | implementation/answer 문서 추가 감사 필요 | 4 |
| 08 | Realtime WebSocket | `spring-boot-realtime-communication-lab` | `08-implementation` | `08-answer` | 확인 필요 | manifest상 `needs-visual-lab` | Visual Lab 미완성 | 4 |
| 09 | Docker/Runtime | `spring-boot-deployment-runtime-lab` | `09-implementation` | `09-answer` | 확인 필요 | manifest상 `needs-visual-lab` | Visual Lab 미완성 | 4 |
| 10 | CI/CD Deployment | `spring-boot-deployment-runtime-lab` | `10-implementation` | `10-answer` | 확인 필요 | manifest상 `needs-visual-lab` | Visual Lab 미완성 | 4 |
| 11 | Refactoring Foundation | `spring-boot-refactoring-foundation-lab` | `11-implementation` | `11-answer` | main 범위 혼입 정리 완료, implementation/answer 추가 점검 필요 | main 4파일 스펙 정리 완료 | implementation/answer 문서 추가 감사 필요 | 3 |
| 12 | Event Driven | `spring-boot-event-driven-lab` | `12-implementation` | `12-answer` | main legacy 정리 완료, implementation/answer 추가 점검 필요 | main 4파일 스펙 정리 완료 | 원격 HEAD가 `12-answer`를 가리킬 수 있음 | 2 |

## 3. 레포별 문제 요약

| Repo | 요약 |
|---|---|
| `spring-boot-rest-crud-lab` | SEQ 01 main Visual Lab을 `index.html`, `styles.css`, `visual-lab-data.js`, `visual-lab.js` 기준으로 정리했습니다. main의 legacy 안내 문서는 외부 링크 가능성을 고려해 삭제하지 않고 deprecated 안내로 축소했습니다. |
| `spring-boot-rest-crud-lab` `01-implementation` | `README.md`, `docs/implementation.md`, `docs/answer-guide.md`에서 answer 브랜치명과 정답 안내 노출을 제거했습니다. |
| `spring-boot-db-access-lab` | 02~06 공통 레포입니다. 한 시퀀스 작업이 다른 시퀀스 브랜치와 Visual Lab에 영향을 줄 수 있어 묶음 감사가 필요합니다. |
| `spring-boot-redis-cache-lab` | main Visual Lab을 현재 4파일 스펙에 맞춰 정리하고, 존재하지 않는 legacy answer-guide 안내를 제거했습니다. |
| `spring-boot-realtime-communication-lab` | manifest상 Visual Lab 미완성 구간입니다. |
| `spring-boot-deployment-runtime-lab` | 09~10 공통 레포이며 Visual Lab 미완성 구간입니다. |
| `spring-boot-refactoring-foundation-lab` | main에 남아 있던 10 CI/CD 문서 범위 혼입을 SEQ 11 리팩토링 범위로 정리하고 Visual Lab을 현재 4파일 스펙에 맞췄습니다. |
| `spring-boot-event-driven-lab` | main Visual Lab을 현재 4파일 스펙에 맞춰 정리하고, main의 긴 정답 가이드를 deprecated 안내로 낮췄습니다. 원격 default branch가 `12-answer`를 가리킬 가능성은 GitHub UI 수동 조치가 필요합니다. |

## 4. 정답 노출 의심 목록

| 위치 | 상태 | 처리 |
|---|---|---|
| `spring-boot-rest-crud-lab` main Visual Lab | 정답 브랜치명/answerBranch 노출 없음 | 처리 완료 |
| `spring-boot-rest-crud-lab` `01-implementation` 문서 | `01-answer`, 정답 코드, 정답 해설 노출 제거 | 처리 완료 |
| `spring-boot-db-access-lab` 02~06 implementation 브랜치 | 추가 검색 필요 | 미처리 |
| `spring-boot-redis-cache-lab` main Visual Lab/guide docs | answerBranch, `07-answer`, 정답 코드, 긴 완성 구현 코드 노출 없음 | 처리 완료 |
| `spring-boot-redis-cache-lab` `07-implementation` | 추가 검색 필요 | 미처리 |
| `spring-boot-realtime-communication-lab` `08-implementation` | 추가 검색 필요 | 미처리 |
| `spring-boot-deployment-runtime-lab` 09~10 implementation 브랜치 | 추가 검색 필요 | 미처리 |
| `spring-boot-refactoring-foundation-lab` main Visual Lab/legacy answer guide | answerBranch, `11-answer`, 정답 코드, 긴 완성 구현 코드 노출 제거 | 처리 완료 |
| `spring-boot-refactoring-foundation-lab` `11-implementation` | 추가 검색 필요 | 미처리 |
| `spring-boot-event-driven-lab` main Visual Lab/legacy answer guide | answerBranch, `12-answer`, 정답 코드, 긴 완성 구현 코드 노출 제거 | 처리 완료 |
| `spring-boot-event-driven-lab` `12-implementation` | 추가 검색 필요 | 미처리 |

## 5. Visual Lab 스펙 미준수 목록

기준 파일:

- `docs/visual-lab/index.html`
- `docs/visual-lab/styles.css`
- `docs/visual-lab/visual-lab-data.js`
- `docs/visual-lab/visual-lab.js`

현재 확인:

| Repo | 상태 |
|---|---|
| `spring-boot-rest-crud-lab` | SEQ 01 main에서 4파일 스펙 정리 완료. 외부 CDN 없음, `window.visualLabData` 사용, answer 노출 없음. |
| `spring-boot-db-access-lab` | 공통 Visual Lab 파일과 추가 legacy CSS/JS 후보 재감사 필요. |
| `spring-boot-redis-cache-lab` | SEQ 07 main에서 4파일 스펙 정리 완료. 외부 CDN 없음, `window.visualLabData` 사용, answer 노출 없음. |
| `spring-boot-realtime-communication-lab` | manifest상 `needs-visual-lab`. |
| `spring-boot-deployment-runtime-lab` | manifest상 `needs-visual-lab`. |
| `spring-boot-refactoring-foundation-lab` | SEQ 11 main에서 4파일 스펙 정리 완료. 외부 CDN 없음, `window.visualLabData` 사용, answer 노출 없음. |
| `spring-boot-event-driven-lab` | SEQ 12 main에서 4파일 스펙 정리 완료. 외부 CDN 없음, `window.visualLabData` 사용, answer 노출 없음. |

## 6. 레거시 후보 목록

| Repo | 후보 | 현재 판단 |
|---|---|---|
| `spring-boot-rest-crud-lab` | legacy `implementation`, `answer` branch | 삭제하지 않음. README/중앙 문서에서 deprecated 수동 조치 대상으로 유지. |
| `spring-boot-rest-crud-lab` | `docs/answer-guide.md` | 외부 링크 가능성 때문에 삭제하지 않고 deprecated 안내로 축소. |
| `spring-boot-rest-crud-lab` | `docs/assets.md`, `docs/branch-guide.md` | 삭제하지 않음. 오래된 표현만 낮은 위험으로 정리. |
| `aandi-prerequisite-bootcamp` | legacy `implementation`, `answer` branch | 추가 확인 필요. |
| `spring-boot-db-access-lab` | legacy `implementation` branch, 공통 Visual Lab 구버전 파일명 후보 | 추가 확인 필요. |
| `spring-boot-refactoring-foundation-lab` | `docs/answer-guide.md` | 외부 링크 가능성 때문에 삭제하지 않고 deprecated 안내로 축소. |
| `spring-boot-event-driven-lab` | 원격 HEAD/default branch가 `12-answer`일 가능성 | GitHub UI 수동 조치 필요. |
| `spring-boot-event-driven-lab` | `docs/answer-guide.md` | 외부 링크 가능성 때문에 삭제하지 않고 deprecated 안내로 축소. |

## 7. 이번 5시간 안에 처리할 우선순위

1. SEQ 01 REST CRUD: main Visual Lab, legacy 안내, implementation 정답 노출 제거를 우선 완료합니다.
2. 중앙 기준 문서: Minimal Sequence Documentation Rule, PAAR 윤문 기준, Visual Lab 4파일 스펙, answer 노출 제한을 반영합니다.
3. SEQ 12 Event Driven: main Visual Lab과 legacy guide 정리는 완료했습니다. 원격 HEAD/default branch 리스크와 implementation/answer 문서 감사는 남았습니다.
4. SEQ 11 Refactoring Foundation: main의 10 CI/CD 내용 혼입 정리는 완료했습니다. implementation/answer 문서 감사는 남았습니다.
5. SEQ 07~10: SEQ 07 main Visual Lab 정리는 완료했습니다. 08~10은 중앙 스펙에 맞춰 순차 정리합니다.
6. SEQ 02~06: 공통 DB Access 레포는 영향 범위가 커서 별도 묶음 감사 후 작업합니다.

## 8. 이번 5시간 안에 처리하지 못한 항목

- SEQ 01 `01-answer` 문서 구조 보강은 아직 수행하지 않았습니다. implementation 구조와 맞춘 뒤 멘토 비교 포인트를 보강해야 합니다.
- SEQ 02~12 각 implementation 브랜치의 정답 노출 검색과 문서 보강은 아직 수행하지 않았습니다. 단, SEQ 01 implementation 정답 노출 제거는 완료했습니다.
- SEQ 08~10 Visual Lab 신규 구현 또는 보강은 아직 수행하지 않았습니다. SEQ 07, 11, 12 main Visual Lab 정리는 완료했습니다.
- legacy 브랜치 삭제, default branch 변경, 원격 branch 정리는 수행하지 않았습니다. 이는 GitHub UI 또는 명시적 승인 후 처리해야 합니다.
