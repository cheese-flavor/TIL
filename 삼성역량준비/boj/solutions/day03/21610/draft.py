'''
n x n 격자에서 연습 / 이동은 8가지 방향 <- 부터 1
A[r][c]는 (r, c)에 있는 바구니에 저장되어 있는 물의 양
#### 물은 고정, 구름만 이동 ####
1. di 방향으로 si칸 이동
2. 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가 구름이 모두 삭제
3. 2에서 물이 증가한 칸 (r, c)에 대각선 1인 칸에 물이 있는 바구니의 수만큼 증가
4. 물의 양이 2 이상인 모든 칸에 구름 생성 후, 물의 양이 2 감소 
    - 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸 x
5. M번의 이동 후 전체 물의 양의 합
'''
# 초기값 설정
n, m = map(int, input().split()) # 격자, 이동수
water = [list(map(int, input().split())) for _ in range(n)] # 격자별 물 보유 상황
command = [list(map(int, input().split())) for _ in range(m)] # 명령 리스트
cloud = [[0]*n for _ in range(n)] #구름 여부
n_cloud = [[0]*n for _ in range(n)] #구름 간에 겹칠 때

# 구름 초기 (n-1, 0), (n, 1), (n-2, 0), (n-2, 1)
# 구름이 있는 곳 = 1, 구름 직전 소멸 = -1, 0은 아무것도 없음
cloud[n-1][0], cloud[n-1][1], cloud[n-2][0],cloud[n-2][1] = 1, 1, 1, 1

# 물 채우기 대각선 확인
w_dr = [-1, -1, 1, 1]
w_dc = [-1, 1, -1, 1]

# 구름 이동 대각선 확인
c_dr = [0, -1, -1, -1, 0, 1, 1, 1]
c_dc = [-1, -1, 0, 1, 1, 1, 0, -1]

# 이동명령에 따라 시작
for com in command:
    d, s = com[0]-1, com[1]
    n_cloud = [[0] * n for _ in range(n)]
    
    #1. 구름이 방향으로 이동
    for r in range(n):
        for c in range(n):
            if cloud[r][c] == 1:
                nr, nc = (r+(c_dr[d]*s))%n, (c+(c_dc[d]*s))%n
                n_cloud[nr][nc] += 1
    cloud = n_cloud
                
    #2. 이동 지점에 water +1, 구름 -1로 바뀜
    for r in range(n):
        for c in range(n):
            if cloud[r][c] == 1:
                water[r][c] += 1
                cloud[r][c] = -1
                
    #3. 물복사버그
    for r in range(n):
        for c in range(n):
            if cloud[r][c] == -1
                for i in range(4):
                    wr, wc = r+w_dr[i], c+w_dc[i]
                    if 0 <= wr < n and 0 <= wc < n and water[wr][wc] >0:
                        water[r][c] += 1

    #4. 소멸 지역 제외 2이상 구름 생성
    for r in range(n):
        for c in range(n):
            if cloud[r][c] != -1 and water[r][c] >= 2:
                cloud[r][c] = 1
                water[r][c] -= 2
                
    #5. 소멸된 구름 복구
    for r in range(n):
        for c in range(n):
            if cloud[r][c] == -1:
                cloud[r][c] = 0

# 전체합 구하기
answer = 0
for i in range(n):
    answer += sum(water[i])
    
print(answer)
