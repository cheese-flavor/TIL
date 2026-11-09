n = int(input())
star = n*2-1

for i in range(n):
    for j in range(i):
        print(' ', end=' ')
        
    print('* '*star, end = ' ')
    star -= 2
    print()
