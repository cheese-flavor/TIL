n, m = map(int, input().split())
print(n, end= ' ')
print(m, end= ' ')
result = n+m
for _ in range(8):
    print(result%10, end = ' ')
    result += m
    m = result - m

