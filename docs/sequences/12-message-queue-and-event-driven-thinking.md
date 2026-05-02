# 12. 메시지 큐와 이벤트 기반 사고

## 이 시퀀스의 목적

이번 시퀀스는 지금까지의 요청/응답 중심 구조 위에  
결과를 이벤트로 분리해 다른 흐름으로 넘기는 방식을 처음 소개하는 단계입니다.

핵심은 고급 메시징 운영을 배우는 것이 아니라, 학생이 아래 질문에 답할 수 있게 만드는 것입니다.

- 왜 직접 호출만으로는 점점 불편해질 수 있을까
- 이벤트는 어떤 역할을 할까
- 메시지 큐는 발행자와 소비자를 어떻게 덜 묶어줄까
- 서비스가 분리된 구조라면 이벤트가 큐를 통해 어떻게 이동할까

즉, 이번 시퀀스의 목표는 완전한 MSA 구현이 아니라 이벤트 기반 사고를 입문 수준에서 한 번 확장해보는 것입니다.

## 이전 시퀀스와의 연결

- 시작 기준: `11-answer`
- 실제 12 실습 레포: `spring-boot-event-driven-lab`

11 시퀀스까지는 구조를 다시 읽고 책임을 나누는 감각을 다뤘습니다.  
12 시퀀스에서는 그 감각 위에서 서비스 사이 연결 방식 자체를 바꿔서 생각해봅니다.

## 기초적으로 이해해야 할 것

- 동기 호출은 상대의 작업이 끝날 때까지 기다리는 방식입니다.
- 이벤트는 어떤 일이 일어났다는 사실을 전달하는 메시지입니다.
- 메시지 큐는 발행자와 소비자 사이에서 메시지를 중간 전달해주는 장치입니다.
- 서비스가 분리될수록 직접 메서드 호출보다 이벤트 전달이 더 자연스러운 장면이 늘어납니다.

## 이번 시퀀스의 실무 확장 개념

이번 시퀀스의 실무 확장 개념은 MSA 관점의 서비스 분리와 이벤트 이동입니다.

문제 코드는 보통 이런 그림입니다.

```kotlin
fun createOrder(request: OrderCreateRequest): OrderResponse {
    val saved = orderRepository.save(...)
    notificationService.sendOrderCreated(saved.id, request.userId)
    return OrderResponse(...)
}
```

이 구조는 동작은 하지만 주문 서비스가 알림 서비스의 존재를 직접 알아야 합니다.  
후속 작업이 늘어날수록 주문 서비스는 점점 더 많은 책임을 가지게 됩니다.

정리된 그림은 이런 방향을 가집니다.

```kotlin
fun createOrder(request: OrderCreateRequest): OrderResponse {
    val saved = orderRepository.save(...)
    eventPublisherService.publishOrderCreated(
        OrderCreatedEvent(...)
    )
    return OrderResponse(...)
}
```

그 다음 알림 소비자는 별도로 이벤트를 받아 후속 작업을 처리합니다.  
중요한 점은 발행자와 소비자가 직접 강하게 묶이지 않는다는 것입니다.

## 학생이 직접 구현할 순서

1. 이벤트 DTO를 만든다.
2. 이벤트 발행 코드를 만든다.
3. 이벤트 소비 코드를 만든다.
4. 흐름을 실행해본다.
5. 동기 호출과 이벤트 전달 차이를 비교한다.

## 학생이 직접 수정하는 핵심 파일

- `OrderCreatedEvent.kt`
- `EventPublisherService.kt`
- `NotificationConsumer.kt`

## 학생이 최종적으로 이해해야 하는 것

- 동기 호출과 비동기 전달의 차이
- 이벤트가 최소한 어떤 정보를 담아야 하는지
- 메시지 큐가 왜 필요한지
- 주문 서비스와 알림 서비스가 분리된다고 가정했을 때 이벤트가 어떤 연결 고리가 되는지
- 이번 시퀀스가 MSA 전체 구현이 아니라 그 사고방식을 맛보는 단계라는 점

## 제공 전제로 두는 것

- RabbitMQ 실행 환경
- Producer / Consumer 기본 틀
- `OrderService`, `NotificationService`, `EventConfig`
- 주문 생성 API와 알림 조회 API
- 실행 가능한 starter 환경

학생은 보일러플레이트보다 발행/소비 흐름을 손으로 따라치는 데 집중합니다.

## 이번 시퀀스의 범위

이번 시퀀스에서 다룹니다.

- 주문 생성 -> 이벤트 발행 -> 알림 소비
- 동기 호출과 이벤트 전달 비교
- 메시지 큐의 역할
- 서비스 분리 관점의 입문 설명

이번 시퀀스에서 다루지 않습니다.

- Kafka, RabbitMQ 운영 심화
- consumer group, partition, offset
- saga, outbox, CDC
- 실제 멀티 레포 MSA 구성
- 분산 트랜잭션

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
- `12-implementation`: 학생용 starter
- `12-answer`: 정답 브랜치

## 완료 기준

이번 시퀀스는 아래가 모두 맞아야 완료입니다.

- `12-implementation`, `12-answer`, `main` 브랜치가 정리되어 있음
- starter TODO가 이벤트 DTO, 발행, 소비 흐름에 맞게 배치되어 있음
- answer 코드가 이벤트 이동 흐름을 보여줌
- 문서가 기초 이론, 현재 코드 흐름, 실무 확장 개념을 모두 담고 있음
- `./gradlew test` 검증이 가능함
