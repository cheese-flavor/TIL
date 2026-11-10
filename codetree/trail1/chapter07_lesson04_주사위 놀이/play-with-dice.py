num = list(map(int, input().split()))
count = [0 for _ in range(6)]

for i in range(10):
    count[num[i]-1] += 1

for j in range(6):
    print(f"{j+1} - {count[j]}")
