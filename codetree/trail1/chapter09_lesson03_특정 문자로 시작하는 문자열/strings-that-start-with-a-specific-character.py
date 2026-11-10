n = int(input())
sen = [input() for _ in range(n)]
'''
for _ in range(n):
    s = input()
    sen.append(s)
'''
c = input()

count = 0
len_sum = 0

for s in sen:
    if s[0] == c:
        count += 1
        len_sum += len(s)

print(count, f"{round((len_sum/count),2):0.2f}")



