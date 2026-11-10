num = list(map(int, input().split()))
result = 0

for i in range(len(num)):
    if i % 2 == 0:
        result += num[i]
    else:
        result -= num[i]

print(abs(result))

