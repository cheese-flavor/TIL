a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def mull(a,o,c):
    if o == '+':
        return a+c
    elif o == '-':
        return a-c
    elif o == '*':
        return a*c
    elif o == '/':
        return int(a/c)
    else:
        return False
if mull(a,o,c):
    print(a, o, c, '=', mull(a,o,c))
else:
    print('False')
