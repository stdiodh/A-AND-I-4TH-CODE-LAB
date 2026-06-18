# Visual Theory Sync Audit Report

생성일: 2026-06-16

## 범위

- 중앙 manifest: `docs/manifest/sequences.yml`
- 대상 sequence: `00` ~ `12`
- 대상 토픽 레포: manifest의 `repoPath` 기준 8개 레포
- 작업 방식: 토픽 레포별 subagent 1개를 배정해 audit만 수행했습니다.
- 제한: 이번 단계에서는 토픽 레포 문서와 코드를 수정하지 않았습니다.

## 전체 요약

| 항목 | 개수 |
| :--- | ---: |
| 전체 sequence | 13 |
| PASS | 1 |
| WARN | 10 |
| FAIL | 2 |
| P0 | 1 |
| P1 | 10 |
| P2 | 2 |

가장 먼저 처리할 항목은 sequence `08`입니다. WebSocket 핵심 코드 경로와 문서/Visual Lab의 STOMP destination이 맞지 않아 수업 진행 전에 정렬이 필요합니다.

다음 우선순위는 sequence `10`입니다. 문서와 Visual Lab은 deploy/verify script 분리를 전제로 설명하지만 실제 레포에는 해당 script가 없고 workflow도 단일 job 구조입니다.

반복적으로 보이는 문제는 Visual Lab 상세 데이터의 source 링크가 `../theory.md`처럼 잡혀 상세 페이지 기준으로 깨지는 경우와, Visual Lab code snippet이 현재 코드보다 오래된 경우입니다.

## Subagent 배정

| Subagent 범위 | Repo | Sequence |
| :--- | :--- | :--- |
| prerequisite | `aandi-prerequisite-bootcamp` | `00` |
| REST CRUD | `spring-boot-rest-crud-lab` | `01` |
| DB Access 계열 | `spring-boot-db-access-lab` | `02`, `03`, `04`, `05`, `06` |
| Redis | `spring-boot-redis-cache-lab` | `07` |
| Realtime | `spring-boot-realtime-communication-lab` | `08` |
| Deployment | `spring-boot-deployment-runtime-lab` | `09`, `10` |
| Refactoring | `spring-boot-refactoring-foundation-lab` | `11` |
| Event Driven | `spring-boot-event-driven-lab` | `12` |

## Sequence별 PASS/WARN/FAIL

| Sequence | Repo | Status | Priority | PASS | WARN | FAIL |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| `00` | `aandi-prerequisite-bootcamp` | WARN | P1 | manifest/theory 반영, 필수 문서 존재, theory 핵심 경로 존재 | Visual Lab source 링크 깨짐, codePoint가 실제 파일 경로가 아닌 표시 문구, 학생 README에 legacy bare branch 언급 | 없음 |
| `01` | `spring-boot-rest-crud-lab` | WARN | P1 | manifest/theory 반영, 상세 페이지 존재, 핵심 Kotlin 경로 존재 | Visual Lab source 링크 깨짐, 학생 README와 branch guide에 legacy branch 운영 메모 노출 | 없음 |
| `02` | `spring-boot-db-access-lab` | WARN | P1 | manifest/theory 반영, 상세 페이지 존재, theory 경로 존재 | Visual Lab `PostService.create` snippet이 현재 `create(request, authorEmail)`와 불일치 | 없음 |
| `03` | `spring-boot-db-access-lab` | WARN | P1 | manifest/theory 반영, 상세 페이지 존재, 코드 경로 존재 | Visual Lab `PostCreateRequest` snippet에 현재 DTO에 없는 `author` 필드 포함 | 없음 |
| `04` | `spring-boot-db-access-lab` | WARN | P2 | 상세 페이지와 JWT/security 경로 존재 | theory가 로그인/JWT 중심이고 manifest의 회원가입 흐름 반영이 약함 | 없음 |
| `05` | `spring-boot-db-access-lab` | WARN | P1 | manifest/theory 반영, 상세 페이지 존재 | Visual Lab codePoint 파일이 `main`에는 없고 `05-implementation`/`05-answer`에만 존재, TODO 해답 노출 가능성 | 없음 |
| `06` | `spring-boot-db-access-lab` | WARN | P1 | manifest/theory 반영, 상세 페이지 존재, 테스트 경로 존재 | Visual Lab test/fixture snippet이 현재 시그니처와 불일치 | 없음 |
| `07` | `spring-boot-redis-cache-lab` | WARN | P1 | manifest/theory 반영, 상세 페이지 존재, 문서 순서와 Visual Lab 흐름 대체로 일치 | Visual Lab codePoint 경로가 `main`에는 없고 sequence branch 기준, repo guide에 단독 `implementation 브랜치` 표현 | 없음 |
| `08` | `spring-boot-realtime-communication-lab` | FAIL | P0 | 상세 페이지와 Visual Lab 허브 파일 존재, 문체와 금칙어 기준 통과 | theory 제목/초반부에 `08`/`Realtime WebSocket` 명시 부족, repo guide에 단독 `implementation 브랜치` 표현 | WebSocket 핵심 파일과 dependency 누락, theory/implementation과 Visual Lab destination 불일치, README의 테스트 안내와 실제 test 경로 불일치 |
| `09` | `spring-boot-deployment-runtime-lab` | PASS | P2 | manifest/theory/Visual Lab 반영, 상세 페이지 존재, `Dockerfile`, `application-prod.yaml`, `deploy/compose.prod.yaml` 존재 | 운영 배포 검증은 로컬 정적 audit 밖 | 없음 |
| `10` | `spring-boot-deployment-runtime-lab` | FAIL | P1 | manifest/theory/Visual Lab 반영, 상세 페이지 존재 | workflow trigger가 `09-answer` 중심이라 sequence 10 의도 확인 필요 | `scripts/deploy.sh`, `scripts/check-deploy.sh` 누락, Visual Lab의 job 분리 설명과 실제 workflow 구조 불일치 |
| `11` | `spring-boot-refactoring-foundation-lab` | WARN | P1 | manifest/theory 반영, 상세 페이지 존재, 핵심 Kotlin 경로 존재, legacy bare branch 노출 없음 | theory와 Visual Lab snippet이 현재 starter 코드와 불일치, source 링크 깨짐 | 없음 |
| `12` | `spring-boot-event-driven-lab` | WARN | P1 | manifest/theory 반영, 상세 페이지 존재, 핵심 Kotlin 경로 존재 | Visual Lab 클래스명 불일치, source 링크 깨짐, combined codePoint file 경로가 단일 실제 경로가 아님 | 없음 |

## Sequence별 누락 파일

| Sequence | 누락 파일 |
| :--- | :--- |
| `00` | 필수 파일 누락 없음 |
| `01` | 필수 파일 누락 없음 |
| `02` | 필수 파일 누락 없음 |
| `03` | 필수 파일 누락 없음 |
| `04` | 필수 파일 누락 없음 |
| `05` | 필수 파일 누락 없음. 단, Visual Lab codePoint의 `OAuthAccountService.kt`, `AccountRecoveryService.kt`는 `main`에는 없고 `05-implementation`/`05-answer`에만 존재 |
| `06` | 필수 파일 누락 없음 |
| `07` | 필수 파일 누락 없음. 단, Visual Lab codePoint의 `PostQueryService.kt`, `PostCacheService.kt`는 `main`에는 없고 sequence branch 기준 |
| `08` | `src/main/kotlin/com/andi/rest_crud/config/WebSocketConfig.kt`, `src/main/kotlin/com/andi/rest_crud/controller/WebSocketController.kt`, `src/main/kotlin/com/andi/rest_crud/dto/ChatMessage.kt`, `src/main/resources/static/realtime-demo.html` |
| `09` | 필수 파일 누락 없음 |
| `10` | `scripts/deploy.sh`, `scripts/check-deploy.sh`. `docs/branch-guide.md`가 언급하는 `ci.yml`도 실제 파일 확인 필요 |
| `11` | 필수 파일 누락 없음 |
| `12` | 필수 파일 누락 없음 |

## Theory / Visual Lab 불일치

- `00`: Visual Lab source 링크가 상세 페이지 기준 실제 `docs/*.md`로 해석되지 않습니다. `codePoints[].file` 값도 실제 starter 파일 경로 대신 표시 문구입니다.
- `01`: Visual Lab source 링크 `../theory.md`, `../implementation.md`, `../checklist.md`가 상세 페이지 기준으로 깨집니다.
- `02`: Visual Lab `PostService.create` snippet이 `create(request)`와 `request.author`를 사용하지만 현재 코드는 `create(request, authorEmail)`입니다.
- `03`: Visual Lab `PostCreateRequest` snippet에 현재 DTO에 없는 `author` 필드가 남아 있습니다.
- `04`: `docs/theory.md`가 로그인/JWT와 보호 API는 다루지만 manifest learning goal의 회원가입 흐름은 약하게 반영합니다.
- `05`: Visual Lab snippet이 `05-implementation` TODO보다 앞선 해답 형태로 보일 수 있습니다.
- `06`: Visual Lab test/fixture snippet이 현재 `PostServiceTest`와 `TestFixtureFactory` 시그니처와 맞지 않습니다.
- `07`: Visual Lab codePoint 경로가 `main` 기준으로는 존재하지 않아 sequence branch 기준임을 명시해야 합니다.
- `08`: theory/implementation은 `@MessageMapping("/chat")`, `@SendTo("/topic/messages")`를 말하지만 Visual Lab은 `/app/chat.send`, `/topic/chat`, `@MessageMapping("/chat.send")`, `@SendTo("/topic/chat")` 기준입니다.
- `10`: Visual Lab은 `build -> deploy -> verify` job 분리를 보여주지만 실제 `.github/workflows/deploy.yml`은 단일 `deploy` job에서 test/build/upload/deploy/log 확인을 처리합니다.
- `11`: theory의 `TestFixtureFactory.postUpdateRequest()` 예시와 Visual Lab의 validation snippet이 현재 코드에 존재하지 않는 함수/흐름을 암시합니다.
- `12`: Visual Lab 데이터가 실제 `OrderEventController`를 `EventOrderController`로 표시하고, `EventPublisherService.kt / NotificationConsumer.kt`를 하나의 file 값으로 묶습니다.

## Legacy / 문체 점검

- 금칙어 `당연히`, `그냥`, `무조건`, `이 정도는`, `시사하는 바`, `에 있어서`, `할 수 있을 것으로 보인다`는 subagent 범위에서 발견되지 않았습니다.
- `00`, `01`, `02~06`, `07`, `08`에는 학생 문서 또는 repo guide에 단독 `implementation` branch 표현이 남아 있어 `NN-implementation` 또는 운영자용 문맥으로 정리해야 합니다.
- `12`에는 bare legacy branch 안내는 없지만 학생 문서에 `12-answer` 비교 안내가 직접 노출됩니다. 중앙 학습 흐름과 충돌하지는 않지만, answer 안내 최소화 기준을 엄격히 적용할지 수동 판단이 필요합니다.
- 문체는 전반적으로 `합니다/입니다` 중심입니다. 일부 Visual Lab 질문형 표현은 더 단정한 설명형으로 다듬을 수 있습니다.

## 수동 확인이 필요한 항목

- Visual Lab 상세 페이지를 브라우저에서 열고 Theory/Implementation/Checklist source 링크 클릭 동작 확인
- `08-implementation` / `08-answer` 브랜치에 WebSocket 파일이 있는지 확인
- `05`와 `07`의 Visual Lab codePoint가 의도적으로 sequence branch 기준인지 확인
- `10`은 script 파일을 만들지, 아니면 문서/Visual Lab을 현재 inline workflow 구조에 맞출지 결정
- GitHub 원격 default branch가 `main`인지 확인: 특히 manifest notes가 언급하는 `01`, `12`
- GitHub Actions, EC2, Secrets 기반 배포 검증은 로컬 정적 audit만으로 확인 불가
- 기존 worktree에 여러 submodule 수정 상태와 `docs/audit/visual-lab-refactor-sweep.md` 수정 상태가 있었으므로 수정 loop 전에 소유자 확인 필요

## 수정 우선순위

### P0

1. `08` Realtime WebSocket
   - 핵심 코드 경로와 dependency가 현재 worktree에서 확인되지 않습니다.
   - theory/implementation과 Visual Lab의 STOMP endpoint/destination이 다릅니다.

### P1

1. `10` CI/CD Deployment
   - deploy/verify script와 workflow 구조 중 하나로 기준을 정해야 합니다.
2. `00`, `01`, `11`, `12`
   - Visual Lab source 링크가 상세 페이지 기준으로 깨집니다.
3. `02`, `03`, `06`, `11`, `12`
   - Visual Lab snippet이 현재 코드와 어긋납니다.
4. `05`, `07`
   - Visual Lab codePoint 기준 브랜치가 `main`인지 sequence branch인지 명시해야 합니다.
5. `00`, `01`, `02~06`, `07`, `08`
   - 학생 문서 또는 repo guide의 단독 `implementation` 표현을 정리해야 합니다.

### P2

1. `04`
   - 회원가입 learning goal을 theory에 짧게 보강하면 충분합니다.
2. `09`
   - 현재 audit 기준에서는 PASS입니다. 배포 환경 검증만 별도 수동 확인하면 됩니다.

## Sequence별 수정용 Codex 프롬프트

### 00

```text
Repository root: /Users/dh/Desktop/Code/A&I BE/AandI_4rdPeriod_code_lab
Topic repo: aandi-prerequisite-bootcamp
Sequence: 00

sequence 00만 수정하세요. Visual Lab 상세 데이터의 source 링크를 docs/visual-lab/sequences/00/index.html 기준 실제 docs/theory.md, docs/implementation.md, docs/checklist.md로 열리게 고치세요. codePoints의 file 값은 존재하는 starter 경로로 바꾸세요. 학생-facing README에서는 legacy bare implementation/answer 운영 메모를 제거하거나 instructor/operator 문맥으로 옮기세요. 새 문서를 만들지 말고, 수정 후 rg로 legacy bare branch 표현과 금칙어를 재검사하세요.
```

### 01

```text
Repository root: /Users/dh/Desktop/Code/A&I BE/AandI_4rdPeriod_code_lab
Topic repo: spring-boot-rest-crud-lab
Sequence: 01

sequence 01만 수정하세요. Visual Lab 상세 페이지의 source 문서 링크가 실제 docs/theory.md, docs/implementation.md, docs/checklist.md로 열리도록 상대경로를 고치고, 학생-facing README에서 legacy implementation/answer 및 remote default branch 운영 메모를 제거하거나 운영자용 위치로 옮기세요. 새 파일은 만들지 말고 기존 문체를 유지하세요. 수정 후 validate-visual-labs.py와 관련 rg path check를 실행하세요.
```

### 02

```text
Repository root: /Users/dh/Desktop/Code/A&I BE/AandI_4rdPeriod_code_lab
Topic repo: spring-boot-db-access-lab
Sequence: 02

sequence 02 Visual Lab snippet만 현재 PostService.create(request, authorEmail) 구현과 맞게 갱신하세요. docs/visual-lab/sequences/02/visual-lab-data.js 중심으로 수정하고 새 파일은 만들지 마세요. request.author처럼 현재 코드에 없는 값을 제거하고, 관련 코드 경로가 실제 존재하는지 확인하세요.
```

### 03

```text
Repository root: /Users/dh/Desktop/Code/A&I BE/AandI_4rdPeriod_code_lab
Topic repo: spring-boot-db-access-lab
Sequence: 03

sequence 03 Visual Lab의 PostCreateRequest snippet에서 현재 DTO에 없는 author 필드를 제거하세요. docs/visual-lab/sequences/03/visual-lab-data.js의 설명과 체크 문구가 현재 DTO(title, content)와 validation 흐름에 맞는지 확인하세요. 코드 변경은 하지 말고 문서/Visual Lab 정렬만 수행하세요.
```

### 04

```text
Repository root: /Users/dh/Desktop/Code/A&I BE/AandI_4rdPeriod_code_lab
Topic repo: spring-boot-db-access-lab
Sequence: 04

sequence 04의 docs/theory.md에 manifest learning goal인 회원가입과 로그인 흐름을 짧게 보강하세요. AuthController/AuthService 책임과 JWT 발급/검증 흐름만 연결하고, 중앙 docs나 새 문서를 늘리지 마세요. 기존 합니다/입니다 문체를 유지하고 상세 이론을 과도하게 추가하지 마세요.
```

### 05

```text
Repository root: /Users/dh/Desktop/Code/A&I BE/AandI_4rdPeriod_code_lab
Topic repo: spring-boot-db-access-lab
Sequence: 05

sequence 05 Visual Lab code points가 main 기준인지 05-implementation 기준인지 명확히 하세요. OAuthAccountService.kt와 AccountRecoveryService.kt가 main에 없다는 점을 학생이 혼동하지 않게 짧게 정리하고, TODO 해답을 과도하게 노출하는 snippet은 힌트 수준으로 줄이세요. 토픽 코드 자체는 변경하지 마세요.
```

### 06

```text
Repository root: /Users/dh/Desktop/Code/A&I BE/AandI_4rdPeriod_code_lab
Topic repo: spring-boot-db-access-lab
Sequence: 06

sequence 06 Visual Lab의 test/fixture snippets를 현재 PostServiceTest와 TestFixtureFactory 시그니처에 맞게 갱신하세요. postService.create(request)나 fixture author arg처럼 현재 코드와 맞지 않는 예시는 제거하거나 현재 호출 형태로 바꾸세요. 변경 범위는 docs/visual-lab/sequences/06/visual-lab-data.js와 필요한 설명 문구로 제한하세요.
```

### 07

```text
Repository root: /Users/dh/Desktop/Code/A&I BE/AandI_4rdPeriod_code_lab
Topic repo: spring-boot-redis-cache-lab
Sequence: 07

sequence 07만 수정하세요. docs/repo-guide.md의 일반 “implementation 브랜치” 표현을 07-implementation 또는 학생 시작 브랜치로 고치고, Visual Lab codePoint 경로가 07-implementation/07-answer 기준임을 학생이 알 수 있게 짧게 명시하세요. Visual Lab의 질문형 표현은 합니다/입니다 톤으로 정리하세요. 코드 변경은 하지 말고 rg로 legacy branch 표현과 금칙어를 확인하세요.
```

### 08

```text
Repository root: /Users/dh/Desktop/Code/A&I BE/AandI_4rdPeriod_code_lab
Topic repo: spring-boot-realtime-communication-lab
Sequence: 08

sequence 08만 수정하세요. 먼저 현재 브랜치와 08-implementation/08-answer의 의도 차이를 확인한 뒤, 문서와 Visual Lab의 STOMP destination을 하나로 통일하세요. 기준은 /ws-chat, /app/chat.send, /topic/chat로 둘지 먼저 확인하고, 필요한 경우 spring-boot-starter-websocket, WebSocketConfig.kt, WebSocketController.kt, ChatMessage.kt, realtime-demo.html, 관련 테스트를 최소 구현하세요. docs/theory.md, docs/implementation.md, docs/checklist.md, docs/visual-lab/sequences/08/visual-lab-data.js가 같은 경로와 순서를 말하도록 맞추고, docs/repo-guide.md의 단독 “implementation 브랜치” 표현을 고치세요.
```

### 09

```text
Repository root: /Users/dh/Desktop/Code/A&I BE/AandI_4rdPeriod_code_lab
Topic repo: spring-boot-deployment-runtime-lab
Sequence: 09

sequence 09는 현재 audit 기준 PASS입니다. 수정하지 말고, Dockerfile, src/main/resources/application-prod.yaml, deploy/compose.prod.yaml, docs/visual-lab/sequences/09/index.html 경로가 유지되는지만 재확인하세요. 배포 환경 검증은 수동 항목으로 남기세요.
```

### 10

```text
Repository root: /Users/dh/Desktop/Code/A&I BE/AandI_4rdPeriod_code_lab
Topic repo: spring-boot-deployment-runtime-lab
Sequence: 10

sequence 10 CI/CD 문서, Visual Lab, workflow를 수술적으로 정렬하세요. scripts/deploy.sh와 scripts/check-deploy.sh를 실제로 만들고 workflow를 build/deploy/verify로 분리할지, 아니면 docs/theory.md, docs/implementation.md, docs/checklist.md, docs/visual-lab/sequences/10/visual-lab-data.js를 현재 .github/workflows/deploy.yml 단일 job 구조에 맞출지 먼저 선택하세요. 선택한 방향으로 경로와 stage 설명을 일치시키고, GitHub Actions/EC2/Secrets 검증은 수동 확인 항목으로 남기세요.
```

### 11

```text
Repository root: /Users/dh/Desktop/Code/A&I BE/AandI_4rdPeriod_code_lab
Topic repo: spring-boot-refactoring-foundation-lab
Sequence: 11

sequence 11 documentation/Visual Lab consistency만 수정하세요. app code는 refactor하지 마세요. docs/visual-lab/sequences/11/visual-lab-data.js source links가 상세 페이지 기준 실제 docs/theory.md, docs/implementation.md, docs/checklist.md로 열리게 고치세요. docs/theory.md와 Visual Lab code snippets는 현재 starter code와 맞추거나, nonexistent function/test를 암시하지 않는 conceptual snippet으로 바꾸세요. full answer implementation과 legacy implementation/answer branch guidance는 노출하지 마세요.
```

### 12

```text
Repository root: /Users/dh/Desktop/Code/A&I BE/AandI_4rdPeriod_code_lab
Topic repo: spring-boot-event-driven-lab
Sequence: 12

sequence 12의 P1 audit issue만 수정하세요. docs/visual-lab/sequences/12/visual-lab-data.js에서 EventOrderController 표기를 실제 OrderEventController로 고치고, source links가 docs/visual-lab/sequences/12/index.html 기준 docs/theory.md, docs/implementation.md, docs/checklist.md로 열리게 고치세요. EventPublisherService.kt / NotificationConsumer.kt가 한 file 값에 묶인 codePoint는 각각 존재하는 경로로 나누거나 구조적으로 표현하세요. unrelated visual-lab JS/CSS는 refactor하지 마세요.
```

## 다음 수정 loop 운영 방법

1. P0인 `08`부터 시작합니다.
2. 한 번에 하나의 sequence 또는 하나의 topic repo만 수정합니다.
3. 수정 전 이 보고서의 해당 sequence prompt를 그대로 전달합니다.
4. 수정 후 해당 topic repo에서 path check, 금칙어 check, 필요한 테스트를 실행합니다.
5. 중앙 레포에서는 `python3 scripts/validate-visual-labs.py`, `git diff --check`, `git status --short`를 확인합니다.
6. 다음 sequence로 넘어가기 전 submodule dirty 상태와 변경 주체를 확인합니다.
