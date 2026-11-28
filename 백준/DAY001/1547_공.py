# 플랫폼: 백준 (BOJ)
# 회차: DAY001
# 문제: 1547 - 공
# 난이도: Bronze III (기존 배정 기준, 최신 메타데이터 미검증)
# 링크: https://acmicpc.net/problem/1547
# 채점: 정답 (사용자 확인)
# 시간복잡도: O(N)
# 공간복잡도: O(1)

n = int(input())
cup = [1, 2, 3]

for _ in range(n):
    c1, c2 = map(int, input().split())
    index1 = cup.index(c1)
    index2 = cup.index(c2)
    cup[index1], cup[index2] = c2, c1

print(cup[0])
