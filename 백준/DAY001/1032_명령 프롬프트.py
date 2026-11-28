# 플랫폼: 백준 (BOJ)
# 회차: DAY001
# 문제: 1032 - 명령 프롬프트
# 난이도: Bronze I (기존 배정 기준, 최신 메타데이터 미검증)
# 링크: https://acmicpc.net/problem/1032
# 채점: 정답 (사용자 확인)
# 시간복잡도: O(NM)
# 공간복잡도: O(NM)

n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

sen = list(arr[0])

for i in range(1, n):
    for j in range(len(sen)):
        if sen[j] != arr[i][j]:
            sen[j] = '?'

print(''.join(sen))
