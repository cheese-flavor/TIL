a, b = map(int, input().split())

# Please write your code here.
def onjeon(i):
    if i % 2 == 0:
        return False
    if str(i)[-1] == '5':
        return False
    if i % 3 == 0 and i % 9 != 0:
        return False
    
    return True

count = 0

for i in range(a, b+1):
    if onjeon(i):
        count += 1

print(count)

