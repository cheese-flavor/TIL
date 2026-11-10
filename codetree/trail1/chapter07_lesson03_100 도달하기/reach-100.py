n = int(input())

result = 1+n

print(1, end =' ')
print(n, end = ' ')


while result <= 100:
    print(result, end = ' ')

    second = result
    result += n
    n = second
print(result, end = ' ')

