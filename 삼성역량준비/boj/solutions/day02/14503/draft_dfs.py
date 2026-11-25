# 초기 설정
n, m = map(int, input().split())
r, c, d = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(n)]

#이동 크기 정리
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c, d, answer):
    
    if house[r][c] == 0:
        house[r][c] = 2 # 청소완료 2, 청소안됨 0, 벽 1
        answer += 1
    
    # 4방향 탐색 후 (북 0, 동 1, 남 2, 서 3)
    for i in range(1, 5):
        nd = (d-i) % 4 # 새 방향
        
        # 해당 방향 조건이 되는지 확인
        nr, nc = r + dr[nd], c + dc[nd]
        if 0 <= nr < n and 0 <= nc < m and house[nr][nc] == 0:
            return dfs(nr, nc, nd, answer)
                
    # 여기까지 왔으면 이미 다 청소되어있거나, 벽인 경우 -> 반대방향으로 뒤로 갈 수 있나 없나만 보면 될듯? 
    br, bc = r - dr[d], c - dc[d]
    if house[br][bc] == 1:
            return answer
    else:
        return dfs(br, bc, d, answer) #되돌아올께 아니면 return으로 재귀호출

dfs(r, c, d, 0)
print(answer)
