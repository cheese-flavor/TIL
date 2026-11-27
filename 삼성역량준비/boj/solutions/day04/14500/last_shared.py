'''
폴리오미노 = 1x1 정사각형 4개를 이어붙인 도형(1개만 들어가는거네)
- 정사각형끼리 겹치기 x
- 도형은 모두 연결(도형끼리라는듯)
- 정사각형 변끼리 연결(꼭짓점끼리 x)

그냥 4칸이 가는데, 이어지는지만 보면 되지 않을까?
dfs로 0, 0 에서 출발하는데, 상하좌우로 뻗어서 4칸, 각각 넓이써서
'''
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
visited = [[False] * m for _ in range(n)] #이전에 갔던곳으로 돌아가면 안되니까

def dfs(r, c, idx, score):
    global answer

    # 종료 조건
    if idx == 4:
        answer = max(answer, score)
        return
    
    # 상하좌우 탐색
    visited[r][c] = True
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        if 0<= nr < n and 0 <= nc < m and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, idx+1, score+paper[nr][nc])
        
            # T자형
            if idx == 2: #중간에 가운데서 하나를 붙이는 형태니까
                dfs(r, c, idx+1, score+paper[nr][nc])
            visited[nr][nc] = False

# 종이 탐색           
for r in range(n):
    for c in range(m):
        dfs(r, c, 1, paper[r][c])

print(answer)
