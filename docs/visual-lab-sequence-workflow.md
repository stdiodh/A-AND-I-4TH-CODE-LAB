# A&I Backend Visual Lab Sequence Workflow

## 1. 문서 목적

이 문서는 A&I Backend Visual Lab 작업이 루트 레포가 아니라 각 시퀀스 서브모듈 안에서 진행되도록 고정하는 실행 프로토콜이다.

루트 레포는 Visual Lab의 기준 문서, 작업 순서, 검수 기준, submodule pointer를 관리한다.
실제 HTML, CSS, JavaScript 구현물은 각 시퀀스 서브모듈의 `docs/visual-lab` 아래에 둔다.

## 2. 반드시 지킬 원칙

- 루트 레포에 `docs/index.html`을 만들지 않는다.
- 루트 레포에 `docs/visualizer/*` 구현 파일을 만들지 않는다.
- 루트 레포의 `docs/visual-lab-*.md` 기준 문서는 삭제하지 않는다.
- 한 번에 하나의 시퀀스만 작업한다.
- 한 시퀀스 작업이 끝나면 반드시 해당 서브모듈을 commit/push 한다.
- 서브모듈 push 후 루트 레포에서 submodule pointer를 commit/push 한다.
- 다음 시퀀스는 사용자 승인 전 시작하지 않는다.

## 3. 표준 작업 흐름

각 시퀀스 Visual Lab은 아래 순서로 진행한다.

```text
1. 루트 레포 기준 문서를 읽는다.
2. 대상 시퀀스 서브모듈을 확인한다.
3. 대상 서브모듈의 현재 브랜치와 작업 상태를 확인한다.
4. 대상 서브모듈 안의 docs/visual-lab에서 HTML/CSS/JS를 구현한다.
5. 대상 서브모듈에서 로컬 검수를 수행한다.
6. 대상 서브모듈에서 commit/push 한다.
7. 루트 레포로 돌아와 submodule pointer 변경을 확인한다.
8. 필요하면 루트 README에 해당 Visual Lab 위치를 추가한다.
9. 루트 레포에서 submodule pointer와 문서 변경을 commit/push 한다.
```

## 4. 작업 전 읽을 루트 문서

Visual Lab 작업 전 반드시 아래 문서를 읽는다.

```text
README.md
AGENTS.md
docs/visual-lab-sequence-workflow.md
docs/visual-lab-design-guide.md
docs/visual-lab-content-spec.md
docs/visual-lab-implementation-plan.md
docs/visual-lab-codex-prompt.md
```

## 5. 시퀀스별 구현 위치

각 시퀀스 구현 위치는 아래 형식을 따른다.

```text
<sequence-submodule>/docs/visual-lab/index.html
<sequence-submodule>/docs/visual-lab/style.css
<sequence-submodule>/docs/visual-lab/components.css
<sequence-submodule>/docs/visual-lab/sequences.js
<sequence-submodule>/docs/visual-lab/app.js
```

예시:

```text
aandi-prerequisite-bootcamp/docs/visual-lab/index.html
spring-boot-rest-crud-lab/docs/visual-lab/index.html
spring-boot-db-access-lab/docs/visual-lab/index.html
```

## 6. 시퀀스별 브랜치 기준

모든 시퀀스는 아래 브랜치 기준을 따른다.

```text
NN-implementation
-> 학생 실습용 starter 브랜치
-> Visual Lab에서는 학생이 실습을 시작할 기준 링크로 연결한다.

NN-answer
-> 강사용 비교/정답 브랜치
-> Visual Lab에서는 완성된 실행 흐름을 시각화할 기준으로 사용한다.
```

`NN`은 중앙 `docs/sequences` 문서 번호와 같아야 한다.

예:

```text
02-implementation
02-answer
```

## 7. 시퀀스 00 기준

시퀀스 00은 선수지식 부트캠프다.

대상 서브모듈:

```text
aandi-prerequisite-bootcamp
```

Visual Lab 위치:

```text
aandi-prerequisite-bootcamp/docs/visual-lab/index.html
```

로컬 실행:

```bash
cd aandi-prerequisite-bootcamp
python3 -m http.server 8080 -d docs/visual-lab
```

접속:

```text
http://localhost:8080
```

시퀀스 00은 Spring Boot 심화 구현이 아니라 HTTP, API, 서버와 클라이언트, JSON, 요청/응답 같은 선수지식을 다룬다.
DB Access Lab의 `PostController -> PostService -> Repository -> MySQL` 흐름은 시퀀스 02에서 대표 사례로 다룬다.

## 8. 시퀀스 완료 기준

한 시퀀스는 아래 조건을 모두 만족해야 완료로 본다.

- 대상 서브모듈의 `docs/visual-lab/index.html`이 로컬 서버에서 열린다.
- 카드 렌더링과 상세 영역 업데이트가 동작한다.
- 디자인 가이드의 색상, 카드, 배경 장식, 타이포그래피 규칙을 따른다.
- 외부 JS 라이브러리와 빌드 도구를 사용하지 않는다.
- 중앙 루트에 구현 HTML/CSS/JS 파일을 만들지 않았다.
- 서브모듈 변경사항이 commit/push 되었다.
- 루트 레포의 submodule pointer가 commit/push 되었다.

## 9. 다음 시퀀스 시작 조건

다음 시퀀스는 이전 시퀀스의 서브모듈 commit/push와 루트 submodule pointer commit/push가 끝난 뒤에만 시작한다.

루트 push가 인증 문제로 실패하면, 다음 시퀀스 시작 전에 사용자에게 루트 push 미완료 상태를 보고하고 해결을 기다린다.
