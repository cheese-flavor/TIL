a, b = map(int, input().split())

# Please write your code here.
def three(n):
    count = 0
    for i in str(n):
        count += int(i)

    if count % 2 == 0:
        return True
    return False

def alone(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    
    return True and three(n)

count = 0

for i in range(a, b+1):
    if alone(i):
        count += 1

print(count)



