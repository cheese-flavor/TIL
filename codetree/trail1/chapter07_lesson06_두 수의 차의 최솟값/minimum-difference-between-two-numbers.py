n = int(input())
num = list(map(int,input().split()))
min_num = 100

for i in range(n-1):
    for j in range(i+1, n):
        min_num = min(min_num, abs(num[j]-num[i]))
print(min_num)


        
