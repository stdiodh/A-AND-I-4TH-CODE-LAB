# Visual Lab Design System Review

## 1. Goal Result

중앙 manifest에 등록된 8개 토픽 저장소의 00~12 Visual Lab을 학생 중심 `Guided System Story`로 통일했다.

```text
필수 전제
-> 결과를 숨긴 입력 조건
-> 학생의 예측
-> 주제 관계도
-> 한 단계 관찰
-> 이유와 실제 증거
-> 반대 조건 비교
-> 인과 규칙과 다음 질문
```

학생은 경로와 결과를 보기 전에 먼저 예상해야 한다. 공개 뒤에는 같은 actor를 행마다 반복하지 않는 topology와 2~7개의 실제 transition을 이전/다음으로 관찰한다. 현재 transition, 이유, 코드·요청·테스트 증거와 반대 조건이 같은 학습 문맥을 가리킨다.

## 2. Design Direction

- Subject: 운영 중인 백엔드 요청과 상태 변화를 실제 증거로 설명하는 학습 환경.
- Audience: DTO, Entity, Repository, JWT, Redis, STOMP, runtime과 event 경계를 아직 자연스럽게 연결하지 못하는 Spring Boot 학습자.
- Single job: 한 화면 안에서 조건을 예측하고, 현재 한 단계의 상태 변화를 관찰하며, 누가 무엇을 왜 다음 책임에 넘겼는지 자기 말로 설명하게 한다.
- Signature: `Learning Signal Trace`. 선택한 조건의 actor topology를 유지하면서 현재 transition 하나, 전달물, 이유와 증거만 강조한다.
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

`#176F72`와 `#6F82B8`은 각각 상태 ink와 강한 구조선에만 쓰는 지원색이다. 상태는 색상만 사용하지 않고 label과 설명을 함께 표시한다.

### Typography roles

- Display: system sans, 700~900. 현재 질문과 장의 핵심 판단에만 사용한다.
- Body: system sans, 400~700, line-height 1.6 이상. 한국어 이론, 이유와 비교에 사용한다.
- Utility/Data: system mono, 500~900. HTTP, status, path, command, payload와 progress에 사용한다.

외부 font, CDN, framework와 package는 추가하지 않았다.

## 3. Genericity Critique

첫 적용은 아이콘이 붙은 일반 시스템 inspector에 가까웠다. 한 번에 20~25개의 edge를 펼쳤고, `miss`, `hit`, `blocked` 같은 scenario 이름이 답을 먼저 공개했으며, 작은 sprite icon은 실제 화면에서 거의 보이지 않았다. 자동 재생도 학생이 인과를 읽는 속도보다 기능 자체를 두드러지게 했다.

최종안에서는 다음을 보정했다.

- scenario 이름은 요청값, 저장 상태, fixture, header 같은 입력 조건만 말한다.
- native radio로 예측을 확정하기 전에는 결과, 관계도, path와 outcome을 렌더링하지 않는다.
- 필수 용어는 기본 닫힌 `details`로 두어 모르는 학생만 먼저 확인할 수 있다.
- 주제별 설명 SVG를 예측과 관찰 사이에 두고 memory/DB, cache lifecycle, fan-out, runtime nesting처럼 해당 주차에서만 성립하는 관계를 먼저 보여준다.
- topology에서 actor를 한 번만 표시하고 현재 transition과 인접 이유·증거를 함께 읽게 한다.
- 모든 lane을 2~7 transition으로 제한하고 실제 Controller, Service, Adapter, Repository, DB, broker 경계를 건너뛰지 않는다.
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
| 09 | Runtime Nesting | source, jar, image, container, process와 env |
| 10 | Pipeline Gates | build, deploy, verify 입력과 최초 실패 gate |
| 11 | Behavior Invariant | 반환·예외·검증된 호출과 구조 변경 범위 |
| 12 | Response/Event Fork | 동기 응답, event 발행, 중복 전달, publish 실패 |

manifest의 13개 시퀀스는 모두 `ready`다. 현재 planned 시퀀스가 없으므로 planned 전용 화면은 적용 대상이 아니다. 데이터 누락과 asset load 실패는 공통 renderer가 확인 파일과 text fallback을 보여준다.

## 5. Component Coverage

### 변경한 항목

- Topbar와 brand mark: repository·sequence 문맥만 남긴 compact context bar와 로컬 favicon을 적용했다.
- Hub: 마케팅형 Hero와 card grid를 실제 학습 순서가 보이는 journey로 바꿨다.
- Hero와 learning nav: 현재 질문을 먼저 보여주고 질문, 관찰, 개념·코드, 검증, 다음 질문으로 이동한다.
- Scenario selector: 결과 대신 입력 조건을 말하며 선택 상태를 text와 `aria-pressed`로 표시한다.
- Terms와 prediction: compact `details`, native radio, 명시적인 결과 공개 button을 추가했다.
- Topic visual: 13개의 주제별 SVG와 visible caption, load error fallback을 연결했다.
- Learning Signal Trace: actor-once topology, lane, 2~7 transition, 현재 이유·증거, native progress와 수동 이전/다음을 적용했다.
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
- 13개 topic diagram, `visual-lab-mark.svg`, 원본·호환용 `system-icons.svg`, `SOURCE.md`, `LICENSES.md`를 저장소 내부에 보존했다.
- 모든 SVG는 `viewBox`를 가지며 외부 URL, script와 font를 포함하지 않는다.
- topic diagram의 최소 visible text는 390px에서 10.5px 이상이 되도록 validator가 viewBox 대비 font-size를 계산한다.
- `<img>`는 `alt`, visible caption과 text fallback을 함께 가지며 browser에서 `complete`, `naturalWidth > 0`, 실제 표시 크기를 확인했다.

## 7. Before & After

| 기준 | Before | After |
|---|---|---|
| 구조 | 반복 카드와 긴 diagram이 동시에 노출 | 전제 -> 입력 -> 예측 -> 관찰 -> 비교 순서 |
| 시각 위계 | 큰 Hero와 상태 badge가 첫 행동보다 앞섬 | 현재 질문과 첫 예측이 390px 첫 화면에 보임 |
| 이론 이해 | node 이름과 다수 edge를 학생이 스스로 재구성 | 주제 SVG 뒤 현재 한 transition의 주체·동사·payload·이유를 설명 |
| 상호작용 | 결과가 먼저 보이고 재생 기능이 중심 | 예측 gate와 수동 이전/다음이 중심 |
| 에셋 | sprite가 작거나 빈 파일처럼 보임 | 직접 렌더링 icon과 13개 설명 SVG가 실제 표시 |
| 모바일 | 긴 nav·diagram과 첫 행동 사이 거리가 큼 | 1열 선택, 읽을 수 있는 SVG, page overflow 0 |
| 접근성 | broad live region과 focus 손실 위험 | native control, 한 곳의 status, focus 복원과 3px ring |

기존 기준 화면과 최종 Guided System Story 화면은 다음 폴더에 보존했다.

- [Before screenshots](./screenshots/visual-lab-redesign/before/)
- [After screenshots](./screenshots/visual-lab-redesign/after/)
- 최종 비교 대상: DB Hub desktop/mobile, Sequence 02 desktop/mobile, Sequence 07 cache, Sequence 12 event.

## 8. Browser Verification

중앙 root를 `python3 -m http.server 4173 --directory .`로 열어 모든 서브모듈을 같은 origin에서 검수했다.

| 대상 | Viewport | 상태 수 | 결과 |
|---|---|---:|---|
| 00~12 예측 전 | 1440x1000, 1024x900, 768x1024, 390x844 | 52 | 통과 |
| 00~12의 모든 scenario 예측 후 | 1440x1000, 390x844 | 100 | 통과 |
| 8개 repository hub | 1440x1000, 390x844 | 16 | 통과 |

예측 전에는 질문, terms, scenario, prediction만 존재하고 topic visual, path, result와 outcome은 없음을 확인했다. 예측 후에는 topic SVG, 유일한 semantic diagram, 2~7 transition, 현재 step 1개, 수동 이전/다음, 이유·증거, comparison과 local icon이 함께 나타났다.

각 상태에서 H1 1개, heading jump 0, page-level overflow 0, broken image 0, persistent status 1개와 console error 0을 확인했다. 390px에서는 첫 prediction option이 첫 viewport에 보이고 긴 한국어·path가 영역 밖으로 넘지 않았다.

Keyboard 검수에서는 skip link, brand, terms, scenario, native radio, 공개 button과 transition control의 순서와 3px focus ring을 확인했다. scenario 변경과 공개 뒤 focus가 선택한 control 또는 첫 transition으로 돌아왔다. reduced-motion 강제 환경에서는 transition과 smooth scroll이 제거되고 자동 재생 없이 같은 active state가 정적으로 남았다.

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

node --check: 모든 Visual Lab JavaScript 통과
xmllint: 모든 SVG 통과
git diff --check: 중앙 및 8개 토픽 저장소 통과
shared CSS SHA-256: 8/8 동일 (`e3101f166e95b871596bff505e5f6c73e0e474f1`)
shared JavaScript SHA-256: 8/8 동일 (`722b37d15ab0313ee225ad6b7a251c08a1831a6a`)
direct icon SHA-256: 같은 이름 8/8 동일
```

## 10. Remaining Issues

구현·검증 범위에서 남은 기능 오류는 없다. 현재 manifest에 planned 시퀀스가 없어 planned 전용 상태는 브라우저 검수 대상이 아니었다. 이후 planned status가 등록되면 같은 design skill과 validator 계약으로 이유와 다음 가능 조건을 표시해야 한다.
