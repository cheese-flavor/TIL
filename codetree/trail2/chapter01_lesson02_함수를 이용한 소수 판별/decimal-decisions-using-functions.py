a, b = map(int, input().split())

# Please write your code here.
def is_magic(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

count = 0

for i in range(a, b+1):
    if is_magic(i):
        count += i

print(count)

