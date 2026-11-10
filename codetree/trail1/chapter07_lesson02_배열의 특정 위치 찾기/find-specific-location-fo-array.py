num = list(map(int, input().split()))
first = 0
second = 0

for i in range(len(num)):
    if i % 2 == 1:
        first += num[i]
    
    if (i+1) % 3 == 0:
        second += num[i]

print(first, round(second/3,1))
