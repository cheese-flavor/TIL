sum, count = 0, 0
while True:
    n = int(input())

    if abs(n - 20) < 10:
        sum += n
        count += 1
    
    else:
        break

print(f"{sum/count:0.2f}")
