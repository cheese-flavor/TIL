sen = []
for _ in range(10):
    sen.append(input())

c = input()
possible = True
for s in sen:
    if s[-1] == c:
        print(s)
        possible = False

if possible:
    print(None)
