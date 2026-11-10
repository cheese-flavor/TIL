a = input()
b = input()

def num(s, n):
    for c in s:
        if c.isdigit():
            n += c
    return n

a_num=''
b_num=''
a_num = num(a, a_num)
b_num = num(b, b_num)

print(int(a_num) + int(b_num))


