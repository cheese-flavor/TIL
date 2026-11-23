# 삼성 SW 역량테스트 — Day 6~19 집중 커리큘럼

**적용 계획:** 기존 30일 계획의 Day 1~5 및 코드·기록은 그대로 유지. Day 6부터 새롭게 14일간 운영. 실제 달력 날짜는 Day 6 채팅에서 기록.

## 목표와 범위

- 기준 [삼성 기출 83문제](PROBLEMS.md) 중 기존 [30일 계획](PLAN.md)의 Day 1~5에 이미 배정된 **15문제 제외**. 새로운 14일 과정에 **68문제 전부 1회씩 배정**.
- 이전에 배정됐지만 미해결인 문제는 정답으로 간주하지 않음. 기존 Day 1~5 문제·파일·대화는 유지하고 이월 목록으로 분리.
- **ChatGPT 프로젝트의 채팅 하나 = Day 하나.** 해당 날짜의 Trail 기본 1문제 + 삼성 기출 4~5문제.
- 목표는 68문제 **모두 직접 시도하고 풀이 과정을 학습하는 것**. 68개 전부 시간 내 독립 정답은 보장되지 않으므로 **실제 CodeTree 정답**과 **도움 후 정답**, **부분 구현/개념 이해**를 구분.
- Day 19에는 [2026년 하반기 오전 1·2번 기출](https://www.codetree.ai/ko/frequent-problems)을 실제 시험과 같이 4시간으로 묶어 시도.

## 매일 시간 운영

| 세션 | Trail 기본 | 기출 대표 1번 | 나머지 기출 | 기록 | 총합 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 기출 5문제 | 25분 | 실전형 120분 | 동행형 40분 × 4 | 20분 | **325분 (5시간 25분)** |
| 기출 4문제 | 25분 | 실전형 120분 | 동행형 55분 × 3 | 20분 | **330분 (5시간 30분)** |
| Day 19 | 15분 | 모의 120분 × 2 | 동행형 25분 × 3 | 15분 | **345분 (5시간 45분)** |

**실전형 120분**: 문제 해석·설계(15분) → 독립 풀이 **최대 60분**(L14 이상은 25~40분부터 막힌 지점 점검) → 남은 시간 ChatGPT와 단계별 구현·검증. 정답을 일찍 얻으면 다음 문제로 이동.
**동행형 40분**: 독립 10~15분 + ChatGPT와 설계·핵심 함수·반례 25~30분. **동행형 55분**: 독립 15~20분 + 동행 35~40분.
**모의 120분 × 2**: 합계 4시간 동안 ChatGPT 힌트·해설 없이 실전처럼 진행. 남는 3문제는 빠른 설계·동행(각 25분)이며 정답 코드 완성까지 보장하는 시간은 아님.
시간이 끝났으면 미완료 부분과 다음 시도를 기록하고 이동. L15~L19의 어려운 문제는 제한 시간 내 정답이 어려울 수 있으므로 **실전 통과/동행 통과/부분 구현/이해만 완료/미해결/미시도**로 정확히 구분.

## 14일 요약

| Day | 유형 | 기출 수 | 대표 실전 문제 |
| --- | --- | ---: | --- |
| [Day 6](#day-6) | 다중 객체·동시 갱신 | 5 | [나무 타이쿤](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/tree-tycoon/description) |
| [Day 7](#day-7) | 방향·회전·격자 변환 | 5 | [드래곤 커브](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/dragon-curve/description) |
| [Day 8](#day-8) | BFS·연결 요소·다중 출발점 | 4 | [토스트 계란틀](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/toast-eggmold/description) |
| [Day 9](#day-9) | BFS 최단거리·동률 처리 | 5 | [전투 로봇](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/fighting-robot/description) |
| [Day 10](#day-10) | 백트래킹 기본·조합 | 5 | [외주 수익 최대화하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/max-of-outsourcing-profit/description) |
| [Day 11](#day-11) | 고난도 백트래킹·상태 복사 | 5 | [이상한 체스](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/odd-chess/description) |
| [Day 12](#day-12) | 연쇄 충돌·객체 상태 | 5 | [왕실의 기사 대결](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/royal-knight-duel/description) |
| [Day 13](#day-13) | 복잡한 시뮬레이션·중력·확산 | 5 | [색깔 폭탄](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/colored-bomb/description) |
| [Day 14](#day-14) | 격자 BFS·회전 복합 구현 | 4 | [고대 문명 유적 탐사](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ancient-ruin-exploration/description) |
| [Day 15](#day-15) | 정렬·우선순위·이벤트 | 5 | [격자 숫자 놀이](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/matrix-number-play/description) |
| [Day 16](#day-16) | 다익스트라·힙·우선순위 큐 | 5 | [개구리의 여행](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/frog-journey/description) |
| [Day 17](#day-17) | 연결 리스트·트리·세그먼트 트리 | 5 | [산타의 선물 공장](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/santa-gift-factory/description) |
| [Day 18](#day-18) | DP·누적합·이진/매개변수 탐색 | 5 | [여왕 개미](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/queen-ant/description) |
| [Day 19](#day-19) | 2026 최신 기출 4시간 모의·복기 | 5 | [수하물 컨베이어 벨트](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/baggage-conveyor-belt/description) |

## Day별 세부 문제와 개별 제한 시간

### Day 6 — 다중 객체·동시 갱신

**Trail 기본 1문제 (25분)**: Trail 4 · 1-5 격자 안에서 여러 객체를 이동 · [벽이 있는 충돌 실험](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-collision-experiment-with-wall/description)

**학습 질문:** 각 객체 이동 중 이전 객체 갱신값을 참조하면 왜 문제가 생기는가?

| 순서 | 삼성 기출(연도) | 레벨 | 제한 시간 | 집중 학습 요소 |
| --- | --- | --- | --- | --- |
| 1 | [나무 타이쿤](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/tree-tycoon/description) (2021) | L11 | **실전 120분** | 순환 좌표 이동, 대각선 이웃, 턴별 상태 |
| 2 | [원자 충돌](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/atom-collision/description) (2020) | L12 | 동행 40분 | 토러스 격자, 방향 벡터, 충돌 후 합치기 |
| 3 | [시공의 돌풍](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/heros-of-storm/description) (2019) | L12 | 동행 40분 | 격자 확산, 새 배열에 동시 반영, 경로 추적 |
| 4 | [나무박멸](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/tree-kill-all/description) (2022) | L12 | 동행 40분 | 동시 성장·번식, 대각선 범위, 수명 관리 |
| 5 | [종전](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/war-finish/description) (2019) | L13 | 동행 40분 | 격자 구역 경계, 후보 열거, 구역 합 비교 |

### Day 7 — 방향·회전·격자 변환

**Trail 기본 1문제 (25분)**: Trail 4 · 1-1 격자 안에서 완전탐색 · [기울어진 직사각형](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-slanted-rectangle/description)

**학습 질문:** 회전 전후의 좌표·상태를 분리하여 검증할 수 있는가?

| 순서 | 삼성 기출(연도) | 레벨 | 제한 시간 | 집중 학습 요소 |
| --- | --- | --- | --- | --- |
| 1 | [드래곤 커브](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/dragon-curve/description) (2018) | L12 | **실전 120분** | 방향 목록 역순 확장, 회전, 격자 표시 |
| 2 | [정육면체 한번 더 굴리기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/cube-rounding-again/description) (2021) | L13 | 동행 40분 | 주사위 면 추적, BFS 연결 요소, 방향 전환 |
| 3 | [회전하는 빙하](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/rotating-glacier/description) (2020) | L13 | 동행 40분 | 부분 격자 회전, 동시 갱신, BFS 연결 요소 |
| 4 | [예술성](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/artistry/description) (2022) | L13 | 동행 40분 | BFS 그룹 라벨, 접촉 변 개수, 부분 회전 |
| 5 | [2048 게임](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/2048-game/description) (2016) | L14 | 동행 40분 | 방향별 밀기, 한 번만 합치기, 상태 복사 |

### Day 8 — BFS·연결 요소·다중 출발점

**Trail 기본 1문제 (25분)**: Trail 4 · 4-1 BFS 탐색 · [갈 수 있는 곳들](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-places-can-go/description)

**학습 질문:** 방문 처리는 언제 하고 하루 단위의 그룹 갱신은 언제 적용하는가?

| 순서 | 삼성 기출(연도) | 레벨 | 제한 시간 | 집중 학습 요소 |
| --- | --- | --- | --- | --- |
| 1 | [토스트 계란틀](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/toast-eggmold/description) (2018) | L11 | **실전 120분** | 조건부 인접 BFS, 연결 요소, 하루 단위 갱신 |
| 2 | [민트 초코 우유](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/mint-choco-milk/description) (2025) | L12 | 동행 55분 | BFS 그룹, 대표 정렬, 전파 순서 |
| 3 | [미생물 연구](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/microbial-research/description) (2025) | L13 | 동행 55분 | BFS 연결성, 격자 배치, 순서와 인접 관계 |
| 4 | [바이러스 백신](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/vaccine-for-virus/description) (2019) | L12 | 동행 55분 | 시작점 조합, 다중 시작점 BFS, 빈칸 도달 시간 |

### Day 9 — BFS 최단거리·동률 처리

**Trail 기본 1문제 (25분)**: Trail 4 · 4-2 가중치가 동일한 그래프에서의 BFS · [나이트](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-knight-movements/description)

**학습 질문:** 거리 동률에서 행·열 또는 지정된 우선순위를 어떻게 보장하는가?

| 순서 | 삼성 기출(연도) | 레벨 | 제한 시간 | 집중 학습 요소 |
| --- | --- | --- | --- | --- |
| 1 | [전투 로봇](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/fighting-robot/description) (2018) | L13 | **실전 120분** | BFS 최단거리, 행·열 동률 처리, 크기 갱신 |
| 2 | [코드트리 빵](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-mon-bread/description) (2022) | L14 | 동행 40분 | BFS 최단거리, 동률 처리, 통행 금지 갱신 시점 |
| 3 | [AI 로봇청소기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ai-robot/description) (2025) | L13 | 동행 40분 | BFS 도달 거리, 우선순위, 격자 상태 |
| 4 | [자율주행 전기차](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/autonomous-electric-car/description) (2020) | L14 | 동행 40분 | BFS 목적지 선택, 거리·좌표 동률, 연료 갱신 |
| 5 | [미지의 공간 탈출](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/escape-unknown-space/description) (2024) | L14 | 동행 40분 | 여러 면의 좌표 변환, 시간 제약, BFS |

### Day 10 — 백트래킹 기본·조합

**Trail 기본 1문제 (25분)**: Trail 4 · 2-3 N개 중에 M개 고르기(Simple) · [XOR 결과 최대 만들기](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-max-of-xor/description)

**학습 질문:** 선택/미선택 재귀 분기와 상태 복원은 어떻게 구현하는가?

| 순서 | 삼성 기출(연도) | 레벨 | 제한 시간 | 집중 학습 요소 |
| --- | --- | --- | --- | --- |
| 1 | [외주 수익 최대화하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/max-of-outsourcing-profit/description) (2017) | L8 | **실전 120분** | 날짜별 선택·건너뛰기, 종료 조건 |
| 2 | [조삼모사](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/three-at-dawn-and-four-at-dusk/description) (2017) | L9 | 동행 40분 | 절반 선택 조합, 선택 집합과 보집합 비교 |
| 3 | [병원 거리 최소화하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/min-of-hospital-distance/description) (2018) | L11 | 동행 40분 | 시설 조합, 맨해튼 거리, 최소합 |
| 4 | [연산자 배치하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/arrange-operator/description) (2017) | L10 | 동행 40분 | 연산자 개수로 분기, 재귀 복원, 음수 나눗셈 |
| 5 | [방화벽 설치하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/firewall-installation/description) (2017) | L12 | 동행 40분 | 벽 후보 조합, 상태 복원, 다중 시작점 BFS |

### Day 11 — 고난도 백트래킹·상태 복사

**Trail 기본 1문제 (25분)**: Trail 4 · 2-4 순열 만들기 · [거꾸로 순열](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-backward-permutation/description)

**학습 질문:** 분기마다 어떤 상태를 복구해야 하며 가지치기는 언제 가능한가?

| 순서 | 삼성 기출(연도) | 레벨 | 제한 시간 | 집중 학습 요소 |
| --- | --- | --- | --- | --- |
| 1 | [이상한 체스](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/odd-chess/description) (2018) | L12 | **실전 120분** | 방향별 감시 범위, 후보 조합, 격자 복원 |
| 2 | [디버깅](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/debugging/description) (2018) | L13 | 동행 40분 | 후보 선택, 열별 연속 구간 검사, 가지치기 |
| 3 | [2개의 사탕](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/two-candies/description) (2015) | L15 | 동행 40분 | 두 객체의 좌표 상태, 벽·구멍, 이동 횟수 제한 |
| 4 | [윷놀이 사기단](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/woodstick-fraud/description) (2019) | L14 | 동행 40분 | 분기 경로, 말의 위치 상태, 선택·복원 |
| 5 | [술래잡기 체스](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/odd-chess2/description) (2020) | L14 | 동행 40분 | 객체 순서에 따른 이동, 재귀 상태 복사 |

### Day 12 — 연쇄 충돌·객체 상태

**Trail 기본 1문제 (25분)**: Trail 4 · 1-5 격자 안에서 여러 객체를 이동 · [수의 순차적 이동](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-sequential-movement-of-numbers/description)

**학습 질문:** 다른 객체에 이동이 전파될 때 가능 여부와 일괄 반영을 어떻게 분리하는가?

| 순서 | 삼성 기출(연도) | 레벨 | 제한 시간 | 집중 학습 요소 |
| --- | --- | --- | --- | --- |
| 1 | [왕실의 기사 대결](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/royal-knight-duel/description) (2023) | L13 | **실전 120분** | 직사각형 충돌 전파, 이동 가능성 검사, 일괄 적용 |
| 2 | [승자독식 모노폴리](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/odd-monopoly/description) (2020) | L14 | 동행 40분 | 방향 우선순위, 냄새 수명, 동시 이동·충돌 |
| 3 | [싸움땅](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/battle-ground/description) (2022) | L14 | 동행 40분 | 객체별 상태, 충돌과 이동 우선순위, 칸별 장비 |
| 4 | [루돌프의 반란](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/rudolph-rebellion/description) (2023) | L14 | 동행 40분 | 거리와 동률, 연쇄 충돌, 기절 상태 |
| 5 | [꼬리잡기놀이](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/tail-catch-play/description) (2022) | L15 | 동행 40분 | 팀 경로 추적, 순서 관리, 방향 반전 |

### Day 13 — 복잡한 시뮬레이션·중력·확산

**Trail 기본 1문제 (25분)**: Trail 4 · 1-3 격자 안에서 터지고 떨어지는 경우 · [십자 모양의 지속적 폭발](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-cross-shape-continuous-bomb/description)

**학습 질문:** 긴 턴을 3~5개의 검증 가능한 함수로 나눌 수 있는가?

| 순서 | 삼성 기출(연도) | 레벨 | 제한 시간 | 집중 학습 요소 |
| --- | --- | --- | --- | --- |
| 1 | [색깔 폭탄](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/colored-bomb/description) (2021) | L14 | **실전 120분** | BFS 그룹 선택, 공용 칸 방문 처리, 중력·회전 |
| 2 | [미로 타워 디펜스](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/maze-tower-defense/description) (2021) | L15 | 동행 40분 | 나선 인덱스, 연속 그룹 제거·압축 |
| 3 | [냉방 시스템](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/cooling-system/description) (2021) | L16 | 동행 40분 | 벽을 고려한 확산, 온도 동시 조절, 여러 단계의 종료 조건 |
| 4 | [팩맨](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/pacman/description) (2021) | L15 | 동행 40분 | 복제, 경로 열거, 시체 수명, 다중 개체 상태 |
| 5 | [Sam의 피자학교](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/sam-pizza-school/description) (2021) | L16 | 동행 40분 | 배열 접기·쌓기, 이웃 간 이동과 재배열 |

### Day 14 — 격자 BFS·회전 복합 구현

**Trail 기본 1문제 (25분)**: Trail 4 · 4-1 BFS 탐색 · [돌 잘 치우기](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-clear-stones-well/description)

**학습 질문:** 후보 평가·탐색·실제 격자 변경이 섞이지 않았는가?

| 순서 | 삼성 기출(연도) | 레벨 | 제한 시간 | 집중 학습 요소 |
| --- | --- | --- | --- | --- |
| 1 | [고대 문명 유적 탐사](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ancient-ruin-exploration/description) (2024) | L12 | **실전 120분** | 회전 후보 비교, BFS 그룹, 제거 후 연쇄 갱신 |
| 2 | [마법의 숲 탐색](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/magical-forest-exploration/description) (2024) | L13 | 동행 55분 | 다중 칸 객체 이동, 출구 조건, BFS |
| 3 | [포탑 부수기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/destroy-the-turret/description) (2023) | L15 | 동행 55분 | 대상 정렬, 순환 격자 BFS 경로 복원, 단계별 피해 |
| 4 | [메두사와 전사들](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/medusa-and-warriors/description) (2024) | L15 | 동행 55분 | BFS 경로, 시야와 가림, 이동 우선순위 |

### Day 15 — 정렬·우선순위·이벤트

**Trail 기본 1문제 (25분)**: Trail 2 · 3-3 객체 정렬 · [키, 몸무게를 기준으로 정렬](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-sort-by-height-and-weight/description)

**학습 질문:** 동률 우선순위와 시간 순 이벤트의 적용 시점을 명확히 했는가?

| 순서 | 삼성 기출(연도) | 레벨 | 제한 시간 | 집중 학습 요소 |
| --- | --- | --- | --- | --- |
| 1 | [격자 숫자 놀이](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/matrix-number-play/description) (2019) | L12 | **실전 120분** | 빈도 집계, 튜플 정렬, 행·열 재구성 |
| 2 | [메이즈 러너](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/maze-runner/description) (2023) | L13 | 동행 40분 | 이동 우선순위, 회전 영역 선택, 좌표 변환 |
| 3 | [택배 하차](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/delivery-service/description) (2025) | L12 | 동행 40분 | 격자 객체 배치, 이동·제거 순서, 경계 검사 |
| 4 | [해적 선장 코디](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/pirate-captain-coddy/description) (2025) | L14 | 동행 40분 | 상태 시뮬레이션, 우선순위 큐와 갱신 |
| 5 | [코드트리 오마카세](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-omakase/description) (2023) | L18 | 동행 40분 | 시간 순 이벤트, 모듈러 좌표, 해시와 정렬 |

### Day 16 — 다익스트라·힙·우선순위 큐

**Trail 기본 1문제 (25분)**: Trail 5 · 1-5 Priority Queue · [배열 추출](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-array-extraction/description)

**학습 질문:** 힙의 오래된 항목과 갱신되는 점수·거리를 어떻게 관리하는가?

| 순서 | 삼성 기출(연도) | 레벨 | 제한 시간 | 집중 학습 요소 |
| --- | --- | --- | --- | --- |
| 1 | [개구리의 여행](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/frog-journey/description) (2025) | L13 | **실전 120분** | 상태를 포함한 가중 그래프, 다익스트라 |
| 2 | [코드트리 투어](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-tour/description) (2024) | L14 | 동행 40분 | 다익스트라, 우선순위 큐, 시작점 변경 |
| 3 | [토끼와 경주](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/rabit-and-race/description) (2023) | L15 | 동행 40분 | 힙과 다중 키, 반사 이동, 점수 누적 |
| 4 | [코드트리 채점기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-judger/description) (2023) | L16 | 동행 40분 | 우선순위 큐, 도메인별 상태, 시각 처리 |
| 5 | [가로등 설치](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/street-light-installation/description) (2025) | L15 | 동행 40분 | 우선순위 큐, 양방향 연결 관계, 이웃 갱신 |

### Day 17 — 연결 리스트·트리·세그먼트 트리

**Trail 기본 1문제 (25분)**: Trail 5 · 1-6 Doubly-LinkedList · [새치기](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-cut-in-line/description)

**학습 질문:** 삽입·삭제·연결 시 머리/꼬리 및 양쪽 포인터를 어떻게 검증하는가?

| 순서 | 삼성 기출(연도) | 레벨 | 제한 시간 | 집중 학습 요소 |
| --- | --- | --- | --- | --- |
| 1 | [산타의 선물 공장](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/santa-gift-factory/description) (2022) | L17 | **실전 120분** | ID 조회, 연결 리스트, 구간 이동 |
| 2 | [산타의 선물 공장 2](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/santa-gift-factory-2/description) (2022) | L16 | 동행 40분 | 양방향 연결 관계, 머리·꼬리, 묶음 이동 |
| 3 | [코드트리 메신저](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-messenger/description) (2023) | L17 | 동행 40분 | 트리와 깊이별 상태, 갱신 전파 |
| 4 | [코드트리 등산 게임](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-mountain-climbing-games/description) (2024) | L18 | 동행 40분 | 세그먼트 트리 활용과 상태 갱신 |
| 5 | [코드트리 DB](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-db/description) (2024) | L19 | 동행 40분 | 키 조회, 동적 세그먼트 트리, 순위·누적합 |

### Day 18 — DP·누적합·이진/매개변수 탐색

**Trail 기본 1문제 (25분)**: Trail 5 · 2-1 Prefix Sum · [구간에 속한 문자의 개수](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-the-number-of-characters-in-the-interval/description)

**학습 질문:** 단조성·누적합 경계·DP 상태와 전이를 구별해 설계하는가?

| 순서 | 삼성 기출(연도) | 레벨 | 제한 시간 | 집중 학습 요소 |
| --- | --- | --- | --- | --- |
| 1 | [여왕 개미](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/queen-ant/description) (2025) | L13 | **실전 120분** | 판정 함수, 이진탐색, 그리디 검사 |
| 2 | [식량 보급](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/commissariat/description) (2026) | L13 | 동행 40분 | 정렬, 누적합, 이진탐색 |
| 3 | [코디의 향수 공방](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/perfume-workshop/description) (2026) | L13 | 동행 40분 | 전처리, DP 상태와 전이 |
| 4 | [코디의 보석 공방](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/jewel-workshop/description) (2026) | L13 | 동행 40분 | DP 상태, 투 포인터로 범위 유지 |
| 5 | [색깔 트리](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/color-tree/description) (2024) | L17 | 동행 40분 | 트리 제약과 서브트리, 색 상태 전파 |

### Day 19 — 2026 최신 기출 4시간 모의·복기

**Trail 기본 1문제 (15분)**: Trail 4 · 4-1 BFS 탐색 (짧은 복습) · [갈 수 있는 곳들](https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-places-can-go/description)

**학습 질문:** 두 문제를 4시간 안에 구현·검증하고 우선순위를 관리하는가?

| 순서 | 삼성 기출(연도) | 레벨 | 제한 시간 | 집중 학습 요소 |
| --- | --- | --- | --- | --- |
| 1 | [수하물 컨베이어 벨트](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/baggage-conveyor-belt/description) (2026) | L13 | **모의 120분** | 단계별 격자 갱신, BFS 탐색 |
| 2 | [코디의 퍼즐 공방](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/cody-puzzle-workshop/description) (2026) | L13 | **모의 120분** | 퍼즐 모서리 표현, 배치 변화와 개수 갱신 |
| 3 | [아기 바다거북의 대모험: 해저 화산 지대](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/a-little-sea-turtles-big-adventure/description) (2026) | L12 | 동행 25분 | 격자 상태 갱신, BFS 탐색 |
| 4 | [아기 고래의 첫 항해](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/baby-whale-first-voyage/description) (2026) | L12 | 동행 25분 | 격자 상태 갱신, BFS 탐색 |
| 5 | [호수의 물결](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/wave-of-lake/description) (2026) | L13 | 동행 25분 | 격자 파동, BFS 전파와 상태 갱신 |

- 모의 첫 두 문제는 2026년 하반기 오전 세트. 다른 3문제는 4시간 종료 후 별도 동행 학습.

## 프로젝트 ChatGPT 학습 규칙

1. **새 채팅 = Day 하나:** 먼저 본 계획에서 당일 Day 행과 [PROGRESS.md](PROGRESS.md)를 열어 진행 중인 문제·과거 미해결 문제를 확인.
2. **문제 안내:** Trail 번호·챕터-레슨·레슨명·문제 제목·직접 링크. 관련 기출의 L레벨과 유형, 문제별 시도 상한 안내.
3. **문제 해결:** 규칙 요약 → 자료구조/상태 정의 → 손 추적 질문 → 독립 코드 작성. 독립 상한 도달 시 작은 힌트 1개부터, 다음에는 의사코드·함수별 공동 구현·완성 코드(요청 시) 순서로 도움.
4. **설명 초점:** '왜 이런 자료구조/순서/상태를 택했는지', 반례와 시간·공간복잡도를 함께 이해. 정답만 복사하지 않음.
5. **Day 종료:** 각 문제의 독립 시도/동행 시도 시간, 코드트리 채점 정답 여부, 사용자 원본 코드, 반례, 다음 재풀이 날짜를 [solutions/](solutions/)의 dayNN와 PROGRESS.md에 기록. 성공적으로 GitHub에 커밋됐는지 확인하고, 실패 시 미반영 사실 고지.
6. **기존 기록 보호:** Day 1~5 폴더와 TIL 루트의 codetree 자동 연동 폴더는 변경하지 않음. 원래의 30일 계획은 과거 계획으로 보존.

## Day 1~5에서 제외된 기존 배정 15문제

| 기존 Day | 제외된 문제(배정 기준, 완료 여부와 다름) |
| --- | --- |
| Day 1 | [바이러스 검사](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/virus-detector/description) |
| Day 2 | [자율주행 자동차](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/autonomous-driving/description) · [돌아가는 팔각 의자](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/rounding-eight-angle/description) · [바이러스 실험](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/virus-experiment/description) |
| Day 3 | [자율주행 자동차](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/autonomous-driving/description) · [테트리스 블럭 안의 합 최대화 하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/max-sum-of-tetris-block/description) · [놀이기구 탑승](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/go-on-the-rides/description) · [2차원 테트리스](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/tetris-2d/description) |
| Day 4 | [불안한 무빙워크](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/unstable-moving-walk/description) · [이상한 다트 게임](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/odd-dart-game/description) · [이상한 윷놀이](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/odd-woodstick-game/description) · [보도블럭](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/crosswalk/description) |
| Day 5 | [정육면체 굴리기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/cube-rounding/description) · [청소는 즐거워](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/cleaning-is-joyful/description) · [술래잡기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/hide-and-seek/description) · [생명과학부 랩 인턴](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/biology-lab-intern/description) |

**배정 검증:** 83 - 15 = **68문제**. Day 6~19 중복 **0건**, 83문제 원목록 대비 누락 **0건**. 실제 독립 정답·도움 후 정답 및 미해결 숫자는 PROGRESS.md에서 따로 관리.
