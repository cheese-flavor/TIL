# 플랫폼: 백준 (BOJ)
# 회차: DAY001
# 문제: 1085 - 직사각형에서 탈출
# 난이도: Bronze III (기존 배정 기준, 최신 메타데이터 미검증)
# 링크: https://acmicpc.net/problem/1085
# 채점: 정답 (사용자 확인)
# 시간복잡도: O(1)
# 공간복잡도: O(1)

x, y, w, h = map(int, input().split())
answer = float('inf')
answer = min(answer, abs(x-w), abs(y-h), x, y)
print(answer)
