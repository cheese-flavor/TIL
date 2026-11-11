# 삼성 SW 역량테스트 기출 목록

2026-11-11 코드트리 공개 목록 기준 삼성 기출 83문제. 공식 레벨과 태그는 목록에서 가져왔다. Python 연습 난도와 개념은 공개 태그, 연계 학습, 문제 규칙을 바탕으로 정리한 학습용 판단이다. 전체 제출 코드나 실행시간을 검증한 평가는 아니다. 최근 문제 일부는 공개 태그에서 확인되는 개념 수준으로 적었다.

[코드트리 기출문제](https://www.codetree.ai/ko/frequent-problems) · [코드트리 기출 유형 분석](https://www.codetree.ai/blog/ko/삼성-기출문제로-보는-최근-기업-코딩-테스트-난이도) · [풀이 순서](PLAN.md)

## 연도별 유형

문제 수는 각 연도의 공개 문항 수다. 유형은 복수 집계이며, 기타에는 앞의 네 유형과 함께 붙은 태그도 들어간다.

| 연도 | 문제 수 | 구현 | BFS | 백트래킹 | 우선순위 큐 | 기타 태그와 빈도 |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| [2015](#2015년) | 2 | 1 | 0 | 1 | 0 | Basic 1 |
| [2016](#2016년) | 2 | 2 | 0 | 1 | 0 | — |
| [2017](#2017년) | 8 | 4 | 1 | 4 | 0 | — |
| [2018](#2018년) | 7 | 5 | 2 | 3 | 0 | — |
| [2019](#2019년) | 8 | 6 | 1 | 2 | 0 | Basic 1 |
| [2020](#2020년) | 8 | 6 | 2 | 1 | 0 | Basic 1 |
| [2021](#2021년) | 8 | 8 | 1 | 0 | 0 | — |
| [2022](#2022년) | 8 | 8 | 1 | 0 | 0 | LinkedList 2 |
| [2023](#2023년) | 8 | 8 | 1 | 0 | 2 | DP 1, Exhaustive Search 1, HashMap 1, HashSet 1, Sorting 1, Tree 1 |
| [2024](#2024년) | 8 | 4 | 4 | 0 | 1 | Dijkstra 1, Dynamic Segment Tree 1, Tree DP 1, 태그 미표시 1 |
| [2025](#2025년) | 8 | 5 | 3 | 0 | 2 | Binary Search 1, Dijkstra 1, Doubly Linked List 1, Greedy 1, Parametric Search 1 |
| [2026](#2026년) | 8 | 5 | 4 | 0 | 0 | Binary Search 1, DP 2, Incremental Counting 1, Prefix Sum 1, Preprocessing 1, Sorting 1, Two Pointers 1 |
| 합계 | 83 | 62 | 20 | 12 | 5 | Basic 3, Binary Search 2, DP 3, Dijkstra 2, Doubly Linked List 1, Dynamic Segment Tree 1, Exhaustive Search 1, Greedy 1, HashMap 1, HashSet 1, Incremental Counting 1, LinkedList 2, Parametric Search 1, Prefix Sum 1, Preprocessing 1, Sorting 2, Tree 1, Tree DP 1, Two Pointers 1, 태그 미표시 1 |

## Python 연습 난도

| 난도 | 판단 기준 |
| --- | --- |
| 입문 | 입출력과 계산을 한 번 순회하며 처리 |
| 기본 | 한 가지 핵심 패턴과 관리할 상태가 적은 구현 |
| 응용 | 격자 갱신, 동률, 회전 또는 탐색 등 여러 규칙을 결합 |
| 도전 | 상태 복사·복원이나 여러 객체의 상태 관리가 까다롭거나, 별도 알고리즘·자료구조가 필요 |

난도는 공식 L레벨과 함께 본다. 예를 들어 L11인 **자율주행 자동차**는 좌표와 방향 연습으로, 같은 L11인 **토스트 계란틀**은 BFS와 하루 단위 갱신 연습으로 사용한다.

## 2015년

| 문제 | 회차 | 공식 레벨 | 공개 유형 | Python 연습 난도 | 들어가는 개념 |
| --- | --- | --- | --- | --- | --- |
| [바이러스 검사](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/virus-detector/description) | 하반기 1번 문제 | L4 | Basic | 입문 | 리스트 순회, 올림 나눗셈 |
| [2개의 사탕](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/two-candies/description) | 하반기 2번 문제 | L15 | Backtracking, Simulation | 도전 | 두 객체의 좌표 상태, 벽·구멍, 이동 횟수 제한 |

## 2016년

| 문제 | 회차 | 공식 레벨 | 공개 유형 | Python 연습 난도 | 들어가는 개념 |
| --- | --- | --- | --- | --- | --- |
| [정육면체 굴리기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/cube-rounding/description) | 하반기 1번 문제 | L12 | Simulation | 응용 | 주사위 면의 상태, 방향별 회전, 격자 경계 |
| [2048 게임](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/2048-game/description) | 하반기 2번 문제 | L14 | Backtracking, Simulation | 도전 | 방향별 밀기, 한 번만 합치기, 상태 복사 |

## 2017년

| 문제 | 회차 | 공식 레벨 | 공개 유형 | Python 연습 난도 | 들어가는 개념 |
| --- | --- | --- | --- | --- | --- |
| [테트리스 블럭 안의 합 최대화 하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/max-sum-of-tetris-block/description) | 상반기 오전 1번 문제 | L12 | Simulation | 응용 | 모양과 방향 열거, 격자 합, 경계 |
| [외주 수익 최대화하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/max-of-outsourcing-profit/description) | 상반기 오전 2번 문제 | L8 | Backtracking | 기본 | 날짜별 선택·건너뛰기, 종료 조건 |
| [자율주행 자동차](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/autonomous-driving/description) | 상반기 오후 1번 문제 | L11 | Simulation | 기본 | 격자 좌표, 방향 순환, 방문 상태 |
| [방화벽 설치하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/firewall-installation/description) | 상반기 오후 2번 문제 | L12 | Backtracking, BFS | 응용 | 벽 후보 조합, 상태 복원, 다중 시작점 BFS |
| [조삼모사](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/three-at-dawn-and-four-at-dusk/description) | 하반기 오전 1번 문제 | L9 | Backtracking | 기본 | 절반 선택 조합, 선택 집합과 보집합 비교 |
| [보도블럭](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/crosswalk/description) | 하반기 오전 2번 문제 | L13 | Simulation | 응용 | 경사로 배치, 높이 차, 이미 사용한 칸 |
| [돌아가는 팔각 의자](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/rounding-eight-angle/description) | 하반기 오후 1번 문제 | L11 | Simulation | 응용 | 원형 배열, 회전 전 상태로 전파 판단 |
| [연산자 배치하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/arrange-operator/description) | 하반기 오후 2번 문제 | L10 | Backtracking | 기본 | 연산자 개수로 분기, 재귀 복원, 음수 나눗셈 |

## 2018년

| 문제 | 회차 | 공식 레벨 | 공개 유형 | Python 연습 난도 | 들어가는 개념 |
| --- | --- | --- | --- | --- | --- |
| [이상한 체스](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/odd-chess/description) | 상반기 오전 1번 문제 | L12 | Backtracking, Simulation | 응용 | 방향별 감시 범위, 후보 조합, 격자 복원 |
| [디버깅](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/debugging/description) | 상반기 오전 2번 문제 | L13 | Backtracking, Simulation | 응용 | 후보 선택, 열별 연속 구간 검사, 가지치기 |
| [드래곤 커브](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/dragon-curve/description) | 상반기 오후 1번 문제 | L12 | Simulation | 응용 | 방향 목록 역순 확장, 회전, 격자 표시 |
| [병원 거리 최소화하기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/min-of-hospital-distance/description) | 상반기 오후 2번 문제 | L11 | Backtracking | 기본 | 시설 조합, 맨해튼 거리, 최소합 |
| [토스트 계란틀](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/toast-eggmold/description) | 하반기 오전 2번 문제 | L11 | BFS | 기본 | 조건부 인접 BFS, 연결 요소, 하루 단위 갱신 |
| [바이러스 실험](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/virus-experiment/description) | 하반기 오후 1번 문제 | L13 | Simulation | 응용 | 나이별 개체 관리, 계절별 갱신, 번식 |
| [전투 로봇](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/fighting-robot/description) | 하반기 오후 2번 문제 | L13 | Simulation, BFS | 응용 | BFS 최단거리, 행·열 동률 처리, 크기 갱신 |

## 2019년

| 문제 | 회차 | 공식 레벨 | 공개 유형 | Python 연습 난도 | 들어가는 개념 |
| --- | --- | --- | --- | --- | --- |
| [시공의 돌풍](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/heros-of-storm/description) | 상반기 오전 1번 문제 | L12 | Simulation | 응용 | 격자 확산, 새 배열에 동시 반영, 경로 추적 |
| [생명과학부 랩 인턴](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/biology-lab-intern/description) | 상반기 오전 2번 문제 | L13 | Simulation | 응용 | 열별 대상 선택, 반사 이동, 충돌 해결 |
| [격자 숫자 놀이](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/matrix-number-play/description) | 상반기 오후 1번 문제 | L12 | Basic | 응용 | 빈도 집계, 튜플 정렬, 행·열 재구성 |
| [바이러스 백신](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/vaccine-for-virus/description) | 상반기 오후 2번 문제 | L12 | Backtracking, BFS | 응용 | 시작점 조합, 다중 시작점 BFS, 빈칸 도달 시간 |
| [종전](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/war-finish/description) | 하반기 오전 1번 문제 | L13 | Simulation | 응용 | 격자 구역 경계, 후보 열거, 구역 합 비교 |
| [이상한 윷놀이](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/odd-woodstick-game/description) | 하반기 오전 2번 문제 | L13 | Simulation | 응용 | 원형 판의 회전, 인접 검사, 삭제와 평균 |
| [이상한 다트 게임](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/odd-dart-game/description) | 하반기 오후 1번 문제 | L13 | Simulation | 응용 | 원형 행 회전, 인접 판정, 일괄 삭제 |
| [윷놀이 사기단](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/woodstick-fraud/description) | 하반기 오후 2번 문제 | L14 | Backtracking, Simulation | 도전 | 분기 경로, 말의 위치 상태, 선택·복원 |

## 2020년

| 문제 | 회차 | 공식 레벨 | 공개 유형 | Python 연습 난도 | 들어가는 개념 |
| --- | --- | --- | --- | --- | --- |
| [2차원 테트리스](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/tetris-2d/description) | 상반기 오전 1번 문제 | L14 | Simulation | 도전 | 두 판의 블록 이동, 줄 제거, 특수 구역 처리 |
| [술래잡기 체스](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/odd-chess2/description) | 상반기 오전 2번 문제 | L14 | Backtracking | 도전 | 객체 순서에 따른 이동, 재귀 상태 복사 |
| [승자독식 모노폴리](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/odd-monopoly/description) | 상반기 오후 1번 문제 | L14 | Simulation | 도전 | 방향 우선순위, 냄새 수명, 동시 이동·충돌 |
| [자율주행 전기차](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/autonomous-electric-car/description) | 상반기 오후 2번 문제 | L14 | Simulation, BFS | 도전 | BFS 목적지 선택, 거리·좌표 동률, 연료 갱신 |
| [불안한 무빙워크](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/unstable-moving-walk/description) | 하반기 오전 1번 문제 | L11 | Simulation | 기본 | 원형 인덱스, 내구도, 역순 이동 |
| [원자 충돌](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/atom-collision/description) | 하반기 오전 2번 문제 | L12 | Simulation | 응용 | 토러스 격자, 방향 벡터, 충돌 후 합치기 |
| [청소는 즐거워](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/cleaning-is-joyful/description) | 하반기 오후 1번 문제 | L13 | Basic | 응용 | 나선 이동, 방향별 분산 패턴, 격자 밖 집계 |
| [회전하는 빙하](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/rotating-glacier/description) | 하반기 오후 2번 문제 | L13 | Simulation, BFS | 응용 | 부분 격자 회전, 동시 갱신, BFS 연결 요소 |

## 2021년

| 문제 | 회차 | 공식 레벨 | 공개 유형 | Python 연습 난도 | 들어가는 개념 |
| --- | --- | --- | --- | --- | --- |
| [놀이기구 탑승](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/go-on-the-rides/description) | 상반기 오전 1번 문제 | L11 | Simulation | 기본 | 빈칸 후보 평가, 인접 점수와 동률 정렬 |
| [색깔 폭탄](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/colored-bomb/description) | 상반기 오전 2번 문제 | L14 | Simulation, BFS | 응용 | BFS 그룹 선택, 공용 칸 방문 처리, 중력·회전 |
| [나무 타이쿤](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/tree-tycoon/description) | 상반기 오후 1번 문제 | L11 | Simulation | 기본 | 순환 좌표 이동, 대각선 이웃, 턴별 상태 |
| [미로 타워 디펜스](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/maze-tower-defense/description) | 상반기 오후 2번 문제 | L15 | Simulation | 도전 | 나선 인덱스, 연속 그룹 제거·압축 |
| [정육면체 한번 더 굴리기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/cube-rounding-again/description) | 하반기 오전 1번 문제 | L13 | Simulation | 응용 | 주사위 면 추적, BFS 연결 요소, 방향 전환 |
| [냉방 시스템](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/cooling-system/description) | 하반기 오전 2번 문제 | L16 | Simulation | 도전 | 벽을 고려한 확산, 온도 동시 조절, 여러 단계의 종료 조건 |
| [팩맨](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/pacman/description) | 하반기 오후 1번 문제 | L15 | Simulation | 도전 | 복제, 경로 열거, 시체 수명, 다중 개체 상태 |
| [Sam의 피자학교](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/sam-pizza-school/description) | 하반기 오후 2번 문제 | L16 | Simulation | 도전 | 배열 접기·쌓기, 이웃 간 이동과 재배열 |

## 2022년

| 문제 | 회차 | 공식 레벨 | 공개 유형 | Python 연습 난도 | 들어가는 개념 |
| --- | --- | --- | --- | --- | --- |
| [술래잡기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/hide-and-seek/description) | 상반기 오전 1번 문제 | L15 | Simulation | 도전 | 나선 왕복, 방향 전환, 여러 객체 갱신 |
| [예술성](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/artistry/description) | 상반기 오전 2번 문제 | L13 | Simulation | 응용 | BFS 그룹 라벨, 접촉 변 개수, 부분 회전 |
| [꼬리잡기놀이](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/tail-catch-play/description) | 상반기 오후 1번 문제 | L15 | Simulation | 도전 | 팀 경로 추적, 순서 관리, 방향 반전 |
| [나무박멸](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/tree-kill-all/description) | 상반기 오후 2번 문제 | L12 | Simulation | 응용 | 동시 성장·번식, 대각선 범위, 수명 관리 |
| [싸움땅](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/battle-ground/description) | 하반기 오전 1번 문제 | L14 | Simulation | 도전 | 객체별 상태, 충돌과 이동 우선순위, 칸별 장비 |
| [산타의 선물 공장](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/santa-gift-factory/description) | 하반기 오전 2번 문제 | L17 | Simulation, LinkedList | 도전 | ID 조회, 연결 리스트, 구간 이동 |
| [코드트리 빵](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-mon-bread/description) | 하반기 오후 1번 문제 | L14 | Simulation, BFS | 도전 | BFS 최단거리, 동률 처리, 통행 금지 갱신 시점 |
| [산타의 선물 공장 2](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/santa-gift-factory-2/description) | 하반기 오후 2번 문제 | L16 | Simulation, LinkedList | 도전 | 양방향 연결 관계, 머리·꼬리, 묶음 이동 |

## 2023년

| 문제 | 회차 | 공식 레벨 | 공개 유형 | Python 연습 난도 | 들어가는 개념 |
| --- | --- | --- | --- | --- | --- |
| [포탑 부수기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/destroy-the-turret/description) | 상반기 오전 1번 문제 | L15 | Simulation, BFS | 도전 | 대상 정렬, 순환 격자 BFS 경로 복원, 단계별 피해 |
| [토끼와 경주](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/rabit-and-race/description) | 상반기 오전 2번 문제 | L15 | Simulation, Priority Queue | 도전 | 힙과 다중 키, 반사 이동, 점수 누적 |
| [메이즈 러너](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/maze-runner/description) | 상반기 오후 1번 문제 | L13 | Simulation, Exhaustive Search | 응용 | 이동 우선순위, 회전 영역 선택, 좌표 변환 |
| [코드트리 채점기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-judger/description) | 상반기 오후 2번 문제 | L16 | Simulation, Priority Queue | 도전 | 우선순위 큐, 도메인별 상태, 시각 처리 |
| [왕실의 기사 대결](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/royal-knight-duel/description) | 하반기 오전 1번 문제 | L13 | Simulation | 응용 | 직사각형 충돌 전파, 이동 가능성 검사, 일괄 적용 |
| [코드트리 메신저](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-messenger/description) | 하반기 오전 2번 문제 | L17 | Simulation, Tree, DP | 도전 | 트리와 깊이별 상태, 갱신 전파 |
| [루돌프의 반란](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/rudolph-rebellion/description) | 하반기 오후 1번 문제 | L14 | Simulation | 도전 | 거리와 동률, 연쇄 충돌, 기절 상태 |
| [코드트리 오마카세](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-omakase/description) | 하반기 오후 2번 문제 | L18 | Simulation, HashSet, HashMap, Sorting | 도전 | 시간 순 이벤트, 모듈러 좌표, 해시와 정렬 |

## 2024년

| 문제 | 회차 | 공식 레벨 | 공개 유형 | Python 연습 난도 | 들어가는 개념 |
| --- | --- | --- | --- | --- | --- |
| [고대 문명 유적 탐사](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ancient-ruin-exploration/description) | 상반기 오전 1번 문제 | L12 | Simulation, BFS | 응용 | 회전 후보 비교, BFS 그룹, 제거 후 연쇄 갱신 |
| [코드트리 투어](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-tour/description) | 상반기 오전 2번 문제 | L14 | Simulation, Dijkstra, Priority Queue | 도전 | 다익스트라, 우선순위 큐, 시작점 변경 |
| [마법의 숲 탐색](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/magical-forest-exploration/description) | 상반기 오후 1번 문제 | L13 | Simulation, BFS | 응용 | 다중 칸 객체 이동, 출구 조건, BFS |
| [색깔 트리](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/color-tree/description) | 상반기 오후 2번 문제 | L17 | Tree DP | 도전 | 트리 제약과 서브트리, 색 상태 전파 |
| [미지의 공간 탈출](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/escape-unknown-space/description) | 하반기 오전 1번 문제 | L14 | BFS | 도전 | 여러 면의 좌표 변환, 시간 제약, BFS |
| [코드트리 DB](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-db/description) | 하반기 오전 2번 문제 | L19 | Dynamic Segment Tree | 도전 | 키 조회, 동적 세그먼트 트리, 순위·누적합 |
| [메두사와 전사들](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/medusa-and-warriors/description) | 하반기 오후 1번 문제 | L15 | Simulation, BFS | 도전 | BFS 경로, 시야와 가림, 이동 우선순위 |
| [코드트리 등산 게임](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-mountain-climbing-games/description) | 하반기 오후 2번 문제 | L18 | 미표시 | 도전 | 세그먼트 트리 활용과 상태 갱신 |

## 2025년

| 문제 | 회차 | 공식 레벨 | 공개 유형 | Python 연습 난도 | 들어가는 개념 |
| --- | --- | --- | --- | --- | --- |
| [민트 초코 우유](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/mint-choco-milk/description) | 상반기 오전 1번 문제 | L12 | Simulation, BFS | 응용 | BFS 그룹, 대표 정렬, 전파 순서 |
| [개구리의 여행](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/frog-journey/description) | 상반기 오전 2번 문제 | L13 | Dijkstra | 도전 | 상태를 포함한 가중 그래프, 다익스트라 |
| [미생물 연구](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/microbial-research/description) | 상반기 오후 1번 문제 | L13 | Simulation, BFS | 응용 | BFS 연결성, 격자 배치, 순서와 인접 관계 |
| [여왕 개미](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/queen-ant/description) | 상반기 오후 2번 문제 | L13 | Greedy, Binary Search, Parametric Search | 도전 | 판정 함수, 이진탐색, 그리디 검사 |
| [택배 하차](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/delivery-service/description) | 하반기 오전 1번 문제 | L12 | Simulation | 응용 | 격자 객체 배치, 이동·제거 순서, 경계 검사 |
| [해적 선장 코디](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/pirate-captain-coddy/description) | 하반기 오전 2번 문제 | L14 | Simulation, Priority Queue | 도전 | 상태 시뮬레이션, 우선순위 큐와 갱신 |
| [AI 로봇청소기](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ai-robot/description) | 하반기 오후 1번 문제 | L13 | Simulation, BFS | 응용 | BFS 도달 거리, 우선순위, 격자 상태 |
| [가로등 설치](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/street-light-installation/description) | 하반기 오후 2번 문제 | L15 | Priority Queue, Doubly Linked List | 도전 | 우선순위 큐, 양방향 연결 관계, 이웃 갱신 |

## 2026년

| 문제 | 회차 | 공식 레벨 | 공개 유형 | Python 연습 난도 | 들어가는 개념 |
| --- | --- | --- | --- | --- | --- |
| [아기 바다거북의 대모험: 해저 화산 지대](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/a-little-sea-turtles-big-adventure/description) | 상반기 오전 1번 문제 | L12 | Simulation, BFS | 응용 | 격자 상태 갱신, BFS 탐색 |
| [코디의 향수 공방](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/perfume-workshop/description) | 상반기 오전 2번 문제 | L13 | DP, Preprocessing | 도전 | 전처리, DP 상태와 전이 |
| [아기 고래의 첫 항해](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/baby-whale-first-voyage/description) | 상반기 오후 1번 문제 | L12 | Simulation, BFS | 응용 | 격자 상태 갱신, BFS 탐색 |
| [코디의 보석 공방](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/jewel-workshop/description) | 상반기 오후 2번 문제 | L13 | DP, Two Pointers | 도전 | DP 상태, 투 포인터로 범위 유지 |
| [수하물 컨베이어 벨트](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/baggage-conveyor-belt/description) | 하반기 오전 1번 문제 | L13 | Simulation, BFS | 응용 | 단계별 격자 갱신, BFS 탐색 |
| [코디의 퍼즐 공방](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/cody-puzzle-workshop/description) | 하반기 오전 2번 문제 | L13 | Simulation, Incremental Counting | 도전 | 퍼즐 모서리 표현, 배치 변화와 개수 갱신 |
| [호수의 물결](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/wave-of-lake/description) | 하반기 오후 1번 문제 | L13 | Simulation, BFS | 응용 | 격자 파동, BFS 전파와 상태 갱신 |
| [식량 보급](https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/commissariat/description) | 하반기 오후 2번 문제 | L13 | Sorting, Prefix Sum, Binary Search | 도전 | 정렬, 누적합, 이진탐색 |
