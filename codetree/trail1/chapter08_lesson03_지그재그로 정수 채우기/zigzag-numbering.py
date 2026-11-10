n, m = map(int, input().split())

# Please write your code here.
arr = [[0]*m for _ in range(n)]
num = -1

for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            num += 1
            arr[j][i] = num

    else:
        for j in range(n-1, -1, -1):
            num += 1
            arr[j][i] = num

for v in range(n):
    for t in range(m):
        print(arr[v][t], end = ' ')
    print()

