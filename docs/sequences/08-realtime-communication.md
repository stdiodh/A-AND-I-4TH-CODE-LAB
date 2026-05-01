# 08. 실시간 통신

## 시퀀스 목표

이번 시퀀스의 목표는 학생이 HTTP 기반 요청/응답 흐름 위에
실시간 메시지 전달 흐름을 직접 붙이면서, WebSocket 기반 통신이 왜 필요한지 입문 수준에서 이해하도록 만드는 것입니다.

학생은 이번 시퀀스를 마친 뒤 아래를 할 수 있어야 합니다.

1. HTTP와 WebSocket의 차이를 설명할 수 있다.
2. 서버가 클라이언트로 다시 메시지를 보낼 수 있는 이유를 말할 수 있다.
3. 메시지 DTO 역할을 설명할 수 있다.
4. 서버가 받은 메시지를 topic으로 다시 보내는 흐름을 말할 수 있다.
5. 메시지 타입을 왜 나누는지 설명할 수 있다.
6. 사용자의 접속/종료 상태를 별도 이벤트로 다뤄야 하는 이유를 말할 수 있다.

## 이번 시퀀스에서 다시 설명해야 하는 기초 개념

이번 08 시퀀스는 `07`까지 조회와 성능 보조 흐름을 배운 상태에서 시작합니다.
그래서 학생이 아래 기초 개념을 다시 이해해야 합니다.

- `HTTP`
  요청이 들어와야 응답이 나가는 기본 웹 통신 방식
- `WebSocket`
  연결을 유지한 채 클라이언트와 서버가 계속 메시지를 주고받을 수 있는 통신 방식
- `STOMP`
  어떤 경로로 보내고 어디를 구독할지 더 읽기 쉽게 다루도록 도와주는 메시지 규약
- `publish`
  서버나 클라이언트가 특정 경로로 메시지를 보내는 행위
- `subscribe`
  특정 topic으로 오는 메시지를 계속 받겠다고 연결해두는 행위
- `message type`
  채팅 메시지, 입장, 퇴장, 시스템 메시지처럼 이벤트 종류를 구분하는 값
- `connection state`
  누가 지금 연결되어 있는지, 끊어졌는지 같은 상태

즉, 이번 시퀀스는 단순히 "메시지가 오간다"에서 끝나지 않고
"이 메시지가 어떤 종류인지"와 "누가 들어오고 나가는지"까지 함께 생각하기 시작하는 단계입니다.

## 현재 코드 흐름에서 어디를 봐야 하는가

이번 시퀀스는 HTTP 기반 앱 위에 가장 작은 실시간 흐름을 붙이는 단계입니다.

1. `realtime-demo.html`
   connect, subscribe, send, receive가 한 화면에서 보이는 시작점
2. `ChatMessage.kt`
   브라우저와 서버가 어떤 구조의 메시지를 주고받는지 보여주는 DTO
3. `WebSocketConfig.kt`
   endpoint, broker, application destination prefix가 모이는 설정 파일
4. `WebSocketController.kt`
   메시지를 받아 다시 topic으로 보내는 핵심 흐름

짧게 말하면 이번 시퀀스는

- `연결 -> 구독 -> 전송 -> 서버 수신 -> topic broadcast -> 실시간 수신`
- `문자열 메시지 1종 -> 이벤트 타입을 가진 메시지로 확장할 필요 인식`

흐름을 함께 이해하는 단계입니다.

## 시작 기준

- 시작 레포: `spring-boot-realtime-communication-lab`
- 이전 기준선: `spring-boot-redis-cache-lab`의 `07-answer`
- 작업 브랜치:
  - `08-implementation`
  - `08-answer`
  - `main` 안내 브랜치 갱신

이번 시퀀스는 캐시와는 다른 학습 도메인이므로 새 토픽 레포로 분리합니다.

## 이번 시퀀스에서 다루는 범위

- WebSocket/STOMP 의존성 추가
- 메시지 DTO 1개
- 메시지 수신 경로 1개
- topic broadcast 흐름 1개
- 테스트 HTML 페이지에서 connect/send/receive 확인
- 메시지 타입 분리와 연결 상태 관리에 대한 입문 설명

## 이번 시퀀스의 실무 확장 개념

이번 08 시퀀스의 실무 확장 개념은 아래 두 가지입니다.

- 메시지 타입 분리
- 연결 상태 관리

핵심은 이렇습니다.

- 처음에는 `sender`, `content`만 있어도 실시간 흐름을 볼 수 있습니다.
- 하지만 실무 채팅이나 알림은 `CHAT`, `JOIN`, `LEAVE`, `SYSTEM`처럼 종류가 다릅니다.
- 연결 상태를 별도로 다루지 않으면 누가 들어왔고 나갔는지, 시스템 메시지를 어떻게 보여줄지 설명하기 어려워집니다.

즉, 이번 시퀀스는 "메시지를 보낸다"에서 한 걸음 더 나아가
"어떤 이벤트를 보냈는지 구조적으로 나눠야 한다"를 이해하는 단계입니다.

## 이번 시퀀스에서 다루지 않는 범위

- 채팅방 관리
- 메시지 저장
- 읽음 처리
- 사용자 세션 추적 심화
- WebSocket 보안 고급 설정
- broker relay 같은 고급 주제
- Redis pub/sub 연동

## 학생 구현 순서

구현 순서는 반드시 아래를 따릅니다.

1. 메시지 DTO를 만든다.
2. WebSocket endpoint와 topic 흐름을 확인한다.
3. 메시지 수신 메서드를 만든다.
4. topic broadcast를 연결한다.
5. 테스트 페이지에서 결과를 확인한다.
6. 문서로 메시지 타입 분리와 연결 상태 관리까지 이해한다.

## 문제 상황과 해결 방향을 코드로 보기

### 문제 1. HTTP 요청/응답만으로는 왜 채팅이 답답한가

아래처럼 요청을 보내야만 응답이 오는 구조는 CRUD에는 자연스럽습니다.

```kotlin
@GetMapping("/messages/latest")
fun latest(): MessageResponse {
    return messageService.getLatest()
}
```

하지만 채팅이나 알림은 사용자가 새 요청을 보내지 않아도
서버가 먼저 "새 메시지가 왔다"고 알려줘야 할 때가 많습니다.

이때 불편해지는 이유는 보통 아래가 겹치기 때문입니다.

- 사용자가 계속 새 요청을 보내야 합니다.
- 서버가 먼저 알려주는 감각이 없습니다.
- 반응이 느리거나 부자연스럽게 느껴질 수 있습니다.

### 해결 방향 1. 연결을 유지한 채 서버가 다시 보내게 만든다

```kotlin
@MessageMapping("/chat.send")
@SendTo("/topic/chat")
fun send(message: ChatMessage): ChatMessage {
    return message
}
```

이 흐름이면 클라이언트가 한 번 연결한 뒤,
서버가 받은 메시지를 다시 topic으로 보내고,
구독 중인 화면이 바로 받을 수 있습니다.

### 문제 2. 문자열 메시지 하나만 있으면 왜 한계가 생기는가

처음에는 아래처럼 `sender`, `content`만 있는 메시지가 자연스럽게 보입니다.

```kotlin
data class ChatMessage(
    val sender: String,
    val content: String
)
```

하지만 이 구조만으로는 아래를 구분하기 어렵습니다.

- 실제 채팅 메시지인지
- 누군가 방에 들어왔다는 시스템 이벤트인지
- 연결이 끊겼다는 퇴장 이벤트인지

### 해결 방향 2. 메시지 타입을 나눌 준비를 한다

```kotlin
data class ChatMessage(
    val type: String,
    val sender: String,
    val content: String
)
```

예를 들면 아래처럼 분리할 수 있습니다.

- `JOIN`
- `CHAT`
- `LEAVE`
- `SYSTEM`

이번 시퀀스에서는 이 구조를 깊게 구현하지 않더라도,
"실무에서는 단순 문자열 하나로는 오래 버티기 어렵다"는 메시지는 반드시 가져가야 합니다.

### 문제 3. 연결 상태를 무시하면 어떤 UX 문제가 생기는가

아무런 상태 이벤트가 없으면 사용자는 아래를 알기 어렵습니다.

- 지금 연결이 되었는지
- 누가 들어왔는지
- 누가 나갔는지

그 결과 채팅 UI는 메시지는 오가더라도
"방 안에 누가 있는지"와 "지금 연결이 살아 있는지"가 흐릿해집니다.

### 해결 방향 3. 연결 상태도 이벤트처럼 생각한다

예를 들면 아래 같은 시스템 메시지를 떠올릴 수 있습니다.

```text
[SYSTEM] andi 님이 입장했습니다.
[SYSTEM] andi 님이 퇴장했습니다.
```

실무에서는 이 상태를 세션 이벤트나 별도 메시지 타입으로 연결하는 경우가 많습니다.

## 문서에 반드시 남겨야 하는 것

이번 시퀀스 문서에는 아래가 함께 들어가야 합니다.

1. 기초 개념 설명
2. 현재 코드 흐름
3. 왜 HTTP만으로는 불편한지
4. 왜 메시지 타입을 나눠야 하는지
5. 왜 연결 상태를 별도 이벤트로 생각해야 하는지
6. 이번 시퀀스에서 실제 구현 범위와 설명-only 범위

## 핵심 TODO 파일

- `src/main/kotlin/com/andi/rest_crud/dto/ChatMessage.kt`
- `src/main/kotlin/com/andi/rest_crud/config/WebSocketConfig.kt`
- `src/main/kotlin/com/andi/rest_crud/controller/WebSocketController.kt`

핵심 TODO는 위 파일에 집중되어야 합니다.

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

- `theory.md`: HTTP와 WebSocket 차이, 연결 유지, STOMP, 메시지 DTO, topic broadcast, 메시지 타입 분리, 연결 상태 설명
- `implementation.md`: 학생이 손으로 칠 순서와 TODO 파일 설명
- `answer-guide.md`: 메시지 DTO, 수신 메서드, topic broadcast, 타입 확장 방향 정답 흐름
- `checklist.md`: 학생 체크리스트와 강사/PPT 체크리스트 분리
- `assets.md`: 미리 제공하는 것과 학생이 직접 작성하지 않는 범위 정리

## 운영 메모

- `08-implementation`은 학생용 starter 브랜치입니다.
- `08-answer`는 비교용 완성 브랜치입니다.
- 서브모듈 `main`은 실습 브랜치가 아니라 안내 브랜치이며, 08 전용 레포의 브랜치 구조와 문서 구조를 보여줘야 합니다.
- 완료 후 루트 `README.md`에는 08 완료 상태와 다음 시퀀스를 반영해야 합니다.
