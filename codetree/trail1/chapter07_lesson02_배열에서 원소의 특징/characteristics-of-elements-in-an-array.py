num = list(map(int, input().split()))

for i in range(10):
    if num[i] % 3 == 0:
        print(num[i-1])
        break
