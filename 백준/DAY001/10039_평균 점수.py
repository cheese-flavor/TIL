# 플랫폼: 백준 (BOJ)
# 회차: DAY001
# 문제: 10039 - 평균 점수
# 난이도: Bronze IV (기존 배정 기준, 최신 메타데이터 미검증)
# 링크: https://acmicpc.net/problem/10039
# 채점: 정답 (사용자 확인)
# 시간복잡도: O(1)
# 공간복잡도: O(1)

answer = 0
score = [int(input()) for _ in range(5)]
for i in range(5):
    if score[i] >= 40:
        answer += score[i]
    else:
        answer += 40

print(answer//5)
