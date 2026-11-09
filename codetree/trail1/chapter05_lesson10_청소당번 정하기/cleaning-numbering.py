n = int(input())
count1, count2, count3 = 0, 0, 0
for i in range(1, n+1):
    if i % 12 == 0:
        count3 += 1
    elif i % 3 == 0:
        count2 += 1
    elif i%2 ==0:
        count1 += 1
print(count1, count2, count3)

