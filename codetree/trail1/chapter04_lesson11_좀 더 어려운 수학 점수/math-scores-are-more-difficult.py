a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

if a1 > b1:
    print('A')
elif a1 < b1:
    print('B')
else:
    if a2 > b2:
        print('A')
    elif a2 < b2:
        print('B')

