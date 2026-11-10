s = list(input())

while len(s) != 1:
    n = int(input())
    if n >= len(s)-1:
        n = len(s)-1
    s.pop(n)
    print(''.join(s))
