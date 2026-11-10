n = int(input())
price = list(map(int, input().split()))
max_p = 0
# Please write your code here.
for i in range(n-1):
    if max(price) > price[i]:

        for j in range(i+1,n):
            max_p = max(max_p, price[j]-price[i])

print(max_p)



        
