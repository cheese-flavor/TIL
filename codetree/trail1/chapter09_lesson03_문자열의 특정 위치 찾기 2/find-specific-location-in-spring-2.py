sen = ["apple","banana", "grape", "blueberry", "orange"]


c = input()
count = 0

for s in sen:
    if c in s[2:4]:
        print(s)
        count += 1
print(count)
