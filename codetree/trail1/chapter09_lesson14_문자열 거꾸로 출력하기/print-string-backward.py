for _ in range(10):
    s = input()
    if s == 'END':
        break
    else:
        for i in range(len(s)-1, -1, -1):
            print(s[i], end ='')
        print()
