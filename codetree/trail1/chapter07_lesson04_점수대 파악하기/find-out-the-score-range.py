num = list(map(int,input().split()))
count = [0 for _ in range(10)]

for s in range(len(num)):
    if num[s] == 0:
        break

    else:
        if num[s] // 10 != 0:
            count[(num[s] // 10)-1] += 1

for i in range(9, -1, -1):
    print(f"{(i+1)*10} - {count[i]}")
