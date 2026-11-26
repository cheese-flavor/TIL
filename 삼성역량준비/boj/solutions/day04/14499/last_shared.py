'''
n*m 지도 / 오른쪽은 동쪽, 위쪽은 북쪽 / 초기 주사위는 모두 0
  2
4 1 3   1이 맨위, 3이 오른쪽
  5
  6     6이 바닥
  
이동 칸이 0이면, 주사위 바닥 -> 칸으로 
이동 칸이 0이 x, 칸 -> 주사위 바닥 / 칸 = 0  
주사위 이동마다 상단에 쓰인값 구하기 (지도 바깥으로 이동 x -> 무시됨 / 출력 x)
'''
n, m, x, y, k = map(int, input().split()) #가로, 세로, x, y, 명령
dice_map = [list(map(int, input().split())) for _ in range(n)]
direction = [map(int, input().split())]
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

lr = [1, 3, 6, 4] # 주사위 좌우
ud = [1, 5, 6, 2] # 주사위 위아래
dice_score = [0] * 6 #주사위 점수 보관 리스트


for d in direction:
    nr, nc = x + dr[d], y + dc[d]
    
    if 0 <= nr < n and 0 <= nc < m: # 내부 경로에 진입 여부
        x, y = nr, nc
        
        # 주사위 바꾸기(동쪽 1, 서쪽 2, 북쪽 3, 남쪽 4)
        if d == 1:
            lr = [lr.pop()]+lr
            ud[0], ud[2] = lr[0], lr[2]
            
        elif d == 2:
            lr = lr[1:]+lr[0]
            ud[0], ud[2] = lr[0], lr[2]

        elif d == 3:
            ud = ud[1:]+ud[0]
            lr[0], lr[2] = ud[0], ud[2] 
        
        else:
            ud = [ud.pop()]+ud
            lr[0], lr[2] = ud[0], ud[2]
        
        # 점수 교환
        if dice_map[x][y] == 0:
            dice_map[x][y] = dice_score[lr[2]-1]
            
        else:
            dice_score[lr[2]-1] = dice_map[x][y]
            dice_map[x][y] = 0
            
        print(dice_score[lr[0]-1])
