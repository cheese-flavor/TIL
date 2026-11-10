A = input()
B = input()

# Please write your code here.
A = list(A)

while B in ''.join(A):
    for i in range(len(A)-len(B)+1):
        if ''.join(A[i:i+len(B)]) == B:
            for j in range(i+len(B)-1, i-1, -1):
                A.pop(j)
            break

print(''.join(A))
