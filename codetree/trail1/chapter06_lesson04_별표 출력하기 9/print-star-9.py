n = int(input())
#star = 

for i in range(n):
    for _ in range(n-i-1):
        print(' ', end =' ')
    print('* '*((i+1)*2-1))
