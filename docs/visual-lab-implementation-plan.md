# A&I Backend Visual Lab Implementation Plan

## 1. 구현 목적

A&I Backend Visual Lab은 각 시퀀스 서브모듈 안에서 정적 HTML, CSS, Vanilla JavaScript만으로 구현한다.

목표는 A&I 백엔드 커리큘럼과 토픽 레포의 이론/코드 흐름을 시각적으로 탐색하는 페이지를 만드는 것이다.

이 페이지는 실제 Spring Boot 서버를 실행하지 않는다.
대신 문서와 코드에서 정의된 흐름을 시각화한다.

## 2. 구현 범위

각 시퀀스 서브모듈 안에서 생성할 파일:

```text
<sequence-submodule>/docs/visual-lab/index.html
<sequence-submodule>/docs/visual-lab/style.css
<sequence-submodule>/docs/visual-lab/components.css
<sequence-submodule>/docs/visual-lab/sequences.js
<sequence-submodule>/docs/visual-lab/app.js
```

루트 레포에는 위 구현 파일을 만들지 않는다.
루트 레포는 기준 문서와 submodule pointer만 관리한다.

이미 존재하거나 먼저 생성되어야 하는 기준 문서:

```text
docs/visual-lab-design-guide.md
docs/visual-lab-content-spec.md
docs/visual-lab-implementation-plan.md
docs/visual-lab-codex-prompt.md
```

## 3. 구현 전 반드시 읽을 문서

Codex는 작업 전 아래 문서를 읽어야 한다.

```text
README.md
docs/visual-lab-sequence-workflow.md
docs/visual-lab-design-guide.md
docs/visual-lab-content-spec.md
docs/visual-lab-implementation-plan.md
docs/visual-lab-codex-prompt.md
```

또한 DB Access Lab 콘텐츠를 만들 때 아래 외부 문서를 참조해야 한다.

```text
https://github.com/stdiodh/spring-boot-db-access-lab/blob/02-answer/docs/theory.md
https://github.com/stdiodh/spring-boot-db-access-lab/blob/02-answer/docs/implementation.md
https://github.com/stdiodh/spring-boot-db-access-lab/tree/02-answer
```

## 4. 모든 시퀀스 확장 원칙

Visual Lab은 `02-answer`만을 위한 페이지가 아니다.
`02-answer`는 DB Access 흐름을 보여주는 첫 대표 사례다.

향후 모든 시퀀스는 아래 규칙으로 추가한다.

```text
NN-implementation
-> 학생이 실습을 시작하는 브랜치
-> TODO와 구현 순서를 보여주는 링크로 연결

NN-answer
-> 완성된 흐름을 시각화할 기준 브랜치
-> 코드 실행 흐름과 문서 링크의 기준으로 사용
```

시퀀스별 콘텐츠 확장 순서:

1. `docs/sequences/NN-...md`를 읽고 주제 범위를 확정한다.
2. 해당 토픽 레포의 `NN-answer` 브랜치에서 완성 흐름을 확인한다.
3. 해당 토픽 레포의 `NN-implementation` 브랜치에서 학생 실습 흐름을 확인한다.
4. 해당 서브모듈의 `docs/visual-lab/sequences.js`에 한 개 이상의 topic 객체를 추가한다.
5. `sourceImplementationBranch`, `sourceAnswerBranch`, `sourceDocs`, `sourceCode`를 반드시 넣는다.
6. HTML에는 핵심 흐름만 표시하고 상세 이론은 링크로 연결한다.

## 5. 서브모듈 작업 완료 흐름

각 시퀀스 구현은 아래 단위를 모두 끝내야 완료된다.

```text
1. 대상 서브모듈에서 docs/visual-lab 구현
2. 대상 서브모듈에서 로컬 검수
3. 대상 서브모듈 commit/push
4. 루트 레포에서 submodule pointer 변경 확인
5. 루트 README 링크가 필요하면 보강
6. 루트 레포 commit/push
```

루트 push가 인증 문제로 실패하면 다음 시퀀스를 시작하지 않고 사용자에게 미완료 상태를 보고한다.

## 6. 구현 원칙

- 외부 라이브러리를 사용하지 않는다.
- React, Vue, Next.js를 사용하지 않는다.
- Bootstrap, Tailwind CDN을 사용하지 않는다.
- HTML/CSS/Vanilla JS만 사용한다.
- GitHub Pages에서 열 수 있도록 상대 경로를 사용한다.
- 기존 커리큘럼 문서를 임의로 변경하지 않는다.
- 상세 이론을 중앙 HTML에 과도하게 복붙하지 않는다.
- Visual Lab은 학습 지도이자 시각화 진입점이다.

## 7. 파일별 구현 계획

### 7.1 docs/visual-lab/index.html

역할:

- Visual Lab의 메인 진입점
- Hero 영역
- Topic Cards 영역
- Detail 영역
- Flow Timeline 영역
- Related Docs 영역
- Footer 영역

필수 연결:

```html
<link rel="stylesheet" href="./style.css" />
<link rel="stylesheet" href="./components.css" />

<script src="./sequences.js"></script>
<script src="./app.js"></script>
```

HTML 구조 예시:

```html
<body>
  <div class="page-shell">
    <header class="hero-section">
      ...
    </header>

    <main>
      <section class="topic-section">
        <div id="topicGrid"></div>
      </section>

      <section class="detail-section">
        <div id="topicDetail"></div>
      </section>
    </main>

    <footer class="site-footer">
      ...
    </footer>
  </div>
</body>
```

필수 id:

```text
topicGrid
detailTitle
detailEnglishTitle
detailCategory
detailDescription
detailWhy
flowTimeline
transformList
pointList
exampleRequest
exampleResponse
relatedDocs
relatedCode
```

### 7.2 docs/visual-lab/style.css

역할:

- CSS 변수 정의
- 기본 reset
- 전체 배경
- 타이포그래피
- Hero 레이아웃
- 전체 grid
- 반응형 처리
- 배경 장식

반드시 구현할 것:

- `:root` 색상 변수
- `.page-shell`
- `.page-shell::before`
- `.page-shell::after`
- `.hero-section`
- `.hero-title`
- `.hero-subtitle`
- `.section-heading`
- 반응형 media query

### 7.3 docs/visual-lab/components.css

역할:

- 카드
- 버튼
- 배지
- 타임라인
- 도식
- 코드 박스
- 관련 링크 카드

반드시 구현할 class:

```text
visual-card
topic-card
topic-card.is-selected
topic-badge
sequence-badge
flow-timeline
flow-step
flow-arrow
transform-card
point-list
code-box
related-link-card
summary-box
```

선택 상태 규칙:

```text
카드 전체를 진한 색으로 뒤집지 않는다.
테두리와 배지 색상만 강조한다.
```

### 7.4 docs/visual-lab/sequences.js

역할:

- Visual Lab 학습 주제 데이터 정의

전역 변수:

```js
const visualLabTopics = [];
```

최소 포함 주제:

```text
HTTP 요청/응답
Controller
DTO
Service
Entity
Repository
Database
CRUD
영속성 저장
계층 분리
수정 흐름
삭제 흐름
JPA 기본 CRUD
N+1 문제 입문
```

DB Access Lab 주제는 반드시 아래 실제 흐름을 포함한다.

```text
POST /posts
-> PostController
-> PostCreateRequest
-> PostService
-> PostEntity
-> PostRepository
-> MySQL
-> PostResponse
-> JSON Response
```

모든 topic은 가능하면 아래 브랜치 필드를 포함한다.

```js
sourceImplementationBranch: "NN-implementation",
sourceAnswerBranch: "NN-answer"
```

### 7.5 docs/visual-lab/app.js

역할:

- `visualLabTopics` 데이터를 렌더링한다.
- 카드 클릭 이벤트를 처리한다.
- 선택된 주제 상세를 표시한다.
- flow를 타임라인으로 표시한다.
- transform을 데이터 변환 카드로 표시한다.
- points를 리스트로 표시한다.
- 관련 문서와 코드 링크를 표시한다.

필수 함수:

```js
renderTopicCards()
renderTopicDetail(topic)
renderFlow(flow)
renderTransforms(transforms)
renderPoints(points)
renderExamples(topic)
renderRelatedLinks(topic)
selectTopic(topicId)
```

방어 코드:

- DOM 요소가 없으면 에러 없이 종료한다.
- 데이터 배열이 비어 있으면 빈 상태 메시지를 보여준다.
- optional field가 없어도 렌더링이 깨지지 않게 한다.

접근성:

- topic card는 button 사용
- 선택된 카드에는 `aria-pressed="true"` 사용
- 키보드 포커스 스타일 유지

## 8. 구현 단계

### Step 1. 기준 문서 확인

- design guide 확인
- content spec 확인
- DB Access Lab theory.md 확인
- DB Access Lab implementation.md 확인
- 실제 코드 파일 URL 확인

### Step 2. HTML 생성

- Hero Section 생성
- Topic Grid 컨테이너 생성
- Detail Section 생성
- Footer 생성

### Step 3. CSS 토큰과 레이아웃 생성

- 색상 변수 생성
- 타이포그래피 생성
- 배경 장식 생성
- 반응형 grid 생성

### Step 4. 컴포넌트 CSS 생성

- 카드
- 배지
- 타임라인
- 도식 노드
- 코드 박스
- 관련 링크

### Step 5. 콘텐츠 데이터 생성

- `visualLabTopics` 작성
- DB Access Lab 기준 주제 우선 작성
- 나머지 주제는 짧은 개념 수준으로 작성
- 전체 시퀀스 확장 시 `NN-implementation` / `NN-answer` 링크를 함께 작성

### Step 6. JS 렌더링 구현

- 카드 목록 렌더링
- 첫 번째 카드 기본 선택
- 클릭 시 상세 업데이트
- 관련 문서/코드 링크 렌더링

### Step 7. 로컬 확인

명령어:

```bash
python3 -m http.server 8080 -d docs/visual-lab
```

접속:

```text
http://localhost:8080
```

### Step 8. README 연결

서브모듈 README 또는 루트 README에 Visual Lab 안내를 추가한다.

내용:

```text
A&I Backend Visual Lab은 각 시퀀스 서브모듈의 docs/visual-lab/index.html에서 확인할 수 있는 정적 학습 시각화 페이지입니다.
이 페이지는 상세 이론을 대체하지 않고, 각 시퀀스와 토픽 레포로 이동하기 위한 시각화 진입점입니다.
```

## 9. 검수 기준

### 9.1 기능 검수

- 페이지가 로컬 서버에서 열린다.
- 카드 목록이 렌더링된다.
- 첫 번째 카드가 기본 선택된다.
- 카드 클릭 시 상세 내용이 바뀐다.
- flow timeline이 표시된다.
- transform card가 표시된다.
- 관련 문서와 코드 링크가 표시된다.

### 9.2 디자인 검수

- 첨부 이미지 스타일과 유사하다.
- 흰색/회백색 배경이다.
- 네이비 제목을 사용한다.
- 블루/청록 강조를 사용한다.
- 카드가 둥글고 부드럽다.
- 좌상단/우하단 장식이 있다.
- 다크모드나 네온 느낌이 없다.

### 9.3 콘텐츠 검수

- DB Access Lab의 실제 흐름이 반영되어 있다.
- `PostController`, `PostService`, `PostEntity`, `PostRepository`, DTO 흐름이 빠지지 않았다.
- 각 시퀀스 확장 시 `NN-implementation` / `NN-answer` 기준이 함께 표시된다.
- 상세 이론을 과도하게 복붙하지 않았다.
- 중앙 레포의 역할을 벗어나지 않는다.

### 9.4 코드 검수

- 외부 라이브러리를 사용하지 않는다.
- 상대 경로를 사용한다.
- DOM 방어 코드가 있다.
- 모바일 반응형이 있다.
- CSS 변수 기반으로 색상을 관리한다.
