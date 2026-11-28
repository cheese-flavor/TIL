# 플랫폼: 백준 (BOJ)
# 회차: DAY001
# 문제: 11365 - !밀비 급일
# 난이도: Bronze IV (기존 배정 기준, 최신 메타데이터 미검증)
# 링크: https://acmicpc.net/problem/11365
# 채점: 정답 (사용자 확인)
# 시간복잡도: O(Σ L²) (최악)
# 공간복잡도: O(max L)

while True:
    l = input()
    if l != 'END':
        answer = ''
        for i in range(len(l)-1, -1, -1):
            answer += l[i]
        print(answer)
        
    else:
        break
