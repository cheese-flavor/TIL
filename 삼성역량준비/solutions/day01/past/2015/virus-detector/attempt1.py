# Day 01 | 학습 시작: 2026-11-11 | 풀이 기록: 2026-11-12
# 삼성 SW 역량테스트 기출 | 2015년 | Level 4
# Problem: 바이러스 검사
# URL: https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/virus-detector/description
# Submission: 첫 풀이 (코드트리 히든 케이스 오답)
# 원본 실행 로직 보존. 문제 정보만 주석으로 추가.

# n개의 식당에 있는 고객들의 체온 측정
# 검사팀장과 검사팀원 => 팀장과 팀원이 검사하는 고객수는 다름
# 가게별 팀장은 오직 한명, 팀원은 여러명 / 가게당 팀장 한명 무조건 필수
# 검사자수 최솟값 구하기
# 팀장이 그냥 할 수 있는 것 / 필요한 팀원
# 우선 각 팀장들을 식당별로 배치 / 가용인원을 넘을 때 팀원을 추가하는 형태
# 팀장을 한명으로 고정 / 각각 배열마다 남은거 % +1 형태로

'''
1. 식당수
2. 각 식당별 고객 수
3. 검사팀장 검사 최대 수, 검사팀원 검사 최대 수
'''
n = int(input())
people = list(map(int, input().split()))
tl, tm = map(int, input().split())

#검사자수 총합
sum_p = 0

#식당별 검사자수 파악
for i in range(n):
    p = people[i] - tl

    if p % tm == 0:
        sum_p += (p//tm)
    else:
        sum_p += (p//tm +1)

print(sum_p+n)
