M, D = map(int, input().split())

# Please write your code here.
def check(m, d):
    y = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if m <= 12:
        if y[m-1] >= d:
            return 'Yes'
    
    return 'No'

print(check(M, D))
