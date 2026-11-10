n = int(input())
num = 0
for _ in range(n):
    num += int(input())

l = len(str(num))
arr = []

for i in range(l):
    arr.append(str(num)[i])

k = arr.pop(0)

print(''.join(arr)+k)

