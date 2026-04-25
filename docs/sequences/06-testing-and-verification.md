# 06. 테스트와 검증

## 시퀀스 목표

이번 시퀀스의 목표는 학생이 이미 만든 Service 흐름을 테스트로 다시 확인하면서,
테스트가 왜 필요한지 현실적으로 이해하도록 만드는 것입니다.

학생은 이번 시퀀스를 마친 뒤 아래를 할 수 있어야 합니다.

1. 테스트가 왜 필요한지 설명할 수 있다.
2. 정상 케이스와 실패 케이스를 구분해서 테스트할 수 있다.
3. Service 단위 테스트를 작성할 수 있다.
4. fixture, mock, given-when-then 흐름을 설명할 수 있다.
5. 변경 이후에도 기존 기능을 다시 신뢰할 수 있다는 점을 이해할 수 있다.

## 시작 기준

- 시작 레포: `spring-boot-db-access-lab`
- 시작 기준 브랜치: `05-answer`
- 작업 브랜치:
  - `06-implementation`
  - `06-answer`
  - `main` 안내 브랜치 갱신

이번 시퀀스는 같은 도메인 위의 연속 실습이므로 새 레포를 만들지 않습니다.

## 이번 시퀀스에서 다루는 범위

- `PostService` 정상 케이스 테스트
- `PostService` 예외 케이스 테스트
- `AuthService` 인증 성공 테스트
- `AuthService` 인증 실패 테스트
- fixture와 mock 사용
- `./gradlew test`로 결과 검증

## 이번 시퀀스에서 다루지 않는 범위

- controller 테스트
- repository 테스트
- 통합 테스트
- e2e 테스트
- TDD 이론 심화

## 학생 구현 순서

구현 순서는 반드시 아래를 따릅니다.

1. 테스트 대상 Service를 확인한다.
2. fixture 또는 given 데이터를 준비한다.
3. 정상 케이스 테스트를 작성한다.
4. 예외 케이스 테스트를 작성한다.
5. 인증 흐름 테스트를 추가한다.
6. 테스트를 다시 실행하며 결과를 확인한다.

## 핵심 TODO 파일

- `src/test/kotlin/com/andi/rest_crud/support/TestFixtureFactory.kt`
- `src/test/kotlin/com/andi/rest_crud/service/PostServiceTest.kt`
- `src/test/kotlin/com/andi/rest_crud/service/AuthServiceTest.kt`

핵심 TODO는 위 파일에 집중되어야 합니다.

## 필수 산출물

각 브랜치에는 아래 산출물이 모두 있어야 합니다.

- `README.md`
- `docs/theory.md`
- `docs/implementation.md`
- `docs/answer-guide.md`
- `docs/checklist.md`
- `docs/assets.md`
- starter 테스트 코드
- answer 테스트 코드

## 문서 작성 기준

- `theory.md`: 왜 지금 테스트가 필요한지, 정상/실패 흐름 차이, fixture/mock/given-when-then 설명
- `implementation.md`: 학생이 손으로 칠 순서와 TODO 파일 설명
- `answer-guide.md`: 강사가 빠르게 비교할 수 있는 정답 흐름
- `checklist.md`: 학생 체크리스트와 강사/PPT 체크리스트 분리
- `assets.md`: 미리 제공하는 것과 학생이 직접 작성하지 않는 범위 정리

## 운영 메모

- `06-implementation`은 학생용 starter 브랜치입니다.
- `06-answer`는 비교용 완성 브랜치입니다.
- 서브모듈 `main`은 실습 브랜치가 아니라 안내 브랜치이며, 06까지의 브랜치 구조와 문서 구조를 보여줘야 합니다.
- 완료 후 루트 `README.md`에는 06 완료 상태와 다음 시퀀스를 반영해야 합니다.
