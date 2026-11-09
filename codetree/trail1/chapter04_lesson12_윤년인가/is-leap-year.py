y= int(input())
possible = True

if y % 4 == 0:
    if y % 100 == 0 and y % 400 != 0:
        print('false')
        possible = False
    if possible:
       print('true')
else:
    print('false')
