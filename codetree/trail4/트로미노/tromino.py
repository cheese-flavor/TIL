n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
sum_block = 0

#4칸 정사각형에서 하나씩 빼는 형태로 4개
for i in range(n-1):
    for j in range(m-1):
        four = sum(grid[i][j:j+2]) + sum(grid[i+1][j:j+2])
        sum_block = max(sum_block, four-grid[i][j], four-grid[i][j+1],four-grid[i+1][j], four-grid[i+1][j+1])

#3칸씩 가로
for i in range(n):
    for j in range(m-2):
        sum_block = max(sum_block, sum(grid[i][j:j+3]))

#3칸씩 세로
grid2 = []
for j in range(m):
    l = []
    for i in range(n):
        l.append(grid[i][j])
    grid2.append(l)

for i in range(m):
    for j in range(n-2):
        sum_block = max(sum_block, sum(grid2[i][j:j+3]))

print(sum_block)