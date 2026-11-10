arr = []
count = 0

while True:
    s = input()
    if s == '0':
        break
    else:
        arr.append(s)
        count += 1

print(count)
for i in range(count):
    if i % 2 == 0:
        print(arr[i]) 
