# Day 02 | 2026-11-12
# Trail 2 | Chapter 05: dx dy technique | Lesson 03: dx dy technique
# Problem: 격자 위의 편안한 상태
# URL: https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-comfortable-state-on-the-grid/description
# Result: 검토 중인 오답 변형, 제출 여부 미확인 (사용자 보고)
# 채팅에 공유된 제출 코드의 서식 강조만 정상 Python 문법으로 복원; 실행 로직 보존

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
space = [[0]*n for _ in range(n)]
mv = [-1, 0, 1, 0, 0, -1, 0, 1]

for i in range(m):
    #해당 격자 1로 변경
    c, r = points[i][0]-1, points[i][1]-1
    space[c][r] = 1

    #편안한 상태 점검 // 가지치기를 더 진행해보는 방향으로
    count = 0
    stop = 0

    for i in range(0, 8, 2):
        new_c, new_r = c+mv[i], r+mv[i+1]

        if 0 <= new_c < n and 0 <= new_r < n:
            if space[new_c][new_r] == 1:
                count += 1
            else:
                stop += 1
        else:
            stop += 1

        if stop == 2:
            print(0)
            break

    if count == 3:
        print(1)

    else:
        print(0)
