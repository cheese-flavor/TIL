n, q = map(int, input().split())
num = list(map(int, input().split()))

for _ in range(q):
    quest = list(map(int, input().split()))

    if quest[0] == 1:
        print(num[quest[1]-1])
    
    elif quest[0] == 2:

        for k in num:
            if k == quest[1]:
                print(num.index(k)+1)
                possible = False
                break
                
        if quest[1] not in num:
            print(0)
    
    elif quest[0] == 3:
        for j in range(quest[1]-1, quest[2]):
            print(num[j], end = ' ')
        print()

