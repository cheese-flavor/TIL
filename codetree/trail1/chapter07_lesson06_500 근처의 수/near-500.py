num = list(map(int, input().split()))
max_num = 0
min_num = 1000

for n in num:
    if n < 500:
        max_num = max(max_num, n)
    elif n > 500:
        min_num = min(min_num, n)
print(max_num, min_num)
