arr = list(map(int, input().split()))
end = 0


for i in range(len(arr)):
    if arr[i] >= 250:
        end = i
        break

if end:
    f1 = sum(arr[:end])
    f2 = f1/(end)
    print(f"{f1} {f2:0.1f}")

else:
    f1 = sum(arr)
    f2 = sum(arr) / len(arr)
    print(f"{f1} {f2:0.1f}")
