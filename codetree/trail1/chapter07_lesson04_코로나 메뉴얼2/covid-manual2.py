a_count, b_count, c_count, d_count = 0, 0, 0, 0

for _ in range(3):
    o, t = input().split()

    if o == 'Y':
        if int(t) >= 37:
            a_count += 1
        else:
            c_count += 1
    if o == 'N':
        if int(t) >= 37:
            b_count += 1
        else:
            d_count += 1
print(a_count, b_count, c_count, d_count, end = ' ')
if a_count >= 2:
    print('E')




    
