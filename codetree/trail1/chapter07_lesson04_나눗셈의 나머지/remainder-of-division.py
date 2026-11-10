a, b = map(int, input().split())
result = 0
count = [0 for _ in range(b)]

while a > 1:
    count[a % b] += 1
    a = a // b

for i in range(len(count)):
    result += (count[i]) ** 2

print(result)

