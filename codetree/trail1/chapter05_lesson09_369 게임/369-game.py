n = int(input())
for i in range(1, n+1):
    count = 0
    if len(str(i)) == 1:
        if i in [3,6,9]:
            print(0, end = ' ')
        else:
            print(i, end = ' ')
    else:
        for j in range(len(str(i))):
            if count == 0 and int(str(i)[j]) in [3,6,9]:
                print(0, end = ' ')
                count += 1
        if count == 0:
            if i % 3 == 0:
                print(0, end = ' ')
            else:
                print(i, end = ' ')

                



