count = [0 for _ in range(9)]

n = int(input())
num = list(map(int, input().split()))

for i in range(n):
    count[num[i]-1] += 1

for j in count:
    print(j)
