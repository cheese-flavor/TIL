# Day 02 — 방향 벡터와 회전

- 학습일 · **2026-11-12**
- 현재 상태 · **Trail 3문제 정답**, 삼성 기출 3문제 아직 미완료 (**Day 2 진행 중**)
- 학습 계획 · [30일 로드맵](../../PLAN.md) · [전체 진도](../../PROGRESS.md)
- 채점 근거 · **사용자가 채팅에서 코드트리 정답 확인**; 별도 로컬 테스트·공식 제출 데이터 자동 조회와 구분
- 학습 시간 · 문제별 독립 시도 / 전체 시간 미기록

## 완료 문제

| 순서 | 학습 위치 | 문제명 | 판정 | 코드 및 리뷰 |
| --- | --- | --- | --- | --- |
| 1 | Trail 2 → Chapter 5 → Lesson 3 (dx dy technique) | [격자 위의 편안한 상태](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-comfortable-state-on-the-grid/description) | 최초 오답 2안 → 리뷰 후 정답 | [최종·오답 코드 / 리뷰](trail2/comfortable-state/README.md) |
| 2 | Trail 2 → Chapter 5 → Lesson 3 (dx dy technique) | [되돌아오기](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-come-back/description) | 독립 정답 | [제출 코드 / 최적화 리뷰](trail2/come-back/README.md) |
| 3 | Trail 2 → Chapter 5 → Lesson 3 (dx dy technique) | [되돌아오기 2](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-come-back-2/description) | 방향·시간 조건 리뷰 후 정답 | [최종·초기 코드 / 리뷰](trail2/come-back-2/README.md) |

## 기초 진단

- 4방향 좌표 이동 · **3문항 모두 정답**
- `(1,2)`에서 네 방향 좌표 / `(0,0)` 모서리 유효 이동 2개 / `(2,3)`의 아래쪽 경계 초과 확인
- Day 1의 행·열 구분, 경계 검사를 Day 2의 실제 코드에 적용

## 오답과 핵심 학습

- **격자 위의 편안한 상태** · `count >= 3`에서 4칸 색칠 반례 발생 → `count == 3`; 내부 `print`로 중복 출력 → 반복문 밖 최종 판정; `stop == 2` 조기 종료는 논리적으로 타당
- **되돌아오기** · 한 칸씩 이동하는 시뮬레이션으로 정답; 이후 단일 직선 이동의 원점 통과 여부를 구간으로 판정하는 `O(N)` 최적화 학습 (**개선 코드 미제출**)
- **되돌아오기 2** · 결합 방향 벡터의 인덱스 `0,2,4,6`은 `%8`로 순환; 회전 명령도 1초 소요
- 원본 코드 주석과 실행 로직 보존; 채팅 서식의 강조 기호만 Python 문법으로 복원
- 코드트리 자동 제출용 `TIL/codetree/`는 이 학습 기록과 별도 관리

## 남은 DAY 2 기출 (미완료)

| 순서 | 문제명 | 수준 | 상태 |
| --- | --- | --- | --- |
| 1 | [자율주행 자동차](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/autonomous-driving/description) | 2017 · L11 | **다음 풀이 예정** |
| 2 | [돌아가는 팔각 의자](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/rounding-eight-angle/description) | 2017 · L11 | 미시도 |
| 3 | [바이러스 실험](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/virus-experiment/description) | 2018 · L13 | 미시도 |

## 다음 행동

- **자율주행 자동차**에서 방향 상태, 방문 처리, 좌회전, 후진, 정지 조건을 구분하여 독립 설계·구현
- 기출 정답은 아직 증가하지 않음. 전체 기출 정답 **1/83** (Day 1 바이러스 검사)
- 복습 · Day 7에 격자 위의 편안한 상태 조기 종료·출력 시점 재확인
