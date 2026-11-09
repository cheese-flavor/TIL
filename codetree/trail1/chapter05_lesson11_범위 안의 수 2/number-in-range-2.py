sum = 0
count = 0

for _ in range(10):
    n = int(input())
    if 0 <= n <= 200:
        sum += n
        count += 1

print(f"{sum} {sum/count:0.1f}")
