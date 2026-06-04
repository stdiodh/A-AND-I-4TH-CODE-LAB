# Demo Capture

> 메인 README로 돌아가기: [README](../README.md)

이번 정리는 코드랩 중앙 허브의 문서 구조와 운영 흐름을 증빙하는 작업입니다.
백엔드 API 실행 화면이나 서비스 UI가 아니라 교육 운영 문서가 핵심 산출물이므로 GIF를 억지로 생성하지 않았습니다.

## 생성된 데모 파일

| 기능 | 파일 | 생성 방식 | 상태 |
| :--- | :--- | :--- | :--- |
| 브랜치 전략 다이어그램 | [branch-strategy.png](./assets/images/branch-strategy.png) | 정적 PNG 다이어그램 | 생성 |
| 문서 구조 다이어그램 | [documentation-structure.png](./assets/images/documentation-structure.png) | 정적 PNG 다이어그램 | 생성 |
| 세션 흐름 다이어그램 | [session-flow.png](./assets/images/session-flow.png) | 정적 PNG 다이어그램 | 생성 |

## 자동 생성 시도 결과

| 항목 | 결과 |
| :--- | :--- |
| 로컬 실행 | 해당 없음 |
| 브라우저 실행 | 해당 없음 |
| PNG 생성 | 성공 |
| GIF 생성 | 미생성 |
| GIF 미생성 사유 | 이번 작업은 정적 문서 증빙 정리이며, 별도 앱 실행이나 UI 조작 대상이 없습니다. PNG 다이어그램이 더 적합합니다. |
| 커버리지 확인 | coverage 도구 설정이 없어 미측정 |
| 성능 측정 | 현재 before/after 측정값은 없습니다. |

## 수동 촬영 기준

| 기능 | 권장 파일명 | 촬영 범위 | 반드시 보여줄 액션 |
| :--- | :--- | :--- | :--- |
| 브랜치 전략 | `docs/assets/images/branch-strategy.png` | [Branch Strategy](./branch-strategy.md)의 Mermaid 다이어그램 | `NN-implementation`에서 시작해 `NN-answer`와 diff 비교하는 흐름 |
| 문서 구조 | `docs/assets/images/documentation-structure.png` | [Documentation Structure](./documentation-structure.md)의 Mermaid 다이어그램 | README에서 theory, implementation, checklist, visual-lab로 이어지는 구조 |
| 세션 흐름 | `docs/assets/images/session-flow.png` | [Session Operation](./session-operation.md)의 Mermaid 다이어그램 | 실습, 질문, 테스트, diff 비교, 회고 흐름 |

## 민감정보 기준

- 실제 학생 개인정보, 이메일, 토큰, 운영 서버 주소를 촬영하지 않습니다.
- GitHub 화면을 촬영할 경우 private 정보와 개인 알림 영역을 제외합니다.
- 토픽 레포 실행 화면을 촬영할 경우 실제 OAuth2 client secret, SMTP password, 운영 DB 접속 정보를 노출하지 않습니다.
