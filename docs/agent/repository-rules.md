# Repository Rules For Agents

자동화 작업자는 중앙 레포와 토픽 레포의 역할을 구분해야 합니다.

## 수정 가능한 것

- 중앙 운영 문서
- manifest
- 시퀀스 범위 문서
- 서브모듈 포인터
- 사용자가 요청한 토픽 레포 파일

## 수정하면 안 되는 것

- 사용자 요청 없는 다음 시퀀스
- 중앙 `docs` 안의 상세 이론 복붙
- 학생용 문서에 정답 코드 전체 노출
- 원격 default branch 직접 변경
- remote branch 직접 삭제

## 브랜치 규칙

- 가이드 브랜치: `main`
- 학생 시작 브랜치: `NN-implementation`
- 참고 정답 브랜치: `NN-answer`
- legacy `implementation` / `answer`는 새 안내에 사용하지 않습니다.

## 문서 분리

- 학생용: 시작, 실행, 테스트, 문제 해결
- 강사용: answer 브랜치, 리뷰, 운영 기준
- 에이전트용: 작업 규칙, 금지 범위, 검증 절차

## 검증

문서 변경 후에는 최소한 아래를 실행합니다.

```bash
git diff --check
git status --short
```

코드 변경이 있으면 해당 토픽 레포에서 관련 테스트를 실행합니다.

## Repository Integrity CI

중앙 레포는 GitHub Actions에서 문서와 구조 무결성을 확인합니다.

Workflow:

```text
.github/workflows/repository-integrity.yml
```

실행 시점:

- `pull_request`
- `main` 브랜치 push

CI에서 실행하는 로컬 검증 명령:

```bash
python3 scripts/validate-manifest.py
python3 scripts/validate-visual-labs.py
```

검증 범위:

- `docs/manifest/sequences.yml` 존재 여부와 시퀀스 `00`~`12` 등록 여부
- `sequenceDoc` 파일 존재 여부
- `guideBranch: main`, `NN-implementation`, `NN-answer` 브랜치명 규칙
- `docs/sequences` 문서 번호 누락 여부
- 중앙 README의 로컬 파일 링크 깨짐 여부
- 루트 `docs/index.html` 생성 금지
- 각 서브레포 `docs/visual-lab`의 필수 파일과 외부 CDN 사용 여부

CI가 실패하면 GitHub Actions의 실패 step 로그에서 `FAIL:` 항목을 확인합니다.
로그에는 실패한 파일, 이유, 수정 힌트가 함께 출력됩니다.
