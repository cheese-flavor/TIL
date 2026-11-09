arr = []
count = 0

for _ in range(3):
    arr.append(input().split())

for i in arr:
    if i[0] == 'Y' and int(i[1]) >= 37:
        count += 1

if count >= 2:
    print('E')
else:
    print('N')

