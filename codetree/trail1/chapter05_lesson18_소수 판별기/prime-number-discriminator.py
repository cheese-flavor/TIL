n = int(input())
possible = False

for i in range(2, n//2+1):
    if n % i == 0:
        print('C')
        possible = True
        break

if not possible:
    print('P')
