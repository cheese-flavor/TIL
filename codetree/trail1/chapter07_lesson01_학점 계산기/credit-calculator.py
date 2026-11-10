n = int(input())
num = list(map(float, input().split()))

result = round(sum(num)/n,1)

print(result)

if result >= 4.0:
    print('Perfect')
elif result >= 3.0:
    print('Good')
else:
    print('Poor')
