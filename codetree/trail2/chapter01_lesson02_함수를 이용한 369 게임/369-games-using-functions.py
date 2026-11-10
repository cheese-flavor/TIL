a, b = map(int, input().split())

# Please write your code here.
def magic_num(n):
    return '3' in str(n) or '6' in str(n) or '9' in str(n)


def is_magic(n):
    return n % 3 == 0 or magic_num(n)

count = 0

for i in range(a, b+1):
    if is_magic(i):
        count += 1

print(count)
