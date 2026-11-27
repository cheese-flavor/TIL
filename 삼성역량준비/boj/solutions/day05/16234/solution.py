# BOJ 16234 인구 이동
# https://www.acmicpc.net/problem/16234
# 채팅 최종 공유본 (실제 제출 원문 미대조)
'''
n = 크기, 1 칸당 나라하나 = 인구수

인구이동 = 하루동안 / 더 할 수 없으면 종료
- 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하 -> 국경선 오픈 
- 국경선이 모두 열렸다면, 인구 이동 시작
- 국경선이 열려있어 인접한 칸만을 이용해 이동, 그 나라를 하루 동안은 연합
- 연합을 이루고 있는 각 칸의 인구수는 int(연합 인구수 / 연합 이루는 칸 개수)
- 연합을 해체하고, 모든 국경선 닫음

각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하기
'''
# 초기 설정
n, L, R = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(n)]
day = 0
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

# dfs로 연합의 연결만들기
def dfs(r, c, g):
    g.append((r, c))
    
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        if (0 <= nr < n and 0 <= nc < n 
            and not visited[nr][nc] 
            and L <= abs(people[r][c] - people[nr][nc]) <= R):
            visited[nr][nc] = True
            dfs(nr, nc, g)

# 전체 탐색
while True:
    visited = [[False]*n for _ in range(n)]
    possible = False #종료 조건으로 쓰려 했는데 애매하네
    
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                group = []
                visited[r][c] = True
                dfs(r, c, group)
                
                #연합끼리 합산 후 분배
                if len(group) > 1:
                    possible = True
                    
                    sum_p = 0
                    for gr, gc in group:
                        #visited[gr][gc] = True  #이미 앞에서 진행중
                        sum_p += people[gr][gc]
                    avg_p = sum_p // len(group)
                
                    for gr, gc in group:
                        people[gr][gc] = avg_p
                        
    if not possible:
        break
    day += 1

print(day)
