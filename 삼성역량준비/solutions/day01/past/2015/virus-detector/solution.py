# Day 01 | 학습 시작: 2026-11-11 | 풀이 기록: 2026-11-12
# 삼성 SW 역량테스트 기출 | 2015년 | Level 4
# Problem: 바이러스 검사
# URL: https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/virus-detector/description
# Submission: 수정한 두 번째 풀이 (코드트리 정답)
# 원본 실행 로직 보존. 문제 정보만 주석으로 추가.

n = int(input())
people = list(map(int, input().split()))
tl, tm = map(int, input().split())

#검사자수 총합
sum_p = 0

#식당별 검사자수 파악
for i in range(n):

    #팀장만으로 가능하게 되면 넘기기
    if people[i] < tl:
        continue

    #팀원이 필요한 경우
    else:
        p = people[i] - tl

        #나머지 보다 한명 더 많게
        if p % tm == 0:
            sum_p += (p//tm)
        else:
            sum_p += (p//tm +1)

print(sum_p+n)
