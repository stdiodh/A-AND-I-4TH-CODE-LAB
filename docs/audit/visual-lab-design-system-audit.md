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
