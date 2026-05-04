# A&I Backend Visual Lab Design Guide

## 1. 문서 목적

이 문서는 A&I Backend Visual Lab의 디자인 시스템을 정의한다.

A&I Backend Visual Lab은 A&I 4기 백엔드 커리큘럼을 글이 아닌 시각적 흐름으로 이해하기 위한 정적 HTML 학습 페이지다.

이 페이지는 다음을 목표로 한다.

- 백엔드 이론을 교육용 인포그래픽처럼 보여준다.
- Controller, DTO, Entity, Repository, DB 흐름을 시각화한다.
- 문서와 코드 사이의 연결을 눈으로 확인할 수 있게 한다.
- A&I 공식 사이트의 밝고 깔끔한 브랜드 톤을 유지한다.
- 첨부된 자료구조 인포그래픽 스타일 가이드를 따른다.

## 2. 반드시 참조해야 할 디자인 자료

### 2.1 A&I 공식 사이트

참조 URL:

```text
https://aandiclub.com/
```

사용 목적:

- A&I 브랜드 톤 참고
- 밝은 배경
- 깔끔한 동아리/학습 커뮤니티 분위기
- 과하지 않은 색상 사용
- 친근하지만 가벼워 보이지 않는 개발자 학습 페이지 느낌

주의:

- 사이트를 그대로 복제하지 않는다.
- 브랜드 톤만 참고한다.
- Visual Lab 자체는 첨부된 교육용 인포그래픽 스타일에 더 가깝게 만든다.

### 2.2 첨부된 스타일 가이드 MD

참조 파일:

```text
stitch_ai_datastructure_image_style_guide.md
```

이 파일의 규칙을 반드시 따른다.
만약 현재 레포에 이 파일이 없다면, 작업 요청에 첨부된 동일 이름의 스타일 가이드 내용을 기준으로 삼는다.

핵심 규칙:

- 개발자 학습용 슬라이드 느낌
- 깔끔한 벡터형 인포그래픽
- 한국어 제목 중심 레이아웃
- 자료구조 개념을 한눈에 이해할 수 있는 시각화
- 시리즈 간 폰트/레이아웃 일관성 유지
- 1280x720 교육용 슬라이드 감성
- 네이비 / 로열블루 / 청록 중심 팔레트
- 흰색 또는 회백색 배경
- 둥근 카드
- 얇은 파란색 계열 테두리
- 부드러운 그림자
- 단순한 도식과 화살표
- 번호 배지와 아이콘 사용

## 3. 디자인 콘셉트

A&I Backend Visual Lab은 일반 문서 페이지가 아니다.

아래 느낌을 가져야 한다.

- CS 스터디 슬라이드
- 백엔드 부트캠프 강의 자료
- 기술 블로그 대표 이미지
- 개발자가 이해하기 쉬운 흐름도
- 로컬에서 실행 가능한 학습형 대시보드

피해야 할 느낌:

- 일반 블로그 글
- 무거운 관리자 페이지
- 다크모드 개발자 콘솔
- 3D 그래픽 사이트
- 네온 사이버펑크
- 지나치게 귀여운 교육 사이트

## 4. 고정 색상 토큰

CSS에는 반드시 아래 변수를 정의한다.

```css
:root {
  --color-bg-base: #F8F9FB;
  --color-card-white: #FFFFFF;

  --color-title-navy: #0C2691;
  --color-accent-blue: #2955E4;
  --color-accent-teal: #3F8996;

  --color-body-navy: #111B3F;
  --color-subtext: #4B587C;

  --color-line-blue-light: #C9D6F3;
  --color-panel-blue-tint: #EAF0FB;
  --color-panel-mint-tint: #D4E8E9;

  --color-decor-blue: #E8EEF9;
  --color-decor-stripe: #CAD8F7;
  --color-dot-grid: #C7D5F1;

  --color-outline-soft: #D8DDEB;

  --color-summary-bg: #F1F7FF;
  --color-summary-border: #8FB1FF;
  --color-summary-title: #2F62F4;

  --color-correct: #2C9FA0;
  --color-correct-bg: #ECFBFA;
  --color-incorrect: #2F62F4;
  --color-incorrect-bg: #EEF4FF;
}
```

## 5. 색상 사용 규칙

### 5.1 메인 제목

- 기본 색상: `#0C2691`
- 영어 병기 또는 강조: `#2955E4`
- 두 번째 줄 강조: `#3F8996`

예시:

```html
<h1>
  백엔드 흐름을
  <span>눈으로 이해하는 공간</span>
</h1>
```

### 5.2 카드

- 카드 배경: `#FFFFFF`
- 카드 테두리: `#D8DDEB`
- 연한 블루 카드 배경: `#EAF0FB`
- 연한 민트 카드 배경: `#D4E8E9`

### 5.3 상태 표현

정답/선택/활성 상태가 필요할 경우:

- 전체 카드를 진한 색으로 뒤집지 않는다.
- 테두리, 작은 배지, 아이콘 색상만 바꾼다.
- 빨강/초록 상태색을 기본으로 사용하지 않는다.
- 정답 또는 긍정 상태는 청록 계열
- 선택 또는 강조 상태는 블루 계열

## 6. 타이포그래피

### 6.1 기본 폰트

아래 순서로 사용한다.

```css
font-family: "Pretendard", "SUIT", "Noto Sans KR", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
```

외부 폰트 import는 하지 않는다.

### 6.2 메인 제목

메인 제목은 첨부 이미지처럼 매우 굵고 단정해야 한다.

규칙:

- `font-weight: 800` 이상
- 큰 크기
- 중앙 정렬
- 줄간격은 촘촘하지만 읽기 좋게
- 명조체, 손글씨체, 귀여운 둥근 폰트 금지

예시 CSS:

```css
.hero-title {
  font-size: clamp(44px, 7vw, 88px);
  font-weight: 900;
  line-height: 1.05;
  color: var(--color-title-navy);
}
```

### 6.3 부제

- 제목보다 작게
- `#4B587C`
- Medium 또는 SemiBold
- 1~2줄 이내

### 6.4 카드 제목

- 짧고 명확하게
- Bold
- 네이비 또는 블루 사용
- 긴 문장 금지

## 7. 배경 장식

첨부 이미지 스타일처럼 배경 장식을 CSS로 구현한다.

필수 장식:

### 7.1 좌상단 사분원 장식

- 화면 밖으로 일부 잘린 큰 원
- 연한 블루 배경
- 사선 패턴
- 콘텐츠보다 뒤에 있어야 함

### 7.2 우하단 원형 장식

- 화면 밖으로 일부 잘린 큰 원
- 연한 민트 또는 연한 블루
- 필요하면 얇은 원형 outline 추가

### 7.3 점 패턴

- 작은 점 그리드
- 우상단 또는 좌하단
- 연한 블루 계열
- 콘텐츠를 방해하지 않아야 함

예시 CSS:

```css
.page-shell::before {
  content: "";
  position: fixed;
  top: -90px;
  left: -80px;
  width: 260px;
  height: 260px;
  border-radius: 50%;
  background:
    repeating-linear-gradient(
      135deg,
      transparent 0,
      transparent 10px,
      var(--color-decor-stripe) 10px,
      var(--color-decor-stripe) 12px
    ),
    var(--color-decor-blue);
  opacity: 0.8;
  z-index: -1;
}
```

## 8. 카드 디자인

카드 규칙:

- 배경: 흰색
- 테두리: 연한 블루 그레이
- 둥근 모서리: 20px~28px
- 약한 그림자
- 충분한 내부 여백
- 카드 간 간격 넓게
- 한 카드에 너무 많은 텍스트를 넣지 않기

예시 CSS:

```css
.visual-card {
  background: var(--color-card-white);
  border: 1px solid var(--color-outline-soft);
  border-radius: 24px;
  box-shadow: 0 14px 34px rgba(12, 38, 145, 0.08);
  padding: 24px;
}
```

## 9. 도식 스타일

백엔드 개념은 자료구조 이미지처럼 단순 도식으로 표현한다.

사용 가능한 도식 요소:

- 둥근 사각형 노드
- 화살표
- 번호 배지
- 코드 라벨
- JSON 박스
- DTO 박스
- Entity 박스
- DB 테이블 박스
- 계층 카드

예시 흐름:

```text
HTTP Request
-> Controller
-> Request DTO
-> Service
-> Entity
-> Repository
-> MySQL
-> Response DTO
-> JSON Response
```

## 10. 레이아웃

### 10.1 Hero Section

포함 요소:

- 작은 코드 아이콘
- 큰 제목
- 부제
- 장식선
- 짧은 설명

### 10.2 Topic Cards Section

포함 요소:

- 학습 주제 카드 목록
- 각 카드에는 카테고리, 제목, 짧은 설명, 미니 도식 포함

### 10.3 Detail Section

포함 요소:

- 선택된 주제 제목
- 왜 중요한지
- 실행 흐름
- 코드 포인트
- 데이터 변환
- 관련 문서
- 관련 코드 파일

## 11. 반응형 규칙

데스크톱:

- 넓은 중앙 컨테이너
- 카드 grid 3~4열
- 상세 영역 2열 가능

태블릿:

- 카드 grid 2열

모바일:

- 카드 grid 1열
- 도식은 줄바꿈 또는 가로 스크롤
- 제목 크기 축소
- 텍스트가 잘리지 않아야 함

## 12. 금지 사항

사용하지 말 것:

- 외부 JS 라이브러리
- React, Vue, Next.js
- Bootstrap
- Tailwind CDN
- 실사 이미지
- 3D 렌더링
- 다크모드
- 네온 효과
- 복잡한 배경
- 빨강/주황/노랑 중심 팔레트
- 손글씨체
- 명조체
- 과하게 귀여운 둥근 폰트
