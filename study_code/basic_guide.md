## 셤 준비 ##
> 공부 구조
```
자료구조 개념

Djikstra
Heap
Bucket
Union find
DFS
Segtree
Trie
Game
Hash
```

> 일시
```
8월 29일 / 약 9일

-1일차: 전체 개념 정리 (알고리즘 가볍게, 메서드)
-2일차:

```


## 개념정리 144p ##
> 자료구조 및 DFS, BFS
```
데이터를 표현하고 처리하기 위한 구조
오버플로 = 수용공간 크기를 벗어나게되면

스택: 선입후출 구조 / stack, append, pop
큐: 선입선출 구조
    from collections import deque (= 스택과 큐 장점 모두 채택)
    queue = deque()
    queue.append() / queue.popleft()


재귀함수: 자기자신을 다시 호출 -> 초기화값, 입력변수, 조건기반 종료


DFS = 깊이 우선 탐색, 깊은 부분을 우선적 탐색

    그래프: 노드와 간선
    인접행렬: 모든 노드에 연결된 노드에 대한 정보 차례대로 연결하여 저장
             인접리스트 방식으로 처리할 때 2차원 리스트 활용
             graph[0].append((1, 7))
    
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
    2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 스택에 넣고 방문처리
    3. 방문하지 않은 인접 노드가 없으며 스택에서 최상단 노드를 꺼낸다 (이를 반복)

    def dfs(graph, v, visited):
        #현재 노드 방문처리
        visited[v] = True
        print(v, end= ' ')

        #현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)

    #각 노드가 연결된 정보를리스트 자료형으로 표현(2차원)
    graph = [ [], [2,3,8], [1,7] ]

    #방문기록용
    vistied = [False] * 9

    #정의된 dfs 함수 호출
    dfs(graph, 1, visited)



BFS = 너비 우선 탐색, 가까운 노드부터 탐색하는 / 큐 자료구조에 기초하여 구현     
     
     1. 탐색 시작 노드를 큐에 삽입하고 방문처리
     2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입
     3. 2번 과정을 더 이상 수행 x 반복
     
     



```




