n, m = map(int, input().split())
a = ''.join(input().split())
b = ''.join(input().split())

if n < m:
    a, b = b, a

if b in a:
    print('Yes')
else:
    print('No')

    
