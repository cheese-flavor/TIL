n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def check(a, b):
    l = len(b)
    for i in range(len(a)):
        if a[i:i+l] == b:
            return 'Yes'
    return 'No'

print(check(a,b))

