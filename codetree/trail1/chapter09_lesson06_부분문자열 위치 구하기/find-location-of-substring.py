input_str = input()
target_str = input()

# Please write your code here.
possible = True

if target_str in input_str:
    print(input_str.index(target_str))
    possible = False
    
if possible:
    print(-1)

'''
for i in range(len(input_str)-len(target_str)+1):
    if target_str == input_str[i:i+len(target_str)]:
        print(i)
        possible = False
        break

if possible:
    print(-1)
'''
