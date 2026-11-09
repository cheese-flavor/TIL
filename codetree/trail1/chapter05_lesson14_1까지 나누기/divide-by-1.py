N = int(input())
i = 1
while N > 1:
    N = N // i
    i += 1

print(i-1)
