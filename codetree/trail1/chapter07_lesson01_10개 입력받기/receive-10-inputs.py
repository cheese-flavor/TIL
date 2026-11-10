num = list(map(int, input().split()))
possible = True

for i in range(len(num)):
    if num[i] == 0:
        print(f"{sum(num[:i])} {sum(num[:i])/i:0.1f}")
        possible = False
        break

if possible:
    print(f"{sum(num)} {sum(num)/len(num):0.1f}")

