# 07. 캐시와 Redis

## 시퀀스 목표

이번 시퀀스의 목표는 학생이 기존 조회 흐름 위에 Redis 캐시를 직접 붙이면서,
캐시가 왜 필요한지와 cache-aside 흐름을 입문 수준에서 이해하도록 만드는 것입니다.

학생은 이번 시퀀스를 마친 뒤 아래를 할 수 있어야 합니다.

1. DB와 캐시의 차이를 설명할 수 있다.
2. cache hit와 miss를 설명할 수 있다.
3. 먼저 캐시를 보고, 없으면 DB를 보는 흐름을 말할 수 있다.
4. TTL이 왜 필요한지 설명할 수 있다.
5. 같은 요청을 두 번 보냈을 때 hit/miss 차이를 확인할 수 있다.

## 시작 기준

- 시작 레포: `spring-boot-redis-cache-lab`
- 이전 기준선: `spring-boot-db-access-lab`의 `06-answer`
- 작업 브랜치:
  - `07-implementation`
  - `07-answer`
  - `main` 안내 브랜치 갱신

이번 시퀀스는 저장/인증/테스트 기본기 레포와 학습 도메인이 달라지므로
새 토픽 레포로 분리합니다.

## 이번 시퀀스에서 다루는 범위

- Redis 연결 설정
- 게시글 단건 조회 1개에 대한 cache-aside 흐름
- cache hit / miss 확인
- TTL 설정
- MySQL + Redis 로컬 실행 환경

## 이번 시퀀스에서 다루지 않는 범위

- pub/sub
- stream
- distributed lock
- 세션 저장
- 토큰 블랙리스트
- 복잡한 캐시 무효화 전략
- 여러 캐시 전략 비교

## 학생 구현 순서

구현 순서는 반드시 아래를 따릅니다.

1. 캐시 조회 메서드를 만든다.
2. miss면 DB 조회로 연결한다.
3. 조회 결과를 캐시에 저장한다.
4. TTL을 설정한다.
5. hit/miss 차이를 확인한다.

## 핵심 TODO 파일

- `src/main/kotlin/com/andi/rest_crud/config/RedisConfig.kt`
- `src/main/kotlin/com/andi/rest_crud/service/PostCacheService.kt`
- `src/main/kotlin/com/andi/rest_crud/service/PostQueryService.kt`

핵심 TODO는 `RedisConfig.kt`, `PostCacheService.kt`에 집중하고,
조회 흐름 연결은 `PostQueryService.kt`에서 마무리합니다.

## 필수 산출물

각 브랜치에는 아래 산출물이 모두 있어야 합니다.

- `README.md`
- `docs/theory.md`
- `docs/implementation.md`
- `docs/answer-guide.md`
- `docs/checklist.md`
- `docs/assets.md`
- starter 코드
- answer 코드

## 문서 작성 기준

- `theory.md`: DB와 캐시 차이, hit/miss, TTL, Redis 역할 설명
- `implementation.md`: 학생이 손으로 칠 순서와 TODO 파일 설명
- `answer-guide.md`: cache 조회, miss -> DB -> set, TTL 정답 흐름
- `checklist.md`: 학생 체크리스트와 강사/PPT 체크리스트 분리
- `assets.md`: 미리 제공하는 것과 학생이 직접 작성하지 않는 범위 정리

## 운영 메모

- `07-implementation`은 학생용 starter 브랜치입니다.
- `07-answer`는 비교용 완성 브랜치입니다.
- 서브모듈 `main`은 실습 브랜치가 아니라 안내 브랜치이며, 07 전용 레포의 브랜치 구조와 문서 구조를 보여줘야 합니다.
- 완료 후 루트 `README.md`에는 07 완료 상태와 다음 시퀀스를 반영해야 합니다.
