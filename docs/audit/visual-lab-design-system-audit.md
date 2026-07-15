# Visual Lab Design System Audit

## 1. 조사 범위와 기준 상태

조사 기준일은 2026-07-15이다. 중앙 `docs/manifest/sequences.yml`에 등록된 8개 토픽 저장소와 00~12 전체 시퀀스를 대상으로 했다.

공통 구현 파일은 다음과 같다.

```text
docs/visual-lab/index.html
docs/visual-lab/styles.css
docs/visual-lab/visual-lab-data.js
docs/visual-lab/visual-lab.js
docs/visual-lab/sequences/NN/index.html
docs/visual-lab/sequences/NN/visual-lab-data.js
```

8개 저장소의 `styles.css`와 `visual-lab.js`는 SHA-256이 동일하다. 데이터는 시퀀스별로 다르지만 화면은 같은 범용 렌더러를 사용한다.

기준 검증은 통과했다.

```text
python3 scripts/validate-manifest.py
python3 scripts/validate-visual-labs.py
node --check */docs/visual-lab/*.js
node --check */docs/visual-lab/sequences/*/*.js
```

브라우저 기준 화면은 `docs/audit/screenshots/visual-lab-redesign/before`에 기록했다.

## 2. 현재 경험 요약

상세 화면은 모든 시퀀스를 다음 13개 섹션으로 동일하게 표현한다.

```text
Overview -> Why -> Before / After -> Flow -> Code Points
-> Object Flow -> Responsibilities -> Concepts -> Terminology
-> Practical Points -> References -> Checklist -> Next
```

학습 데이터는 정확하고 풍부하지만, 현재 무엇을 조작하고 무엇을 판단해야 하는지보다 긴 문서 목차와 흰 카드 묶음이 먼저 보인다. 같은 실행 흐름이 Overview, Sequence Diagram, Step Rail, Object Flow에서 반복되어 화면 길이에 비해 새로운 정보가 적다.

## 3. UI 인벤토리

| 항목 | 현재 목적과 위계 | 문제와 위험 | 유지할 요소 | 변경할 요소 |
|---|---|---|---|---|
| Topbar / Brand | A&I와 저장소 식별 | 모바일에서 두 줄이 되지만 하단 sticky offset은 고정 | 저장소 맥락 | 높이를 줄이고 실제 학습 위치 표시 |
| Hub Hero | 저장소 설명 | 큰 마케팅 Hero와 장식 카드로 보임 | 저장소 제목과 범위 | 시퀀스 관계와 현재 질문 우선 |
| Sequence Cards | 상세 페이지 진입 | 같은 카드 반복, 선행 관계가 보이지 않음 | 실제 시퀀스 링크 | 연결된 학습 경로로 전환 |
| Sequence Switcher | 현재 시퀀스 표시 | 단일 시퀀스에서도 노출 | 현재 번호 | 다중 시퀀스 저장소에서만 사용 |
| Section Nav | 13개 섹션 이동 | 항상 Overview만 active, 문서 목차가 핵심 경험처럼 보임 | 빠른 이동 | 학습 판단 단계 trace로 축소 |
| Hero | 질문, 문제, 목표 | 제목과 빈 공간이 과도하고 랜딩 페이지처럼 보임 | 실제 질문과 목표 | compact 판단 헤더 |
| Why | 배경과 한계 | Before/After, Concepts와 내용 중복 | 문제와 선택 근거 | 현재 실험 조건에 통합 |
| Before / After | 사고 전환 | 모든 주차가 같은 2카드 비교 | 비교가 실제인 시퀀스의 데이터 | 06·11 등 적합한 주차에서만 핵심 UI로 사용 |
| Flow Tabs | 여러 흐름 선택 | 실제 시나리오 선택 기능은 유효 | 실제 flow 데이터 | 주차별 실험 조건 선택기로 명명 |
| Sequence Diagram | actor 이동 | 모든 주제를 같은 lane으로 평탄화, 모바일 lane 과다 | actors, from/to, message | 주차별 primary workbench로 교체 |
| Step Rail | 단계 선택 | 단계가 바뀔 때 전체 앱 재렌더링, focus 손실 위험 | 순서와 선택 | 부분 상태 업데이트와 의미 있는 progress |
| Step Detail | Problem/Concept/Action/Check | 6개 작은 카드가 같은 비중, 전체 `aria-live`가 과도 | 단계별 근거 | 관찰·판단·확인을 한 맥락 패널로 통합 |
| Playback | 흐름 자동 진행 | reduced-motion 미지원, 정보보다 재생 기능이 두드러질 수 있음 | 이전/다음 | 신호 이동 한 순간만 표현, autoplay 기본 정지 |
| Code Points | 실제 코드 연결 | 별도 카드 그리드로 흐름과 분리 | 실제 경로와 짧은 코드 | 선택한 신호 단계의 evidence drawer |
| Object Flow | 객체/레이어 이동 | Flow와 반복 | 실제 변환 정보 | 주차별 workbench 내부에 합침 |
| Responsibilities | 계층 책임 | Concept과 중복 | 책임 경계 | 선택 actor의 context로 표시 |
| Concepts | 핵심 개념 | 독립 카드 목록으로 판단 흐름에서 이탈 | 기술적으로 정확한 설명 | 선택 상태에 연결된 concept panel |
| Terminology | 용어 표 | 모바일 수평 스크롤, 핵심 흐름을 끊음 | 용어와 주의점 | 접을 수 있는 reference shelf |
| Practical Points | 범위와 한계 | Concept/Why 반복 가능 | 의도적으로 남긴 한계 | decision 조건과 caution으로 연결 |
| References | 공식 문서 | 렌더러에 00~12 링크가 하드코딩됨 | 공식 링크 | 시퀀스 데이터로 이동 |
| Checklist | 말로 설명할 기준 | 정적 질문 카드라 완료 상태가 없음 | 실제 확인 질문 | 체크 가능한 verification strip |
| Next | 다음 시퀀스 맥락 | 링크 없이 설명만 존재 | 이어지는 질문 | 실제 상세 링크와 action 제공 |
| Empty / Error | 데이터 부재 방어 | 준비 중 문구만 있고 해결 방향이 약함 | 안전한 fallback | 누락 항목과 확인 대상을 명시 |
| Disabled | 첫/마지막 이동 방지 | 이유는 시각적으로만 추론 | native disabled | 이유를 label로 제공 |
| Hover | 링크·카드 피드백 | `translateY`가 장식이며 레이아웃 움직임을 만듦 | 경계 강조 | 위치 이동 제거 |
| Focus | 키보드 위치 표시 | 기본 outline은 있으나 전체 재렌더링으로 focus 유실 가능 | 3px visible outline | 상태 갱신 후 focus 보존 |
| Mobile | 1열과 내부 scroll | topbar/nav sticky 겹침, `overflow-x:hidden`이 문제를 숨길 수 있음 | 1열 전환 | page overflow 자체 제거, 넓은 도식만 국소 scroll |

## 4. Genericity 진단

- 검은 배경이나 네온을 쓰지는 않지만, 흰 배경·파란 accent·둥근 카드만 남으면 다른 교육 대시보드와 구분하기 어렵다.
- 13개 섹션을 모두 보여주는 구조는 내용이 많아 보이지만, 학습자가 내려야 할 현재 판단을 강조하지 않는다.
- 번호는 실제 순서에 쓰여 의미가 있지만, badge와 divider 일부는 장식에 가깝다.
- Hero는 제품 소개 랜딩 페이지에 가깝고, 핵심 조작은 첫 viewport 아래에 있다.
- Sequence Diagram은 요청 흐름에는 맞지만 테스트, 리팩토링, 캐시 상태, CI/CD gate를 충분히 표현하지 못한다.
- terminal 또는 code 스타일은 실제 명령·로그·코드 증거에서만 의미가 있다. 장식용 terminal을 새로 만들 이유가 없다.

## 5. 접근성과 모션 위험

- `prefers-reduced-motion` 처리가 없다.
- `scroll-behavior: smooth`와 progress transition이 항상 적용된다.
- 단계 상세 전체가 `aria-live="polite"`라 자동 재생 시 과도하게 읽힐 수 있다.
- progress가 값이 있는 progressbar 의미를 갖지 않는다.
- 일부 38px 버튼은 모바일 touch target이 작다.
- section nav의 active 상태가 실제 scroll 위치와 동기화되지 않는다.
- 선택 시 전체 DOM을 교체하여 keyboard focus가 사라질 수 있다.

## 6. 저장소 위험

- `spring-boot-db-access-lab`의 02~06과 `spring-boot-deployment-runtime-lab`의 09~10은 공통 CSS/JS를 공유한다. 한 시퀀스 변경은 같은 저장소의 모든 시퀀스를 회귀 검증해야 한다.
- 8개 저장소에 같은 runtime이 복제되어 있어 수동 동기화 drift 위험이 있다. 외부 runtime dependency를 만들지 않고 검증 가능한 동일 복사본을 유지해야 한다.
- DB Access 저장소의 미추적 `src/main/resources/static/index.html`과 중앙 `.idea/`는 현재 작업 범위가 아니며 보존한다.

## 7. 결론

데이터 계약과 실제 콘텐츠는 유지할 가치가 높다. 리디자인의 중심은 카드를 다시 꾸미는 일이 아니라, 공통 shell을 줄이고 각 주차의 실제 시스템 상태를 조작하는 하나의 primary workbench를 만드는 일이다.

## 8. Semantic Diagram Follow-up Audit

첫 디자인 시스템 적용 뒤 실제 00~12 workbench를 다시 읽어 보니 `route`가 순서를 보여주는 데는 성공했지만, 학습자가 화살표의 의미를 이론과 연결하기에는 정보가 부족했다.

- actor, DTO, Entity, token, status, command가 같은 node 모양으로 표시됐다.
- connector에는 방향만 있고 동작 동사와 전달 payload가 없었다.
- route node와 legacy flow step 수가 다르면 위치 비례로 evidence가 연결돼 다른 코드 포인트를 보여줄 수 있었다.
- 실패는 이후 node를 흐리게 만드는 데 그쳐 exception, handler, 실제 응답과 실행되지 않은 mutation을 설명하지 못했다.
- 서로 독립적인 lane을 전체 step index 하나로 재생하면 00의 Git/DB 준비나 12의 HTTP 응답/event 전달 사이에 가짜 시간 순서가 생길 수 있었다.
- icon만 추가하는 안은 일반 flowchart와 다르지 않고 같은 모호성을 남겼다.

유지할 요소는 실제 scenario selector, snapshot, evidence, code point, verification과 다음 질문이다. 변경 대상은 diagram 문법과 단계 연결이다.

```text
책임 주체
-- 동사 · 전달 payload -->
다음 책임 주체
```

새 기준은 node에 icon, 종류, 역할과 visible 책임 경계를 함께 표시하고, edge에 `from`, `to`, `verb`, `payload`, `kind`를 둔다. DTO, Entity, token, status와 event payload는 edge로 이동한다. failure는 실제 handler/응답과 `notReached` 이유를 표현한다. progress는 현재 lane 안에서 동작하고 다른 lane은 `선택 가능` 경로로 남긴다.

## 9. Student Comprehension Follow-up Audit

Semantic diagram 적용 뒤 저장된 desktop/mobile 화면을 학생의 첫 진입 순서로 다시 검수했다. 기술 구조의 정확성은 좋아졌지만 “무엇을 먼저 해야 하는가”는 여전히 불명확했다.

| 항목 | 학생 관점 문제 | 유지 | 변경 |
|---|---|---|---|
| 첫 viewport | 큰 질문 header가 조건과 첫 행동을 아래로 밀어냄 | 실제 학습 질문 | compact briefing과 첫 조건을 함께 배치 |
| Scenario label | `miss`, `hit`, `blocked`가 결과를 미리 공개 | 실제 조건 데이터 | 입력 조건만 표시하고 예측 뒤 결과 공개 |
| Semantic lane | 모든 actor와 transition을 펼쳐 현재 단계가 묻힘 | 실제 from/to/verb/payload | topology는 고정하고 현재 transition 한 개만 확장 |
| Controls | 긴 diagram 아래에 있어 mobile에서 수십 화면 이동 | 이전/다음과 progress | 현재 이유·증거와 같은 viewport에 배치 |
| Playback | 재생·속도가 학습 목표보다 먼저 보임 | 수동 단계 이동 | autoplay와 속도 control 제거 |
| 용어 | 첫 화면에 전문 용어가 동시에 등장 | 정확한 기술 용어 | 첫 등장 시 짧은 한국어 역할 설명 |
| Evidence | 개념 모델과 실제 실행 증거의 범위가 혼합될 수 있음 | 실제 code point와 check | 개념·코드·단위 테스트·수동 runtime label 분리 |
| Icon asset | 21px sprite icon이 반복 node 안에서 사실상 보이지 않음 | 공통 outline 문법과 visible label | 40~48px 개별 SVG `<img>`와 text fallback |
| Topic visual | 전체 path만 있어 memory/DB, cache state, fan-out 같은 선행 관계를 재구성해야 함 | 실제 시스템 관계 | 주차별 설명 SVG 한 개를 예측과 관찰 사이에 배치 |
| Mobile | 저장된 390px 첫 화면 일부가 잘리고 실제 조작 진입을 증명하지 못함 | 1열 전환 | page overflow 0, 첫 행동 노출, asset bounding box 재검증 |

추가 asset audit에서 `system-icons.svg`는 HTTP 200, `image/svg+xml`, 유효 XML과 30개 symbol을 가진 정상 파일이었다. 그러나 symbol만 포함하므로 파일을 직접 열면 빈 화면처럼 보이며, 외부 `<use>`는 `file://`에서 안정적이지 않다. 따라서 기술적으로 로드 가능한 것과 학생이 실제로 보았는지를 분리해 검사해야 한다.

새 완료 기준은 broken request 0뿐 아니라 `img.complete`, `naturalWidth > 0`, 화면 안의 최소 표시 크기, 390px과 desktop 가시성, 200% zoom과 text fallback까지 포함한다.

## 10. Lifeline과 이론 연결 재검수

actor-once topology와 transition 카드 적용 뒤 13개 시퀀스, 50개 scenario를 다시 읽었다. 책임 이름은 정확해졌지만 학생은 actor 목록과 transition grid를 머릿속에서 다시 이어야 했다.

| 항목 | 현재 문제 | 이번 변경 기준 |
|---|---|---|
| 시간 순서 | transition grid가 viewport에 따라 줄바꿈돼 실행 시간이 좌우·상하로 섞임 | participant header 아래 수직 lifeline과 위→아래 message |
| 현재 변화 | from/to와 payload는 보이지만 단계 전후 상태가 흩어짐 | 현재 message에 subject, before, after를 함께 표시 |
| message 종류 | self-call, 응답, event, failure의 선 문법이 약함 | loop, 역방향, 점선, 중단 표식과 visible label 병행 |
| 모바일 | actor 카드 목록이 첫 transition보다 먼저 길게 쌓임 | 현재 `출발 책임 → 도착 책임` 한 단계가 먼저 보이는 압축 lifeline |
| 코드 근거 | 파일 경로 badge가 코드가 맡은 일보다 먼저 보임 | 짧은 설명/주석 → 실제 핵심 코드 → 바뀌는 상태 |
| 이론 왕복 | Visual Lab은 theory 문서 루트만 가리키고 theory에는 돌아오는 링크가 없음 | `seq-00`~`seq-12` 명시 anchor와 양방향 link |
| 관찰 후 정리 | 대부분 prediction 뒤 결과를 읽고 끝남 | 모든 scenario에서 인과 규칙을 자기 말로 쓰는 reflection |
| 문구 | 영문 meta label과 quiz형 칭찬이 학습 내용과 경쟁 | 주제별 질문과 행동을 말하는 자연스러운 한국어 |

유지할 요소는 실제 local SVG asset, scenario prediction gate, 수동 이전/다음, native progress, code point 계약과 기술 콘텐츠다. 변경의 중심은 새 카드를 추가하는 일이 아니라 같은 실제 데이터를 시간 순서, 상태 변화와 확인 근거로 다시 연결하는 것이다.

## 11. Theory와 브랜치 근거 재검수

화면 문법을 고친 뒤 guide, implementation, answer branch의 실제 파일을 `git show`로 다시 대조했다. 흐름의 모양이 맞아도 다른 주차 코드나 완성 뒤 코드가 섞이면 학생에게는 틀린 증거가 되므로 다음 항목을 별도 수정 대상으로 잡았다.

| 범위 | 발견한 문제 | 반영 기준 |
|---|---|---|
| 01~02 | starter TODO와 뒤 주차의 인증 포함 create 코드가 현재 코드처럼 보임 | starter와 완성 뒤 모양을 구분하고 02는 `request.author` 범위로 복원 |
| 03~04 | GET path binding을 Bean Validation으로 묶고 JWT 검증·subject 추출을 한 호출로 합침 | DTO 검증과 path binding, `validateToken`과 `getEmail`을 실제 단계로 분리 |
| 05~06 | TODO인 OAuth·SMTP 구현과 answer/main의 서로 다른 테스트를 현재 증거처럼 혼합 | 구현된 helper, 구현 목표, 단위 테스트가 보장하는 범위를 따로 표시 |
| 09 | `.dockerignore`가 jar를 build context에서 제외하고 기본 Compose는 app을 실행하지 않음 | 현재 COPY blocker와 prod Compose 선행 조건을 성공 경로와 분리 |
| 10 | 분리 job·script는 완성 목표이고 중첩 heredoc 때문에 현재 remote deploy가 중단됨 | answer-only 구조와 현재 최초 실패 gate를 명시하고 verify 성공을 단정하지 않음 |
| 11 | answer에는 구조 정리뿐 아니라 trim, 예외, save·validation 변화가 함께 있음 | 유지된 test subset과 의도적 동작 변경을 별도 lane으로 표시 |
| 12 | publish 호출, HTTP 응답과 consumer 완료 순서를 직선으로 확정하고 mock을 broker 성공으로 확대 | 호출 순서와 비동기 fork를 분리하고 publisher confirm 없는 broker 상태는 unknown으로 표시 |

이 재검수 뒤에는 `호출 전/후 책임`, `반환 대기/보유`, `판정 입력/결과`처럼 어느 단계에도 붙일 수 있는 effect 문장도 실제 값과 상태로 교체한다. 중앙 validator는 같은 문구, theory의 sequenceDiagram·상태표·코드 block 누락, 영어 meta label을 실패로 처리한다.
