n, m = map(int,input().split())

if n >= 90:
    if  m >= 95:
        print(100000)
    elif m >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)
