# 플랫폼: 백준 (BOJ)
# 회차: DAY001
# 문제: 1100 - 하얀 칸
# 난이도: Bronze II (기존 배정 기준, 최신 메타데이터 미검증)
# 링크: https://acmicpc.net/problem/1100
# 채점: 정답 (사용자 확인)
# 시간복잡도: O(1) (8×8 고정)
# 공간복잡도: O(1) (8×8 고정)

board = [list(input()) for _ in range(8)]
answer = 0
for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0:
            if board[i][j] == 'F':
                answer += 1
        elif i % 2 == 1 and j % 2 == 1:
            if board[i][j] == 'F':
                answer += 1
print(answer)
