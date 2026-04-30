# 07. 캐시와 Redis

## 시퀀스 목표

이번 시퀀스의 목표는 학생이 기존 조회 흐름 위에 Redis 캐시를 직접 붙이면서,
캐시가 왜 필요한지와 `cache-aside` 흐름을 입문 수준에서 이해하도록 만드는 것입니다.

학생은 이번 시퀀스를 마친 뒤 아래를 할 수 있어야 합니다.

1. DB와 캐시의 역할 차이를 설명할 수 있다.
2. `cache hit`와 `cache miss`를 코드 기준으로 설명할 수 있다.
3. `miss -> DB 조회 -> cache set -> 다음 hit` 흐름을 말할 수 있다.
4. TTL이 왜 필요한지 설명할 수 있다.
5. 수정 이후 캐시를 지우지 않으면 왜 오래된 값이 남을 수 있는지 설명할 수 있다.

## 이번 시퀀스에서 다시 설명해야 하는 기초 개념

이번 07 시퀀스는 `06`까지 기능과 테스트가 정리된 상태에서 시작합니다.
그래서 학생이 아래 기초 개념을 다시 이해해야 합니다.

- `cache`
  자주 다시 쓰는 데이터를 더 빠르게 꺼내기 위해 잠깐 두는 보조 저장소
- `Redis`
  메모리 기반으로 빠르게 값을 저장하고 조회하는 저장소
- `cache-aside`
  먼저 캐시를 보고, 없으면 DB를 조회한 뒤 다시 캐시에 넣는 패턴
- `hit / miss`
  캐시에 값이 있어서 바로 응답하는 경우와, 없어서 DB로 가는 경우
- `TTL`
  캐시 값이 얼마나 오래 살아 있을지 정하는 시간
- `stale data`
  DB는 바뀌었는데 캐시에 예전 값이 남아 있는 상태

즉, 이번 시퀀스는 단순히 Redis를 붙이는 시간이 아니라
"조회는 빨라질 수 있지만, 값이 낡을 위험도 함께 생긴다"는 감각을 배우는 단계입니다.

## 현재 코드 흐름에서 어디를 봐야 하는가

이번 시퀀스는 기존 조회 흐름 앞에 캐시 레이어를 얹는 단계입니다.

1. `PostController.kt`
   단건 조회 요청을 어디로 넘기는지 보는 시작점
2. `PostQueryService.kt`
   hit / miss 분기와 cache-aside 흐름이 가장 잘 보이는 파일
3. `PostCacheService.kt`
   Redis key, TTL, 문자열 저장/조회 흐름을 모아둔 파일
4. `RedisConfig.kt`
   Spring과 Redis가 만나는 연결 지점
5. `PostService.kt`
   miss 이후 실제 DB 조회가 이어지는 기존 서비스

짧게 말하면 이번 시퀀스는

- `요청 -> 캐시 조회 -> miss면 DB 조회 -> 캐시 저장 -> 응답`
- `수정/삭제 -> 캐시 정리 필요 여부 판단`

흐름을 함께 이해하는 단계입니다.

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
- 게시글 단건 조회 1개에 대한 `cache-aside` 흐름
- `cache hit / miss` 확인
- TTL 설정
- 캐시 무효화 전략 입문
- MySQL + Redis 로컬 실행 환경

## 이번 시퀀스의 실무 확장 개념

이번 07 시퀀스의 실무 확장 개념은 `캐시 무효화 전략`입니다.

핵심은 이렇습니다.

- 캐시는 조회를 빠르게 만들지만, 수정 후 예전 값을 남길 수 있습니다.
- TTL만으로 문제를 늦출 수는 있지만, 항상 즉시 해결되는 것은 아닙니다.
- 그래서 수정/삭제 시점에는 `evict` 같은 명시적 정리가 필요할 수 있습니다.

즉, 이번 시퀀스는 "캐시는 빠르다"에서 끝나지 않고
"캐시는 빠르지만 관리하지 않으면 오래된 값을 보여줄 수 있다"까지 이해하는 단계입니다.

## 이번 시퀀스에서 다루지 않는 범위

- pub/sub
- stream
- distributed lock
- 세션 저장
- 토큰 블랙리스트
- 다중 노드 캐시 운영
- 고급 일관성 전략

## 학생 구현 순서

구현 순서는 반드시 아래를 따릅니다.

1. Redis 연결 Bean을 확인한다.
2. 캐시 조회 메서드를 만든다.
3. miss면 DB 조회로 연결한다.
4. 조회 결과를 캐시에 저장한다.
5. TTL을 설정한다.
6. hit / miss 차이를 확인한다.
7. 문서로 캐시 무효화 전략을 함께 이해한다.

## 문제 상황과 해결 방향을 코드로 보기

### 문제 1. 같은 조회를 매번 DB만 보면 왜 점점 부담이 되는가

처음에는 아래 코드가 자연스럽게 보입니다.

```kotlin
fun getPost(id: Long): PostResponse {
    return postService.getById(id)
}
```

게시글 하나 정도를 로컬에서 보는 동안에는 큰 차이가 없어 보일 수 있습니다.
하지만 같은 게시글 상세를 여러 사용자가 반복해서 읽는 상황이 오면,
요청마다 DB 조회가 계속 발생합니다.

이때 느려지는 이유는 보통 아래가 겹치기 때문입니다.

- 매 요청마다 DB 연결과 조회 비용이 반복됩니다.
- 같은 데이터를 매번 다시 직렬화해서 응답합니다.
- 트래픽이 늘면 DB가 병목이 되기 쉽습니다.

### 해결 방향 1. 먼저 캐시를 보고, 없을 때만 DB를 본다

```kotlin
fun getPost(id: Long): PostResponse {
    val cached = postCacheService.get(id)
    if (cached != null) {
        return cached
    }

    val response = postService.getById(id)
    postCacheService.set(id, response)
    return response
}
```

이 흐름이면 첫 요청은 여전히 DB를 보지만,
같은 데이터의 다음 요청은 캐시에서 더 가볍게 응답할 수 있습니다.

### 문제 2. 수정 후 캐시를 그대로 두면 왜 stale data가 생기는가

아래처럼 조회에만 캐시를 붙이고 수정 이후 정리를 하지 않으면,
DB와 캐시가 서로 다른 값을 가질 수 있습니다.

```kotlin
fun updatePost(id: Long, request: PostUpdateRequest): PostResponse {
    return postService.update(id, request)
}
```

이 코드만 있으면 DB는 새 제목으로 바뀌어도,
캐시 안에는 이전 제목이 TTL이 끝날 때까지 남아 있을 수 있습니다.

### 해결 방향 2. 수정/삭제 시점에는 캐시 정리도 함께 생각한다

```kotlin
fun updatePost(id: Long, request: PostUpdateRequest): PostResponse {
    val updated = postService.update(id, request)
    postCacheService.evict(id)
    return updated
}
```

또는 삭제 시점에도 같은 방식으로 캐시를 비울 수 있습니다.

```kotlin
fun deletePost(id: Long) {
    postService.delete(id)
    postCacheService.evict(id)
}
```

이번 시퀀스에서는 이 무효화 전략을 깊게 구현하지 않더라도,
"조회 캐시를 붙였으면 정리 전략도 같이 생각해야 한다"는 메시지는 반드시 가져가야 합니다.

### 문제 3. TTL만 있으면 항상 충분한가

TTL은 캐시가 영원히 남지 않게 도와줍니다.
하지만 TTL이 10분인데 1분 뒤에 데이터가 수정되면,
그 9분 동안은 여전히 stale data가 보일 수 있습니다.

### 해결 방향 3. TTL은 보조 장치이고, 즉시성은 evict가 맡는다

- TTL: 캐시가 무한정 남지 않게 하는 안전장치
- evict: 수정/삭제 직후 오래된 값을 바로 치우는 장치

실무에서는 둘 중 하나만 믿기보다,
"얼마나 빨리 최신성이 필요하냐"에 따라 둘을 함께 설계합니다.

## 문서에 반드시 남겨야 하는 것

이번 시퀀스 문서에는 아래가 함께 들어가야 합니다.

1. 기초 개념 설명
2. 현재 코드 흐름
3. 왜 캐시가 필요한지
4. 왜 stale data가 생길 수 있는지
5. TTL과 evict의 역할 차이
6. 이번 시퀀스에서 실제 구현 범위와 설명-only 범위

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

- `theory.md`: 캐시 필요성, DB와 캐시 차이, hit/miss, TTL, stale data, 캐시 무효화 전략 설명
- `implementation.md`: 학생이 손으로 칠 순서와 TODO 파일 설명
- `answer-guide.md`: `cache-aside`, TTL, `evict` 관점의 정답 흐름
- `checklist.md`: 학생 체크리스트와 강사/PPT 체크리스트 분리
- `assets.md`: 미리 제공하는 것과 학생이 직접 작성하지 않는 범위 정리

## 운영 메모

- `07-implementation`은 학생용 starter 브랜치입니다.
- `07-answer`는 비교용 완성 브랜치입니다.
- 서브모듈 `main`은 실습 브랜치가 아니라 안내 브랜치이며, 07 전용 레포의 브랜치 구조와 문서 구조를 보여줘야 합니다.
- 완료 후 루트 `README.md`에는 07 완료 상태와 다음 시퀀스를 반영해야 합니다.
