arr = [list(map(int, input().split())) for _ in range(2)]

for i in range(2):
    print(f"{sum(arr[i])/4:0.1f}", end= ' ')
print()

for j in range(4):
    k = 0
    for i in range(2):
        k += arr[i][j]
    print(f"{k/2:0.1f}", end = ' ')
print()
        
print(f"{(sum(arr[0])+sum(arr[1]))/8:0.1f}")
