# 11. 리팩토링과 기초 보강

## 이 시퀀스의 목적

이번 시퀀스는 지금까지 만든 기능 위에서
좋은 구조가 무엇인지 다시 읽고 정리하는 단계입니다.

학생은 이번 단계에서 아래 흐름을 이해해야 합니다.

1. 지금까지 만든 코드를 다시 읽는다.
2. 역할이 섞인 부분을 찾는다.
3. Validation 또는 Exception Handling을 보강한다.
4. 테스트를 추가한다.
5. README 또는 문서를 보강한다.

즉, 이번 시퀀스의 핵심은
**서비스 리팩토링 + 검증/예외 보강 + 테스트 보강 + 문서 보강**입니다.

## 이전 시퀀스와의 연결

- 시작 기준: `10-answer`
- 시작 레포: `spring-boot-deployment-runtime-lab`
- 실제 11 실습 레포: `spring-boot-refactoring-foundation-lab`

이번 시퀀스는 새 기술을 하나 더 붙이는 단계가 아닙니다.
이미 있는 구조를 다시 읽고, 설명 가능하게 다듬는 데 집중합니다.

## 학생이 직접 구현할 순서

구현 순서는 반드시 아래 순서를 따릅니다.

1. 개선 대상 Service를 하나 고른다.
2. 역할이 섞인 부분을 찾는다.
3. Validation 또는 Exception Handling을 보강한다.
4. 테스트를 추가한다.
5. README 또는 문서를 보강한다.

## 학생이 직접 수정하는 핵심 파일

- `PostService.kt`
- `AuthService.kt`
- `GlobalExceptionHandler.kt`
- `README.md`
- `*Test.kt`

## 학생이 최종적으로 이해해야 하는 것

- 좋은 구조가 왜 읽기 쉬운지
- 역할이 섞인 코드와 분리된 코드를 어떻게 비교하는지
- Validation, Exception Handling, 테스트가 왜 연결되는지
- README 보강이 왜 복습 도구가 되는지

## 제공 전제로 두는 것

- 10 시퀀스 answer 기반 코드
- 기본 패키지 구조
- 기존 테스트 구조
- 실행 가능한 starter 환경

학생에게는 핵심 개선 흐름만 직접 구현하게 합니다.

## 이번 시퀀스의 범위

이번 시퀀스에서 다룹니다.

- Service 리팩토링 포인트 1~2개
- 서비스 레벨 검증 또는 예외 보강 1개
- 테스트 보강 1~2개
- README 및 문서 보강

이번 시퀀스에서 다루지 않습니다.

- Kafka, CQRS, DDD, 멀티모듈
- 성능 최적화 전체
- 전면 재작성 수준의 대규모 리팩토링
- 새로운 대형 기술 주제

## 결과물 기준

각 브랜치는 아래 결과물을 갖춰야 합니다.

- `README.md`
- `docs/theory.md`
- `docs/implementation.md`
- `docs/answer-guide.md`
- `docs/checklist.md`
- `docs/assets.md`
- starter 코드 또는 answer 코드

브랜치 구조는 아래를 따릅니다.

- `main`: 안내 브랜치
- `11-implementation`: 학생용 starter
- `11-answer`: 정답 브랜치

## 완료 기준

이번 시퀀스는 아래가 모두 맞아야 완료입니다.

- 새 토픽 레포 생성 및 루트 서브모듈 연결
- `11-implementation`, `11-answer`, `main` 브랜치 준비
- starter TODO가 서비스/예외/테스트/README에 맞게 배치됨
- answer 코드가 리팩토링 포인트와 테스트 보강을 보여줌
- `./gradlew test` 검증 완료
- 루트 README 상태표 갱신 완료
