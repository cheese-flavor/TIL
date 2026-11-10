s = list(input())

for i in range(len(s)):
    if s[i] == 'e':
        s.pop(i)
        print(''.join(s))
        break

