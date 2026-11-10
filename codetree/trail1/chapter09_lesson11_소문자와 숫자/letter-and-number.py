arr = input()
s = ''
for c in arr:
    if c.isdigit() or c.isalpha():
        s += c

print(s.lower())
