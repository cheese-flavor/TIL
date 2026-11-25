# BOJ 14888 연산자 끼워넣기
# 채팅 기반 정리본: 이전 사용자 정수 나눗셈 분기 복원, 제출 원문 미대조
n = int(input())
num = list(map(int, input().split()))
cal = list(map(int, input().split()))

max_answer = -1000000000
min_answer = 1000000000

def dfs(idx, value):
    global max_answer
    global min_answer
    
    # 종료 조건부터 생각하기
    if idx == n:
        max_answer = max(max_answer, value)
        min_answer = min(min_answer, value)
        return
    
    # 사칙연산별로 진행
    if cal[0] > 0:
        cal[0] -= 1
        dfs(idx+1, value+num[idx])
        cal[0] += 1
    
    if cal[1] > 0:
        cal[1] -= 1
        dfs(idx+1, value-num[idx])
        cal[1] += 1
    
    if cal[2] > 0:
        cal[2] -= 1
        dfs(idx+1, value*num[idx])
        cal[2] += 1
    
    if cal[3] >0:
        cal[3] -= 1
        if value < 0:
            dfs(idx+1, -(abs(value)//num[idx]))
        else:
            dfs(idx+1, value//num[idx])
        cal[3] += 1
        
dfs(1, num[0])
print(max_answer)
print(min_answer)
