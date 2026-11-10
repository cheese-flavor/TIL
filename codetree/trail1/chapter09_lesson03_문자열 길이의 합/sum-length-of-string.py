n = int(input())
a_count = 0
l_count = 0

for _ in range(n):
    s = input()
    if s[0] == 'a':
        a_count += 1
    
    l_count += len(s)

print(l_count, a_count)
