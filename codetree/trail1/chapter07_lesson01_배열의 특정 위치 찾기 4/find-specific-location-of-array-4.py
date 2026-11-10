num = list(map(int, input().split()))
count = 0
result = 0

if 0 in num:
    k = num.index(0)
    
    for i in range(k):
        if num[i] % 2 == 0:
            count += 1
            result += num[i]
    print(count, result)

else:
    for j in num:
        if j % 2 == 0:
            count += 1
            result += j
    
    print(count, result)


