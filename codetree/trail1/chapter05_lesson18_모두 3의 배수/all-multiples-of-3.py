possible = True
for _ in range(5):
    n = int(input())
    
    if n % 3 != 0:
        possible = False
        print(0)
        break

if possible:
    print(1)


