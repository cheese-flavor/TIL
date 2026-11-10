n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort(reverse = True)

max_list = []
max_count = []

for n in nums:
    if n in max_list:
        max_count[max_list.index(n)] += 1
    else:
        max_list.append(n)
        max_count.append(1)

possible = True

for i in range(len(max_count)):
    if max_count[i] == 1:
        possible = False
        print(max_list[i])
        break

if possible:
    print(-1)

