num = list(map(int, input().split()))
count = [0 for _ in range(9)]

for i in num:
    if i == 0:
        break

    else:
        if i // 10 != 0:
            count[i// 10-1] += 1

for k in range(9):
    print(f"{k+1} - {count[k]}")

