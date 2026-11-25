'''
길이가 n인 컨베이어 벨트, 2n인 벨트 위아래
1번 칸이 올리는 위치, n번 칸이 내리는 위치
로봇이 올라간 칸의 위치에만 올림 -> 내구도 1 닳음
로봇이 이동하면 그 칸의 내구도 1 닳음

1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 가능하면 이동 
   - 만약 이동할 수 없다면 가만히
   - 로봇이 이동하려는 칸은 비어있으며, 내구도가 1 이상 남아야함
3. 올리는 위치 내구도가 0이 아니면 로봇을 올림
4. 내구도가 0인 칸의 개수가 K개 이상이면 종료 / 그렇지 않으면 1번으로 돌아감

종료되었을 때의 진행중인 단계, 처음 수행되는 단계는 1번째 단계
'''

n, k = map(int, input().split()) #컨베이어 길이, 종료조건
belt = list(map(int, input().split())) # 각 칸별 내구도
loca = [0] * n # 로봇 위치 알려주는 리스트
stop, answer = 0, 0 # 종료 조건 목적, 단계

#하차지점에 따른 자동 제거
def arrive(n):
    if loca[n-1] == 1:
        loca[n-1] = 0

while stop < k:
    answer += 1
    
    # 과정1: 벨트랑 같이 돌리기
    belt = belt.pop()+belt[:-1]
    loca = loca.pop()+loca[:-1]
    
    arrive(n)
    
    # 과정2: 먼저 올라간 로봇부터 이동
    for i in range(n-2, 0, -1):
        if loca[i] == 1 and loca[i+1] == 0 and belt[i+1] > 0:
            belt[i+1] -= 1
            loca[i], loca[i+1] = 0, 1
            arrive(n)
            
            if belt[i+1] == 0:
                stop += 1

    # 과정3: 로봇 올리기
    if belt[0] > 0:
        loca[0] = 1
        belt[0] -= 1
        
        if belt[0] == 0:
            stop += 1
            
print(answer)
