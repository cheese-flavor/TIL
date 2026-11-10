s = input()
ee_count = 0
eb_count = 0

for i in range(len(s)-1):
    if s[i:i+2] == 'ee':
        ee_count += 1
    if s[i:i+2] == 'eb':
        eb_count += 1

print(ee_count, eb_count)
