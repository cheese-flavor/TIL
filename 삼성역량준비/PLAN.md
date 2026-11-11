# 4주 수업 계획

평일 또는 주말을 포함해 주 6회, 회당 60~90분을 가정했다. 각 주의 6회차는 복습과 밀린 학습에 쓴다. 시험 날짜가 확정되면 마지막 모의고사를 기준으로 일정을 맞춘다. 실제 모의 시간은 본인 응시 안내에 적힌 제한을 사용한다.

## 오늘 · 1회차

1. 아래 두 문제 중 2차원 배열 문제부터 20분간 풀어 본다. 기존 TIL의 함수 문제도 한 번 다시 풀어 `return`과 조건 분기를 점검한다.
2. 2차원 배열을 입력받고, 좌표 하나에서 상하좌우를 돌며 범위 안인 칸만 출력한다. 한 줄 또는 한 열인 격자와 모서리를 손으로 확인한다.
3. ChatGPT에 내 코드, 기대값과 실제값, 막힌 줄을 전달한다. 다음 공부를 시작할 수 있도록 `PROGRESS.md`의 상태를 갱신한다.

- [Trail 1 · 2차원 배열](https://www.codetree.ai/trail-info/novice-low/)에서 **2차원 배열 입력**, **격자로서의 2차원 배열**의 연습 문제를 각 1개 고른다.
- [Trail 2 · 그 계절, 그 날](https://www.codetree.ai/trails/complete/curated-cards/test-that-season-that-day)은 기존 TIL에 통과 기록이 있어 복습용으로 사용한다.

## 회차별 수업

| 주차 | 1~2회차 | 3~4회차 | 5~6회차 | 다음 단계로 가는 기준 |
| --- | --- | --- | --- | --- |
| 1주 · Python과 격자 | `input().split()`, `map`, 리스트·문자열, 반복문, 함수와 반환값. 2차원 리스트 행을 각각 생성 | 좌표, `dx/dy`, 범위 검사, 방향 전환, 90도 회전. 반복 범위로 `O(N)`과 `O(N²)` 구분 | 격자 완전탐색 1문제 후 [바이러스 검사][virus]. 틀린 기초 문제 1개 재풀이 | 빈 파일에서 격자 입력과 4방향 탐색을 쓰고 모서리 반례를 통과 |
| 2주 · 탐색과 상태 갱신 | `deque` 큐, 스택, `set`·`dict`, 튜플 정렬. DFS와 BFS의 방문 순서를 손으로 비교 | BFS 연결 요소와 최단거리. 큐에 넣을 때 방문 표시. 재귀 종료 조건, 선택·복원과 가지치기 | [외주 수익 최대화하기][outsource], [토스트 계란틀][toast]. 시간 부족 시 토스트를 3주 첫날로 이동 | BFS로 도달 가능 여부와 최단거리를 구분해 작성하고, 재귀의 상태와 종료 조건을 설명 |
| 3주 · 기출 구현 | [자율주행 자동차][car], [불안한 무빙워크][walk]로 이동·회전과 단계별 상태 갱신 | [메이즈 러너][maze]로 좌표 회전, 동률 처리, 종료 조건 연습 | [고대 문명 유적 탐사][ruin]로 구현+BFS 연습. 막힌 문제를 새 파일에서 재풀이 | 한 턴의 처리 순서를 적고, 복사본이 필요한 단계와 즉시 갱신할 단계를 구분 |
| 4주 · 최신 기출과 실전 | 최근 세트 하나를 모의시험으로 사용. 2025 하반기 오전 [택배 하차][delivery]와 [해적 선장 코디][pirate] 권장 | 복기 후 가장 자주 틀린 유형 1개 보강. 힙은 기본 문제 해결이 안정적일 때 `heapq`까지 | 2026 하반기 오후 [호수의 물결][wave]와 [식량 보급][food]으로 두 번째 모의시험. 마지막 회차에 오답 재풀이 | 시작 10분 내 우선 풀 문제를 고르고, 종료 전에 예제·최소 입력·경계·동률을 검사 |

## 트레일에서 고를 문제

각 항목은 트레일의 단원 또는 연습 문제를 찾을 때 사용할 이름이다. 처음에는 예제 1개와 연습 1개를 선택한다.

| 트레일 | 연습 순서 | 기출에서 쓰이는 곳 |
| --- | --- | --- |
| [Trail 1 · 프로그래밍 기초](https://www.codetree.ai/trail-info/novice-low/) | 한 줄에 여러 개 입력 → 인덱스 참조 → 2차원 배열 입력 → 격자로서의 2차원 배열 | 입력 해석, 좌표, 집계 |
| [Trail 2 · 프로그래밍 연습](https://www.codetree.ai/trail-info/novice-mid/) | 값을 반환하는 함수 → 일반 정렬 → 객체 정렬 → dx dy technique → 구간 단위로 완전탐색 → 값을 반환하는 재귀함수 | 함수 분리, 동률 정렬, 이동 규칙, 후보 비교 |
| [Trail 3 · 자료구조 알고리즘](https://www.codetree.ai/trail-info/novice-high/) | 반복문의 시간복잡도 → Stack / Queue / Deque → 해싱. 여유가 있으면 Heap | 탐색 대기열, 중복 확인, 개수 집계, 우선순위 |
| [Trail 4 · 알고리즘 입문](https://www.codetree.ai/trail-info/intermediate-low/) | 격자 안에서 완전탐색 → 격자 안에서 단일 객체를 이동 → N개 중에 M개 고르기(Simple) → DFS → BFS 탐색 → 가중치가 동일한 그래프에서의 BFS | 격자 구현, 조합, 연결 요소와 최단거리 |

## 공부하는 순서

- 기초 회차는 개념 15분, 문제 30~50분, 반례와 기록 10~15분을 기준으로 한다. 20분 이상 막히면 현재 생각을 정리해 힌트 하나를 요청한다.
- 첫 기출은 2015년 **바이러스 검사**(L4)로 시작한다. 2015년 **2개의 사탕**(L15)은 상태 탐색까지 연습한 뒤 여유가 있을 때 풀어 본다. 2017~2020년에서 유형별 기본기를 익힌 다음 2023~2026년 문제로 옮긴다.
- 시간 여유가 적으면 1주차 격자, 2주차 BFS, 3주차 구현 기출 2개, 4주차 모의 1회부터 마친다. DP·다익스트라·세그먼트 트리는 핵심 문제를 독립적으로 푼 뒤 필요한 주제만 추가한다.
- 힌트로 해결한 문제는 다음날, 오답이 반복된 문제는 3~7일 뒤에 새 파일에서 다시 푼다.

[virus]: https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/virus-detector/description
[outsource]: https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/max-of-outsourcing-profit/description
[toast]: https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/toast-eggmold/description
[car]: https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/autonomous-driving/description
[walk]: https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/unstable-moving-walk/description
[maze]: https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/maze-runner/description
[ruin]: https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ancient-ruin-exploration/description
[delivery]: https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/delivery-service/description
[pirate]: https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/pirate-captain-coddy/description
[wave]: https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/wave-of-lake/description
[food]: https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/commissariat/description
