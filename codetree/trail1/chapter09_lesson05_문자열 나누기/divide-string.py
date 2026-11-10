s = ''
n = int(input())
arr = ''.join(input().split())

for i in range(0, len(arr), 5):
    print(arr[i:i+5])
