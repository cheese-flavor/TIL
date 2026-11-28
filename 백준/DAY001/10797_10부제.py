# 플랫폼: 백준 (BOJ)
# 회차: DAY001
# 문제: 10797 - 10부제
# 난이도: Bronze IV (기존 배정 기준, 최신 메타데이터 미검증)
# 링크: https://acmicpc.net/problem/10797
# 채점: 정답 (사용자 확인)
# 시간복잡도: O(1)
# 공간복잡도: O(1)

n = int(input())
car = list(map(int, input().split()))
count = 0

for i in range(5):
    if car[i] == n:
        count += 1
        
print(count)
