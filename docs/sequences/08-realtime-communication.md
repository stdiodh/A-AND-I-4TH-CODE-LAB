# 08. 실시간 통신

## 목표

HTTP 요청/응답 흐름을 넘어 WebSocket/STOMP로 연결, 구독, 발행 흐름을 구현합니다.
서버가 연결된 클라이언트에게 다시 메시지를 보내는 구조를 확인합니다.

## 이 시퀀스에서 배우는 것

- HTTP와 WebSocket의 차이
- WebSocket 연결 endpoint
- STOMP 구독과 발행
- topic broadcast 흐름
- 테스트 페이지에서 connect/send/receive 확인

## 시작 브랜치

```bash
git checkout 08-implementation
```

## 실습 전 확인

- 토픽 레포: `spring-boot-realtime-communication-lab`
- 가이드 브랜치: `main`
- 시작 브랜치: `08-implementation`
- 이전 기준: `07-answer`
- MySQL과 Redis가 필요한 기존 기능이 함께 실행될 수 있습니다.

## 구현할 TODO

1. WebSocket/STOMP 설정을 확인합니다.
2. 연결 endpoint를 확인합니다.
3. 메시지 DTO를 작성합니다.
4. 클라이언트가 topic을 구독하는 흐름을 확인합니다.
5. 메시지 발행 API 또는 STOMP handler를 연결합니다.
6. 서버가 topic으로 broadcast하는 흐름을 확인합니다.
7. 테스트 페이지에서 연결, 발행, 수신을 확인합니다.

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

- 기존 애플리케이션 context와 Service 단위 테스트가 계속 통과하는지 확인합니다.
- 실시간 데모 페이지와 SockJS 연결 정보가 인증 없이 열리는지 확인합니다.
- WebSocket 연결, topic 구독, 발행, broadcast 수신은 테스트 페이지에서 직접 확인합니다.
- 실제 STOMP 메시지 왕복 자동화는 현재 답안 범위에 포함되지 않습니다.

실패하면 먼저 볼 것:

- connect가 완료되기 전에 subscribe나 send를 실행하지 않았는지 확인합니다.
- 구독 경로와 발행 경로가 서로 다른 역할로 설정되어 있는지 봅니다.
- 자동화 테스트를 확장한다면 timeout과 메시지 타입을 함께 확인합니다.

완료 기준:

- `./gradlew test`가 통과합니다.
- 테스트 페이지에서 연결, 구독, 발행, 수신을 직접 확인했습니다.

## 확인할 API 또는 화면

- 테스트 페이지: `http://localhost:8080/realtime-demo.html`
- WebSocket endpoint: `/ws-chat`
- topic 구독 상태
- 메시지 발행 후 수신 결과

## 자주 발생하는 문제

- HTTP처럼 요청을 보내면 바로 응답이 온다고 생각합니다. WebSocket은 연결을 유지합니다.
- 구독 전에 메시지를 발행합니다. 먼저 connect와 subscribe를 확인합니다.
- topic 경로와 발행 경로를 혼동합니다. 구독 경로와 전송 경로를 분리해서 봅니다.
- 브라우저 테스트 페이지에서 연결 상태를 확인하지 않고 메시지만 보냅니다.
- 개발용 localhost Origin 설정을 운영에 그대로 사용합니다. 운영에서는 `APP_WEBSOCKET_ALLOWED_ORIGIN_PATTERNS`를 실제 프런트 Origin으로 제한합니다.

## 완료 기준

- 클라이언트가 WebSocket에 연결됩니다.
- topic을 구독한 뒤 메시지를 받을 수 있습니다.
- 메시지 발행 후 연결된 클라이언트에 broadcast됩니다.
- HTTP 요청/응답과 WebSocket 흐름의 차이를 설명할 수 있습니다.
- `./gradlew test`가 통과합니다.

## 정답과 비교하는 방법

막혔거나 실습을 마친 뒤에만 참고 정답과 비교합니다.

```bash
git diff 08-implementation..08-answer
```

## 다음 시퀀스

다음은 `09. 배포와 실행 환경`입니다.
애플리케이션을 Docker와 운영 설정으로 실행 가능한 단위로 묶습니다.
