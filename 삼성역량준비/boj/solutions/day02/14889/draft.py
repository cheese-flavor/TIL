n = int(input())
player = [list(map(int, input().split())) for _ in range(n)]

# 기본 정의
answer = float('inf')

def dfs(start, a):
    global answer
    
    # 종료 조건(A팀 구성이 완료) 차이값 min으로
    if len(a) == n//2:
        b = []
        
        #A에 없는 애들로 B 구성
        for i in range(n):
            if i not in a:
                b.append(i)
        
        #A스탯과 B스탯 계산
        a_stat, b_stat = 0, 0
        for i in range(len(a)-1):
            for j in range(i+1, len(a)):
                a_stat += (player[a[i]][a[j]] + player[a[j]][a[i]])
                
        for i in range(len(b)-1):
            for j in range(i+1, len(b)):        
                b_stat += (player[b[i]][b[j]] + player[b[j]][b[i]])
                
        #차이값 최소
        answer = min(answer, abs(a_stat - b_stat))
        return
    
    for i in range(start, n):
        a.append(i)
        dfs(i+1, a)
        a.pop()

dfs(0, [])
print(answer)
