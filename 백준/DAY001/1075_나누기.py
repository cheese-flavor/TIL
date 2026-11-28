# 플랫폼: 백준 (BOJ)
# 회차: DAY001
# 문제: 1075 - 나누기
# 난이도: Bronze II (기존 배정 기준, 최신 메타데이터 미검증)
# 링크: https://acmicpc.net/problem/1075
# 채점: 정답 (사용자 확인)
# 시간복잡도: O(1)
# 공간복잡도: O(1)

n = int(input())
f = int(input())

n = (n//100)*100

for i in range(100):
    if (n+i) % f == 0:
        n = n+i
        print(str(n)[-2:])
        break
