n = int(input())

# Please write your code here.
def num(n, count):
    for i in range(1, n+1):
        count += i
    return count//10
count = 0
result = num(n, count)
print(result)
