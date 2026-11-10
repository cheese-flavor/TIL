n = int(input())

arr = [[0]*n for _ in range(n)]
k = 0
count = 0

for j in range(n-1, -1, -1):
    if count % 2 == 0:
        for i in range(n-1, -1, -1):
            k += 1
            arr[i][j] = k
    else:
        for i in range(n):
            k += 1
            arr[i][j] = k

    count += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()
