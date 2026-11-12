N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
c, r = 0, 0
sum_dist = 0
possible = False

# 범위 포함 여부로 / 
for i in range(N):
    if not possible:
        
        if dir[i] == 'W':
            for _ in range(1, dist[i]+1):
                r -= 1
                sum_dist += 1

                if c == 0 and r == 0:
                    print(sum_dist)
                    possible = True
                    break

        elif dir[i] == 'E':
            for _ in range(1, dist[i]+1):
                r += 1
                sum_dist += 1

                if c == 0 and r == 0:
                    print(sum_dist)
                    possible = True
                    break
        
        elif dir[i] == 'S':
            for _ in range(1, dist[i]+1):
                c += 1
                sum_dist += 1

                if c == 0 and r == 0:
                    print(sum_dist)
                    possible = True
                    break

        else:
            for _ in range(1, dist[i]+1):
                c -= 1
                sum_dist += 1

                if c == 0 and r == 0:
                    print(sum_dist)
                    possible = True
                    break

if not possible:
    print(-1)
