# BOJ 15686 치킨 배달 | Gold V(공개 자료 기준)
# https://www.acmicpc.net/problem/15686
# 마지막 공유 코드에서 dfs 호출의 i를 m으로 수정한 정리본. 실제 제출 원문 미대조.
'''
각 칸: 빈 칸 0, 집 1, 치킨집 2
최소 거리수 / 제한 매장 내로 /
'''

# 초기 설정
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

house, chicken, chicken_street = [], [], []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i,j])
        elif arr[i][j] == 2:
            chicken.append([i, j])
            
# m개 당 가능한 치킨집 조합            
def dfs(idx, start, num, semi_street):
    global chicken_street
    
    if idx == num:
        chicken_street.append(semi_street[:])
        return
    
    for i in range(start, len(chicken)):
        semi_street.append(chicken[i])
        dfs(idx+1, i+1, num, semi_street)
        semi_street.pop()

answer = float('inf')
        
#제한개수별 치킨집 조합과 최소거리 구하기
# for i in range(1, m+1): 결국 똑같다는데 잘 모르겠

dfs(0, 0, m, [])
for comb in chicken_street:
    comb_cal = 0 #조합별 최소거리
    
    for r2, c2 in house:
        home_cal = float('inf') #하나의 집에서 최소거리
        
        for r1, c1 in comb:
            home_cal = min(home_cal, abs(r1-r2)+abs(c1-c2))
        comb_cal += home_cal # 각 집별 최소 거리 조합 합
        
    answer = min(answer, comb_cal) # 최종 최소 거리

print(answer)
