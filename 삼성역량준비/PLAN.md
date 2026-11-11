# 4주 로드맵

주 6회, 회당 60~90분 기준이다. 각 단계에서 **필수 트레일 체크박스를 모두 완료하고, 통과 기준을 확인한 다음 오른쪽의 기출**을 푼다. 전체 기출은 [연도·유형별 목록](PROBLEMS.md)에서 찾아볼 수 있다.

| 단계 | 시기 | 트레일에서 먼저 연습 | 다음 기출 |
| --- | --- | --- | --- |
| 1. Python과 격자 | 1주차 1~3회 | 리스트·함수·2차원 배열·경계 검사 | 입출력이 막힐 때만 바이러스 검사 |
| 2. 격자 구현 | 1주차 4~6회 | 방향 배열·완전탐색·한 객체 이동 | 자율주행 자동차 |
| 3. BFS와 자료구조 | 2주차 1~4회 | 큐·방문 표시·연결 요소·최단거리 | 토스트 계란틀 |
| 4. 재귀와 백트래킹 | 2주차 5회~3주차 1회 | 종료 조건·선택과 복원·조합 | 외주 수익 최대화하기 |
| 5. 여러 규칙 합치기 | 3주차 2~6회 | 정렬 키·회전·단계별 갱신 | 메이즈 러너 → 고대 문명 유적 탐사 |
| 6. 최근 기출 | 4주차 | 이전 오답의 트레일 문제 1개 재풀이 | 택배 하차 → 2026 하반기 오후 모의 |

## 1. Python과 격자

- [ ] [Trail 1 · 1차원 배열](https://www.codetree.ai/trail-info/novice-low/) → **한 줄에 여러 개 입력** 연습 1개. `list(map(int, input().split()))`으로 읽고 합계나 개수를 계산한다.
- [ ] [Trail 1 · 두 개의 격자 비교하기](https://www.codetree.ai/ko/trails/complete/curated-cards/test-compare-two-grid/description) → 2차원 입력, 행·열 인덱스, 중첩 반복문.
- [ ] [Trail 2 · 그 계절, 그 날](https://www.codetree.ai/ko/trails/complete/curated-cards/test-that-season-that-day/description) → 기존 TIL 통과 문제를 새 파일에서 풀며 함수 인자, `return`, 경계 조건을 확인한다.

**통과 기준** · 빈 파일에서 격자를 입력받고 지정된 좌표의 상하좌우 중 유효한 칸만 출력한다. 1×1과 직사각형으로 확인하고, 새 2차원 리스트의 각 행이 독립적으로 생성되는 이유를 설명한다.

**선택 기출** · 입력이나 반복문에서 막혔다면 [바이러스 검사](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/virus-detector/description)(2015, 입문)로 한 번 더 확인한다.

## 2. 격자 구현

- [ ] [Trail 2 · 격자 위의 편안한 상태](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-comfortable-state-on-the-grid/description) → `dx/dy`, 범위 검사, 칸의 상태 기록.
- [ ] [Trail 4 · 행복한 수열의 개수](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-number-of-happy-sequence/description) → 행과 열을 각각 검사하고 연속 길이를 센다.
- [ ] [Trail 4 · Simulation](https://www.codetree.ai/trail-info/intermediate-low/) → **격자 안에서 단일 객체를 이동** 연습 1개. 이동 전 좌표와 방향을 표로 추적한다.

**통과 기준** · 작은 격자에서 3턴을 손으로 추적하고 코드의 위치·방향과 일치시킨다. 한 칸 검사와 전체 격자 순회의 반복 횟수를 비교한다.

**기출** · [자율주행 자동차](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/autonomous-driving/description)(2017, 기본). 한 번 방문한 칸과 벽, 방향 변경을 따로 검사한다.

## 3. BFS와 자료구조

- [ ] [Trail 3 · 스택, 큐, 덱](https://www.codetree.ai/trail-info/novice-high/) → **Queue** 연습 1개. `deque.append`와 `popleft`로 선입선출을 재현하고 Stack과 비교한다.
- [ ] [Trail 4 · BFS](https://www.codetree.ai/trail-info/intermediate-low/) → **BFS 탐색** 연습 1개. 방문 가능한 칸의 집합 또는 연결 요소를 구한다.
- [ ] [Trail 4 · BFS](https://www.codetree.ai/trail-info/intermediate-low/) → **가중치가 동일한 그래프에서의 BFS** 연습 1개. 도달 불가와 최단거리 결과를 구분한다.

**통과 기준** · 큐에 넣는 시점에 방문 표시를 하고, 막힌 격자와 시작점이 곧 목적지인 격자를 직접 테스트한다.

**기출** · [토스트 계란틀](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/toast-eggmold/description)(2018, 기본). 한 그룹을 찾는 로직과 하루 종료 판정을 나눠 검증한다.

## 4. 재귀와 백트래킹

- [ ] [Trail 2 · 재귀함수](https://www.codetree.ai/trail-info/novice-mid/) → **값을 반환하는 재귀함수** 연습 1개. 종료 조건과 반환값을 손으로 추적한다.
- [ ] [Trail 4 · Backtracking](https://www.codetree.ai/trail-info/intermediate-low/) → **N개 중에 M개 고르기(Simple)** 연습 1개. 중복 없는 후보를 만들고 선택을 복원한다.

**통과 기준** · 4개 중 2개 조합이 6개인지 확인하고, 재귀 호출마다 무엇이 바뀌고 복원되는지 설명한다.

**기출** · [외주 수익 최대화하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/max-of-outsourcing-profit/description)(2017, 기본). 날짜별 선택·건너뛰기와 기간 초과 조건을 점검한다.

## 5. 여러 규칙 합치기

- [ ] [Trail 2 · 정렬](https://www.codetree.ai/trail-info/novice-mid/) → **객체 정렬** 연습 1개. `key`에 튜플을 써서 주 기준과 동률 기준을 테스트한다.
- [ ] [Trail 4 · Simulation](https://www.codetree.ai/trail-info/intermediate-low/) → **격자 안에서 터지고 떨어지는 경우** 연습 1개. 제거할 위치를 먼저 확정하고 갱신을 단계별로 확인한다.
- [ ] [Trail 4 · 금 채굴하기](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-gold-mining/description) → 격자의 후보 위치와 범위를 비교한다. 이어 3×3 격자를 90도 회전하는 함수를 따로 확인한다.

**통과 기준** · 규칙을 함수 단위로 적고, 회전 결과와 갱신 전후 상태를 작은 입력으로 검증한다.

**기출** · [메이즈 러너](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/maze-runner/description)(2023, 응용) → [고대 문명 유적 탐사](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ancient-ruin-exploration/description)(2024, 응용). 후자는 회전 후보 비교와 BFS를 합치는 연습이다.

## 6. 최근 기출과 모의시험

- [ ] 1~5단계에서 힌트를 받거나 틀렸던 트레일 문제 1개를 새 파일에서 재풀이한다.
- [ ] [택배 하차](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/delivery-service/description)(2025, 응용)를 시간을 재며 푼다. 실전처럼 제출 전에 최소 입력과 경계 입력을 확인한다.
- [ ] 아직 문제를 열어보지 않은 상태에서 2026 하반기 오후 [호수의 물결](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/wave-of-lake/description)과 [식량 보급](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/commissariat/description)을 실제 시험 안내 시간에 맞춰 모의로 푼다. 시작 10분 동안 두 문제를 읽고 먼저 완성할 문제를 정한다. 이미 본 회차라면 [기출 목록](PROBLEMS.md)에서 다른 최근 회차를 고른다.
- [ ] 풀이 순서, 첫 실패 원인, 다음에 먼저 검사할 반례를 기록한다. 시간이 남으면 모의에서 부족했던 정렬·누적합·이진탐색 또는 힙 중 하나를 트레일에서 보강한다.

## 회차 운영

처음 15분은 개념과 손 추적, 다음 30~50분은 풀이, 마지막 10~15분은 테스트와 기록에 쓴다. 단원명으로 적은 항목은 해당 단원의 Challenge나 Test 한 문항을 골라 링크를 [진도](PROGRESS.md)에 남긴다. 막힌 문제는 힌트 하나를 받은 뒤 직접 다시 시도하고, 다음날 빈 파일에서 재풀이한다. 시간이 밀리면 필수 트레일과 최근 모의 한 세트를 우선하고, 5단계의 기출은 한 문제로 줄인다.
