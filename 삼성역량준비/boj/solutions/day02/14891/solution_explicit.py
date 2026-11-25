'''
톱니바퀴 4개 / 12시방향 = [0], 시계방향 순
[0] N이면 0점, s면 아래와 같이
1번 1점, 2번 2점, 3번 4점, 4번 8점
톱니간의 접점은 [2] <-> [6]
'''

# 초기 설정
t1 = str(input())
t2 = str(input())
t3 = str(input())
t4 = str(input())
k = int(input())

for _ in range(k):
    num, d = map(int, input().split())
    
    # 각 톱니별로 어떻게 움직이는지를 미리 다 구현해두면 될지도?
    # dfs로 양방향 진행하는걸 해볼까
    # 일단 4개만 진행하면 되니까 그냥 빡구현으로
    
    # 회전 형태 여부 정의
    check12 = t1[2] != t2[6]
    check23 = t2[2] != t3[6]
    check34 = t3[2] != t4[6]
    
    # 1 시작
    if num == 1:
        if d == 1:
            t1 = t1[-1]+t1[:-1]
        else:
            t1 = t1[1:]+t1[0]
            
        # 2와 비교
        if check12:
            if d == 1:
                t2 = t2[1:]+t2[0]
            else:
                t2 = t2[-1]+t2[:-1]
            
            # 3과 비교
            if check23:
                if d == 1:
                    t3 = t3[-1]+t3[:-1]
                else:
                    t3 = t3[1:]+t3[0]
                
                # 4와 비교
                if check34:
                    if d == 1:
                        t4 = t4[1:]+t4[0]
                    else:
                        t4 = t4[-1]+t4[:-1]
    # 2 시작
    if num == 2:
        if d == 1:
            t2 = t2[-1]+t2[:-1]
        else:
            t2 = t2[1:]+t2[0]
            
        # 3과 비교
        if check23:
            if d == 1:
                t3 = t3[1:]+t3[0]
            else:
                t3 = t3[-1]+t3[:-1]
            
            # 4와 비교
            if check34:
                if d == 1:
                    t4 = t4[-1]+t4[:-1]
                else:
                    t4 = t4[1:]+t4[0]
        # 1과 비교
        if check12:
            if d == 1:
                t1 = t1[1:]+t1[0]
            else:
                t1 = t1[-1]+t1[:-1]
                
    # 3 시작
    if num == 3:
        if d == 1:
            t3 = t3[-1]+t3[:-1]
        else:
            t3 = t3[1:]+t3[0]
            
        # 4와 비교
        if check34:
            if d == 1:
                t4 = t4[1:]+t4[0]
            else:
                t4 = t4[-1]+t4[:-1]
                
        # 2와 비교
        if check23:
            if d == 1:
                t2 = t2[1:]+t2[0]
            else:
                t2 = t2[-1]+t2[:-1]
            
            # 1과 비교
            if check12:
                if d == 1:
                    t1 = t1[-1]+t1[:-1]
                else:
                    t1 = t1[1:]+t1[0]
                    
    # 4 시작
    if num == 4:
        if d == 1:
            t4 = t4[-1]+t4[:-1]
        else:
            t4 = t4[1:]+t4[0]
                
        # 3과 비교
        if check34:
            if d == 1:
                t3 = t3[1:]+t3[0]
            else:
                t3 = t3[-1]+t3[:-1]
            
            # 2와 비교
            if check23:
                if d == 1:
                    t2 = t2[-1]+t2[:-1]
                else:
                    t2 = t2[1:]+t2[0]
                
                # 1과 비교
                if check12:
                    if d == 1:
                        t1 = t1[1:]+t1[0]
                    else:
                        t1 = t1[-1]+t1[:-1]

# 각 바퀴별 [0]값 계산
answer = 0

if t1[0] == '1':
    answer += 1
if t2[0] == '1':
    answer += 2
if t3[0] == '1':
    answer += 4
if t4[0] == '1':
    answer += 8

print(answer)
