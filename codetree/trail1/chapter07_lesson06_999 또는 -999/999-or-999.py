num = list(map(int, input().split()))
max_num = -999
min_num = 999
for n in num:
    if n == 999 or n == -999:
        print(max_num, min_num)
        break
    else:
        max_num = max(n, max_num)
        min_num = min(n, min_num)
