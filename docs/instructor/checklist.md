# Instructor Checklist

## 수업 전

- [ ] 오늘 시퀀스 번호를 확인했습니다.
- [ ] [manifest](../manifest/sequences.yml)의 repo, branch, run/test command를 확인했습니다.
- [ ] 중앙 레포에서 `python3 scripts/verify-sequences.py`를 실행했습니다.
- [ ] 테스트까지 확인해야 하는 날에는 `python3 scripts/verify-sequences.py --run-tests`를 실행했습니다.
- [ ] 학생 시작 브랜치가 `NN-implementation`인지 확인했습니다.
- [ ] default branch가 `main`인지 확인했습니다.
- [ ] 01 REST CRUD 원격 default branch가 `main`인지 GitHub UI에서 확인했습니다.
- [ ] 12 Event Driven 원격 default branch가 `main`인지 GitHub UI에서 확인했습니다.
- [ ] Codex는 GitHub 원격 default branch를 직접 바꾸지 못합니다.
- [ ] 토픽 레포 `docs/visual-lab/index.html` 허브와 `docs/visual-lab/sequences/NN/index.html` 상세 페이지가 열리는지 확인했습니다.
- [ ] 필요한 Docker 서비스가 무엇인지 확인했습니다.

## 수업 중

- [ ] 학생이 중앙 레포가 아니라 토픽 레포에서 명령을 실행하는지 확인합니다.
- [ ] TODO가 오늘 목표와 직접 연결되는지 확인합니다.
- [ ] 실행 명령과 테스트 명령을 수업 중 한 번 이상 직접 확인합니다.
- [ ] 학생이 answer 브랜치를 먼저 열지 않도록 안내합니다.

## 수업 후

- [ ] 학생이 자신의 구현을 `NN-answer`와 비교할 수 있게 안내합니다.
- [ ] 과도하게 어려운 TODO나 누락된 힌트를 기록합니다.
- [ ] 다음 수업 전에 README와 checklist 보완이 필요한지 확인합니다.
