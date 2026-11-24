N = int(input())
T, P = [], [] #상담시간, 금액

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

answer = 0

#재귀함수로 풀기
def dfs(day, profit):
    global answer
    
    # 종료조건
    if day == N:
        answer = max(answer, profit)
        return
    
    # 현재 날짜를 넣는 경우
    if day+T[day] <= N:
        dfs(day+T[day], profit + P[day])
    
    # 넣지 않는 경우
    dfs(day+1, profit)
        
            
dfs(0, 0)
print(answer)
