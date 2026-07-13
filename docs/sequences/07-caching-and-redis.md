# 07. 캐시와 Redis

## 목표

기존 조회 흐름 위에 Redis 캐시를 붙입니다.
cache hit, cache miss, invalidation 흐름을 실행 결과로 확인합니다.

## 이 시퀀스에서 배우는 것

- DB와 캐시의 역할 차이
- cache-aside 패턴
- cache hit와 cache miss
- TTL과 캐시 만료
- 수정/삭제 후 캐시 무효화

## 시작 브랜치

```bash
git checkout 07-implementation
```

## 실습 전 확인

- 토픽 레포: `spring-boot-redis-cache-lab`
- 가이드 브랜치: `main`
- 시작 브랜치: `07-implementation`
- 이전 기준: `06-answer`
- MySQL과 Redis가 함께 실행되어야 합니다.

## 구현할 TODO

1. Redis 설정을 확인합니다.
2. 캐시 key 규칙을 정합니다.
3. 조회 시 먼저 캐시를 확인합니다.
4. cache miss일 때 DB에서 조회하고 캐시에 저장합니다.
5. TTL을 설정합니다.
6. TTL 이후 캐시가 다시 채워지는 흐름을 확인합니다.
7. 수정/삭제가 성공하면 해당 게시글 캐시를 제거합니다.

## 실행 방법

```bash
docker compose up -d
./gradlew bootRun
```

## 테스트 방법

```bash
./gradlew test
```

테스트가 확인하는 것:

- cache miss 시 DB를 조회하고 결과를 Redis에 저장하는지 확인합니다.
- cache hit 시 DB 대신 캐시 값을 반환하는지 확인합니다.
- 조회 cache hit/miss와 TTL 저장을 확인합니다.
- 수정 또는 삭제 성공 후 해당 key가 evict되는지 확인합니다.

실패하면 먼저 볼 것:

- 캐시 key가 저장할 때와 조회할 때 같은 규칙을 쓰는지 확인합니다.
- 캐시 hit/miss를 확인하는 테스트에서 DB 호출 횟수 또는 로그 기준이 명확한지 봅니다.
- 수정/삭제 후 이전 캐시 key를 제거하는 호출이 빠지지 않았는지 확인합니다.

완료 기준:

- cache miss 테스트가 통과합니다.
- cache hit 테스트가 통과합니다.
- 수정/삭제 후 invalidation 테스트가 통과합니다.

## 확인할 API 또는 화면

- Swagger: `http://localhost:8080/swagger`
- 게시글 단건 조회 API
- 같은 조회를 두 번 실행했을 때 cache hit/miss 흐름
- 수정 또는 삭제 후 캐시 무효화 결과
- Redis 컨테이너 상태

## 자주 발생하는 문제

- 캐시가 있으면 DB가 필요 없다고 생각합니다. 캐시는 DB를 대체하지 않습니다.
- 수정/삭제가 실패했는데 캐시부터 지웁니다. DB 변경이 성공한 뒤 캐시를 제거합니다.
- TTL만 믿고 즉시성이 필요한 데이터를 방치합니다. 즉시 반영이 필요한 경우 evict가 필요합니다.
- key 이름이 요청마다 달라져 캐시가 재사용되지 않습니다.

## 완료 기준

- cache miss일 때 DB 조회 후 캐시에 저장됩니다.
- 같은 조회에서 cache hit 흐름을 확인했습니다.
- 수정/삭제 성공 후 해당 게시글 캐시가 제거됩니다.
- 수정/삭제 후 무효화가 필요한 이유와 TTL만으로 부족한 경우를 설명할 수 있습니다.
- TTL의 역할과 한계를 설명할 수 있습니다.
- `./gradlew test`가 통과합니다.

## 정답과 비교하는 방법

막혔거나 실습을 마친 뒤에만 참고 정답과 비교합니다.

```bash
git diff 07-implementation..07-answer
```

## 다음 시퀀스

다음은 `08. 실시간 통신`입니다.
WebSocket/STOMP로 서버가 연결된 클라이언트에게 메시지를 보냅니다.
