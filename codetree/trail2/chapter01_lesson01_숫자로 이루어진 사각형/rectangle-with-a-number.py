n = int(input())

# Please write your code here.

def rectangle(n):
    num = 1
    for _ in range(n):
        num_s = ''
        for _ in range(n):
            num_s += str(num)

            if len(num_s) == n:
                print(' '.join(num_s))

            if num == 9:
                num = 1
            else:
                num += 1

rectangle(n)


