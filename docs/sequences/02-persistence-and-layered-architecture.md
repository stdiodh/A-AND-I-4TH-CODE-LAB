# 02. 영속성 저장과 계층 분리

## 시퀀스 목적

이 시퀀스는 `01`의 메모리 CRUD를 실제 DB 저장으로 바꾸면서,
학생이 아래 흐름을 선명하게 이해하게 만드는 단계입니다.

- 메모리 저장 대신 DB 저장이 된다
- Controller가 요청을 받는다
- Service가 처리 흐름을 맡는다
- Repository가 DB 접근을 맡는다
- Entity가 테이블과 연결된다
- CRUD 흐름이 기본 형태로 완성된다

즉, 이번 시퀀스의 핵심은 JPA 문법 자체보다
왜 메모리 저장이 부족한지, 왜 Repository가 필요한지, 왜 계층을 나누는지를
코드와 실행 결과로 이해하는 것입니다.

## 학생이 완성해야 하는 최종 이해

학생은 이 시퀀스를 마친 뒤 아래를 설명할 수 있어야 합니다.

1. 메모리 저장과 DB 저장의 차이
2. Entity가 DB 테이블과 연결된다는 감각
3. Repository가 왜 필요한지
4. `Controller -> Service -> Repository -> DB` 흐름
5. 생성 / 전체 조회 / 단건 조회 / 수정 / 삭제 기본 CRUD 흐름
6. MySQL에 실제로 데이터가 저장되는 것을 확인하는 방법

## 시작 기준

이번 시퀀스는 `01-answer` 기준 레포 위에서 시작합니다.

이미 존재한다고 가정하는 것:

- 기본 Spring Boot 프로젝트
- Swagger 설정
- 기본 패키지 구조
- Request DTO / Response DTO 최소 형태
- Controller / Service / 메모리 저장소 기반 CRUD 일부

이번 단계에서는 이 구조를 완전히 새로 만들지 않고,
메모리 저장을 MySQL 저장으로 교체하고 CRUD를 확장하는 것에 집중합니다.

## 레포 전략

- 사용 레포: `spring-boot-db-access-lab`
- 학생 starter: `02-implementation`
- 정답 브랜치: `02-answer`
- 안내 브랜치: `main`

## 학생 구현 순서

구현 순서는 반드시 아래 순서를 따릅니다.

1. `Entity` 핵심 필드와 어노테이션을 작성합니다.
2. `Repository` 인터페이스를 선언합니다.
3. `Service`의 저장 흐름을 메모리 저장에서 DB 저장으로 바꿉니다.
4. `findAll()`을 연결합니다.
5. `findById()`를 연결합니다.
6. `deleteById()`를 연결합니다.
7. `update()` 핵심 로직을 작성합니다.
8. Controller에서 수정 / 삭제 API를 연결합니다.
9. MySQL 저장 결과를 확인합니다.

문서와 TODO도 반드시 이 순서를 기준으로 설계합니다.

## TODO를 넣는 핵심 파일

- `PostEntity.kt`
- `PostRepository.kt`
- `PostService.kt`
- `PostController.kt`

핵심 TODO는 위 네 파일에 집중합니다.

## 미리 제공하는 것

- datasource 설정
- MySQL 실행 환경 또는 Docker Compose 예시
- application 설정 예시
- 기본 build 설정
- 메인 애플리케이션 클래스
- Swagger 설정
- 테스트용 H2 설정

학생은 영속 저장으로 바뀌는 핵심 흐름만 직접 구현합니다.

## 실무 확장 개념

이번 시퀀스부터는 메인 구현 흐름 외에
주니어 백엔드 개발자가 실무에서 반드시 만나게 되는 확장 개념 1개를 같이 가져갑니다.

`02`의 실무 확장 개념은 아래입니다.

- 관계 매핑 입문
- N+1 문제 입문

중요한 기준은 이렇습니다.

- 이번 시퀀스의 구현 메인 흐름은 단일 테이블 CRUD로 유지합니다.
- 대신 이론 문서에서 `@ManyToOne`, `@OneToMany`가 왜 필요한지,
  연관 데이터를 잘못 조회하면 왜 쿼리가 여러 번 나가는지,
  그것이 N+1의 시작이라는 점을 상세히 설명합니다.
- 해결책도 이름만 던지고 끝내지 않습니다.
  이론 문서에는 문제 코드와 함께 fetch join 예시 코드를 넣어서
  “보통 어떤 방향으로 조회 코드를 바꾸는가”까지 보여줍니다.

예를 들어 문서에는 아래 흐름이 들어가야 합니다.

1. `postRepository.findAll()` 뒤에 `post.comments.size`를 읽는 문제 코드
2. 목록 1번 + 댓글 N번 조회가 되는 예상 쿼리 흐름
3. 왜 데이터가 많아질수록 느려지는지
4. `findAllWithComments()` 같은 `fetch join` 해결 코드 예시

즉 `02`의 실무 확장 개념은
문제 이름 소개가 아니라
문제 코드와 해결 코드까지 같이 읽는 입문 단계로 설계합니다.

## 구현 제약

- Validation, Exception Handling, Security는 넣지 않습니다.
- 구현 메인 흐름에 연관관계 매핑을 강제로 넣지 않습니다.
- 구현 메인 흐름에 N+1 해결 코드를 억지로 넣지 않습니다.
- 이번 시퀀스의 목표는 `기본 CRUD + MySQL 영속 저장 + 계층 분리`입니다.
- 실무 확장 개념인 관계 매핑과 N+1은 이론 문서에서 상세히 다룹니다.
- 단, 이론 문서에는 반드시 `문제 코드 -> 느려지는 이유 -> 해결 코드 예시`가 함께 들어가야 합니다.

## 필수 산출물

각 브랜치에는 아래 산출물이 모두 있어야 합니다.

- `README.md`
- `docs/theory.md`
- `docs/implementation.md`
- `docs/answer-guide.md`
- `docs/checklist.md`
- `docs/assets.md`
- `02-implementation` starter 코드
- `02-answer` 완성 코드

## 검증 기준

- `02-implementation`은 실행 가능한 starter여야 합니다.
- `02-answer`는 CRUD 흐름이 완성되어 있어야 합니다.
- 테스트는 H2로 독립 실행 가능합니다.
- 런타임 가이드는 MySQL 기준으로 정리되어 있어야 합니다.
- 루트 허브와 브랜치 문서가 같은 시퀀스 내용을 설명해야 합니다.

## 수업 메시지

이번 단계에서 학생이 꼭 가져가야 할 문장은 아래입니다.

- 메모리 CRUD는 흐름 연습에 좋지만 실제 저장은 DB가 맡습니다.
- Entity, Repository, Service, Controller는 역할이 다릅니다.
- JPA를 쓰면 CRUD는 편해지지만, 관계가 생기면 조회 성능 문제도 같이 신경 써야 합니다.
- 관계 매핑과 N+1은 바로 다음 심화에서 자주 만나게 되는 대표 실무 개념입니다.
