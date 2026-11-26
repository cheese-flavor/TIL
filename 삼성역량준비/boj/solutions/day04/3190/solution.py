# BOJ 3190 뱀 | https://www.acmicpc.net/problem/3190
# 사용자 정답 보고; 실제 제출 원문 미대조. 마지막 공유 코드에서 방향 전환 시점만 수정한 재구성본.
'''
n = 격자 / 0, 0 = 시작 / 뱀 시작 길이 1, 출발 오른쪽

규칙
- 뱀은 몸길이를 늘려 머리를 다음칸에 위치 (매 초마다 이동)
- 벽이나 자기자신의 몸과 부딪히면 게임 끝 (종료 조건)
- 이동 칸에 사과 0, 그 칸에 있던 사과 x -> 꼬리는 움직임 x = 길이가 길어진 상태?
- 이동 칸에 사과 x, 몸길이를 줄여서 꼬리가 위치한 칸을 비움 => 몸길이 변화 x
  -> 이동보다는 앞을 추가하고 뒤를 0으로 바꾸는 느낌으로?
사과의 위치와 뱀의 이동경로가 주어질 때 -> 몇 초에 끝나는지 계산
'''

# 초기 설정
n = int(input())
k = int(input())
time = 0 #시간
snake = [[0, 0]] #뱀이 도착한 위치들

apple = [] #사과 위치
for i in range(k):
    r, c = map(int, input().split())
    apple.append([r-1, c-1])

l = int(input())
direction = [] #방향 위치
for i in range(l):
    x, c = input().split()
    direction.append([int(x), c])

#방향 (오른쪽부터)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d = 0

# 반복
while True:
    time += 1

    #1. 전진 위치 설정
    r, c = snake[0][0] + dr[d], snake[0][1] + dc[d]
    
    #2. 종료조건들
    if 0 <= r < n and 0 <= c < n and [r, c] not in snake:
        snake = [[r, c]] + snake
    else:
        break
        
    #3. 사과 여부
    if [r, c] not in apple:
        snake.pop() #꼬리만 짤리니까
    else:
        apple.remove([r, c])
        
    #4. 이동 완료 후 시간별 방향전환
    if direction and time == direction[0][0]:
        if direction[0][1] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        direction.pop(0)
        
print(time)
