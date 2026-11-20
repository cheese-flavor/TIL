n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
# 1초에 한칸씩만 움직이는 로봇 2개
# 다른곳에 있다가 같이 합쳐지는 경우의 수
# 처음에 같이 있기는하는데, 이건 그냥 -1 하면 될듯?
# n개까지 a, m개까지 b / 시작점을 둘다 0으로 두면 될듯

#print(t,d) 확인용
#print(t_b, d_b)

list_a, list_b = [], []
a, b = 0, 0

# 각각 리스트 만들기
for i in range(n):
    if d[i] == 'L':
        for _ in range(t[i]):
            a -= 1
            list_a.append(a)
    else:
        for _ in range(t[i]):
            a += 1
            list_a.append(a)

for i in range(m):
    if d_b[i] == 'L':
        for j in range(t_b[i]):
            b -= 1
            list_b.append(b)
    else:
        for j in range(t_b[i]):
            b += 1
            list_b.append(b)

# a를 긴쪽으로 만들기
if len(list_a) < len(list_b):
    list_a, list_b = list_b, list_a

# 비교 진행
count = 0
possible = False
x, y = len(list_a), len(list_b)

# 짧은 길이만큼 비교
for i in range(y):
    if possible and list_a[i] == list_b[i]:
        count += 1
        possible = False
    elif not possible and list_a[i] != list_b[i]:
        possible = True

# 길이가 같지 않을때
if x-y > 0:
    for i in range(y, x):

        # 0이 없으니까 한쪽만 움직여서 무조건 같거나 다름 상태가 됨
        if list_b[-1] == list_a[i]:
            count += 1


print(count)
    

