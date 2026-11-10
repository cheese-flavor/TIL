num = list(map(int, input().split()))

for i in range(len(num)):
    if num[i] == 0:
        print(sum(num[i-3:i]))
        break
