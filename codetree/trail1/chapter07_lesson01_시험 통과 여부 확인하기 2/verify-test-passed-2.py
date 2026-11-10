n = int(input())
count = 0

for _ in range(n):
    num = list(map(int, input().split()))

    result = round(sum(num)/4, 1)

    if result >= 60:
        print('pass')
        count += 1
    else:
        print('fail')
    
print(count)
