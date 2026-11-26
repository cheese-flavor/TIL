'''
0, 0 = 1, 1
n = 교실크기, n제곱 = 학생수
인접 = 상하좌우용으로만

1. 비어있는 칸 중 좋아하는 학생 인접칸에 가장 많은 칸으로 자리 정함
2. 1을 만족하는 칸이 여러 개, 인접칸 중에서 빈칸이 가장 많은 칸으로 자리를 정함
3. 2를 만족하는 칸도 여러 개, 행의 번호가 가장 작은 칸으로 정함
   그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로
   
결과: 만족도 (학생과 인접한 칸에 앉은 좋아하는 학생의 수)(10**n)
'''
# 초기 설정
n = int(input())
favorite = [list(map(int, input().split())) for _ in range(n**2)]
final_room = [[0]*n for _ in range(n)] #최종룸

# 상하좌우 탐색
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

#배치 코드
for i in range(n**2):

    #1. 좋아하는 학생 기반        
    # 인접점수 매기기
    favorite_room = [[0]*n for _ in range(n)] # 점수용 룸 배열 생성
    for r in range(n):
        for c in range(n):
            if final_room[r][c] in favorite[i][1:]:
                
                # 방향 탐색
                for d in range(4):
                    new_dr, new_dc = r+dr[d], c+dc[d]
                    if 0<= new_dr < n and 0 <= new_dc < n and final_room[new_dr][new_dc] == 0:
                        favorite_room[new_dr][new_dc] += 1
                        
    # 비교해서 리스트 최신화 / 점수마다 최신화 -> 최적화 이후에 따로 하기
    f_score = 0 #최대 스코어
    f_seat = [] #자리 리스트
    for r in range(n):
        for c in range(n):
            
            if fianl_room[r][c] != 0:
                continue
            
            if f_score < favorite_room[r][c]:
                f_score = favorite_room[r][c]
                f_seat = [] #스코어 갱신에 따른 초기화
                f_seat.append([r,c])
            elif f_score == favorite_room[r][c]:
                f_seat.append([r,c])
    
    if len(f_seat) == 1:
        final_room[f_seat[0][0]][f_seat[0][1]] = favorite[i][0]
        continue
        
    #2. 빈칸 기반  
    else:
        # f_seat기반으로 빈칸 인접 룸 생성 / 이후 비교를 실제 룸과
        blank_room = [[0]*n for _ in range(n)] #빈칸 인접 룸
        
        for f in f_seat:
            r, c = f[0], f[1]
            
            # 방향 탐색
            for d in range(4):
                new_dr, new_dc = r+dr[d], c+dc[d]
                if 0<= new_dr < n and 0 <= new_dc < n and final_room[new_dr][new_dc] == 0:
                    blank_room[r][c] += 1
                    
        # 비교해서 리스트 최신화 / 점수마다 최신화 -> 최적화 이후에 따로 하기
        b_score = -1 #최대 스코어
        b_seat = [] #최종 자리
        
        for f in f_seat: # 자리별로 계산
            r, c = f[0], f[1]            
            if b_score < blank_room[r][c]:
                b_score = blank_room[r][c]
                b_seat = [r, c]
                
            elif b_score == blank_room[r][c]:
                if b_seat[0] > r:
                    b_score = blank_room[r][c]
                    b_seat = [r, c]
                elif b_seat[0] == r:
                    if b_seat[1] > c:
                        b_score = blank_room[r][c]
                        b_seat = [r, c]

        final_room[b_seat[0]][b_seat[1]] = favorite[i][0]


#만족도 계산
answer = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        
        for f in favorite:
            if final_room[i][j] == f[0]:
                for d in range(4):
                    new_dr, new_dc = i+dr[d], j+dc[d]
                                
                    if 0 <= new_dr < n and 0 <= new_dc < n :
                        if final_room[new_dr][new_dc] in f[1:]:
                            cnt += 1
        if cnt > 0:
            answer += 10**(cnt-1)
print(answer)
