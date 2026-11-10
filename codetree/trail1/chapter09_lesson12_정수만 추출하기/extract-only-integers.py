a, b= input().split()
a = list(a)
b = list(b)
ab = 0
a_pos = True
b_pos = True

for i in range(len(a)):
    if not a[i].isdigit():
        ab += int(''.join(a[:i]))
        a_pos = False
        break

if a_pos:
    ab += int(''.join(a))

for j in range(len(b)):
    if not b[j].isdigit():
        ab += int(''.join(b[:j]))
        b_pos = False
        break
        
if b_pos:
    ab += int(''.join(b))

print(ab)
