# 플랫폼: 백준 (BOJ)
# 회차: DAY001
# 문제: 1330 - 두 수 비교하기
# 난이도: Bronze V (기존 배정 기준, 최신 메타데이터 미검증)
# 링크: https://acmicpc.net/problem/1330
# 채점: 정답 (사용자 확인)
# 시간복잡도: O(1)
# 공간복잡도: O(1)

A, B= map(int,input().split())
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")
