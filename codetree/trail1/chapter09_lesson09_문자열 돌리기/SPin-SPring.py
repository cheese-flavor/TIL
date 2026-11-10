s= input()
l = len(s)

print(s)
for i in range(l):
    s = list(s)
    a = s.pop()
    s = a+(''.join(s))
    print(s)
