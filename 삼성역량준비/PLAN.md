# 삼성 SW 역량테스트 30일 로드맵

하루 5~6시간, Day 1을 실제 시작일로 잡는다. 트레일에서 개념과 Python 구현을 연습하고, 그날 같은 개념이 들어간 기출을 1문제씩 푼다. 기출 2번은 선택으로 표시했으며, Day 29 모의에서는 두 문제를 모두 본다. 복습일에도 트레일과 기출을 각각 다시 푼다.

[기출 83문제와 유형](PROBLEMS.md) · [진도 기록](PROGRESS.md) · [ChatGPT 시작 프롬프트](CHAT.md) · [풀이 저장법](solutions/README.md)

## 하루 5시간 15분

| 시간 | 할 일 |
| --- | --- |
| 45분 | 개념 공부와 손 추적. 오늘 쓸 자료구조, 상태, 복잡도를 적는다. |
| 90분 | 표의 트레일 1~2문제. 먼저 독립 풀이하고 제출한다. |
| 100분 | 기출 1번 독립 시도. 읽기·설계 15분, 구현 60분, 테스트 25분을 기준으로 한다. |
| 50분 | 기출 2번을 시도하거나 1번의 실패 원인부터 고친다. 6시간이 가능하면 이 구간에 최대 45분을 추가한다. |
| 30분 | 반례, 소요 시간, 힌트 사용 여부와 다음 재풀이 날짜를 TIL에 기록한다. |

트레일에서 개념이 막히면 25~30분 독립 시도 후 ChatGPT에 힌트 하나를 요청한다. 기출 1번을 시간 안에 못 끝냈다면 실패한 함수나 작은 부분을 완성하고 다음 복습일에 이어서 푼다. Day 7·14·21·28은 재풀이 위주로 운영하며, 목표를 끝내면 남은 시간을 쉬거나 밀린 문제에 쓴다. 모의시험은 실제 응시 안내의 제한 시간으로 운영한다.

## 일자별 트레일과 기출

T1~T5는 코드트리 트레일 번호다. 링크에 적힌 카드 제목과 소속 트레일은 코드트리 CLI 조회로 확인했다. 열람 및 제출 가능 범위는 로그인과 이용권에 따라 달라질 수 있다.

### 1주차 · Python과 시뮬레이션

| 일자 | 학습 주제 | 코드트리 트레일 먼저 | 삼성 기출 | 확인할 것 |
| --- | --- | --- | --- | --- |
| Day 1 | Python 진단과 직사각형 격자 | T1 [두 개의 격자 비교하기](https://www.codetree.ai/ko/trails/complete/curated-cards/test-compare-two-grid/description)<br>T2 [그 계절, 그 날](https://www.codetree.ai/ko/trails/complete/curated-cards/test-that-season-that-day/description) | [바이러스 검사](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/virus-detector/description) (2015, L4) | 격자 입력·상하좌우를 20분 안에 작성하고 모서리와 1×1 확인. 이미 익숙하면 함수 문제는 복습만. |
| Day 2 | 방향 벡터와 회전 | T2 [격자 위의 편안한 상태](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-comfortable-state-on-the-grid/description)<br>T2 [되돌아오기](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-come-back/description) | [자율주행 자동차](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/autonomous-driving/description) (2017, L11) | 벽·경계·후진을 각각 테스트. |
| Day 3 | 격자 완전탐색과 모양 | T4 [행복한 수열의 개수](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-number-of-happy-sequence/description)<br>T4 [트로미노](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-tromino/description) | [자율주행 자동차](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/autonomous-driving/description) (2017, L11 · 재풀이)<br>[테트리스 블럭 안의 합 최대화 하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/max-sum-of-tetris-block/description) (2017, L12 · 선택) | 후보 개수와 각 후보의 검사 비용을 계산. |
| Day 4 | 원형 배열과 회전 순서 | T4 [삼각형 컨베이어 벨트](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-conveyor-belt-triangle/description)<br>T2 [좌우로 움직이는 로봇](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-robot-moving-from-side-to-side/description) | [불안한 무빙워크](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/unstable-moving-walk/description) (2020, L11) | 회전 직후와 이동 직후를 출력해 비교. |
| Day 5 | 단일 객체의 상태 | T4 [주사위 던지기](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-roll-a-dice/description) | [정육면체 굴리기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/cube-rounding/description) (2016, L12) | 좌표와 주사위 면을 따로 검증. |
| Day 6 | 여러 객체와 일괄 갱신 | T4 [수의 순차적 이동](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-sequential-movement-of-numbers/description)<br>T4 [벽이 있는 충돌 실험](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-collision-experiment-with-wall/description) | [나무 타이쿤](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/tree-tycoon/description) (2021, L11)<br>[원자 충돌](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/atom-collision/description) (2020, L12 · 선택) | 2번은 선택. 갱신 순서와 모듈러 좌표 확인. |
| Day 7 | 1주차 복습 | 재풀이 T2 [격자 위의 편안한 상태](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-comfortable-state-on-the-grid/description)<br>재풀이 T4 [트로미노](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-tromino/description) | [불안한 무빙워크](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/unstable-moving-walk/description) (2020, L11 · 재풀이) | 힌트 없이 한 턴을 재구현하고 원형 인덱스 반례 기록. |

### 2주차 · BFS, DFS와 백트래킹

| 일자 | 학습 주제 | 코드트리 트레일 먼저 | 삼성 기출 | 확인할 것 |
| --- | --- | --- | --- | --- |
| Day 8 | 큐·BFS·연결 요소 | T3 [스택 vs 큐](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-stack-versus-queue/description)<br>T4 [갈 수 있는 곳들](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-places-can-go/description) | [토스트 계란틀](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/toast-eggmold/description) (2018, L11) | 큐에 넣을 때 방문 처리하고 하루 종료 조건을 확인. |
| Day 9 | 최단거리와 동률 | T4 [나이트](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-knight-movements/description)<br>T2 [키, 몸무게를 기준으로 정렬](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-sort-by-height-and-weight/description) | [전투 로봇](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/fighting-robot/description) (2018, L13) | 최단거리 후보 여러 개의 행·열 동률 테스트. |
| Day 10 | DFS와 연결 구역 | T4 [마을 구분하기](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-seperate-village/description)<br>재풀이 T4 [갈 수 있는 곳들](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-places-can-go/description) | [정육면체 한번 더 굴리기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/cube-rounding-again/description) (2021, L13) | 격자 연결 요소를 DFS와 BFS로 비교하고 점수만 먼저 검증. |
| Day 11 | 조합과 상태 탐색 | T2 [Factorial](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-factorial/description)<br>T4 [XOR 결과 최대 만들기](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-max-of-xor/description) | [외주 수익 최대화하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/max-of-outsourcing-profit/description) (2017, L8)<br>[병원 거리 최소화하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/min-of-hospital-distance/description) (2018, L11 · 선택) | 2번은 선택. 선택·건너뛰기와 조합 열거를 비교. |
| Day 12 | 재귀 복원과 가지치기 | T4 [거꾸로 순열](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-backward-permutation/description)<br>T4 [1차원 윷놀이](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-yutnori-1d/description) | [연산자 배치하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/arrange-operator/description) (2017, L10) | 연산자 개수 복원과 음수 나눗셈 확인. |
| Day 13 | 조합과 다중 시작점 BFS | 재풀이 T4 [XOR 결과 최대 만들기](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-max-of-xor/description)<br>T4 [상한 귤](https://www.codetree.ai/ko/trails/complete/curated-cards/test-oranges-have-gone-bad/description) | [방화벽 설치하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/firewall-installation/description) (2017, L12)<br>[바이러스 백신](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/vaccine-for-virus/description) (2019, L12 · 선택) | 2번은 선택. 후보 조합과 BFS 비용을 따로 계산. |
| Day 14 | 2주차 복습 | 재풀이 T4 [갈 수 있는 곳들](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-places-can-go/description)<br>재풀이 T4 [XOR 결과 최대 만들기](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-max-of-xor/description) | [토스트 계란틀](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/toast-eggmold/description) (2018, L11 · 재풀이) | 해설 없이 재풀이한 뒤 처음 틀린 입력을 다시 제출. |

### 3주차 · 복합 구현, DP, 누적합, 힙

| 일자 | 학습 주제 | 코드트리 트레일 먼저 | 삼성 기출 | 확인할 것 |
| --- | --- | --- | --- | --- |
| Day 15 | 빈도 집계·정렬 | T5 [대응되는 수와 문자](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-corresponding-numbers-and-characters/description)<br>T2 [키, 몸무게를 기준으로 정렬](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-sort-by-height-and-weight/description) | [격자 숫자 놀이](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/matrix-number-play/description) (2019, L12) | dict 집계와 정렬 키를 분리하고 행·열 변환 확인. |
| Day 16 | 회전 영역과 우선순위 | T4 [금 채굴하기](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-gold-mining/description)<br>T4 [기울어진 직사각형](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-slanted-rectangle/description) | [메이즈 러너](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/maze-runner/description) (2023, L13) | 회전 전후 좌표 변환을 따로 테스트. |
| Day 17 | 삭제·낙하·연쇄 처리 | T4 [십자 모양 폭발](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-cross-shape-bomb/description)<br>T4 [십자 모양의 지속적 폭발](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-cross-shape-continuous-bomb/description) | [고대 문명 유적 탐사](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ancient-ruin-exploration/description) (2024, L12) | 후보 평가와 실제 반영을 분리. |
| Day 18 | DP 기초와 전처리 | T4 [계단 오르기](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-climbing-stairs/description)<br>T4 [알바로 부자 되기](https://www.codetree.ai/ko/trails/complete/curated-cards/test-being-rich-by-working-part-time/description) | [외주 수익 최대화하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/max-of-outsourcing-profit/description) (2017, L8 · 재풀이)<br>[코디의 향수 공방](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/perfume-workshop/description) (2026, L13 · 선택) | 1번을 DP로 다시 풀고 상태와 전이 설명. 2번은 선택. |
| Day 19 | 누적합·이진탐색 | T5 [구간에 속한 문자의 개수](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-the-number-of-characters-in-the-interval/description)<br>T5 [범위 내에 있는 점의 수 2](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-the-number-of-points-within-the-range-2/description) | [식량 보급](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/commissariat/description) (2026, L13) | 정렬·누적합·경계 탐색을 따로 검증. 최종 모의는 다른 회차 사용. |
| Day 20 | 힙과 우선순위 | T5 [배열 추출](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-array-extraction/description)<br>T5 [자주 등장한 top K 숫자](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-top-k-frequent-elements/description) | [해적 선장 코디](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/pirate-captain-coddy/description) (2025, L14) | heapq 튜플의 동률과 갱신 처리 확인. |
| Day 21 | 3주차 복습 | 재풀이 T4 [알바로 부자 되기](https://www.codetree.ai/ko/trails/complete/curated-cards/test-being-rich-by-working-part-time/description)<br>재풀이 T5 [구간에 속한 문자의 개수](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-the-number-of-characters-in-the-interval/description) | [고대 문명 유적 탐사](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ancient-ruin-exploration/description) (2024, L12 · 재풀이) | 회전 또는 연쇄 갱신 중 실패한 부분부터 재현. |

### 4주차 · 심화 유형과 최신 구현

| 일자 | 학습 주제 | 코드트리 트레일 먼저 | 삼성 기출 | 확인할 것 |
| --- | --- | --- | --- | --- |
| Day 22 | 가중 그래프와 다익스트라 | T5 [최단 거리 3](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-shortest-distance-3/description)<br>재풀이 T5 [배열 추출](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-array-extraction/description) | [개구리의 여행](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/frog-journey/description) (2025, L13)<br>[코드트리 투어](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-tour/description) (2024, L14 · 선택) | 2번은 선택. 상태 정의와 오래된 힙 항목 처리 점검. |
| Day 23 | 판정 함수와 매개변수 탐색 | T5 [최소 통과 시간](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-minimum-transit-time/description) | [여왕 개미](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/queen-ant/description) (2025, L13) | 가능 여부가 단조인지 설명하고 경계에서 검사. |
| Day 24 | 연결 관계와 빠른 이동 | T5 [새치기](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-cut-in-line/description)<br>재풀이 T5 [대응되는 수와 문자](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-corresponding-numbers-and-characters/description) | [산타의 선물 공장 2](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/santa-gift-factory-2/description) (2022, L16) | 머리·꼬리·빈 목록을 테스트. 심화 문제 첫 시도는 구현 또는 부분 구현까지. |
| Day 25 | DP와 투 포인터 | T5 [연속하는 정수 N개의 합](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-sum-of-consecutive-n-integers/description)<br>T4 [숫자 전쟁](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-number-war/description) | [코디의 보석 공방](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/jewel-workshop/description) (2026, L13) | 윈도우 조건과 DP 상태를 각각 적는다. |
| Day 26 | 최신 격자 구현 | T4 [쌓인 수들의 순차적 이동](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-sequential-movement-of-stacked-numbers/description)<br>재풀이 T4 [기울어진 직사각형](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-slanted-rectangle/description) | [택배 하차](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/delivery-service/description) (2025, L12) | 객체 제거 순서와 경계 반례를 만든다. |
| Day 27 | BFS와 상태 갱신 종합 | T4 [돌 잘 치우기](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-clear-stones-well/description)<br>재풀이 T2 [키, 몸무게를 기준으로 정렬](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-sort-by-height-and-weight/description) | [AI 로봇청소기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ai-robot/description) (2025, L13)<br>[미생물 연구](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/microbial-research/description) (2025, L13 · 선택) | 2번은 선택. 우선순위와 그룹 갱신 중 약한 쪽에 집중. |
| Day 28 | 모의 전 복습 | 재풀이 T5 [배열 추출](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-array-extraction/description)<br>재풀이 T4 [벽이 있는 충돌 실험](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-collision-experiment-with-wall/description) | [메이즈 러너](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/maze-runner/description) (2023, L13 · 재풀이) | 회전 함수와 동률 반례를 빈 파일에서 다시 작성. |

### 최종 모의와 복기

| 일자 | 학습 주제 | 코드트리 트레일 먼저 | 삼성 기출 | 확인할 것 |
| --- | --- | --- | --- | --- |
| Day 29 | 최근 회차 모의 | 재풀이 T2 [격자 위의 편안한 상태](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-comfortable-state-on-the-grid/description) | [수하물 컨베이어 벨트](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/baggage-conveyor-belt/description) (2026, L13)<br>[코디의 퍼즐 공방](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/cody-puzzle-workshop/description) (2026, L13) | 트레일은 짧게 풀고 별도 시험 시간을 잰다. 2026 하반기 오전 두 문제를 함께 시작. |
| Day 30 | 실전 복기 | 재풀이 T4 [갈 수 있는 곳들](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-places-can-go/description)<br>재풀이 T5 [구간에 속한 문자의 개수](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-the-number-of-characters-in-the-interval/description)<br>둘 중 오답 유형에 맞는 한 문제를 고른다. | Day 29 미완료 또는 가장 오래 걸린 기출 1문제 재풀이 | 첫 실패 원인, 반례, 시험 당일 점검 순서를 기록. |

## 난도와 순서 조정

- Day 1에 격자 입력과 4방향 범위 검사를 독립적으로 통과하면 첫날 복습 구간을 줄이고 Day 2의 방향 문제를 당겨도 된다.
- 구현·BFS·백트래킹을 앞에 두고, 최근 기출에서 확인된 DP·투 포인터·누적합·이진탐색·힙을 3~4주차에 배치했다. 다익스트라, 매개변수 탐색, 연결 리스트는 해당 기출을 직접 읽고 한 번 시도할 수 있도록 시간을 따로 잡았다.
- Day 29 오전 세트를 이미 봤다면 같은 해 오후의 식량 보급도 Day 19에서 풀었으므로, [기출 목록](PROBLEMS.md)에서 미열람 최근 회차를 고른다.
- 트리 DP와 세그먼트 트리는 필수 일정에서 뺐다. 핵심 일정 이후 여유가 생기면 T6 [트리의 부모 노드](https://www.codetree.ai/ko/trails/complete/curated-cards/intro-parent-node-of-the-tree/introduction)로 트리 구조를 익히고, 기출 목록의 색깔 트리 또는 코드트리 DB를 읽어 필요한 자료구조를 확인한다.

[코드트리 트레일](https://www.codetree.ai/trail-info) · [공개 기출 목록](https://www.codetree.ai/ko/frequent-problems)
