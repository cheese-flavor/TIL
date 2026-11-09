a, b = map(int, input().split())

n1 = len(str(a//b))
answer = str(a//b)+'.'
a %= b

for _ in range(20):
    a *= 10
    answer += str(a//b)

    a %= b
print(answer)

