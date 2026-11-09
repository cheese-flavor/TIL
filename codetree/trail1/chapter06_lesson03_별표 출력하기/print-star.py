n = int(input())
star = n+n-1
for i in range(star):
    if i < n:
        print('* '*(i+1))
    else:
        print('* '*(star-i))

