s= list(input())
c1 = s[0]
c2 = s[1]

for i in range(1, len(s)):
    if s[i] == c2:
        s[i] = c1
print(''.join(s))

