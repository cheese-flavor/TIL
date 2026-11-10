arr = input()
s = ''

for c in arr:
    if c.islower():
        s += c.upper()
    else:
        s += c.lower()

print(s)
