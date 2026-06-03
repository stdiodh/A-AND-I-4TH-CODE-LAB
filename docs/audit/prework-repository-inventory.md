# Prework Repository Inventory

감사 일시: 2026-06-03 KST

감사 범위:

- 중앙 레포: `AandI_4rdPeriod_code_lab`
- 서브레포: `docs/manifest/sequences.yml`에 등록된 repoPath 전체
- 기준 문서: `docs/manifest/sequences.yml`, `docs/sequences/*`

이번 단계에서 수행하지 않은 일:

- 문서 내용 정리
- 코드 수정
- 파일 삭제, 이동, 리네임
- 브랜치 삭제 또는 default branch 변경
- 서브모듈 포인터 커밋

## 전체 요약

- 중앙 레포는 `main` 기준 작업 공간이며 `origin/main`과 ahead/behind 차이가 없습니다.
- `git submodule update --init --recursive`를 실행했고, 모든 서브모듈은 로컬에 존재합니다.
- 중앙 레포와 모든 서브레포에서 원격 정보를 fetch했습니다.
- 모든 서브모듈의 현재 `main`은 `origin/main`과 같은 커밋입니다.
- manifest에는 시퀀스 `00`부터 `12`까지 13개가 등록되어 있습니다.
- 모든 시퀀스의 `main`, `NN-implementation`, `NN-answer` 브랜치는 로컬과 `origin`에 모두 존재합니다.
- 모든 `NN-implementation` / `NN-answer` 브랜치에는 `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`가 존재합니다.
- main 기준으로는 일부 레포가 `README.md`와 Visual Lab만 가진 가이드 브랜치 형태입니다.
- Visual Lab 필수 파일 4개는 모든 repoPath에 존재합니다.
- `python3 scripts/validate-manifest.py`와 `python3 scripts/validate-visual-labs.py`는 모두 통과했습니다.
- 구현 브랜치에는 여러 시퀀스에서 `NN-answer`, `docs/answer-guide.md`, `docs/branch-guide.md` 노출이 확인됩니다.
- Visual Lab 내부에서는 `answerBranch`, `NN-answer`, 정답 코드, 긴 구현 코드 노출이 확인되지 않았습니다.

## 실행한 명령

```bash
git submodule update --init --recursive
git submodule foreach 'git fetch --all --prune'
git fetch --all --prune
git submodule foreach 'printf "%s " "$name"; git rev-parse --short HEAD; printf "origin/main "; git rev-parse --short origin/main; if [ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ]; then echo "up-to-date"; else echo "differs"; fi'
python3 scripts/validate-manifest.py
python3 scripts/validate-visual-labs.py
```

참고:

- fetch 중 원격에서 이미 삭제된 tracking ref가 prune되었습니다.
- 서브모듈 `main`은 모두 `origin/main`과 같아서 추가 fast-forward pull은 필요하지 않았습니다.

## 시퀀스별 상태 표

| sequence id | title | repoPath | guideBranch | implementationBranch | answerBranch | sequenceDoc | visualLabPath | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | Prerequisite | `aandi-prerequisite-bootcamp` | `main` | `00-implementation` | `00-answer` | `docs/sequences/00-prerequisite-bootcamp.md` | `docs/visual-lab/index.html` | `ready` |
| 01 | REST CRUD | `spring-boot-rest-crud-lab` | `main` | `01-implementation` | `01-answer` | `docs/sequences/01-request-response-and-memory-crud.md` | `docs/visual-lab/index.html` | `needs-branch-cleanup` |
| 02 | DB Access | `spring-boot-db-access-lab` | `main` | `02-implementation` | `02-answer` | `docs/sequences/02-persistence-and-layered-architecture.md` | `docs/visual-lab/index.html` | `ready` |
| 03 | Validation | `spring-boot-db-access-lab` | `main` | `03-implementation` | `03-answer` | `docs/sequences/03-safe-request-handling.md` | `docs/visual-lab/index.html` | `ready` |
| 04 | JWT | `spring-boot-db-access-lab` | `main` | `04-implementation` | `04-answer` | `docs/sequences/04-authentication-and-jwt.md` | `docs/visual-lab/index.html` | `ready` |
| 05 | OAuth2 + SMTP | `spring-boot-db-access-lab` | `main` | `05-implementation` | `05-answer` | `docs/sequences/05-external-authentication-or-email-verification.md` | `docs/visual-lab/index.html` | `ready` |
| 06 | Testing | `spring-boot-db-access-lab` | `main` | `06-implementation` | `06-answer` | `docs/sequences/06-testing-and-verification.md` | `docs/visual-lab/index.html` | `ready` |
| 07 | Redis Cache | `spring-boot-redis-cache-lab` | `main` | `07-implementation` | `07-answer` | `docs/sequences/07-caching-and-redis.md` | `docs/visual-lab/index.html` | `needs-visual-lab` |
| 08 | Realtime WebSocket | `spring-boot-realtime-communication-lab` | `main` | `08-implementation` | `08-answer` | `docs/sequences/08-realtime-communication.md` | `docs/visual-lab/index.html` | `needs-visual-lab` |
| 09 | Docker/Runtime | `spring-boot-deployment-runtime-lab` | `main` | `09-implementation` | `09-answer` | `docs/sequences/09-deployment-and-runtime-environment.md` | `docs/visual-lab/index.html` | `needs-visual-lab` |
| 10 | CI/CD Deployment | `spring-boot-deployment-runtime-lab` | `main` | `10-implementation` | `10-answer` | `docs/sequences/10-cicd-and-operations-automation.md` | `docs/visual-lab/index.html` | `needs-visual-lab` |
| 11 | Refactoring Foundation | `spring-boot-refactoring-foundation-lab` | `main` | `11-implementation` | `11-answer` | `docs/sequences/11-refactoring-and-foundation-reinforcement.md` | `docs/visual-lab/index.html` | `needs-review` |
| 12 | Event Driven | `spring-boot-event-driven-lab` | `main` | `12-implementation` | `12-answer` | `docs/sequences/12-message-queue-and-event-driven-thinking.md` | `docs/visual-lab/index.html` | `needs-branch-cleanup` |

## repoPath별 main 파일 상태

기준: 현재 로컬 `main`, 각 서브모듈은 `origin/main`과 같은 커밋입니다.

| repoPath | local path | main branch | README.md | docs/theory.md | docs/implementation.md | docs/checklist.md | VL index | VL styles | VL data | VL js |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `aandi-prerequisite-bootcamp` | Y | local+origin | Y | Y | Y | Y | Y | Y | Y | Y |
| `spring-boot-db-access-lab` | Y | local+origin | Y | N | N | N | Y | Y | Y | Y |
| `spring-boot-deployment-runtime-lab` | Y | local+origin | Y | Y | Y | Y | Y | Y | Y | Y |
| `spring-boot-event-driven-lab` | Y | local+origin | Y | Y | Y | Y | Y | Y | Y | Y |
| `spring-boot-realtime-communication-lab` | Y | local+origin | Y | N | N | N | Y | Y | Y | Y |
| `spring-boot-redis-cache-lab` | Y | local+origin | Y | N | N | N | Y | Y | Y | Y |
| `spring-boot-refactoring-foundation-lab` | Y | local+origin | Y | Y | Y | Y | Y | Y | Y | Y |
| `spring-boot-rest-crud-lab` | Y | local+origin | Y | Y | Y | Y | Y | Y | Y | Y |

참고:

- `spring-boot-db-access-lab`, `spring-boot-redis-cache-lab`, `spring-boot-realtime-communication-lab`의 main은 상세 실습 문서 없이 가이드 역할에 가깝습니다.
- 위 세 레포도 각 `NN-implementation`과 `NN-answer` 브랜치에는 README/theory/implementation/checklist가 모두 존재합니다.

## 시퀀스별 브랜치 존재 상태

| sequence id | repoPath | main | implementationBranch | answerBranch |
| --- | --- | --- | --- | --- |
| 00 | `aandi-prerequisite-bootcamp` | local+origin | local+origin | local+origin |
| 01 | `spring-boot-rest-crud-lab` | local+origin | local+origin | local+origin |
| 02 | `spring-boot-db-access-lab` | local+origin | local+origin | local+origin |
| 03 | `spring-boot-db-access-lab` | local+origin | local+origin | local+origin |
| 04 | `spring-boot-db-access-lab` | local+origin | local+origin | local+origin |
| 05 | `spring-boot-db-access-lab` | local+origin | local+origin | local+origin |
| 06 | `spring-boot-db-access-lab` | local+origin | local+origin | local+origin |
| 07 | `spring-boot-redis-cache-lab` | local+origin | local+origin | local+origin |
| 08 | `spring-boot-realtime-communication-lab` | local+origin | local+origin | local+origin |
| 09 | `spring-boot-deployment-runtime-lab` | local+origin | local+origin | local+origin |
| 10 | `spring-boot-deployment-runtime-lab` | local+origin | local+origin | local+origin |
| 11 | `spring-boot-refactoring-foundation-lab` | local+origin | local+origin | local+origin |
| 12 | `spring-boot-event-driven-lab` | local+origin | local+origin | local+origin |

## 레포별 legacy 후보

삭제하지 않았습니다. 아래 항목은 다음 작업에서 검토할 후보입니다.

| repo | branch 후보 | 파일 후보 | 비고 |
| --- | --- | --- | --- |
| central root | local `02-answer`, `02-implementation`, `03-answer`, `03-implementation`, `04-answer`, `04-implementation`, `05-answer`, `05-implementation`, `06-answer`, `06-implementation`, `07-implementation` | 없음 | 중앙 레포의 로컬 작업 브랜치로 보입니다. |
| `aandi-prerequisite-bootcamp` | local `implementation` | `answer/*`, `docs/answer-guide.md`, `docs/branch-guide.md` | `origin/HEAD`가 `origin/implementation`을 가리키는 stale 상태입니다. |
| `spring-boot-db-access-lab` | local `07-implementation`, local `implementation` | `docs/branch-guide.md` | `origin/HEAD`가 `origin/implementation`을 가리키는 stale 상태입니다. |
| `spring-boot-deployment-runtime-lab` | 없음 | `docs/answer-guide.md`, `docs/branch-guide.md` | `origin/HEAD`가 missing-or-dangling 상태입니다. |
| `spring-boot-event-driven-lab` | 없음 | `docs/answer-guide.md`, `docs/branch-guide.md` | `origin/HEAD`가 missing-or-dangling 상태입니다. |
| `spring-boot-realtime-communication-lab` | 없음 | `docs/branch-guide.md` | 원격 브랜치 구조는 manifest와 일치합니다. |
| `spring-boot-redis-cache-lab` | 없음 | `docs/branch-guide.md` | 원격 브랜치 구조는 manifest와 일치합니다. |
| `spring-boot-refactoring-foundation-lab` | 없음 | `docs/answer-guide.md`, `docs/branch-guide.md` | `origin/HEAD`가 missing-or-dangling 상태입니다. |
| `spring-boot-rest-crud-lab` | local `implementation`, remote `origin/answer`, remote `origin/implementation` | `docs/answer-guide.md`, `docs/branch-guide.md` | `origin/HEAD`가 `origin/implementation`을 가리킵니다. |

추가 legacy/중복 파일명 후보:

- `spring-boot-db-access-lab/docs/visual-lab/components.css`
- `spring-boot-db-access-lab/docs/visual-lab/design-tokens.css`
- `spring-boot-db-access-lab/docs/visual-lab/style.css`

위 CSS 파일들은 Visual Lab 필수 파일은 아니지만, 현재 validator 실패 원인은 아닙니다.

## Visual Lab 스펙 미준수 목록

자동 검증 결과:

```text
PASS: 8 repo group(s), 0 issue(s), 0 warning group(s)
```

확인 결과:

- 모든 repoPath에 `docs/visual-lab/index.html`이 있습니다.
- 모든 repoPath에 `docs/visual-lab/styles.css`가 있습니다.
- 모든 repoPath에 `docs/visual-lab/visual-lab-data.js`가 있습니다.
- 모든 repoPath에 `docs/visual-lab/visual-lab.js`가 있습니다.
- `window.visualLabData`가 존재합니다.
- `sequence`, `title`, `goal`, `flow` 필드가 존재합니다.
- 외부 CDN 사용은 validator 기준으로 확인되지 않았습니다.
- Visual Lab 내부 answer 노출은 validator와 추가 검색 기준 모두에서 확인되지 않았습니다.

미준수는 아니지만 다음 검토 후보:

- `spring-boot-db-access-lab/docs/visual-lab`에 필수 4개 외 CSS 파일이 있습니다.

## answer 노출 의심 목록

기준:

- 각 `NN-implementation` 브랜치에서 `NN-answer`, `answerBranch`, `sourceAnswerBranch`, `정답`, `답안`, `완성 코드`, `answer branch`, `solution branch`를 검색했습니다.
- 원격 브랜치가 있으면 `origin/NN-implementation`을 기준으로 검색했습니다.
- 아래 항목은 삭제 대상이 아니라 다음 문서 정리 단계에서 판단할 후보입니다.

| sequence | implementationBranch | 의심 위치 |
| --- | --- | --- |
| 00 | `00-implementation` | `README.md:40`, `docs/answer-guide.md:4`, `docs/assets.md:22`, `docs/implementation.md:91`에서 `00-answer` 노출 |
| 01 | `01-implementation` | `README.md:51`, `docs/answer-guide.md:4`, `docs/answer-guide.md:25`, `docs/implementation.md:85`에서 `01-answer` 노출 |
| 02 | `02-implementation` | `README.md:22`, `README.md:36`, `README.md:64`에서 `02-answer` 노출 |
| 03 | `03-implementation` | `README.md:22`, `README.md:36`, `README.md:64`에서 `03-answer` 노출 |
| 04 | `04-implementation` | `README.md:23`, `README.md:37`, `README.md:64`에서 `04-answer` 노출 |
| 05 | `05-implementation` | `README.md:26`, `README.md:40`, `README.md:64`에서 `05-answer` 노출 |
| 06 | `06-implementation` | `README.md:27`, `README.md:41`, `README.md:63`, `docs/answer-guide.md:144`에서 `06-answer` 노출 |
| 07 | `07-implementation` | `README.md:23`, `README.md:37`, `README.md:60`, `docs/answer-guide.md:143`에서 `07-answer` 노출 |
| 08 | `08-implementation` | `README.md:21`, `README.md:35`, `README.md:58`, `docs/answer-guide.md:102`에서 `08-answer` 노출 |
| 09 | `09-implementation` | `.github/workflows/deploy.yml:7`, `README.md:33`, `docs/answer-guide.md:4`에서 `09-answer` 노출 |
| 10 | `10-implementation` | `.github/workflows/ci.yml:7`, `.github/workflows/deploy.yml:7`, `README.md:33`, `docs/answer-guide.md:4`에서 `10-answer` 노출 |
| 11 | `11-implementation` | `README.md:6`, `docs/answer-guide.md:4`, `docs/branch-guide.md:13`, `docs/branch-guide.md:15`, `docs/branch-guide.md:16`, `docs/branch-guide.md:22`에서 `11-answer` 또는 정답 브랜치 설명 노출 |
| 12 | `12-implementation` | `docs/answer-guide.md:3`, `docs/branch-guide.md:13`, `docs/branch-guide.md:15`, `docs/branch-guide.md:16`, `docs/branch-guide.md:22`에서 `12-answer` 또는 정답 브랜치 설명 노출 |

Visual Lab 내부 추가 검색 결과:

- `answerBranch`: 없음
- `sourceAnswerBranch`: 없음
- `NN-answer`: 없음
- `정답 코드`, `답안`, `완성 코드`: 없음
- 긴 Java/Kotlin 구현 코드로 보이는 블록: 없음

## 다음 작업 우선순위

1. 시퀀스별로 `NN-implementation` 문서의 answer 브랜치명 노출을 줄일지 결정합니다.
2. implementation 브랜치에 있는 `docs/answer-guide.md`, `docs/branch-guide.md`를 유지할지, 기존 4개 문서로 흡수할지 시퀀스별로 검토합니다.
3. `09-implementation`, `10-implementation`의 workflow 파일이 answer 브랜치를 trigger에 포함하는 이유를 확인합니다.
4. `spring-boot-rest-crud-lab`, `aandi-prerequisite-bootcamp`, `spring-boot-db-access-lab`의 legacy `implementation` / `answer` 계열 브랜치를 deprecated 처리할지 결정합니다.
5. `origin/HEAD`가 stale 또는 dangling인 레포는 GitHub default branch와 로컬 remote HEAD 정리 필요성을 확인합니다.
6. `spring-boot-db-access-lab/docs/visual-lab`의 추가 CSS 파일이 실제로 필요한지 확인합니다.
7. manifest에서 `needs-review`로 표시된 시퀀스 11은 이전 시퀀스 10 내용이 섞였는지 별도 문서 감사를 먼저 진행합니다.
8. 이후 작업은 `1 sequence = 1 branch = 1 PR` 원칙에 맞춰 한 시퀀스씩 진행합니다.

## 수정하지 않은 항목과 이유

- 문서 본문은 수정하지 않았습니다. 이번 단계는 읽기 전용 감사이며, 허용된 변경은 감사 결과 문서 1개 생성뿐입니다.
- 코드는 수정하지 않았습니다. 정리 작업은 다음 단계에서 시퀀스별로 진행합니다.
- legacy 브랜치와 파일은 삭제하지 않았습니다. 원격 branch 삭제와 default branch 변경은 수동 운영 판단이 필요합니다.
- `origin/HEAD` stale/dangling 상태는 기록만 했습니다. 로컬 remote HEAD 정리도 감사 범위를 넘는 상태 변경입니다.
- Visual Lab 추가 CSS 파일은 삭제하지 않았습니다. 필수 파일이 모두 있고 validator가 통과했으므로 다음 visual cleanup에서 판단합니다.
- Gradle 테스트는 실행하지 않았습니다. 이번 작업은 코드 변경이 없는 repository inventory 감사이며, 실행한 검증은 manifest/Visual Lab 구조 검증입니다.

## 검증 결과

```text
PASS: python3 scripts/validate-manifest.py
PASS: python3 scripts/validate-visual-labs.py
```

추가 확인:

- 중앙 `git status --short`는 감사 문서 생성 전 깨끗했습니다.
- 서브모듈별 `git status --short`는 감사 문서 생성 전 모두 깨끗했습니다.
- 모든 서브모듈의 `HEAD`와 `origin/main`은 같은 커밋입니다.
