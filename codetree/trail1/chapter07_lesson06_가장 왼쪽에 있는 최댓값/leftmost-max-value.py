n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

while n > 0:
    max_num = max(a)
    n = a.index(max_num)
    print(n+1, end=' ')
    a = a[:n]



