a, b, c= map(int, input().split())
possible = False
#c *= (a//c)

while c <= b:
    if a <= c <= b:
        print('NO')
        possible = True
        break
    
    c += c

if not possible:
    print('YES')

    

