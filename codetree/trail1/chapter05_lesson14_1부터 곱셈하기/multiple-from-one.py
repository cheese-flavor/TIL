N = int(input())
mul = 1

for i in range(1, 11):
    mul *= i

    if mul >= N:
        print(i)
        break
    
