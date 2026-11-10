num = list(map(int,input().split()))

if 0 in num:
    k = num.index(0)

    for i in range(k-1, -1, -1):
        print(num[i], end = ' ')
else:
    for i in range(len(num)-1, -1, -1):
        print(num[i], end = ' ')

