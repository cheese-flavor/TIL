# BOJ 21608 상어 초등학교 | Gold V (계획 기준)
# https://www.acmicpc.net/problem/21608
# 복습용 개선 코드 (백준 채점 미수행)
n = int(input())

favorite = {}
order = []

for _ in range(n**2):
    student, *likes = map(int, input().split())
    favorite[student] = set(likes)
    order.append(student)

room = [[0] * n for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

# 학생 배치
for student in order:
    best_score = (-1, -1)

    for r in range(n):
        for c in range(n):
            if room[r][c] != 0:
                continue

            like_cnt, blank_cnt = 0, 0

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]

                if 0 <= nr < n and 0 <= nc < n:
                    if room[nr][nc] in favorite[student]:
                        like_cnt += 1
                    elif room[nr][nc] == 0:
                        blank_cnt += 1

            score = (like_cnt, blank_cnt)

            if score > best_score:
                best_score = score
                best_r, best_c = r, c

    room[best_r][best_c] = student

# 만족도 계산
answer = 0
points = [0, 1, 10, 100, 1000]

for r in range(n):
    for c in range(n):
        student = room[r][c]
        cnt = 0

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if 0 <= nr < n and 0 <= nc < n:
                if room[nr][nc] in favorite[student]:
                    cnt += 1

        answer += points[cnt]

print(answer)
