n = int(input())

for i in range(n):
    print('*'*(n-i), end='')
    
    for _ in range(i):
        print(' ',end=' ')

    print('*'*(n-i))



