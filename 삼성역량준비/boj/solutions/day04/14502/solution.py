# BOJ 14502 연구소 | https://www.acmicpc.net/problem/14502
# 사용자 정답 보고. 마지막 공유 코드의 안전 영역 순회 대상을 수정한 재구성본; 실제 제출 원문 미대조.
'''
연구소 크기 n x m / 빈칸 0, 벽 1, 바이러스 2 로 구성
새로 세울 수 있는 벽의 개수 3 (꼭 3개)
안전 영역 크기의 최댓값을 구하는 프로그램
상하좌우만 막기 / 최적화 없이 생각해서 진행 - dfs 
'''
# 초기 설정
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 증가 방향
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

# 벽 3개 리스트 제작 알고리즘
empty = [] # 빈칸 리스트
for r in range(n):
    for c in range(m):
        if lab[r][c] == 0:
            empty.append([r, c])

# 벽 기준 만들기            
wall = []
def wall_create(start, w):
    # 종료 조건
    if len(w) == 3:
        wall.append(w)
        return
    
    # 랜덤하게 들어가니까
    for i in range(start, len(empty)):
        wall_create(i+1, w+[empty[i]])

wall_create(0, [])
          
# 바이러스 퍼지기 알고리즘
virus = [] #바이러스 리스트 생성
v_count = 0 #기존 바이러스 개수
for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            virus.append([i, j])
            v_count +=1
       
def virus_spread(r, c):        

    # 바이러스 퍼지기 종료: 0만 가능하도록
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        
        if 0<= nr < n and 0 <= nc < m and virus_lab[nr][nc] == 0:
            virus_lab[nr][nc] = 2
            virus_spread(nr, nc)
        
answer = 0

# 바이러스 퍼지기
for w in wall:
    # 벽마다 다른 랩 생성
    virus_lab = [row[:] for row in lab]
    for wr, wc in w:
        virus_lab[wr][wc] = 1
        
    semi_answer = 0
    # 바이러스 리스트 기반 펼치기
    for v in virus:
        vr, vc = v[0], v[1]
        virus_spread(vr, vc)
        
    for vs in virus_lab:
        semi_answer += vs.count(0)
        
    answer = max(answer, semi_answer)
    
print(answer)
