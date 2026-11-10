min_len = 20
max_len = 0
for _ in range(3):
    s = input()
    min_len = min(min_len, len(s))
    max_len = max(max_len, len(s))

print(max_len-min_len)

