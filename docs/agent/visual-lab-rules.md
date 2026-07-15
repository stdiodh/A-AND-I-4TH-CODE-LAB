# Visual Lab Rules For Agents

Visual Lab은 중앙 레포가 아니라 각 토픽 레포 안에 구현합니다.

## 위치 규칙

허용:

```text
<topic-repo>/docs/visual-lab/index.html
<topic-repo>/docs/visual-lab/styles.css
<topic-repo>/docs/visual-lab/visual-lab.js
<topic-repo>/docs/visual-lab/visual-lab-data.js
<topic-repo>/docs/visual-lab/sequences/NN/index.html
<topic-repo>/docs/visual-lab/sequences/NN/visual-lab-data.js
```

`docs/visual-lab/index.html`은 토픽 레포 단위 허브입니다.
시퀀스 상세 Visual Lab은 `docs/visual-lab/sequences/NN/index.html`에 둡니다.

금지:

```text
docs/index.html
docs/visualizer/*
```

## 기술 규칙

- `docs/visual-lab` 구현 또는 중앙 Visual Lab 디자인 문서를 수정할 때는 먼저 `$aandi-visual-lab-design`을 사용합니다.
- 구현 전에 대상 시퀀스의 실제 질문과 흐름을 기준으로 디자인 계획과 genericity critique를 작성합니다.
- HTML, CSS, Vanilla JavaScript만 사용합니다.
- 외부 JS 라이브러리나 CDN을 추가하지 않습니다.
- React, Vue, Next.js, Bootstrap, Tailwind CDN을 사용하지 않습니다.
- 상대 경로를 사용해 GitHub Pages에서도 열리게 합니다.
- 새 UI 상태는 공통 semantic token과 component rule을 먼저 확장하며, 한 컴포넌트만 별도로 꾸미지 않습니다.
- 학생이 결과를 예측하기 전에 scenario label이나 초기 snapshot으로 답을 공개하지 않습니다.
- actor 카드와 transition 카드 grid를 따로 만들지 않습니다. participant header와 수직 lifeline 위에 message를 위에서 아래로 놓고 현재 단계의 before/after와 evidence를 control 가까이에 둡니다.
- node icon은 `assets/icons/{icon}.svg`, 주제 설명은 `workbench.visual`의 로컬 SVG를 직접 렌더링하며 sprite fragment를 primary runtime 경로로 사용하지 않습니다.
- `assets/SOURCE.md`와 `assets/LICENSES.md`를 유지하고 broken image, 0px asset과 offscreen asset을 완료로 처리하지 않습니다.
- 자동 재생과 속도 control을 추가하지 않습니다. 학생이 이전/다음으로 관찰 속도를 결정하게 합니다.

## 내용 규칙

- Visual Lab은 이론 문서 대체물이 아닙니다.
- 긴 이론과 정답 코드 전체를 넣지 않습니다.
- 파일 경로 tag를 코드 근거의 제목처럼 노출하지 않습니다. 짧은 학생용 설명 또는 올바른 코드 주석, 실제 핵심 코드 3~12줄, 바뀌는 상태 한 문장 순서로 설명합니다.
- `호출 전/후 책임`, `반환 대기/보유`, `판정 입력/결과` 같은 자동 생성형 문장을 상태 변화로 쓰지 않습니다. 해당 주차의 실제 코드와 실행 범위를 대조해 값, 저장 상태, 인증 주체, 연결 대상, 실패 gate 또는 assertion 결과를 구체적으로 적습니다.
- 각 scenario는 관련 `theory.md`의 명시적 sequence anchor를 가리키고, 관찰 뒤 인과 규칙을 다시 쓰는 reflection을 제공합니다.
- `answerBranch`, `sourceAnswerBranch`, `NN-answer` 문자열을 노출하지 않습니다.
- 학생이 흐름을 이해하는 진입점으로 두고, 정답 비교 안내는 README, checklist의 멘토용 접힘 영역 또는 answer 브랜치 문서에서 처리합니다.

## 확인 명령

중앙 레포에서 Visual Lab 규칙을 자동으로 확인합니다.

```bash
python3 scripts/validate-visual-labs.py
```

이 검증은 아래 항목을 확인합니다.

- 각 서브레포에 `docs/visual-lab/index.html`, `styles.css`, `visual-lab.js`, `visual-lab-data.js`가 있는지 확인합니다.
- manifest의 각 시퀀스에 대해 `docs/visual-lab/sequences/NN/index.html`과 `visual-lab-data.js`가 있는지 확인합니다.
- 루트 `docs/index.html`이 생성되어 있으면 실패 처리합니다.
- 외부 CDN, 절대 URL asset, 정답 브랜치 노출 문자열을 최소 기준으로 탐지합니다.
- 시퀀스 상세 데이터에 `window.visualLabData`, `kind`, `sequence`, `title`, `goal`, `problem`, `actors`, `flows`, `codePoints`가 있는지 확인합니다.
- 시퀀스 상세 데이터의 `workbench`와 3~4개 실제 scenario, 모든 step의 effect와 evidence scope가 공통 계약을 만족하는지 확인합니다.

개별 Visual Lab을 브라우저에서 확인할 때는 대상 서브레포 안에서 정적 서버를 띄웁니다.

```bash
python3 -m http.server 8080 -d docs/visual-lab
```

브라우저에서 확인합니다.

```text
http://localhost:8080
```

완료 전에는 전체 화면을 직접 확인하고 1440px, 1024px, 768px, 390px 레이아웃, keyboard focus와 activation, console error, `prefers-reduced-motion` 대체 상태를 검수합니다.

자세한 기존 기준은 [Visual Lab workflow](../visual-lab-sequence-workflow.md)를 참고합니다.
