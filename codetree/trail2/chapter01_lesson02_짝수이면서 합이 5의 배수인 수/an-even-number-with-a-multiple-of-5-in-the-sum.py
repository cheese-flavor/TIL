n = int(input())

# Please write your code here.
def magic_num(n):
    return n % 2 == 0 and (int(str(n)[1]) + int(str(n)[0])) % 5 == 0

if magic_num(n):
    print('Yes')
else:
    print('No')
