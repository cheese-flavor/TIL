n, m = map(int, input().split())

# Please write your code here.

def math2(n, m):
    if n < m:
        n, m = m, n

    if n == m:
        print(n)
    
    elif m == 1:
        print(m*n)
    
    else:
        num = 0
        for i in range(m, 0, -1):
            if n % i == 0 and m % i == 0:
                print(n*m//i)
                break

math2(n,m)



''' #시간 초과 때문인가?
def math2(n, m):
    if n < m:
        n, m = m, n

    if n == m:
        print(n)
    
    else:
        for i in range(m, m*n):
            if i%n == 0  and i%m == 0:
                print(i)
                break
    
math2(n,m)
'''


