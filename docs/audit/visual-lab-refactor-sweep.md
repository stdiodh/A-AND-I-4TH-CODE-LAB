# Visual Lab Refactor Sweep

## 1. 작업 시작 상태

- 기준 파일: `docs/manifest/sequences.yml`
- 기준 repoPath: manifest의 8개 repo group
- 초기 검증:
  - `python3 scripts/validate-manifest.py` 통과
  - `python3 scripts/validate-visual-labs.py` 통과
- 시작 시 모든 repoPath의 `docs/visual-lab`에는 표준 4파일만 존재했습니다.
- 별도 legacy 파일(`style.css`, `app.js`, `data.js`, `components.css`, `dist/*` 등)은 발견되지 않았습니다.
- 기존 구현은 validator 기준은 만족했지만, 대부분 단일 Step Explorer형 구조라 이번 목표의 문서형 섹션 구조, 책임 지도, 용어 표, 실무 포인트, 다중 시퀀스 스위처 요구를 충분히 담지 못했습니다.

판단:

- 루트 워크플로 문서는 "한 번에 하나의 시퀀스"를 기본 원칙으로 두지만, 이번 사용자 목표와 실행 프롬프트는 전체 repoPath 스윕과 다중 시퀀스 앱 수렴을 명시했습니다.
- 더 구체적인 현재 목표를 우선하여 repoPath 단위로 진행했습니다.
- `spring-boot-db-access-lab`은 02~06을 하나의 Visual Lab 앱으로, `spring-boot-deployment-runtime-lab`은 09~10을 하나의 Visual Lab 앱으로 구성했습니다.

## 2. 레포별 Visual Lab 상태

| Repo | Sequences | Required Files | Legacy Candidates | Answer Exposure | Design Status | Data Status | Priority |
|---|---|---|---|---|---|---|---|
| `aandi-prerequisite-bootcamp` | 00 | 4/4 present | None | None | 기존 단일 stepper -> 문서형 UI 적용 | HTTP/JSON/Git/DB 용어 PAAR 반영 | Medium |
| `spring-boot-rest-crud-lab` | 01 | 4/4 present | None | None | 기존 단일 stepper -> 문서형 UI 적용 | 요청/응답, Controller/Service/메모리 저장소 흐름 반영 | Medium |
| `spring-boot-db-access-lab` | 02~06 | 4/4 present | None | None | 다중 시퀀스 switcher와 문서형 UI 적용 | 02~06 각각 why/flows/responsibilities/glossary/practical/checks 작성 | High |
| `spring-boot-redis-cache-lab` | 07 | 4/4 present | None | None | 기존 단일 stepper -> 문서형 UI 적용 | cache-aside, hit/miss, stale data 반영 | Medium |
| `spring-boot-realtime-communication-lab` | 08 | 4/4 present | None | None | 기존 단일 stepper -> 문서형 UI 적용 | connect/subscribe/send/receive, HTTP 비교 반영 | Medium |
| `spring-boot-deployment-runtime-lab` | 09~10 | 4/4 present | None | None | 다중 시퀀스 switcher와 문서형 UI 적용 | runtime 실행 단위와 CI/CD 자동화 흐름 분리 | High |
| `spring-boot-refactoring-foundation-lab` | 11 | 4/4 present | None | None | 기존 단일 stepper -> 문서형 UI 적용 | 테스트 기준, 책임 분리, 예외 응답 보강 흐름 반영 | Medium |
| `spring-boot-event-driven-lab` | 12 | 4/4 present | None | None | 기존 단일 stepper -> 문서형 UI 적용 | 주문 생성, 이벤트 발행/소비, 직접 호출 비교 반영 | Medium |

## 3. 레거시 파일 후보

| Repo | File | Reason | Action |
|---|---|---|---|
| All repoPath | None | `docs/visual-lab` 내부에 표준 4파일 외 파일이 없었습니다. | 삭제 대상 없음 |

## 4. 삭제/병합/유지 결정

| Repo | File | Decision | Reason |
|---|---|---|---|
| All repoPath | `docs/visual-lab/index.html` | 유지 후 교체 | 표준 진입 파일입니다. JS 렌더링 스켈레톤으로 단순화했습니다. |
| All repoPath | `docs/visual-lab/styles.css` | 유지 후 병합/교체 | 기존 스타일 역할을 문서형 2-column 레이아웃, sticky nav, switcher, stepper, glossary table 스타일로 수렴했습니다. |
| All repoPath | `docs/visual-lab/visual-lab.js` | 유지 후 병합/교체 | 기존 단일 flow 렌더링을 단일/다중 시퀀스, hash routing, section nav, flow tabs, step detail 렌더링으로 확장했습니다. |
| All repoPath | `docs/visual-lab/visual-lab-data.js` | 유지 후 교체 | 각 theory의 PAAR 흐름, 시퀀스 다이어그램, 용어 정리, 실무 포인트를 표준 `sequences[]` 데이터로 재작성했습니다. |
| All repoPath | extra legacy files | 삭제 없음 | 추가 파일이 없어 archive 폴더나 legacy 보관 파일을 만들지 않았습니다. |

## 5. 검증 결과

진행 중 갱신:

- 표준 파일 목록 재확인: 모든 repoPath가 `index.html`, `styles.css`, `visual-lab-data.js`, `visual-lab.js` 4파일만 보유
- answer 노출 문자열 재검색: Visual Lab 파일 내 노출 없음
- 외부 CDN/라이브러리: asset 로드 없음

최종 명령 결과:

```bash
node --check <all docs/visual-lab/*.js>
# passed

python3 scripts/validate-manifest.py
# PASS: 4 check group(s), 0 issue(s), 0 warning group(s)

python3 scripts/validate-visual-labs.py
# PASS: 8 repo group(s), 0 issue(s), 0 warning group(s)

git diff --check
# passed
```

브라우저 확인:

- `spring-boot-db-access-lab/docs/visual-lab`을 로컬 서버로 열었습니다.
- `http://localhost:8080/#seq-02`에서 02~06 시퀀스 스위처, flow tab, step rail이 렌더링되는 것을 확인했습니다.
- `http://localhost:8080/#seq-05`에서 OAuth2 + SMTP 시퀀스로 hash 진입이 정상 동작하는 것을 확인했습니다.
- 브라우저 콘솔 error log는 0건이었습니다.

추가 보강 및 재검증: 2026-06-04

- 공통 `visual-lab.js`에 Step Explorer 자동 재생, 일시정지, 속도 변경, 진행률 바를 추가했습니다.
- 공통 `styles.css`에 Visual Lab 디자인 가이드의 필수 색상 토큰을 추가하고 기존 스타일 변수를 해당 토큰에 맞춰 연결했습니다.
- 모바일 폭에서 sticky section nav와 문서 섹션이 가로 overflow를 만들지 않도록 공통 `styles.css`의 grid item 수축 규칙을 보강했습니다.
- 카드 radius 토큰을 디자인 가이드의 둥근 교육용 카드 톤에 맞춰 `24px`로 조정했습니다.
- 8개 repoPath 모두 동일한 공통 JS/CSS 엔진을 사용하도록 동기화했습니다.
- 첨부된 5시간 고도화 프롬프트 기준에 맞춰 `docs/audit/visual-lab-deep-refactor-sweep.md`를 추가했습니다.
- 공통 렌더러에 Before / After, Actor 기반 Diagram View, Step View, 접힘 Source View, Object / Layer Movement, Official References 섹션을 추가했습니다.
- Actor 카드형 Diagram View를 participant lane, lifeline, message arrow가 보이는 `Sequence Diagram` UI로 교체했습니다.
- 공식 문서 레퍼런스는 각 시퀀스 ID별 공통 맵에서 제공하며, 외부 링크는 콘텐츠 링크로만 사용합니다.
- 13개 시퀀스 데이터가 모두 PAAR 유사 흐름을 갖는지 확인했습니다.
  - `why.problem`: Problem
  - `why.limits`: Analyze
  - `flows[].steps[].action`: Action
  - `checks`: Result
- 13개 시퀀스 모두 하나 이상의 `flows[].mermaid`, 용어 4개 이상, 실무 포인트 3개 이상, 확인 질문 4개 이상을 보유함을 확인했습니다.
- Chrome headless로 아래 경로를 열어 렌더링 후 DOM에 `Visual Lab content`, `핵심 흐름과 시퀀스 다이어그램`, `용어 정리`, `실무 포인트`, `재생`, `속도 1x`가 생기는 것을 확인했습니다.
  - `aandi-prerequisite-bootcamp/docs/visual-lab/index.html#seq-00`
  - `spring-boot-rest-crud-lab/docs/visual-lab/index.html#seq-01`
  - `spring-boot-db-access-lab/docs/visual-lab/index.html#seq-02`
  - `spring-boot-db-access-lab/docs/visual-lab/index.html#seq-05`
  - `spring-boot-deployment-runtime-lab/docs/visual-lab/index.html#seq-10`
  - `spring-boot-event-driven-lab/docs/visual-lab/index.html#seq-12`
- 좁은 브라우저 폭에서 위 대표 경로들의 `documentElement.scrollWidth <= clientWidth`를 확인했습니다.
- 00~12 전체 시퀀스를 모바일 523px, 데스크톱 1280px viewport로 확인했고, 모든 경로에서 sequence participant/message 렌더링, page overflow 0건, clipped 후보 0건, console error 0건을 확인했습니다.

## 6. 남은 이슈

- 사용자 프롬프트가 언급한 `DESIGN.md`, `기술_블로그_작성_마스터_가이드.md`, `stitch_ai_datastructure_image_style_guide.md`는 현재 접근 가능한 경로에서 찾지 못했습니다.
- 대신 실행 프롬프트에 포함된 디자인 토큰, 문체 기준, 루트 Visual Lab 가이드 문서를 기준으로 반영했습니다.
- `spring-boot-db-access-lab`, `spring-boot-redis-cache-lab`, `spring-boot-realtime-communication-lab`의 `main` 가이드 브랜치에는 시퀀스별 `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`가 직접 존재하지 않아 Visual Lab의 source link는 main에 존재하는 `repo-guide.md`, `sequence-map.md`, `branch-guide.md`로 연결했습니다.
