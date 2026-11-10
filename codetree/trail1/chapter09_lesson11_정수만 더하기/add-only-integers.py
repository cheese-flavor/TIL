arr = input()
count = 0

for c in arr:
    if c.isdigit():
        count += int(c)
print(count)
