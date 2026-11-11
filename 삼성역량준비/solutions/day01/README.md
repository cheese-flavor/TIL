# Day 01 — Python 진단과 직사각형 격자

- 학습일 · **2026-11-11**
- 상태 · **트레일 2문제 정답**, 삼성 기출 진행 예정
- 학습 계획 · [30일 로드맵](../../PLAN.md) · [전체 진도](../../PROGRESS.md)

## 문제별 기록

| 순서 | 학습 위치 | 문제명 | 채점 결과 | 코드 및 리뷰 |
| --- | --- | --- | --- | --- |
| 1 | Trail 1 · Chapter 8 · Lesson 2 (새로운 2차원 배열의 선언) | 두 개의 격자 비교하기 | 정답 | [풀이·리뷰](trail1/compare-two-grid/README.md) |
| 2 | Trail 2 · Chapter 1 · Lesson 2 (값을 반환하는 함수) | 그 계절, 그 날 | 정답 | [풀이·리뷰](trail2/that-season-that-day/README.md) |
| 3 | 삼성 기출 · 2015년 · L4 | [바이러스 검사](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/virus-detector/description) | 미시도 | 풀이 후 `past/2015/virus-detector/`에 기록 예정 |

## 기초 진단

- 3문제 중 **2문제 정답**
- `grid[행][열]`, `range(n)`(행), `range(m)`(열) 개념 확인
- 진단 2번에서 `n=2, m=3` 조건을 놓쳐 오답 선택. 코드 작성 시 N×M 직사각형 격자 입력 범위 재확인 필요

## 리뷰 및 다음 행동

- 트레일 문제 2개 모두 사용자 코드트리 정답 확인. 풀이 시간 미기록
- 제출 원본은 각 `solution.py`의 상단 메타데이터 주석 아래 보존
- 개선 의견·복잡도·검증 범위는 문제별 `README.md`에서 관리
- **다음 행동 · 바이러스 검사**를 독립적으로 풀이하고 결과 공유
