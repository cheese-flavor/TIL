# 초기 설정
n, m = map(int, input().split())
r, c, d = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(n)]

#이동 크기 정리
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
answer = 0

while house[r][c] != 1: #그냥 뒤로 넘겼을때 1이면 끝내는걸로
    
    # 현위치가 0이면 청소
    if house[r][c] == 0:
        house[r][c] = 2
        answer += 1
    
    possible = False
    for i in range(1, 5):
        nd = (d-1) % 4
        # 갈 수 있는 위치면 이동 / possible 기반 정리   
        if house[r+dr[nd]][c+dc[nd]] == 0:
            r += dr[nd]
            c += dc[nd]
            d = nd
            possible = True
            break
    
    if not possible:
        r -= dr[d]
        c -= dc[d]

print(answer)
