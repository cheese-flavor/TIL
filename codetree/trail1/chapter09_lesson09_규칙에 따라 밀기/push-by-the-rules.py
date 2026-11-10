a = input()
command = list(input())

for i in command:
    a = list(a)
    if i == 'L':
        c = a.pop(0)
        a = ''.join(a) + c
    else:
        c = a.pop()
        a = c + ''.join(a)

print(a)


