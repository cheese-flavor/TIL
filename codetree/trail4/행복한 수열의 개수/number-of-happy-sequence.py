n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

answer = 0

# 왼 -> 오
for i in range(n):
    for j in range(n - m + 1):
        start = grid[i][j]
        possible = True

        for k in range(m):
            if start != grid[i][j + k]:
                possible = False
                break

        if possible:
            answer += 1
            break

# 위 -> 아래
for j in range(n):
    for i in range(n - m + 1):
        start = grid[i][j]
        possible = True

        for k in range(m):
            if start != grid[i + k][j]:
                possible = False
                break

        if possible:
            answer += 1
            break

print(answer)
