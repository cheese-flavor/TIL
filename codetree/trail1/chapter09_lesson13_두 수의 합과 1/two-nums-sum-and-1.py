a, b = map(int, input().split())

s= str(a+b)
count = 0

for i in s:
    if i == '1':
        count += 1

print(count)
