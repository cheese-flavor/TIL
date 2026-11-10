a = list(input())
b = list(input())
possible = True
for i in range(len(b)):
    if a == b:
        print(i)
        possible = False
        break

    else:
        c = a.pop()
        c += ''.join(a)
        a = list(c)

if possible:
    print(-1)





