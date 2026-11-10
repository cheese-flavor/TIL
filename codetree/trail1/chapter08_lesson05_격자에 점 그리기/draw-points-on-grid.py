n, m = map(int, input().split())
k = 0
arr = [[0]*n for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    k += 1
    arr[r-1][c-1] = k

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()
