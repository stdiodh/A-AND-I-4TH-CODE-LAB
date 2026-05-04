# A&I Backend Visual Lab Codex Prompt

## 1. 역할

너는 A&I 4기 Code Lab Central Hub 저장소에서 작업하는 구현 도우미다.

이번 작업은 중앙 레포의 기준 문서를 읽고, 대상 시퀀스 서브모듈 안에 `A&I Backend Visual Lab` 정적 HTML 학습 시각화 페이지를 추가하는 것이다.

중앙 레포는 구현물을 직접 보관하지 않는다.
중앙 레포는 기준 문서, 실행 프로토콜, README 안내, submodule pointer만 관리한다.

## 2. 작업 전 반드시 읽을 문서

작업 전 아래 문서를 읽어라.

```text
README.md
docs/visual-lab-sequence-workflow.md
docs/visual-lab-design-guide.md
docs/visual-lab-content-spec.md
docs/visual-lab-implementation-plan.md
```

DB Access Lab 흐름을 반영할 때는 아래 외부 문서를 참조하라.

```text
https://github.com/stdiodh/spring-boot-db-access-lab/blob/02-answer/docs/theory.md
https://github.com/stdiodh/spring-boot-db-access-lab/blob/02-answer/docs/implementation.md
https://github.com/stdiodh/spring-boot-db-access-lab/tree/02-answer
```

실제 코드 흐름을 확인할 때는 아래 파일을 참조하라.

```text
https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/controller/PostController.kt
https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/service/PostService.kt
https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/domain/PostEntity.kt
https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/repository/PostRepository.kt
https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/dto/PostCreateRequest.kt
https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/dto/PostUpdateRequest.kt
https://raw.githubusercontent.com/stdiodh/spring-boot-db-access-lab/02-answer/src/main/kotlin/com/andi/rest_crud/dto/PostResponse.kt
```

## 3. 모든 시퀀스 브랜치 기준

Visual Lab은 한 시퀀스만 설명하는 페이지가 아니다.
모든 시퀀스는 아래 브랜치 기준으로 확장한다.

```text
NN-implementation
-> 학생 실습용 starter 브랜치
-> TODO와 순서형 힌트를 확인하는 기준
-> Visual Lab에서는 학생이 시작할 흐름 링크로 연결한다.

NN-answer
-> 강사용 비교/정답 브랜치
-> 완성된 코드 흐름을 확인하는 기준
-> Visual Lab에서는 실행 흐름을 시각화할 기준으로 사용한다.
```

`NN`은 중앙 `docs/sequences` 번호와 같아야 한다.

예:

```text
02-implementation
02-answer
```

## 4. 매우 중요한 작업 원칙

- 중앙 레포는 상세 이론 저장소가 아니다.
- Visual Lab 구현 파일은 대상 시퀀스 서브모듈의 `docs/visual-lab` 아래에만 둔다.
- 루트 레포에 `docs/index.html` 또는 `docs/visualizer/*` 구현 파일을 만들지 않는다.
- Visual Lab은 상세 이론을 대체하지 않는다.
- Visual Lab은 시퀀스와 토픽 레포로 이동하기 위한 시각화 진입점이다.
- 기존 커리큘럼 문서와 시퀀스 문서를 임의로 수정하지 않는다.
- 정답 코드를 HTML에 길게 복붙하지 않는다.
- 핵심 흐름과 코드 포인트만 짧게 보여준다.
- 한 시퀀스가 끝날 때마다 서브모듈 commit/push 후 루트 submodule pointer를 commit/push 한다.
- 이전 시퀀스의 루트 pointer 업데이트가 끝나기 전에는 다음 시퀀스를 시작하지 않는다.

## 5. 구현 목표

대상 시퀀스 서브모듈 안에서 아래 파일을 생성 또는 수정한다.

```text
docs/visual-lab/index.html
docs/visual-lab/style.css
docs/visual-lab/components.css
docs/visual-lab/sequences.js
docs/visual-lab/app.js
```

루트 레포에는 `docs/index.html` 또는 `docs/visualizer/*` 구현 파일을 만들지 않는다.

## 6. 디자인 요구사항

반드시 `docs/visual-lab-design-guide.md`를 따른다.

핵심 요약:

- A&I 공식 사이트의 밝고 깔끔한 브랜드 톤을 참고한다.
- 첨부된 자료구조 인포그래픽 스타일 가이드를 따른다.
- 배경은 `#F8F9FB`
- 카드 배경은 `#FFFFFF`
- 메인 제목은 `#0C2691`
- 파란 강조는 `#2955E4`
- 청록 강조는 `#3F8996`
- 카드 테두리는 `#D8DDEB`
- 둥근 카드와 부드러운 그림자를 사용한다.
- 좌상단 사선 패턴 원형 장식을 CSS로 만든다.
- 우하단 연한 민트 원형 장식을 CSS로 만든다.
- 점 패턴 장식을 은은하게 넣는다.
- 제목은 굵고 단정한 한국어 산세리프 고딕체 느낌으로 만든다.
- 실사 이미지, 3D, 다크모드, 네온 효과는 사용하지 않는다.

## 7. 콘텐츠 요구사항

반드시 `docs/visual-lab-content-spec.md`를 따른다.

특히 DB Access Lab 흐름은 아래처럼 시각화한다.

```text
Client
-> POST /posts
-> PostController
-> PostCreateRequest
-> PostService
-> PostEntity
-> PostRepository
-> MySQL
-> PostResponse
-> JSON Response
```

반드시 포함할 대표 주제:

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

전체 시퀀스 확장 시에는 각 주제에 `sourceImplementationBranch`와 `sourceAnswerBranch`를 함께 둔다.

## 8. 구현 요구사항

- HTML/CSS/Vanilla JS만 사용한다.
- 외부 라이브러리를 사용하지 않는다.
- GitHub Pages에서 동작하도록 상대 경로를 사용한다.
- 카드 클릭 시 상세 내용이 변경되어야 한다.
- 첫 번째 카드는 기본 선택 상태여야 한다.
- 선택된 카드는 `aria-pressed="true"`를 가져야 한다.
- DOM 요소가 없어도 에러가 나지 않도록 방어 코드를 작성한다.
- 모바일 반응형을 구현한다.

## 9. sequences.js 데이터 필수 구조

`visualLabTopics` 전역 상수를 사용한다.

```js
const visualLabTopics = [
  {
    id: "db-access-flow",
    sequence: "02",
    title: "DB 접근 흐름",
    englishTitle: "DB Access Flow",
    category: "Persistence",
    shortDescription: "메모리 저장 대신 MySQL에 데이터를 저장하는 계층 흐름입니다.",
    whyItMatters: "백엔드에서는 요청 데이터가 단순히 메모리에 머무르지 않고 DB에 영속적으로 저장되어야 합니다.",
    sourceRepo: "spring-boot-db-access-lab",
    sourceImplementationBranch: "02-implementation",
    sourceAnswerBranch: "02-answer",
    sourceDocs: [],
    sourceCode: [],
    flow: [],
    transform: [],
    points: [],
    exampleRequest: {},
    exampleResponse: {}
  }
];
```

## 10. app.js 필수 함수

아래 함수를 구현한다.

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

## 11. README 추가 내용

루트 README.md에 아래 내용을 추가한다.

````md
## A&I Backend Visual Lab

각 시퀀스 서브모듈의 `docs/visual-lab/index.html`에서 확인할 수 있는 정적 학습 시각화 페이지입니다.

이 페이지는 A&I 백엔드 커리큘럼의 상세 이론을 대체하지 않고,
각 시퀀스와 토픽 레포로 이동하기 위한 시각화 진입점입니다.

로컬 실행:

```bash
python3 -m http.server 8080 -d docs/visual-lab
```

접속:

```text
http://localhost:8080
```
````

## 12. 완료 후 검수

완료 후 아래를 확인한다.

- `python3 -m http.server 8080 -d docs/visual-lab`로 실행되는가
- `http://localhost:8080`에서 페이지가 열리는가
- 카드 클릭이 동작하는가
- DB Access Lab 흐름이 정확한가
- 각 시퀀스 확장 기준에 `NN-implementation` / `NN-answer`가 정의되어 있는가
- 디자인 가이드 색상을 따르는가
- 외부 라이브러리를 쓰지 않았는가
- 기존 커리큘럼 문서를 임의로 수정하지 않았는가
