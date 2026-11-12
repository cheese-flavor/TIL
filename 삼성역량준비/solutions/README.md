# 삼성 SW 역량테스트 — Day별 풀이 보관

30일 학습을 **Day 단위 폴더(`day01`, `day02`, …)** 로 관리. 각 Day에 그날 푼 트레일·삼성 기출 코드와 리뷰를 모두 보관. 기존 TIL 루트의 `codetree/` 자동 제출과 별개로 운영.

## 구조

```text
삼성역량준비/
  PLAN.md
  PROGRESS.md
  CHAT.md
  solutions/
    README.md
    TEMPLATE.md
    day01/
      README.md
      trail1/
        compare-two-grid/
          solution.py
          README.md
      trail2/
        that-season-that-day/
          solution.py
          README.md
      past/                      # 삼성 기출 풀이 시 생성
        2015/
          virus-detector/
            attempt1.py             # 1차 오답 코드 (있을 때)
            solution.py             # 최종 정답 제출 코드
            README.md               # 실패 원인·반례·코드 리뷰
    day02/                       # Day 2 시작 시 생성
      README.md
      ...
```

## 저장·커밋 규칙

1. 새 채팅에서 Day가 시작되면 해당 **`solutions/dayNN/`** 폴더 생성. 그날 푼 문제를 모두 이곳에 저장.
2. 트레일 경로 · `dayNN/trail번호/문제슬러그/`; 삼성 기출 경로 · `dayNN/past/연도/문제슬러그/`.
3. 각 문제의 **`solution.py` 맨 위 주석**에 Day, Trail·Chapter·Lesson 번호 및 명칭(기출은 연도·레벨), 문제명, **코드트리 URL**과 채점 결과 기재. 실행 가능한 **사용자 제출 원본은 주석 아래 변경 없이 보존**.
4. 문제별 **`README.md`** 에 핵심 조건, 풀이 접근, 시간·공간 복잡도, 정답 여부, ChatGPT 리뷰, 개선안, 반례 및 검증 범위 기재. [양식](TEMPLATE.md) 참고.
5. 같은 Day의 **`README.md`** 에 문제 목록·링크·진단·회고 요약. [진도 기록](../PROGRESS.md)도 실제 위치로 연결.
6. 오답 후 재제출했다면 문제 폴더에 `attempt1.py`, `attempt2.py` 등 시도별 코드를 함께 보관하고, 최종 정답 코드는 `solution.py`에 저장. 각 시도의 실패 원인·반례를 문제별 `README.md`에 기록.
7. **문제 풀이·코드 리뷰가 끝나는 즉시 문제별로 커밋**. 문서 체계 변경은 별도 커밋. 자동 커밋은 지속 실행되는 백그라운드 작업이 아니라 채팅에서 명시적으로 반영함.
8. Day 마감 시 학습 회고 및 재풀이 목표 갱신. 코드트리의 정답 기록과 별도 로컬 실행 여부를 구분.

## Day별 목록

- [Day 01 · 2026-11-11](day01/README.md) — 트레일 2문제 정답, 삼성 기출 1문제 정답(1차 실패 후 수정)
- [Day 02 · 2026-11-12](day02/README.md) — 트레일 3문제 정답(정답 코드·오답 검토 기록), 삼성 기출 3문제 진행 예정
