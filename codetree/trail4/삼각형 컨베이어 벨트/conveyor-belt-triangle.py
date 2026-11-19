n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.

# 1자형 리스트를 만들고, 시간마다 맨앞에껄 빼서 맨 뒤에 추가하는 형태로
line = l + r + d

for i in range(t):
    tmp = []
    tmp.append(line.pop())
    line = tmp+line

count = 0
for i in range(len(line)):
    print(line[i], end = ' ')
    count += 1

    if count == n:
        print()
        count = 0


