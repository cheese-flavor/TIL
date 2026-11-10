n, m = map(int, input().split())

num = list(map(int, input().split()))

count = 0

for i in num:
    if i == m:
        count += 1

print(count)

