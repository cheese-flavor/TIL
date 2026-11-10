n = int(input())

count = 0
sum = 0

while count < 2:
    sum += n
    print(sum, end =' ')   
    
    if sum % 5 == 0:
        count += 1
