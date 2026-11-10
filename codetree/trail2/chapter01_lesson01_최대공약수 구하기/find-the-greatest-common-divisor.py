n, m = map(int, input().split())

# Please write your code here.

def math1(n, m):
    max_num = 0
    if n < m:
        n, m = m, n
    
    if m == 1:
        print(1)
    
    elif m == n:
        print(n)
    
    else:
        for i in range(1, m+1):
            if n % i == 0 and m % i == 0:
                max_num = i
    
        print(max_num) 

math1(n, m)
