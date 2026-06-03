# A&I 4기 Code Lab Repository Quality Sweep

## 1. 작업 시작 상태

- 기준 루트: `AandI_4rdPeriod_code_lab`
- 기준 문서: `docs/manifest/sequences.yml`, `docs/sequences/*`
- 사전 감사 문서: `docs/audit/prework-repository-inventory.md`
- 이번 작업 원칙: 커리큘럼 순서 유지, 문서 수 증가 금지, Visual Lab 4파일 스펙 유지, implementation 브랜치 정답 노출 금지

초기 검증과 동기화에서 확인한 내용:

- `git submodule update --init --recursive` 실행
- `git submodule foreach 'git fetch --all --prune'` 실행
- `python3 scripts/validate-manifest.py` 통과
- `python3 scripts/validate-visual-labs.py` 통과
- SEQ 01 `spring-boot-rest-crud-lab` main Visual Lab/legacy 문서 정리 후 `./gradlew test` 통과
- SEQ 01 `01-implementation` 문서 정답 노출 제거 후 `./gradlew test` 통과

현재까지 생성하고 원격에 반영한 커밋:

| 위치 | 브랜치 | 커밋 | 내용 |
|---|---|---|---|
| `spring-boot-rest-crud-lab` | `main` | `405e1d1` | SEQ 01 legacy 문서 축소와 Visual Lab 4파일 스펙 정리 |
| `spring-boot-rest-crud-lab-01-implementation-worktree` | `01-implementation` | `f7edadc` | starter 문서의 answer 브랜치명/정답 안내 노출 제거 |
| `spring-boot-rest-crud-lab-01-answer-worktree` | `01-answer` | `df86d7d` | answer 문서 구조 정리와 멘토 비교 포인트 보강 |
| `spring-boot-event-driven-lab` | `main` | `809df6a` | SEQ 12 Visual Lab 스펙 정리와 main legacy 정답 가이드 축소 |
| `spring-boot-event-driven-lab-12-implementation-worktree` | `12-implementation` | `6b2c924` | starter 문서의 answer 브랜치명/구현 코드 노출 제거 |
| `spring-boot-event-driven-lab-12-answer-worktree` | `12-answer` | `02a94a3` | answer 문서 구조 정리와 멘토 비교 포인트 보강 |
| `spring-boot-refactoring-foundation-lab` | `main` | `4cc498d` | SEQ 11 main 문서 범위 복구와 Visual Lab 스펙 정리 |
| `spring-boot-refactoring-foundation-lab-11-implementation-worktree` | `11-implementation` | `c60e825` | starter 문서의 answer 브랜치명/구현 코드 노출 제거 |
| `spring-boot-refactoring-foundation-lab-11-answer-worktree` | `11-answer` | `f676753` | answer 문서 구조 정리와 멘토 비교 포인트 보강 |
| `spring-boot-redis-cache-lab` | `main` | `6d306f0` | SEQ 07 main Visual Lab 스펙 정리와 guide 문서 보정 |
| `spring-boot-redis-cache-lab-07-implementation-worktree` | `07-implementation` | `a51497a` | starter 문서의 answer 브랜치명/구현 코드 노출 제거 |
| `spring-boot-redis-cache-lab-07-answer-worktree` | `07-answer` | `e5bb3d5` | answer 문서 구조 정리와 멘토 비교 포인트 보강 |
| `spring-boot-realtime-communication-lab` | `main` | `c71e913` | SEQ 08 main Visual Lab 스펙 정리와 guide 문서 보정 |
| `spring-boot-realtime-communication-lab-08-implementation-worktree` | `08-implementation` | `4678fff` | starter 문서의 answer 브랜치명/구현 코드 노출 제거 |
| `spring-boot-realtime-communication-lab-08-answer-worktree` | `08-answer` | `c812125` | answer 문서 구조 정리와 멘토 비교 포인트 보강 |
| `spring-boot-deployment-runtime-lab` | `main` | `bece7e4` | SEQ 09~10 main Visual Lab 스펙 정리와 guide 문서 보정 |
| `spring-boot-deployment-runtime-lab-09-implementation-worktree` | `09-implementation` | `7510cc7` | starter 문서와 workflow의 answer 브랜치명/구현 코드 노출 제거 |
| `spring-boot-deployment-runtime-lab-09-answer-worktree` | `09-answer` | `67e33d6` | answer 문서 구조 정리와 멘토 비교 포인트 보강 |
| `spring-boot-deployment-runtime-lab-10-implementation-worktree` | `10-implementation` | `7be3b18` | starter 문서와 workflow의 answer 브랜치명/구현 코드 노출 제거 |
| `spring-boot-deployment-runtime-lab-10-answer-worktree` | `10-answer` | `93457b9` | answer 문서 구조 정리와 멘토 비교 포인트 보강 |
| `spring-boot-db-access-lab` | `main` | `2cbf184` | SEQ 02~06 공통 main Visual Lab 스펙 정리와 guide 문서 보정 |
| `spring-boot-db-access-lab-02-implementation-worktree` | `02-implementation` | `699fd8b` | starter 문서의 answer 브랜치명/구현 코드 노출 제거 |
| `spring-boot-db-access-lab-02-answer-worktree` | `02-answer` | `b4fc54f` | answer 문서 구조 정리와 멘토 비교 포인트 보강 |
| `spring-boot-db-access-lab-03-implementation-worktree` | `03-implementation` | `2a008a0` | starter 문서의 answer 브랜치명/구현 코드 노출 제거 |
| `spring-boot-db-access-lab-03-answer-worktree` | `03-answer` | `1aa14b0` | answer 문서 구조 정리와 멘토 비교 포인트 보강 |
| `spring-boot-db-access-lab-04-implementation-worktree` | `04-implementation` | `8a598b3` | starter 문서의 answer 브랜치명/구현 코드 노출 제거 |
| `spring-boot-db-access-lab-04-answer-worktree` | `04-answer` | `c6376fb` | answer 문서 구조 정리와 멘토 비교 포인트 보강 |
| `spring-boot-db-access-lab-05-implementation-worktree` | `05-implementation` | `9bd6b11` | theory 문서를 PAAR, 실행 시퀀스, 계층/DTO 흐름, 실무 포인트, 용어 정리 중심으로 재작성 |
| `spring-boot-db-access-lab-05-answer-worktree` | `05-answer` | `dc5bdd3` | answer theory 문서를 PAAR, 실행 시퀀스, 계층/DTO 흐름, 실무 포인트, 용어 정리 중심으로 재작성 |
| `spring-boot-db-access-lab-06-implementation-worktree` | `06-implementation` | `0ff8336` | theory 문서를 PAAR, 실행 시퀀스, 계층/DTO 흐름, 실무 포인트, 용어 정리 중심으로 재작성 |
| `spring-boot-db-access-lab-06-answer-worktree` | `06-answer` | `97c5be1` | answer theory 문서를 PAAR, 실행 시퀀스, 계층/DTO 흐름, 실무 포인트, 용어 정리 중심으로 재작성 |
| `spring-boot-redis-cache-lab-07-implementation-worktree` | `07-implementation` | `2bd33bf` | theory 문서를 PAAR, 실행 시퀀스, 계층/DTO 흐름, 실무 포인트, 용어 정리 중심으로 재작성 |
| `spring-boot-redis-cache-lab-07-answer-worktree` | `07-answer` | `5aae22a` | answer theory 문서를 PAAR, 실행 시퀀스, 계층/DTO 흐름, 실무 포인트, 용어 정리 중심으로 재작성 |
| `spring-boot-realtime-communication-lab-08-implementation-worktree` | `08-implementation` | `ff0e0c1` | theory 문서를 PAAR, 실행 시퀀스, 계층/DTO 흐름, 실무 포인트, 용어 정리 중심으로 재작성 |
| `spring-boot-realtime-communication-lab-08-answer-worktree` | `08-answer` | `a64f5ee` | answer theory 문서를 PAAR, 실행 시퀀스, 계층/DTO 흐름, 실무 포인트, 용어 정리 중심으로 재작성 |
| `spring-boot-deployment-runtime-lab-09-implementation-worktree` | `09-implementation` | `0192b4f` | theory 문서를 PAAR, 실행 시퀀스, 설정 메시지 흐름, 실무 포인트, 용어 정리 중심으로 재작성 |
| `spring-boot-deployment-runtime-lab-09-answer-worktree` | `09-answer` | `c188298` | answer theory 문서를 PAAR, 실행 시퀀스, 설정 메시지 흐름, 실무 포인트, 용어 정리 중심으로 재작성 |
| `spring-boot-deployment-runtime-lab-10-implementation-worktree` | `10-implementation` | `d51af85` | theory 문서를 PAAR, 실행 시퀀스, workflow 메시지 흐름, 실무 포인트, 용어 정리 중심으로 재작성 |
| `spring-boot-deployment-runtime-lab-10-answer-worktree` | `10-answer` | `dd2141d` | answer theory 문서를 PAAR, 실행 시퀀스, workflow 메시지 흐름, 실무 포인트, 용어 정리 중심으로 재작성 |
| `aandi-prerequisite-bootcamp` | `main` | `66def0b` | SEQ 00 main Visual Lab 스펙 정리와 main 정답 자료 노출 축소 |
| `aandi-prerequisite-bootcamp-00-implementation-worktree` | `00-implementation` | `e787d95` | starter 문서의 answer 브랜치명/정답 자료 경로 노출 제거 |
| `aandi-prerequisite-bootcamp-00-answer-worktree` | `00-answer` | `1bf3a1b` | answer 문서 구조 정리와 멘토 비교 포인트 보강 |

## 2. 전체 시퀀스 상태 표

| Seq | Title | Repo | Impl Branch | Answer Branch | Docs | Visual Lab | Risk | Priority |
|---|---|---|---|---|---|---|---|---|
| 00 | Prerequisite | `aandi-prerequisite-bootcamp` | `00-implementation` | `00-answer` | main/implementation/answer 정리 완료 | main 4파일 스펙 정리 완료 | legacy branch 수동 조치 필요 | 6 |
| 01 | REST CRUD | `spring-boot-rest-crud-lab` | `01-implementation` | `01-answer` | main/implementation/answer 정리 완료 | main 4파일 스펙 정리 완료 | 원격 default branch와 legacy branch 수동 조치 필요 | 1 |
| 02 | DB Access | `spring-boot-db-access-lab` | `02-implementation` | `02-answer` | main/implementation/answer 정리 완료 | main 공통 4파일 스펙 정리 완료 | legacy branch 수동 조치 필요 | 5 |
| 03 | Validation | `spring-boot-db-access-lab` | `03-implementation` | `03-answer` | main/implementation/answer 정리 완료 | main 공통 4파일 스펙 정리 완료 | legacy branch 수동 조치 필요 | 5 |
| 04 | JWT | `spring-boot-db-access-lab` | `04-implementation` | `04-answer` | main/implementation/answer 정리 완료 | main 공통 4파일 스펙 정리 완료 | legacy branch 수동 조치 필요 | 5 |
| 05 | OAuth2 + SMTP | `spring-boot-db-access-lab` | `05-implementation` | `05-answer` | main guide 보정 완료, implementation/answer 추가 점검 필요 | main 공통 4파일 스펙 정리 완료 | implementation/answer 문서 추가 감사 필요 | 5 |
| 06 | Testing | `spring-boot-db-access-lab` | `06-implementation` | `06-answer` | main guide 보정 완료, implementation/answer 추가 점검 필요 | main 공통 4파일 스펙 정리 완료 | implementation/answer 문서 추가 감사 필요 | 5 |
| 07 | Redis Cache | `spring-boot-redis-cache-lab` | `07-implementation` | `07-answer` | main/implementation/answer 정리 완료 | main 4파일 스펙 정리 완료 | legacy branch 수동 조치 필요 | 4 |
| 08 | Realtime WebSocket | `spring-boot-realtime-communication-lab` | `08-implementation` | `08-answer` | main/implementation/answer 정리 완료 | main 4파일 스펙 정리 완료 | legacy branch 수동 조치 필요 | 4 |
| 09 | Docker/Runtime | `spring-boot-deployment-runtime-lab` | `09-implementation` | `09-answer` | main/implementation/answer 정리 완료 | main 4파일 스펙 정리 완료 | legacy branch 수동 조치 필요 | 4 |
| 10 | CI/CD Deployment | `spring-boot-deployment-runtime-lab` | `10-implementation` | `10-answer` | main/implementation/answer 정리 완료 | main 4파일 스펙 정리 완료 | legacy branch 수동 조치 필요 | 4 |
| 11 | Refactoring Foundation | `spring-boot-refactoring-foundation-lab` | `11-implementation` | `11-answer` | main/implementation/answer 정리 완료 | main 4파일 스펙 정리 완료 | legacy branch 수동 조치 필요 | 3 |
| 12 | Event Driven | `spring-boot-event-driven-lab` | `12-implementation` | `12-answer` | main/implementation/answer 정리 완료 | main 4파일 스펙 정리 완료 | 원격 HEAD/default branch 수동 확인 필요 | 2 |

## 3. 레포별 문제 요약

| Repo | 요약 |
|---|---|
| `spring-boot-rest-crud-lab` | SEQ 01 main Visual Lab을 `index.html`, `styles.css`, `visual-lab-data.js`, `visual-lab.js` 기준으로 정리했습니다. main의 legacy 안내 문서는 외부 링크 가능성을 고려해 삭제하지 않고 deprecated 안내로 축소했습니다. |
| `spring-boot-rest-crud-lab` `01-implementation` | `README.md`, `docs/implementation.md`, `docs/answer-guide.md`에서 answer 브랜치명과 정답 안내 노출을 제거했습니다. |
| `spring-boot-rest-crud-lab` `01-answer` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`를 starter 구조와 맞추고 answer 브랜치에서만 필요한 비교/멘토 리뷰 포인트를 보강했습니다. |
| `aandi-prerequisite-bootcamp` | SEQ 00 main Visual Lab에서 branch label과 implementationBranch 노출을 제거하고 현재 4파일 스펙에 맞췄습니다. main의 긴 정답 가이드는 deprecated 안내로 낮췄고, `00-answer` 브랜치에 같은 비교 자료가 있어 main의 `answer/` 폴더는 삭제했습니다. |
| `aandi-prerequisite-bootcamp` `00-implementation` | `README.md`, `docs/implementation.md`, `docs/answer-guide.md`, `docs/assets.md`, `docs/checklist.md`에서 answer 브랜치명과 `answer/` 자료 경로 노출을 제거했습니다. |
| `aandi-prerequisite-bootcamp` `00-answer` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`를 starter 흐름과 맞추고 answer 브랜치에서만 필요한 비교/멘토 리뷰 포인트를 보강했습니다. |
| `spring-boot-db-access-lab` | 02~06 공통 main Visual Lab을 현재 4파일 스펙에 맞춰 정리하고, 구버전 CSS 분리 파일을 `styles.css`로 병합했습니다. main guide 문서에서 answer 브랜치에서 starter로 이동하라는 학생-facing 표현을 제거했습니다. |
| `spring-boot-db-access-lab` `02-implementation` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, `docs/answer-guide.md`에서 answer 브랜치명, 구현 코드 조각, 금지 표현을 제거했습니다. |
| `spring-boot-db-access-lab` `02-answer` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, `docs/answer-guide.md`를 starter 흐름과 맞추고 answer 브랜치에서만 필요한 비교/멘토 리뷰 포인트를 보강했습니다. |
| `spring-boot-db-access-lab` `03-implementation` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, `docs/answer-guide.md`에서 answer 브랜치명, 구현 코드 조각, 금지 표현을 제거했습니다. |
| `spring-boot-db-access-lab` `03-answer` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, `docs/answer-guide.md`를 starter 흐름과 맞추고 answer 브랜치에서만 필요한 비교/멘토 리뷰 포인트를 보강했습니다. |
| `spring-boot-db-access-lab` `04-implementation` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, `docs/answer-guide.md`에서 answer 브랜치명, JWT 완성 구현 코드 조각, 금지 표현을 제거했습니다. |
| `spring-boot-db-access-lab` `04-answer` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, `docs/answer-guide.md`를 starter 흐름과 맞추고 JWT answer 비교와 멘토 리뷰 포인트를 보강했습니다. |
| `spring-boot-redis-cache-lab` | main Visual Lab을 현재 4파일 스펙에 맞춰 정리하고, 존재하지 않는 legacy answer-guide 안내를 제거했습니다. |
| `spring-boot-redis-cache-lab` `07-implementation` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, `docs/answer-guide.md`에서 answer 브랜치명, 구현 코드 조각, 금지 표현을 제거했습니다. |
| `spring-boot-redis-cache-lab` `07-answer` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`를 starter 흐름과 맞추고 answer 브랜치에서만 필요한 비교/멘토 리뷰 포인트를 보강했습니다. |
| `spring-boot-realtime-communication-lab` | main Visual Lab을 현재 4파일 스펙에 맞춰 정리하고, 존재하지 않는 legacy answer-guide 안내를 제거했습니다. |
| `spring-boot-realtime-communication-lab` `08-implementation` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, `docs/answer-guide.md`에서 answer 브랜치명, 구현 코드 조각, 금지 표현을 제거했습니다. |
| `spring-boot-realtime-communication-lab` `08-answer` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`를 starter 흐름과 맞추고 answer 브랜치에서만 필요한 비교/멘토 리뷰 포인트를 보강했습니다. |
| `spring-boot-deployment-runtime-lab` | 09~10 공통 main Visual Lab을 현재 4파일 스펙에 맞춰 정리하고, guide 문서의 완성 코드 표현을 비교 기준으로 낮췄습니다. |
| `spring-boot-deployment-runtime-lab` `09-implementation` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, `docs/answer-guide.md`, `.github/workflows/deploy.yml`에서 answer 브랜치명, 구현 코드 조각, 금지 표현을 제거했습니다. |
| `spring-boot-deployment-runtime-lab` `09-answer` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, `docs/answer-guide.md`를 starter 흐름과 맞추고 answer 브랜치에서만 필요한 비교/멘토 리뷰 포인트를 보강했습니다. |
| `spring-boot-deployment-runtime-lab` `10-implementation` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, `docs/answer-guide.md`, `.github/workflows/deploy.yml`에서 answer 브랜치명, 구현 코드 조각, 금지 표현을 제거했습니다. |
| `spring-boot-deployment-runtime-lab` `10-answer` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, `docs/answer-guide.md`를 starter 흐름과 맞추고 answer 브랜치에서만 필요한 비교/멘토 리뷰 포인트를 보강했습니다. |
| `spring-boot-refactoring-foundation-lab` | main에 남아 있던 10 CI/CD 문서 범위 혼입을 SEQ 11 리팩토링 범위로 정리하고 Visual Lab을 현재 4파일 스펙에 맞췄습니다. |
| `spring-boot-refactoring-foundation-lab` `11-implementation` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, `docs/answer-guide.md`, `docs/branch-guide.md`에서 answer 브랜치명, 구현 코드 조각, 범위 혼입 표현을 제거했습니다. |
| `spring-boot-refactoring-foundation-lab` `11-answer` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`를 starter 흐름과 맞추고 answer 브랜치에서만 필요한 비교/멘토 리뷰 포인트를 보강했습니다. |
| `spring-boot-event-driven-lab` | main Visual Lab을 현재 4파일 스펙에 맞춰 정리하고, main의 긴 정답 가이드를 deprecated 안내로 낮췄습니다. 원격 default branch가 `12-answer`를 가리킬 가능성은 GitHub UI 수동 조치가 필요합니다. |
| `spring-boot-event-driven-lab` `12-implementation` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`, `docs/answer-guide.md`, `docs/branch-guide.md`에서 answer 브랜치명, 완성 구현 코드 조각, 금지 표현을 제거했습니다. |
| `spring-boot-event-driven-lab` `12-answer` | `README.md`, `docs/theory.md`, `docs/implementation.md`, `docs/checklist.md`를 starter 흐름과 맞추고 answer 브랜치에서만 필요한 비교/멘토 리뷰 포인트를 보강했습니다. |

## 4. 정답 노출 의심 목록

| 위치 | 상태 | 처리 |
|---|---|---|
| `spring-boot-rest-crud-lab` main Visual Lab | 정답 브랜치명/answerBranch 노출 없음 | 처리 완료 |
| `spring-boot-rest-crud-lab` `01-implementation` 문서 | `01-answer`, 정답 코드, 정답 해설 노출 제거 | 처리 완료 |
| `spring-boot-rest-crud-lab` `01-answer` 문서 | answer 브랜치 내부 비교 코드와 멘토 포인트로 정리. 금지 표현과 answerBranch 메타 필드 없음 | 처리 완료 |
| `aandi-prerequisite-bootcamp` main Visual Lab/legacy answer docs | Visual Lab에는 answerBranch, `00-answer`, 정답 코드, 긴 완성 구현 코드 노출 없음. main의 `answer/` 폴더는 `00-answer` 브랜치에 남아 있어 삭제 | 처리 완료 |
| `aandi-prerequisite-bootcamp` `00-implementation` 문서 | `00-answer`, `answer/`, 정답 코드, 정답 해설 노출 제거 | 처리 완료 |
| `aandi-prerequisite-bootcamp` `00-answer` 문서 | answer 브랜치 내부 비교 자료와 멘토 포인트로 정리. 금지 표현과 answerBranch 메타 필드 없음 | 처리 완료 |
| `spring-boot-db-access-lab` main Visual Lab/guide docs | Visual Lab에는 answerBranch, `02-answer`~`06-answer`, 정답 코드, 긴 완성 구현 코드 노출 없음. main README/branch guide의 branch 표기는 운영 안내로 유지 | 처리 완료 |
| `spring-boot-db-access-lab` `02-implementation` | `02-answer`, 구현 코드 조각, 금지 표현 노출 제거 | 처리 완료 |
| `spring-boot-db-access-lab` `02-answer` | answer 브랜치 내부 비교 코드와 멘토 포인트로 정리. 금지 표현과 answerBranch 메타 필드 없음 | 처리 완료 |
| `spring-boot-db-access-lab` `03-implementation` | `03-answer`, 구현 코드 조각, 금지 표현 노출 제거 | 처리 완료 |
| `spring-boot-db-access-lab` `03-answer` | answer 브랜치 내부 비교 코드와 멘토 포인트로 정리. 금지 표현과 answerBranch 메타 필드 없음 | 처리 완료 |
| `spring-boot-db-access-lab` `04-implementation` | `04-answer`, 구현 코드 조각, 금지 표현 노출 제거 | 처리 완료 |
| `spring-boot-db-access-lab` `04-answer` | answer 브랜치 내부 비교 코드와 멘토 포인트로 정리. 금지 표현과 answerBranch 메타 필드 없음 | 처리 완료 |
| `spring-boot-db-access-lab` 05~06 implementation 브랜치 | 추가 검색 필요 | 미처리 |
| `spring-boot-redis-cache-lab` main Visual Lab/guide docs | answerBranch, `07-answer`, 정답 코드, 긴 완성 구현 코드 노출 없음 | 처리 완료 |
| `spring-boot-redis-cache-lab` `07-implementation` | `07-answer`, 구현 코드 조각, 금지 표현 노출 제거 | 처리 완료 |
| `spring-boot-redis-cache-lab` `07-answer` | answer 브랜치 내부 비교 코드와 멘토 포인트로 정리. 금지 표현과 answerBranch 메타 필드 없음 | 처리 완료 |
| `spring-boot-realtime-communication-lab` main Visual Lab/guide docs | answerBranch, `08-answer`, 정답 코드, 긴 완성 구현 코드 노출 없음 | 처리 완료 |
| `spring-boot-realtime-communication-lab` `08-implementation` | `08-answer`, 구현 코드 조각, 금지 표현 노출 제거 | 처리 완료 |
| `spring-boot-realtime-communication-lab` `08-answer` | answer 브랜치 내부 비교 코드와 멘토 포인트로 정리. 금지 표현과 answerBranch 메타 필드 없음 | 처리 완료 |
| `spring-boot-deployment-runtime-lab` main Visual Lab/guide docs | answerBranch, `09-answer`, `10-answer`, 정답 코드, 긴 완성 구현 코드 노출 없음 | 처리 완료 |
| `spring-boot-deployment-runtime-lab` `09-implementation` | `09-answer`, 구현 코드 조각, 금지 표현 노출 제거. workflow push trigger의 answer 브랜치명도 제거 | 처리 완료 |
| `spring-boot-deployment-runtime-lab` `09-answer` | answer 브랜치 내부 비교 코드와 멘토 포인트로 정리. 금지 표현과 answerBranch 메타 필드 없음 | 처리 완료 |
| `spring-boot-deployment-runtime-lab` `10-implementation` | `10-answer`, 구현 코드 조각, 금지 표현 노출 제거. workflow push trigger의 answer 브랜치명도 제거 | 처리 완료 |
| `spring-boot-deployment-runtime-lab` `10-answer` | answer 브랜치 내부 비교 코드와 멘토 포인트로 정리. 금지 표현과 answerBranch 메타 필드 없음 | 처리 완료 |
| `spring-boot-refactoring-foundation-lab` main Visual Lab/legacy answer guide | answerBranch, `11-answer`, 정답 코드, 긴 완성 구현 코드 노출 제거 | 처리 완료 |
| `spring-boot-refactoring-foundation-lab` `11-implementation` | `11-answer`, 구현 코드 조각, 범위 혼입 표현 노출 제거 | 처리 완료 |
| `spring-boot-refactoring-foundation-lab` `11-answer` | answer 브랜치 내부 비교 코드와 멘토 포인트로 정리. 금지 표현과 answerBranch 메타 필드 없음 | 처리 완료 |
| `spring-boot-event-driven-lab` main Visual Lab/legacy answer guide | answerBranch, `12-answer`, 정답 코드, 긴 완성 구현 코드 노출 제거 | 처리 완료 |
| `spring-boot-event-driven-lab` `12-implementation` | `12-answer`, 완성 구현 코드 조각, 금지 표현 노출 제거 | 처리 완료 |
| `spring-boot-event-driven-lab` `12-answer` | answer 브랜치 내부 비교 코드와 멘토 포인트로 정리. 금지 표현과 answerBranch 메타 필드 없음 | 처리 완료 |

## 5. Visual Lab 스펙 미준수 목록

기준 파일:

- `docs/visual-lab/index.html`
- `docs/visual-lab/styles.css`
- `docs/visual-lab/visual-lab-data.js`
- `docs/visual-lab/visual-lab.js`

현재 확인:

| Repo | 상태 |
|---|---|
| `aandi-prerequisite-bootcamp` | SEQ 00 main에서 4파일 스펙 정리 완료. 외부 CDN 없음, `window.visualLabData` 사용, answer 노출 없음. |
| `spring-boot-rest-crud-lab` | SEQ 01 main에서 4파일 스펙 정리 완료. 외부 CDN 없음, `window.visualLabData` 사용, answer 노출 없음. |
| `spring-boot-db-access-lab` | SEQ 02~06 공통 main에서 4파일 스펙 정리 완료. 외부 CDN 없음, `window.visualLabData` 사용, answer 노출 없음. |
| `spring-boot-redis-cache-lab` | SEQ 07 main에서 4파일 스펙 정리 완료. 외부 CDN 없음, `window.visualLabData` 사용, answer 노출 없음. |
| `spring-boot-realtime-communication-lab` | SEQ 08 main에서 4파일 스펙 정리 완료. 외부 CDN 없음, `window.visualLabData` 사용, answer 노출 없음. |
| `spring-boot-deployment-runtime-lab` | SEQ 09~10 main에서 4파일 스펙 정리 완료. 외부 CDN 없음, `window.visualLabData` 사용, answer 노출 없음. |
| `spring-boot-refactoring-foundation-lab` | SEQ 11 main에서 4파일 스펙 정리 완료. 외부 CDN 없음, `window.visualLabData` 사용, answer 노출 없음. |
| `spring-boot-event-driven-lab` | SEQ 12 main에서 4파일 스펙 정리 완료. 외부 CDN 없음, `window.visualLabData` 사용, answer 노출 없음. |

## 6. 레거시 후보 목록

| Repo | 후보 | 현재 판단 |
|---|---|---|
| `spring-boot-rest-crud-lab` | legacy `implementation`, `answer` branch | 삭제하지 않음. README/중앙 문서에서 deprecated 수동 조치 대상으로 유지. |
| `spring-boot-rest-crud-lab` | `docs/answer-guide.md` | 외부 링크 가능성 때문에 삭제하지 않고 deprecated 안내로 축소. |
| `spring-boot-rest-crud-lab` | `docs/assets.md`, `docs/branch-guide.md` | 삭제하지 않음. 오래된 표현만 낮은 위험으로 정리. |
| `aandi-prerequisite-bootcamp` | legacy `implementation` branch, local gone 상태의 `00-answer` tracking metadata | 브랜치 삭제/정리는 수행하지 않음. 원격에는 `00-implementation`, `00-answer`, `main`이 남아 있습니다. |
| `aandi-prerequisite-bootcamp` | main `answer/` 폴더 | `00-answer` 브랜치에 같은 비교 자료가 있어 main에서 삭제했습니다. |
| `aandi-prerequisite-bootcamp` | `docs/answer-guide.md` | 외부 링크 가능성 때문에 삭제하지 않고 deprecated 안내로 축소. |
| `spring-boot-db-access-lab` | legacy `implementation` branch, `docs/.DS_Store` | 삭제하지 않음. 브랜치 정리와 불필요 tracked 파일 삭제는 별도 승인 또는 시퀀스별 정리 단위에서 처리합니다. |
| `spring-boot-db-access-lab` | `docs/visual-lab/style.css`, `components.css`, `design-tokens.css` | `styles.css`로 병합 후 삭제했습니다. `index.html`에서 더 이상 참조하지 않고 중앙 validator가 요구하는 4파일 스펙과 일치합니다. |
| `spring-boot-refactoring-foundation-lab` | `docs/answer-guide.md` | 외부 링크 가능성 때문에 삭제하지 않고 deprecated 안내로 축소. |
| `spring-boot-event-driven-lab` | 원격 HEAD/default branch가 `12-answer`일 가능성 | GitHub UI 수동 조치 필요. |
| `spring-boot-event-driven-lab` | `docs/answer-guide.md` | 외부 링크 가능성 때문에 삭제하지 않고 deprecated 안내로 축소. |

## 7. 이번 5시간 안에 처리할 우선순위

1. SEQ 01 REST CRUD: main Visual Lab, legacy 안내, implementation 정답 노출 제거를 우선 완료합니다.
2. 중앙 기준 문서: Minimal Sequence Documentation Rule, PAAR 윤문 기준, Visual Lab 4파일 스펙, answer 노출 제한을 반영합니다.
3. SEQ 12 Event Driven: main Visual Lab과 legacy guide 정리는 완료했습니다. 원격 HEAD/default branch 리스크와 implementation/answer 문서 감사는 남았습니다.
4. SEQ 11 Refactoring Foundation: main, implementation, answer 문서 정리를 완료했습니다.
5. SEQ 07~10: SEQ07~10은 implementation/answer까지 완료했습니다.
6. SEQ 02~06: SEQ02~04는 implementation/answer까지 완료했습니다. SEQ05~06 브랜치 문서 감사는 남았습니다.
7. SEQ 00: main Visual Lab과 implementation/answer 문서 정리를 완료했습니다.

## 8. 이번 5시간 안에 처리하지 못한 항목

- SEQ 05~06 각 implementation 브랜치의 정답 노출 검색과 문서 보강은 아직 수행하지 않았습니다. 단, SEQ 00~04, 07~12 implementation 정답 노출 제거는 완료했습니다.
- SEQ 00~12 main Visual Lab 정리는 완료했습니다. 남은 항목은 implementation/answer 문서 감사입니다.
- SEQ 00은 Gradle 프로젝트가 아니라 `./gradlew test`를 실행하지 않았습니다. 대신 main/implementation/answer에서 `java -version`, `git --version`을 확인했고, main Visual Lab은 정적 서버, `node --check`, 중앙 validator로 검증했습니다.
- SEQ 02~06 `./gradlew test`는 실패했습니다. 실패 원인은 `CustomOAuthUserService` 처리 중 `org/springframework/security/oauth2/client/userinfo/OAuth2UserService.class`를 찾지 못하는 Spring 컨텍스트 로딩 오류입니다. 이번 변경 범위는 문서와 정적 Visual Lab 파일이라 코드/의존성 수정은 하지 않았습니다.
- SEQ 12 `./gradlew test`는 implementation/answer 모두 통과했습니다. 단, `Jackson2JsonMessageConverter` deprecation warning은 코드/의존성 범위라 이번 문서 정리에서 수정하지 않았습니다.
- SEQ 11 `./gradlew test`는 implementation/answer 모두 통과했습니다.
- SEQ 07 `./gradlew test`는 implementation/answer 모두 통과했습니다.
- SEQ 08 `./gradlew test`는 implementation/answer 모두 통과했습니다.
- SEQ 09 `./gradlew test`와 `./gradlew bootJar`는 implementation/answer 모두 통과했습니다.
- SEQ 10 `./gradlew test bootJar`와 `bash -n scripts/deploy.sh scripts/check-deploy.sh`는 implementation/answer 모두 통과했습니다.
- SEQ 02 `./gradlew test`는 implementation/answer 모두 통과했습니다.
- SEQ 03 `./gradlew test`는 implementation/answer 모두 통과했습니다.
- SEQ 04 `./gradlew test`는 implementation/answer 모두 통과했습니다.
- legacy 브랜치 삭제, default branch 변경, 원격 branch 정리는 수행하지 않았습니다. 이는 GitHub UI 또는 명시적 승인 후 처리해야 합니다.

## 9. theory.md 재작성 진행 기록

새 목표 기준:

- 대상: SEQ 00~12 각 시퀀스 브랜치의 `docs/theory.md`
- 요구 구조: PAAR, API/실행 시퀀스 다이어그램, 계층/DTO/메시지 흐름, 실무 포인트, 용어 정리
- implementation 브랜치 제한: answer 브랜치명, 정답 코드, 정답 해설 노출 금지

현재 완료:

| Seq | Branch | Commit | 검증 |
|---|---|---|---|
| 05 | `05-implementation` | `9bd6b11` | 금지 노출 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test` 통과 |
| 05 | `05-answer` | `dc5bdd3` | 금지 메타 필드 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test` 통과 |
| 06 | `06-implementation` | `0ff8336` | 금지 노출 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test` 통과 |
| 06 | `06-answer` | `97c5be1` | 금지 메타 필드 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test` 통과 |
| 07 | `07-implementation` | `2bd33bf` | 금지 노출 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test` 통과 |
| 07 | `07-answer` | `5aae22a` | 금지 메타 필드 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test` 통과 |
| 08 | `08-implementation` | `ff0e0c1` | 금지 노출 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test` 통과 |
| 08 | `08-answer` | `a64f5ee` | 금지 메타 필드 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test` 통과 |
| 09 | `09-implementation` | `0192b4f` | 금지 노출 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test bootJar` 통과 |
| 09 | `09-answer` | `c188298` | 금지 메타 필드 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test bootJar` 통과 |
| 10 | `10-implementation` | `d51af85` | theory 금지 노출 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test bootJar`와 `bash -n scripts/deploy.sh scripts/check-deploy.sh` 통과 |
| 10 | `10-answer` | `dd2141d` | 금지 메타 필드 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test bootJar`와 `bash -n scripts/deploy.sh scripts/check-deploy.sh` 통과 |
| 11 | `11-implementation` | `a2b33f0` | 금지 노출 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test` 통과 |
| 11 | `11-answer` | `8d200cc` | 금지 메타 필드 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test` 통과 |
| 12 | `12-implementation` | `7936c85` | 금지 노출 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test` 통과 |
| 12 | `12-answer` | `95e5206` | 금지 메타 필드 검색 통과, 필수 구조 검색 통과, `git diff --check` 통과, `./gradlew test` 통과 |

남은 theory 재작성 대상:

- SEQ 00~04

추가로 확인한 범위 밖 위험:

- `spring-boot-deployment-runtime-lab` `10-implementation`의 `.github/workflows/ci.yml`에는 PR target 목록에 `10-answer`가 남아 있습니다. 이번 theory 재작성 범위에서는 수정하지 않았고, 별도 answer 노출 정리 작업에서 처리해야 합니다.
