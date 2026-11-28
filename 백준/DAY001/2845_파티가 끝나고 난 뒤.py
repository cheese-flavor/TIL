# 플랫폼: 백준 (BOJ)
# 회차: DAY001
# 문제: 2845 - 파티가 끝나고 난 뒤
# 난이도: Bronze IV (기존 배정 기준, 최신 메타데이터 미검증)
# 링크: https://acmicpc.net/problem/2845
# 채점: 정답 (사용자 확인)
# 시간복잡도: O(1)
# 공간복잡도: O(1)

n, m = map(int, input().split())
paper = list(map(int, input().split()))

for i in range(len(paper)):
    print(paper[i] - n * m, end = ' ')
