arr = [ list(map(int, input().split())) for _ in range(4)]
num = 0

for i in range(4):
    for j in range(i+1):
        num += arr[i][j]

print(num)


