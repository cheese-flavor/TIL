n = int(input())
count = 0
for _ in range(n):
    N = int(input())

    if N % 2 == 1 and N % 3 == 0:
        count += N

print(count)

