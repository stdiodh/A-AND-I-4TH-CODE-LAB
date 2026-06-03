# Visual Lab Rules For Agents

Visual Lab은 중앙 레포가 아니라 각 토픽 레포 안에 구현합니다.

## 위치 규칙

허용:

```text
<topic-repo>/docs/visual-lab/index.html
<topic-repo>/docs/visual-lab/styles.css
<topic-repo>/docs/visual-lab/visual-lab.js
<topic-repo>/docs/visual-lab/visual-lab-data.js
```

금지:

```text
docs/index.html
docs/visualizer/*
```

## 기술 규칙

- HTML, CSS, Vanilla JavaScript만 사용합니다.
- 외부 JS 라이브러리나 CDN을 추가하지 않습니다.
- React, Vue, Next.js, Bootstrap, Tailwind CDN을 사용하지 않습니다.
- 상대 경로를 사용해 GitHub Pages에서도 열리게 합니다.

## 내용 규칙

- Visual Lab은 이론 문서 대체물이 아닙니다.
- 긴 이론과 정답 코드 전체를 넣지 않습니다.
- `answerBranch`, `sourceAnswerBranch`, `NN-answer` 문자열을 노출하지 않습니다.
- 학생이 흐름을 이해하는 진입점으로 두고, 정답 비교 안내는 README, checklist의 멘토용 접힘 영역 또는 answer 브랜치 문서에서 처리합니다.

## 확인 명령

중앙 레포에서 Visual Lab 규칙을 자동으로 확인합니다.

```bash
python3 scripts/validate-visual-labs.py
```

이 검증은 아래 항목을 확인합니다.

- 각 서브레포에 `docs/visual-lab/index.html`, `styles.css`, `visual-lab.js`, `visual-lab-data.js`가 있는지 확인합니다.
- 루트 `docs/index.html`이 생성되어 있으면 실패 처리합니다.
- 외부 CDN, 절대 URL asset, 정답 브랜치 노출 문자열을 최소 기준으로 탐지합니다.
- `visual-lab-data.js`에 `window.visualLabData`, `sequence`, `title`, `goal`, `flow`가 있는지 확인합니다.

개별 Visual Lab을 브라우저에서 확인할 때는 대상 서브레포 안에서 정적 서버를 띄웁니다.

```bash
python3 -m http.server 8080 -d docs/visual-lab
```

브라우저에서 확인합니다.

```text
http://localhost:8080
```

자세한 기존 기준은 [Visual Lab workflow](../visual-lab-sequence-workflow.md)를 참고합니다.
