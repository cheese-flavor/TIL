# BOJ 14891 톱니바퀴 — 채팅 기반 리스트 수정본, 제출 원문 미대조
'''
톱니바퀴 4개 / 12시방향 = [0], 시계방향 순
[0] N이면 0점, s면 아래와 같이
1번 1점, 2번 2점, 3번 4점, 4번 8점
톱니간의 접점은 [2] <-> [6]
방향 = 1 시계 방향, -1 반시계 방향
'''

# 초기 설정
t = [str(input()) for _ in range(4)] # 그냥 리스트로 종합 처리해보자 
k = int(input())

for _ in range(k):
    num, d = map(int, input().split())
    d_list = [0, 0, 0, 0] #톱니 이동을 한다 안한다만
    d_list[num-1] = 1
    
    # 이동 여부 확인 / 이걸 조금 더 간결하게
    # 하향식 확인
    if num != 1:
        for i in range(num-1, 0, -1):
            if t[i-1][2] != t[i][6]:
                d_list[i-1] = 1
            else:
                break
                
    # 상향식 확인
    if num != 4:
        for i in range(num-1, 3):
            if t[i][2] != t[i+1][6]:
                d_list[i+1] = 1
            else:
                break
    
    # 톱니 수정
    for i in range(4):
        if d_list[i] == 1: # 회전여부 파악
            if abs((num-1)-i) % 2 == 0: #2칸 차이면 회전방향이 동일하니까
                if d == 1:
                    t[i] = t[i][-1]+t[i][:-1]
                else:
                    t[i] = t[i][1:]+t[i][0]
                    
            else: # 회전방향 반대로 계산
                if d == 1:
                    t[i] = t[i][1:]+t[i][0]
                else:
                    t[i] = t[i][-1]+t[i][:-1]

# 각 바퀴별 [0]값 계산
answer = 0

for i in range(4):
    if t[i][0] == '1':
        answer += 2**i
        
print(answer)
