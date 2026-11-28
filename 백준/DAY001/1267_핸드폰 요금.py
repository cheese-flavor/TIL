# 플랫폼: 백준 (BOJ)
# 회차: DAY001
# 문제: 1267 - 핸드폰 요금
# 난이도: Bronze III (기존 배정 기준, 최신 메타데이터 미검증)
# 링크: https://acmicpc.net/problem/1267
# 채점: 정답 (사용자 확인)
# 시간복잡도: O(N)
# 공간복잡도: O(N)

#영식은 Y로, 민식은 M으로 출력
n = int(input())
call = list(map(int, input().split()))
y, m = 0, 0

for c in call:
    y += (c // 30+1) * 10
    m += (c // 60+1) * 15
    
if y < m:
    print('Y', y)
elif y > m:
    print('M', m)
else:
    print('Y', 'M', y)
