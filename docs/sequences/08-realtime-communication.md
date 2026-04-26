# 08. 실시간 통신

## 시퀀스 목표

이번 시퀀스의 목표는 학생이 HTTP 기반 요청/응답 흐름 위에
실시간 메시지 전달 흐름을 직접 붙이면서, WebSocket 기반 통신이 왜 필요한지 입문 수준에서 이해하도록 만드는 것입니다.

학생은 이번 시퀀스를 마친 뒤 아래를 할 수 있어야 합니다.

1. HTTP와 WebSocket의 차이를 설명할 수 있다.
2. 서버가 클라이언트로 다시 메시지를 보낼 수 있는 이유를 말할 수 있다.
3. 메시지 DTO 역할을 설명할 수 있다.
4. 서버가 받은 메시지를 topic으로 다시 보내는 흐름을 말할 수 있다.
5. 테스트 페이지에서 메시지를 보내고 다시 받는 실시간 흐름을 확인할 수 있다.

## 시작 기준

- 시작 레포: `spring-boot-realtime-communication-lab`
- 이전 기준선: `spring-boot-redis-cache-lab`의 `07-answer`
- 작업 브랜치:
  - `08-implementation`
  - `08-answer`
  - `main` 안내 브랜치 갱신

이번 시퀀스는 캐시와는 다른 학습 도메인이므로
새 토픽 레포로 분리합니다.

## 이번 시퀀스에서 다루는 범위

- WebSocket/STOMP 의존성 추가
- 메시지 DTO 1개
- 메시지 수신 경로 1개
- topic broadcast 흐름 1개
- 테스트 HTML 페이지에서 connect/send/receive 확인

## 이번 시퀀스에서 다루지 않는 범위

- 채팅방 관리
- 메시지 저장
- 읽음 처리
- 사용자 세션 추적
- WebSocket 보안 고급 설정
- broker relay 같은 고급 주제

## 학생 구현 순서

구현 순서는 반드시 아래를 따릅니다.

1. 메시지 DTO를 만든다.
2. 메시지 수신 메서드를 만든다.
3. topic broadcast를 연결한다.
4. 테스트 페이지에서 결과를 확인한다.

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

- `theory.md`: HTTP와 WebSocket 차이, 연결 유지, 메시지 DTO, topic broadcast 설명
- `implementation.md`: 학생이 손으로 칠 순서와 TODO 파일 설명
- `answer-guide.md`: 메시지 DTO, 수신 메서드, topic broadcast 정답 흐름
- `checklist.md`: 학생 체크리스트와 강사/PPT 체크리스트 분리
- `assets.md`: 미리 제공하는 것과 학생이 직접 작성하지 않는 범위 정리

## 운영 메모

- `08-implementation`은 학생용 starter 브랜치입니다.
- `08-answer`는 비교용 완성 브랜치입니다.
- 서브모듈 `main`은 실습 브랜치가 아니라 안내 브랜치이며, 08 전용 레포의 브랜치 구조와 문서 구조를 보여줘야 합니다.
- 완료 후 루트 `README.md`에는 08 완료 상태와 다음 시퀀스를 반영해야 합니다.
