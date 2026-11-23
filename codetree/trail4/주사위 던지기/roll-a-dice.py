n, m, r, c = map(int, input().split())
directions = list(input().split())

# Please write your code here.
# 좌 우 배열 최신화 / 상 하 배열 최신화 / 평면 최신화(0으로 우선 만들면 되겠다)
# 배열 내에서 i/j로 찍는 부분을 두고 이동만 하고, 그에 따른 상하 -> 좌우 최신화 / 좌우 -> 상하 최신
# 배열 넘어가면 이동 생략됨
# n = 격자 크기, m = 주사위 횟수, rc 시작위치, L R D U =  왼 오 아래 위

#격자판 0으로 전체 생성후 최종 후 전체 합 구하기
ground = [[0] * n for _ in range(n)]
#print(ground)

lr = [6, 3, 1, 4]  #좌우 배열
ud = [6, 5, 1, 2]  #상하 배열
i, j = 0, 0 #각 배열별 포인터
r, c = r-1, c-1
ground[r][c] = 6 #초기값 설정

for k in range(m):
    if directions[k] == 'L':
        if 0 <= c-1:
            c -= 1

            i = (i-1) % 4

            ground[r][c] = lr[i]
            ud[j] = lr[i]
            ud[(j+2)%4] = lr[(i+2)%4]

    elif directions[k] == 'R':
        if n > c+1:
            c += 1
            i = (i+1) % 4

            ground[r][c] = lr[i]
            ud[j] = lr[i]
            ud[(j+2)%4] = lr[(i+2)%4]
    
    elif directions[k] == 'D':
        if n > r+1:
            r += 1
            j = (j-1) % 4
            
            ground[r][c] = ud[j]
            lr[i] = ud[j]
            lr[(i+2)%4] = ud[(j+2)%4]

    else:       
        if 0 <= r-1:
            r -= 1
            j = (j+1) % 4

            ground[r][c] = ud[j]
            lr[i] = ud[j]
            lr[(i+2)%4] = ud[(j+2)%4]

#print(ground)

# 전체 행 돌면서 합 계산하기
answer = 0

for t in range(n):
    answer += sum(ground[t])

print(answer)