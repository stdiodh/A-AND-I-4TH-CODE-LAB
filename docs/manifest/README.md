# Curriculum Manifest

`docs/manifest/sequences.yml`은 A&I 4기 백엔드 코드랩의 시퀀스 구조를 한눈에 관리하는 manifest입니다.
코스 구조의 단일 관리 기준은 `docs/manifest/sequences.yml`입니다.

## 필드 의미

- `id`: 시퀀스 번호입니다. 반드시 두 자리 문자열을 사용합니다.
- `title`: 짧은 표시 이름입니다.
- `topic`: 수업 주제 또는 기술 영역입니다.
- `repoName`: 연결된 토픽 레포 이름입니다.
- `repoPath`: 중앙 레포 안의 서브모듈 경로입니다.
- `repoUrl`: 원격 레포 URL입니다.
- `guideBranch`: 가이드 브랜치입니다. 모든 토픽 레포는 `main`을 사용합니다.
- `implementationBranch`: 학생 시작 브랜치입니다. `NN-implementation` 형식을 사용합니다.
- `answerBranch`: 참고 정답 브랜치입니다. `NN-answer` 형식을 사용합니다.
- `sequenceDoc`: 중앙 시퀀스 문서 경로입니다.
- `visualLabPath`: 해당 토픽 레포 안의 기존 Visual Lab 진입점입니다. 호환성을 위해 유지합니다.
- `visualLabHubPath`: 해당 토픽 레포 안의 Visual Lab 허브 경로입니다.
- `visualLabSequencePath`: 해당 시퀀스 전용 Visual Lab 상세 경로입니다.
- `runCommand`: 로컬 실행 명령입니다. 서버 실행이 없는 시퀀스는 `null`을 사용합니다.
- `testCommand`: 테스트 명령입니다. 자동 테스트가 없는 시퀀스는 `null`을 사용합니다.
- `swaggerPath`: Swagger 또는 API 확인 경로입니다. 없거나 확인이 불확실하면 `null`을 사용합니다.
- `prerequisites`: 먼저 완료해야 하는 시퀀스 id 목록입니다.
- `learningGoals`: 학생이 가져가야 할 핵심 목표입니다.
- `status`: 현재 관리 상태입니다.
- `notes`: 불확실한 값, 수동 조치, 운영 주의사항입니다.

## Status 값

- `ready`: 문서, 브랜치, 기본 안내가 현재 정책과 맞습니다.
- `needs-review`: 내용 검토가 필요합니다.
- `needs-branch-cleanup`: default branch 또는 legacy branch 정리가 필요합니다.
- `needs-visual-lab`: Visual Lab 진입점이 없거나 구현 확인이 필요합니다.
- `planned`: 아직 계획 단계입니다.

## 수정 규칙

1. 브랜치 규칙은 `main`, `NN-implementation`, `NN-answer`로 유지합니다.
2. repoName, branchName, command를 추측으로 확정하지 않습니다.
3. 확실하지 않은 값은 `null`로 두고 `notes`에 이유를 적습니다.
4. 중앙 `docs/sequences/*`는 상세 이론 저장소가 아니므로 manifest 수정 때문에 대규모로 갈아엎지 않습니다.
5. Visual Lab 구현 파일은 중앙 레포가 아니라 각 토픽 레포의 `docs/visual-lab` 아래에 둡니다.
6. GitHub default branch 변경과 remote branch 삭제는 manifest에 기록만 하고 수동 조치로 처리합니다.
