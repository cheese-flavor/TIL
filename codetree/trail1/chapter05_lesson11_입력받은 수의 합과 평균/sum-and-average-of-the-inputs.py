N = int(input())
sum = 0

for _ in range(N):
    n = int(input())
    sum += n

print(f"{sum} {sum/N:0.1f}")

