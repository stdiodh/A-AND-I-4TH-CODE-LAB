# Visual Lab Design System Review

## 1. Goal Result

중앙 manifest에 등록된 8개 토픽 저장소의 00~12 Visual Lab을 하나의 `Learning Signal Trace` 경험으로 통일했다.

```text
현재 질문
-> 관찰 조건 선택
-> 실제 시스템 경로
-> 상태 snapshot과 증거
-> 개념·코드 맥락
-> 검증
-> 다음 질문
```

공통 shell과 상호작용 문법은 같지만 primary workbench는 요청, 영속성, 검증 gate, 인증, trust, test, cache, realtime fan-out, runtime, pipeline, refactor invariant, event delivery라는 실제 주제 구조를 따른다. 화면을 같은 카드 묶음으로 복제하지 않고 시퀀스마다 3~4개의 실제 조건을 비교하게 했다.

## 2. Design Direction

- Subject: 실행 중인 백엔드 요청, 객체, 상태, 경계와 전달 단위를 직접 추적하며 이론을 확인하는 정적 학습 환경.
- Audience: Spring Boot 기초부터 이벤트 기반 사고까지 순서대로 학습하는 A&I 백엔드 학습자.
- Single job: 이번 시퀀스에서 조작할 조건, 관찰할 시스템 변화, 설명해야 할 다음 판단을 첫 화면에서 놓치지 않게 한다.
- Core palette: Lab Paper `#F8F9FB`, System Ink `#111B3F`, A&I Navy `#0C2691`, Signal Blue `#2955E4`, Evidence Teal `#3F8996`, Boundary Line `#C9D6F3`.
- Typography: system sans 안에서 Display와 Body의 크기·굵기·폭을 분리하고, path·command·status·data는 system mono를 사용한다.
- Signature: 선택한 조건에 따라 실제 request, object, token, cache, artifact, test 또는 event route가 바뀌는 `Learning Signal Trace` 하나만 사용한다.
- Motion: 사용자가 명시적으로 재생하거나 단계를 이동할 때 active signal만 240ms로 이동한다. 반복 animation은 없으며 reduced motion에서는 즉시 상태를 바꾼다.

상세 계획과 첫 genericity critique는 [Visual Lab Design System Application Plan](./visual-lab-design-system-plan.md)에 기록했다.

## 3. Genericity Critique Result

첫 방향은 selector와 공통 trace만 두면 일반 stepper 또는 관리자 도구가 될 위험이 있었다. 다음처럼 수정했다.

- Hero를 제품 소개 문구가 아닌 실제 시퀀스 질문으로 바꿨다.
- 공통 actor diagram 대신 13개의 topic-specific workbench kind를 만들었다.
- terminal, metric, 번호는 실제 명령·상태·순서를 전달할 때만 허용했다.
- `incident` 문법을 모든 주차에 강제하지 않고 기초·테스트·리팩토링은 입력, 보장 범위와 invariant를 중심에 뒀다.
- 색상 accent보다 실제 경로, 차단 지점, fan-out, 저장 경계와 pipeline gate가 정체성을 만들게 했다.

## 4. Sequence Coverage

| Sequence | Workbench | Scenario | 검수한 핵심 상태 |
|---|---|---:|---|
| 00 | Request Workbench | 4 | GET, POST, invalid request, Git/DB 기초 |
| 01 | Request Packet Trace | 3 | create, read, restart |
| 02 | Persistence Boundary | 4 | save, restart, update, missing id |
| 03 | Failure Gate | 3 | valid, empty title, missing post |
| 04 | Auth Boundary | 4 | login success/fail, no token, wrong author |
| 05 | Trust & Recovery Map | 4 | verified/unverified, account collision, recovery mail |
| 06 | Test Harness | 4 | service, auth, controller, test boundary |
| 07 | Cache State Inspector | 4 | miss, hit, TTL, eviction |
| 08 | Connection & Broadcast Console | 4 | fan-out, pre-connect, unsubscribed sender, origin reject |
| 09 | Runtime Boundary | 4 | runtime success, test block, jar mismatch, missing env |
| 10 | Pipeline Gate | 4 | success, build block, deploy block, verify failure |
| 11 | Behavior Invariant Map | 4 | baseline, small refactor, contract break, scope warning |
| 12 | Event Delivery Trace | 4 | direct call, event, replay, publish failure |

manifest의 13개 시퀀스는 모두 `ready`다. 현재 등록 데이터에는 planned 시퀀스가 없으므로 planned 화면 검수는 적용 대상이 아니다. 데이터 누락과 fatal fallback은 공통 renderer에 유지했다.

## 5. Component Coverage

### 변경한 항목

- Topbar를 compact context bar로 만들고 저장소와 현재 sequence 맥락만 남겼다.
- Hub의 마케팅형 Hero와 카드 grid를 repository learning journey로 바꿨다.
- Sequence Hero를 현재 질문, 목표, topic identity로 축소했다.
- 13개 section 목차를 질문, 관찰, 개념·코드, 검증, 다음 질문의 5단계 nav로 바꿨다.
- Flow tab을 실제 scenario selector로 바꿨다.
- actor diagram과 Step Explorer를 topic workbench, Signal Trace, native progress와 단계 controls로 통합했다.
- Object flow, Responsibility, Concept, Code Point를 선택 단계의 evidence/context drawer로 연결했다.
- Checklist를 session-local checkbox와 progress로 만들었다.
- Next는 실제 다음 질문과 사용 가능한 상세 페이지 link를 함께 제공한다.
- selected, blocked, warning, recovered 상태는 label과 route text를 색상과 함께 표시한다.
- error와 empty fallback은 누락된 데이터와 확인 대상을 설명한다.
- hover 위치 이동을 제거하고 모든 button·link에 3px `:focus-visible`을 제공했다.
- 390px에서는 1열 selector, local trace scroll, 44px target과 긴 한국어·영문·path 줄바꿈을 적용했다.

### 유지한 항목과 이유

- 각 저장소의 `docs/visual-lab/index.html`과 sequence `index.html` entry는 상대 경로와 GitHub Pages 호환 계약을 보존하기 위해 유지했다.
- `window.visualLabData`의 기존 `actors`, `flows`, `codePoints`, `concepts`, `checks`, `next`는 기술 콘텐츠와 과거 소비자 호환을 위해 유지했다.
- 기존 실제 theory, implementation, checklist, 코드 경로와 공식 source link는 기술 범위를 바꾸지 않기 위해 유지했다.
- 8개 저장소에 CSS/JavaScript를 로컬 복제하는 구조는 서브모듈별 독립 GitHub Pages 실행을 위해 유지하고 SHA-256 동일성을 검증했다.
- 별도 terminal panel은 실제 공통 기능이 아니므로 새로 만들지 않았다. 명령과 로그는 해당 시퀀스의 evidence에서만 보여준다.

## 6. Before & After

### 구조

- Before: 13개 문서 섹션과 반복 카드가 같은 내용을 Overview, Diagram, Step, Object Flow에서 다시 설명했다.
- After: 한 질문 아래 condition selector와 주제별 workbench가 먼저 나오고, 선택한 route에 맞는 evidence, concept, code, verification이 이어진다.

### 시각적 위계

- Before: 큰 소개 Hero와 여러 카드가 핵심 조작보다 먼저 보였다.
- After: sequence 질문, workbench instruction, 선택 조건, active route와 결과가 차례로 보인다.

### 상호작용

- Before: 단계 변경 때 전체 앱을 다시 그려 focus가 사라질 수 있었고 broad `aria-live`가 있었다.
- After: scenario와 단계 focus를 복원하고, 실제 상태 요약 한 곳만 `role="status"`로 알린다. 두 native progress가 route 단계와 checklist 완료를 각각 표현한다.

### 모바일과 접근성

- Before: 긴 nav와 diagram이 viewport를 넘을 위험이 있고 reduced-motion 대체가 없었다.
- After: 390px page overflow 0, interactive target 44px 이상, H1 1개와 heading jump 0, visible focus, local trace scroll과 reduced-motion 수동 상태를 확인했다.

기준과 결과 이미지는 다음 폴더에 있다.

- [Before screenshots](./screenshots/visual-lab-redesign/before/)
- [After screenshots](./screenshots/visual-lab-redesign/after/)
- 동일 기준 비교: DB hub 1440/390, Sequence 02 1440/390, Sequence 05 1440.
- 추가 결과: Sequence 08 fan-out, Sequence 10 pipeline, Sequence 12 event.

## 7. Browser Verification

정적 서버는 중앙 root를 `python3 -m http.server 4181`로 열어 모든 서브모듈을 같은 origin에서 검수했다.

| 대상 | Viewport | 결과 |
|---|---|---|
| 00~12 상세 13개 | 1440x1000 | 13/13 통과 |
| 00~12 상세 13개 | 1024x900 | 13/13 통과 |
| 00~12 상세 13개 | 768x1024 | 13/13 통과 |
| 00~12 상세 13개 | 390x844 | 13/13 통과 |
| 8개 저장소 Hub | 1440x1000 | 8/8 통과 |
| 8개 저장소 Hub | 390x844 | 8/8 통과 |

각 상세 화면에서 expected workbench kind, 3~4 scenario, Signal Trace node, H1 1개, heading 순서, 44px button, page overflow, fatal state와 live region 수를 확인했다. 총 52회 상세 검사와 16회 hub 검사에서 실패는 0건이었다.

상호작용 검수:

- 실제 CDP keyboard `Tab`으로 skip link, brand, 질문, 관찰 순서와 각 3px focus ring을 확인했다.
- `Enter`로 `없는 id 수정` scenario를 선택하고 `aria-pressed`와 focus 유지가 바뀌는 것을 확인했다.
- `Enter`로 다음 단계 progress가 1에서 2로 증가하고 focus가 `다음 단계`에 유지되는 것을 확인했다.
- 차단 scenario의 마지막 단계에서도 active node 1개와 blocked node 3개가 유지되는지 확인했다.
- 마지막 단계에서는 focus가 활성 `이전 단계`로, 첫 단계에서는 활성 `다음 단계`로 이동하는 경계 focus를 확인했다.
- `Space`로 verification checkbox와 완료 progress가 0에서 1로 증가하는 것을 확인했다.
- `--force-prefers-reduced-motion` 환경에서 control copy가 `모션 감소: 수동`으로 바뀌고 route progress는 정적으로 남는 것을 확인했다.
- 13개 상세 페이지의 browser console error는 0건이었다.

## 8. Static Verification

```text
python3 scripts/validate-manifest.py
PASS: 4 check group(s), 0 issue(s), 0 warning group(s)

python3 scripts/validate-visual-labs.py
PASS: 8 repo group(s), 0 issue(s), 0 warning group(s)

python3 scripts/validate-visual-lab-colors.py
PASS: 8 repo group(s), 0 issue(s), 0 warning group(s)

node --check: all shared and sequence JavaScript passed
git diff --check: central and all 8 topic repositories passed
shared CSS SHA-256: 8/8 identical
shared JavaScript SHA-256: 8/8 identical
small evidence text contrast: 12.34:1 on white, 11.60:1 on evidence surface
```

새 framework, package, CDN 또는 외부 font는 추가하지 않았다.

## 9. Remaining Issues

구현과 검증 범위에서 남은 기능 오류는 없다. 현재 manifest에 planned 시퀀스가 없으므로 planned 전용 화면은 검수하지 않았으며, 추후 status가 추가되면 같은 design skill과 validator 계약으로 별도 상태를 구현해야 한다.

## 10. Semantic Diagram Follow-up Result

사용자 검토에서 기존 Signal Trace의 각 상자와 연결선이 무엇을 뜻하는지 불명확하다는 문제가 확인됐다. 후속 구현에서는 공통 workbench를 다음 문법으로 보강했다.

- 책임을 수행하는 주체와 lifecycle을 관찰할 resource만 node로 두고 local SVG icon, kind, role, boundary를 visible text로 표시했다.
- DTO, Entity, token, HTTP status, command와 event payload는 `동사 · 전달물` edge에 배치했다.
- 요청, 호출, 변환, 저장, 응답, 실패, event, config, 비교를 edge kind와 text label로 함께 구분했다.
- diagram 위에 scenario 전체를 한 문장으로 읽는 caption과 읽는 법 legend를 추가했다.
- failure/blocked 경로에는 실제 마지막 책임과 실행되지 않은 downstream의 이유를 `notReached`로 표시했다.
- edge 선택을 exact evidence step으로 연결하고 legacy flow 배열 위치 상속을 제거했다.
- 독립 lane은 `선택 가능` 상태로 두고 현재 lane만 `지남/현재/다음`과 progress를 가진다. 자동 재생은 lane 끝에서 멈추며 lane 경계는 `다음 경로`로 명시한다.
- 자동 재생 중 사용자가 다른 탐색 대상으로 이동하면 재생을 멈춰 keyboard focus를 빼앗지 않는다.
- 390px에서는 같은 node → edge → node 문법을 세로 화살표로 바꾸고 label과 payload를 유지한다.

대표 결과 이미지는 다음과 같다.

- [02 Persistence · Desktop](./screenshots/visual-lab-redesign/after/seq-02-semantic-1440x1000.png)
- [02 Persistence · Mobile](./screenshots/visual-lab-redesign/after/seq-02-semantic-390x844.png)
- [08 WebSocket · Desktop](./screenshots/visual-lab-redesign/after/seq-08-semantic-1440x1000.png)
- [12 Event · Desktop](./screenshots/visual-lab-redesign/after/seq-12-semantic-1440x1000.png)

최종 브라우저 회귀는 00~12의 13개 페이지, 50개 scenario를 `1440x1000`, `1024x900`, `768x1024`, `390x844`에서 각각 수행했다. 총 200개 scenario 상태에서 semantic diagram 1개, active edge 1개, accessible edge name, 44px target, clipped text 0, page overflow 0, persistent live region 1개와 console error 0을 확인했다.

추가 상호작용 검수 결과:

- edge 선택 뒤 `aria-current="step"`, lane progress와 evidence가 같은 transition을 가리켰다.
- lane 끝의 `다음 경로` 이동과 다른 lane의 `선택 가능` 상태를 확인했다.
- 2x 자동 재생이 현재 lane 끝에서 멈추고 다른 navigation focus를 선택하면 진행하지 않았다.
- `--force-prefers-reduced-motion`에서 재생과 속도 control이 disabled되고 `모션 감소: 수동` 상태가 표시됐다.
- local `system-icons.svg` symbol이 desktop과 mobile에서 표시됐고 외부 asset 요청은 없었다.
