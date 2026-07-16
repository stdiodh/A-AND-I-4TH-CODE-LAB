# Visual Lab Design System Review

## 1. Goal Result

중앙 manifest에 등록된 8개 토픽 저장소의 00~12 Visual Lab을 학생 중심 `Diagnostic Lifeline`으로 통일하고, 같은 흐름을 8개 `docs/theory.md`의 Mermaid·상태 변화 표·실제 코드와 연결했다.

```text
필수 전제
-> 결과를 숨긴 입력 조건
-> 학생의 예측
-> 참여자와 수직 시간축
-> 메시지별 이전/이후 상태
-> 짧은 설명과 실제 코드
-> 이론 연결과 내 말로 정리
-> 다음 질문
```

학생은 경로와 결과를 보기 전에 먼저 예상한다. 공개 뒤에는 participant를 한 번만 놓고 message를 위에서 아래로 읽는다. 현재 message는 `출발 책임 -> 도착 책임`, 동사, payload, 실제 이전/이후 상태와 근거 범위를 한곳에 보여준다. 모바일은 같은 정보를 한 단계씩 보여주며 이전/다음으로 이동한다.

## 2. Design Direction

- Subject: 운영 중인 백엔드 요청과 상태 변화를 실제 증거로 설명하는 학습 환경.
- Audience: DTO, Entity, Repository, JWT, Redis, STOMP, runtime과 event 경계를 아직 자연스럽게 연결하지 못하는 Spring Boot 학습자.
- Single job: 한 화면 안에서 조건을 예측하고, 현재 한 단계의 상태 변화를 관찰하며, 누가 무엇을 왜 다음 책임에 넘겼는지 자기 말로 설명하게 한다.
- Signature: `Diagnostic Lifeline`. participant, 수직 lifeline과 message row로 실행 시간을 고정하고 현재 상태 변화와 근거만 강조한다.
- Motion: 수동 이전/다음에서 active signal만 240ms로 바뀐다. 자동 재생과 속도 control은 없고, reduced motion에서는 같은 상태를 즉시 표시한다.

### Core palette

| 이름 | HEX | 역할 |
|---|---|---|
| Lab Paper | `#F8F9FB` | 전체 학습 canvas |
| System Ink | `#111B3F` | 본문과 시스템 설명 |
| A&I Navy | `#0C2691` | 질문과 책임 경계 |
| Signal Blue | `#2955E4` | 선택과 현재 transition |
| Evidence Teal | `#3F8996` | 관찰 증거와 회복 상태 |
| Boundary Line | `#C9D6F3` | 계층·trust·runtime 경계 |

`#176F72`와 `#6F82B8`은 각각 통과·회복 상태와 대기 상태·강한 구조선에 쓰는 지원색이다. 상태는 색상만 사용하지 않고 label과 설명을 함께 표시한다.

### System layer palette

후속 가독성 보정에서는 participant의 시스템 위치와 message의 실행 상태를 서로 다른 색상 축으로 분리했다.

| 위치 | Surface / Line | 화면 label |
|---|---|---|
| `outside` | `#F1F5F9` / `#5B677A` | 외부·호출자 |
| `interface` | `#E6F4F7` / `#0E7490` | 입구·출구 |
| `application` | `#F2EDFF` / `#6D43A8` | 서비스·정책 |
| `resource` | `#EAF5EE` / `#2C7352` | 상태·데이터 |
| `integration` | `#FFF4D6` / `#926000` | 연동·메시징 |
| `runtime` | `#EEF2F7` / `#52627A` | 실행·배포 |

진행 상태는 별도로 `current #2955E4`, `passed #176F72`, `failed #B4233C`, `pending #6F82B8`을 사용한다. 레이어색은 실패·경고 의미로 바꾸지 않고, 두 축 모두 visible text를 남긴다.
작은 layer label은 각 surface 위에서 4.5:1 이상을 만족한다. 특히 초기 후보였던 `outside #64748B`와 `resource #2F7D59`는 각각 4.34:1, 4.48:1에 그쳐 `#5B677A`와 `#2C7352`로 어둡게 보정했다.

### Typography roles

- Display: system sans, 700~900. 현재 질문과 장의 핵심 판단에만 사용한다.
- Body: system sans, 400~700, line-height 1.6 이상. 한국어 이론, 이유와 비교에 사용한다.
- Utility/Data: system mono, 500~900. HTTP, status, path, command, payload와 progress에 사용한다.

외부 font, CDN, framework와 package는 추가하지 않았다.

## 3. Genericity Critique

첫 적용은 아이콘이 붙은 일반 시스템 inspector에 가까웠다. 한 번에 20~25개의 edge를 펼쳤고, `miss`, `hit`, `blocked` 같은 scenario 이름이 답을 먼저 공개했으며, 작은 sprite icon은 실제 화면에서 거의 보이지 않았다. 자동 재생도 학생이 인과를 읽는 속도보다 기능 자체를 두드러지게 했다. 두 번째 적용도 actor strip과 transition card grid가 떨어져 있어 학생이 실행 순서를 다시 조립해야 했다.

최종안에서는 다음을 보정했다.

- scenario 이름은 요청값, 저장 상태, fixture, header 같은 입력 조건만 말한다.
- native radio로 예측을 확정하기 전에는 결과, 관계도, path와 outcome을 렌더링하지 않는다.
- 필수 용어는 기본 닫힌 `details`로 두어 모르는 학생만 먼저 확인할 수 있다.
- 주제별 설명 SVG를 예측과 관찰 사이에 두고 memory/DB, cache lifecycle, fan-out, runtime nesting처럼 해당 주차에서만 성립하는 관계를 먼저 보여준다.
- participant를 한 번만 표시하고 수직 lifeline 아래 message를 위에서 아래로 읽게 한다.
- participant header, lifeline과 주제 SVG에 실제 `systemLayer`를 표시해 색을 빼도 “외부 → 입구 → 서비스 → 상태/연동/실행” 위치 관계가 남게 한다.
- active lane에는 그 경로의 step endpoint만 남겨 비교용 전체 node가 현재 흐름처럼 보이는 문제를 줄인다.
- 모든 lane을 2~7 message로 제한하고 실제 Controller, Service, Adapter, Repository, DB, broker 경계를 건너뛰지 않는다.
- `호출 전/후 책임`, `반환 대기/보유` 같은 틀 문장을 실제 값, row·collection, token subject, subscription, build artifact와 assertion 결과로 교체한다.
- 이론과 코드 근거는 해당 시퀀스의 guide·implementation·answer 브랜치를 대조하고, TODO나 완성 뒤 코드의 범위를 명시한다.
- 자동 재생과 속도 control을 제거해 학생이 관찰 속도를 결정한다.

검은 배경이나 accent를 제거해도 `조건 -> 예측 -> 관찰 -> 비교 -> 인과 규칙 수정`이 남으므로 정체성은 색상이 아니라 학습 행위에서 나온다.

## 4. Sequence Coverage

| Sequence | 주제 관계도 | 실제로 비교한 조건 |
|---|---|---|
| 00 | Request & Tool Map | HTTP method·URL·JSON, Git 명령, DB 도구 |
| 01 | Memory CRUD Map | 생성, 조회, 재시작 |
| 02 | Persistence Boundary | 저장, 재시작 뒤 조회, 수정, 없는 id |
| 03 | Request Gates | 요청값, 빈 title, 없는 id |
| 04 | Auth Boundaries | 자격 정보, token header, 작성자 관계 |
| 05 | External Trust | 외부 identity, account collision, 복구 요청 |
| 06 | Test Scope | fixture, repository 반환, 실제·대역 협력자, HTTP 경계 |
| 07 | Cache State Cycle | 빈 cache, 남은 TTL, 만료, mutation 뒤 조회 |
| 08 | Subscription Fan-out | 연결·구독 상태, sender와 subscriber, origin |
| 09 | Runtime Nesting | source, jar, `.dockerignore` build-context gate, image, container, process와 env |
| 10 | Pipeline Gates | build, deploy shell, heredoc blocker, verify 입력과 최초 실패 gate |
| 11 | Behavior Change Ledger | 유지된 테스트 범위와 trim·예외·저장처럼 의도적으로 바뀐 동작 |
| 12 | Response/Event Fork | publish 시도 뒤 producer·broker 병렬 경로, 중복 직접 호출, publisher·consumer 실패 경계 |

manifest의 13개 시퀀스는 모두 `ready`다. 현재 planned 시퀀스가 없으므로 planned 전용 화면은 적용 대상이 아니다. 데이터 누락과 asset load 실패는 공통 renderer가 확인 파일과 text fallback을 보여준다.

8개 토픽의 `docs/theory.md`에는 `seq-00`~`seq-12` anchor를 두고, 각 시퀀스의 주 경로 Mermaid, 4열 상태 변화 표, 학생이 먼저 읽는 짧은 설명, 실제 3~12줄 코드와 Visual Lab 역링크를 배치했다. starter가 TODO인 경우 완성 코드처럼 단정하지 않고 구현 목표 또는 완성 뒤 확인할 모양으로 범위를 표시한다.

## 5. Component Coverage

### 변경한 항목

- Topbar와 brand mark: repository·sequence 문맥만 남긴 compact context bar와 로컬 favicon을 적용했다.
- Hub: 마케팅형 Hero와 card grid를 실제 학습 순서가 보이는 journey로 바꿨다.
- Hero와 learning nav: 현재 질문을 먼저 보여주고 질문, 관찰, 개념·코드, 검증, 다음 질문으로 이동한다.
- Scenario selector: 결과 대신 입력 조건을 말하며 선택 상태를 text와 `aria-pressed`로 표시한다.
- Terms와 prediction: compact `details`, native radio, 명시적인 결과 공개 button을 추가했다.
- Topic visual: 13개의 기본 주제 SVG와 visible caption, load error fallback을 유지하고 실제 조건별 구조가 다른 경우 `scenario.visual`로 교체하는 계약을 추가했다.
- Diagnostic Lifeline: participant header, 수직 lifeline, 2~7 message, 시스템 레이어 label, 현재 이전/이후 상태, 근거 범위, native progress와 수동 이전/다음을 적용했다.
- Incident·Observation·Metric·Cause·Concept·Decision 역할: 모든 주차에 장애 용어를 강제하지 않고 입력 조건, evidence, cause comparison, concept/context, causal decision으로 매핑했다.
- System Map·Flow Explorer·special panel: 공통 관계도 위에 cache, fan-out, runtime, pipeline, invariant, event 등 주제 고유 구조를 데이터로 표현했다.
- Checklist와 Next Question: session-local checkbox/progress와 실제 다음 상세 페이지 또는 repository journey를 연결했다.
- selected, blocked, warning, recovered, empty, fatal: 색상 외 label, 이유, 실행되지 않은 책임과 확인 파일을 표시한다.
- focus, mobile, reduced motion: 3px focus ring, focus 복원, 44px touch target, 390px 1열 예측, 세로 transition과 정적 reduced-motion 대체를 적용했다.

### 유지한 항목과 이유

- 각 저장소의 `docs/visual-lab/index.html`과 sequence `index.html` entry는 상대 경로와 독립 GitHub Pages 실행 계약 때문에 유지했다.
- `window.visualLabData`의 기존 `actors`, `flows`, `codePoints`, `concepts`, `checks`, `next`는 기술 콘텐츠와 기존 소비자 호환 때문에 유지했다.
- theory, implementation, checklist와 실제 코드 경로는 커리큘럼·기술 범위를 임의로 바꾸지 않기 위해 유지했다.
- 8개 저장소에 CSS, JavaScript와 icon을 로컬 복제하는 구조는 각 서브모듈이 단독으로 열려야 하므로 유지하고 checksum 동일성을 검증했다.
- terminal panel은 공통 장식으로 만들지 않았다. 실제 명령이나 log는 해당 transition의 evidence에서만 보여준다.

## 6. Visible Asset Review

- 30개 직접 렌더링 icon을 각 저장소의 `assets/icons`에 두고 화면에서 40px로 표시했다.
- 13개 기본 topic diagram과 조건별 설명 SVG, `visual-lab-mark.svg`, 원본·호환용 `system-icons.svg`, `SOURCE.md`, `LICENSES.md`를 저장소 내부에 보존했다.
- 모든 SVG는 `viewBox`를 가지며 외부 URL, script와 font를 포함하지 않는다.
- topic diagram의 최소 visible text는 390px에서 10.5px 이상이 되도록 validator가 viewBox 대비 font-size를 계산한다.
- `<img>`는 `alt`, visible caption과 text fallback을 함께 가지며 browser에서 `complete`, `naturalWidth > 0`, 실제 표시 크기를 확인했다.

후속 레이어·scenario asset 변경의 browser, 390px, keyboard, reduced-motion, console 검수 결과는 8.1절에 별도로 기록했다. 기존 Guided Story 검수 수치와 이번 후속 검수 수치를 섞어 계산하지 않는다.

## 7. Before & After

| 기준 | Before | After |
|---|---|---|
| 구조 | 반복 카드와 긴 diagram이 동시에 노출 | 전제 -> 입력 -> 예측 -> 관찰 -> 비교 순서 |
| 시각 위계 | 큰 Hero와 상태 badge가 첫 행동보다 앞섬 | 현재 질문과 첫 예측이 390px 첫 화면에 보임 |
| 이론 이해 | node 이름과 다수 edge를 학생이 스스로 재구성 | participant 아래 message를 시간순으로 읽고 실제 이전/이후 상태를 이론·코드와 연결 |
| 상호작용 | 결과가 먼저 보이고 재생 기능이 중심 | 예측 gate와 수동 이전/다음이 중심 |
| 에셋 | sprite가 작거나 빈 파일처럼 보임 | 직접 렌더링 icon과 13개 설명 SVG가 실제 표시 |
| 모바일 | 긴 nav·diagram과 첫 행동 사이 거리가 큼 | 1열 선택, 읽을 수 있는 SVG, page overflow 0 |
| 접근성 | broad live region과 focus 손실 위험 | native control, 한 곳의 status, focus 복원과 3px ring |

기존 `docs/audit/screenshots/visual-lab-redesign` 이미지는 첫 Guided Story·semantic diagram 개편까지의 기록이며, 이번 Diagnostic Lifeline 후속안의 최종 화면은 아니다. 당시 후속 검수는 같은 URL을 고정 폭 iframe에서 열어 viewport, 요소 위치, overflow, asset 크기와 DOM 상태를 수치로 비교했다. 이후 저장한 실제 가독성 after 화면은 8.2절의 새 screenshot을 기준으로 사용한다.

## 8. Browser Verification

중앙 root를 `python3 -m http.server 4184 --directory .`로 열어 모든 서브모듈을 같은 origin에서 검수했다.

| 대상 | Viewport | 상태 수 | 결과 |
|---|---|---:|---|
| 00~12 예측 전 | 1440x1000, 1024x900, 768x1024, 390x844 | 52 | 통과 |
| 00~12의 모든 scenario 예측 후 | 1440x1000, 390x844 | 100 | 통과 |
| 00~12의 모든 lane | 1440x1000, 390x844 | 178 | 통과 |
| 8개 repository hub | 1440x1000, 1024x900, 768x1024, 390x844 | 32 | 통과 |
| 정확성 보정 뒤 09~12 scenario | 1440x1000, 390x844 | 32 | 통과 |
| 정확성 보정 뒤 09~12 lane | 1440x1000, 390x844 | 52 | 통과 |
| 복잡 경로 중간 폭 재검수 | 1024x900, 768x1024 | 4 | 통과 |

예측 전에는 질문, terms, scenario, prediction만 존재하고 topic visual, path, result와 outcome은 없음을 확인했다. 예측 후에는 topic SVG, 유일한 lifeline, 2~7 message, 현재 step 1개, 수동 이전/다음, 실제 이전/이후 상태, 근거 범위, comparison과 local icon이 함께 나타났다.

각 상태에서 H1 1개, heading jump 0, page-level overflow 0, broken image 0, persistent status 1개와 console error 0을 확인했다. 50개 scenario와 89개 lane의 388개 message는 모두 2~7개 lane 제한, 이전·이후 상태, code evidence와 이론 link 계약을 지킨다. 390px에서는 첫 prediction option이 첫 viewport에 보이고 긴 한국어·path가 영역 밖으로 넘지 않았다. 768px과 1024px의 넓은 sequence stage는 page를 밀지 않고 해당 stage 안에서만 수평 이동한다.

Keyboard 검수에서는 skip link, brand, terms, scenario, native radio, 공개 button, lane, message, 성찰 입력, checklist와 theory link의 순서와 3px focus ring을 확인했다. 모바일에서는 이전·다음과 단계 바로 가기를 실행한 뒤 `tabindex="-1"`인 현재 message card로 focus가 돌아오고 같은 3px ring이 표시됐다. reduced-motion 강제 환경에서는 transition과 smooth scroll이 제거되고 자동 재생 없이 같은 active state가 정적으로 남았다. 수정된 09~12를 직접 page에서 다시 열어 26개 lane을 조작한 뒤에도 console log와 error는 0개였다.

### 8.1 System Layer 후속 검수 — 2026-07-16

이 절은 System Layer를 처음 적용했을 당시의 breakpoint와 hash를 보존한다. 현재 `1099px 이하 = 현재 단계 집중 layout` 계약과 최신 checksum은 8.2와 9.1절이 우선한다.

중앙 root를 `python3 -m http.server 4173 --directory .`로 열고 후속 변경을 검수했다. 마지막 hub copy cache 확인만 새 origin인 4174에서 다시 열었다.

| 대상 | Viewport | 확인 상태 | 결과 |
|---|---|---:|---|
| 00~12 모든 scenario와 lane | 1440x1000 | scenario 50, lane 89 | 통과 |
| 00~12 모든 scenario와 lane | 390x844 | scenario 50, lane 89 | 통과 |
| 02·07·12 전체 scenario와 lane | 1024x900 | scenario 12, lane 21 | 통과 |
| 02·07·12 전체 scenario와 lane | 768x1024 | scenario 12, lane 21 | 통과 |
| 8개 repository hub | 위 네 viewport | 32 | 통과 |

각 공개 상태에서 topic SVG의 `complete`와 `naturalWidth`, page overflow, H1 한 개, heading jump, 현재 message 한 개, 최대 7개 message, participant `systemLayer`, visible layer label과 layer rail을 검사했다. 900px 이하는 desktop stage를 숨기고 출발·도착 actor의 layer label 두 개를 표시했으며, 1024px은 desktop lifeline을 유지했다. 12의 네 조건은 direct call, response/event fork, duplicate/idempotency, publisher/consumer failure SVG로 각각 교체됐다. browser console warning과 error는 0개였다.

키보드로 skip link와 모바일 current message에 이동했을 때 3px solid focus ring과 3px offset을 확인했다. 공개와 단계 전환 뒤 focus는 desktop message button 또는 mobile current card로 복원됐다. 현재 브라우저는 reduced-motion media emulation을 제공하지 않아 query 자체는 `false`였지만, 로드된 CSSOM에서 단일 `prefers-reduced-motion: reduce` rule, smooth scroll 제거, animation 0.01ms와 단일 iteration을 직접 확인했다. 레이어 색은 움직이지 않으며 기존 message animation 외 새 motion은 없다.

후속 화면 증거는 `docs/audit/screenshots/visual-lab-layer-system`에 보존했다.

- `hub-desktop-1440.jpg`
- `hub-mobile-390.jpg`
- `12-desktop-1440.jpg`
- `02-mobile-390.jpg`

### 8.2 시퀀스 가독성·문구 감량 후속 검수 — 2026-07-16

중앙 root를 `python3 -m http.server 4173 --directory .`로 열고 현재 단계 정보 소유권, SVG geometry와 문구 감량을 다시 검수했다.

| 대상 | Viewport | 확인 상태 | 결과 |
|---|---|---:|---|
| 00~12 모든 scenario·lane·step | 1440x1000 | scenario 50, lane 89, step 388 | 통과 |
| 00~12 모든 scenario·lane·step | 390x844 | scenario 50, lane 89, step 388 | 통과 |
| 02·08·12 첫 scenario의 전체 lane·step | 1024x900 | lane 4, step 18 | 통과 |
| 02·08·12 첫 scenario의 전체 lane·step | 768x1024 | lane 4, step 18 | 통과 |
| 8개 repository hub | 위 네 viewport | 32 | 통과 |
| 설명 SVG | native 1280x720과 308px 축소 기준 | 16 | 통과 |

총 776개 공개 step 상태에서 현재 payload 한 번, before/after 한 쌍, H1 한 개, page overflow 0, broken image 0과 제거 대상 renderer marker 0을 확인했다. 이전·다음 실행 뒤 focus는 desktop message button 또는 mobile current card로 돌아왔고 3px solid outline과 3px offset을 유지했다. browser console warning과 error는 0개였다.

390px에서는 actor layer와 boundary, verb/payload, before/after를 한 surface가 소유한다. 02 첫 step의 반복 영역은 약 1,533px에서 509px로 줄었고 전체 388 step의 현재 surface와 controls 합은 최대 750px이었다. 1024px과 768px도 desktop lifeline을 억지로 축소하거나 내부 가로 이동시키지 않고 같은 현재 단계 집중 layout을 사용했다.

16개 SVG는 browser client rect 기준 viewBox 밖 text 0, owner box를 침범한 text 0이었다. 최소 author font-size는 22px이고 validator의 308px 환산 결과는 모두 10.5px 이상이었다. 308px 축소 contact sheet에서도 text/arrow 교차와 잘린 결론이 없었다. 공통 layer 이름과 footer 결론은 group당 한 번만 남기고 cache cycle, fan-out, runtime nesting, pipeline gate와 event fork의 서로 다른 topology는 유지했다.

50개 scenario의 visible 역할 문구는 30,252자에서 26,045자로 13.9% 줄었다. 120자 초과 역할 문구는 0개이며 변경 경로는 prompt, prediction, caption, lane description, evidence, outcome과 reflection 역할에만 한정했다. step, effect, check, ID, lane 구조와 기술 결론은 유지했다.

현재 브라우저는 reduced-motion media query 강제 emulation을 제공하지 않았다. 대신 로드된 CSSOM에서 단일 `prefers-reduced-motion: reduce` rule, smooth scroll 제거, 0.01ms duration과 1회 iteration을 확인했고 기본 상태에서도 자동 재생이 없음을 확인했다. 별도 browser zoom 제어도 제공되지 않아 1536px 화면의 200%에 해당하는 768 CSS px와 더 좁은 390 CSS px에서 text overlap과 page overflow 0을 확인했다.

새 화면 증거는 `docs/audit/screenshots/visual-lab-readability`에 보존했다.

- `hub-db-desktop-1440.png`
- `hub-db-mobile-390.png`
- `sequence-02-desktop-1440.png`
- `sequence-02-mobile-390.png`
- `sequence-08-mobile-390.png`
- `sequence-12-desktop-1440.png`

## 9. Static Verification

```text
python3 scripts/validate-manifest.py
PASS: 4 check group(s)

python3 scripts/verify-sequences.py
PASS: 13 sequence(s), 0 failure(s)

python3 scripts/validate-visual-labs.py
PASS: 8 repo group(s), 0 issue(s), 0 warning group(s)

python3 scripts/validate-visual-lab-colors.py
PASS: 8 repo group(s), 0 issue(s), 0 warning group(s)

node --check: Visual Lab JavaScript 29개 통과
xmllint: Visual Lab HTML 21개와 SVG 272개 통과
diagram inventory: 기본 13개 + scenario 전용 3개 = 16개
git diff --check: 중앙 및 8개 토픽 저장소 통과
shared CSS SHA-256: 8/8 동일 (`66b108420516411f9fac480ab0f84ff3eebcf9ed4b7c3f402c649fc130a88388`)
shared JavaScript SHA-256: 8/8 동일 (`f6e7dfa8c1f7e3d49c6e67a8f05dac1ba3a14a9af87c3a177a63476e20192e6f`)
direct icon SHA-256: 같은 이름 8/8 동일
```

### 9.1 가독성 감량 후 최신 정적 검증 — 2026-07-16

```text
python3 scripts/validate-manifest.py
PASS: 4 check group(s), 0 issue(s), 0 warning(s)

python3 scripts/verify-sequences.py
PASS: 13 sequence(s), 0 failure(s), 0 warning(s)

python3 scripts/validate-visual-labs.py
PASS: 8 repo group(s), 0 issue(s), 0 warning group(s)

python3 scripts/validate-visual-lab-colors.py
PASS: 8 repo group(s), 0 issue(s), 0 warning group(s)

node --check: Visual Lab JavaScript 29개 통과
xmllint: Visual Lab HTML 21개, SVG 272개 통과
git diff --check: 중앙 및 8개 토픽 저장소 통과
legacy duplicate filename 후보: 0개
shared CSS SHA-256: 8/8 동일 (`10a2f65671dd144fb1d21832105973eb258eb0eb99a8194c9923bce0e07ac479`)
shared JavaScript SHA-256: 8/8 동일 (`c640a2b678fa2657157ef0b17131b6f93576493073713efb2edf786fb02154ba`)
```

### 9.2 서브모듈 반영 기록

| 저장소 | `main` commit |
|---|---|
| `aandi-prerequisite-bootcamp` | `fd851a6` |
| `spring-boot-rest-crud-lab` | `90a213a` |
| `spring-boot-db-access-lab` | `1fa0117` |
| `spring-boot-redis-cache-lab` | `3ac7f47` |
| `spring-boot-realtime-communication-lab` | `68aa3e6` |
| `spring-boot-deployment-runtime-lab` | `e8051ea` |
| `spring-boot-refactoring-foundation-lab` | `fba3be6` |
| `spring-boot-event-driven-lab` | `6bea28b` |

8개 commit을 각 origin `main`에 먼저 push하고 원격 SHA 일치를 확인한 뒤 중앙 저장소의 submodule pointer를 갱신했다. 자식 코드와 중앙 포인터는 서로 다른 commit 단계로 처리했다.

## 10. Remaining Issues

Visual Lab renderer와 링크 계약에서 확인된 기능 오류는 없다. 다만 deployment 토픽의 현재 코드에는 문서 범위 밖의 실행 blocker와 보안 확인 지점이 남아 있다. `.dockerignore`가 `build`를 제외하면서 Dockerfile은 `build/libs/*.jar`를 복사하고, deploy workflow의 중첩 heredoc 종료 토큰에는 remote shell 기준 들여쓰기가 남는다. 또한 workflow YAML에는 secret reference만 있지만 실행 시 실제 값이 EC2 `.env`에 기록되며 현재 workflow에는 이 파일을 위한 명시적 `chmod`, `chown` 또는 제한적 `umask`가 없다. 이번 작업은 이를 성공한 경로로 숨기지 않고 09·10 theory와 Visual Lab의 최초 실패 gate와 secret 경계로 표현하며, Docker 정책과 workflow 자체는 별도 코드 변경으로 남긴다.

현재 manifest에 planned 시퀀스가 없어 planned 전용 화면은 브라우저 검수 대상이 아니었다. 이후 planned status가 등록되면 같은 design skill과 validator 계약으로 이유와 다음 가능 조건을 표시해야 한다.
