a, b, c = map(int, input().split())
possible = False

while c <= b:
    if a <= c <= b:
        print('YES')
        possible = True
        break
    c += c

if not possible:
    print('NO')
    

    
