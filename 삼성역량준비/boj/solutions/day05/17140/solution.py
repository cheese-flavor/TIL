# BOJ 17140 이차원 배열과 연산
# https://www.acmicpc.net/problem/17140
# 채팅 최종 공유본, 실제 제출 원문 미대조 (최종 출력문 수정 여부 미확인)
'''
크기가 3×3인 배열 A / 배열의 인덱스는 1부터 시작 / 1초마다 배열에 연산 적용

R 연산: 배열 A의 모든 행 정렬 수행 / 행의 개수 ≥ 열의 개수인 경우에 적용
C 연산: 배열 A의 모든 열 정렬 수행 / 행의 개수 < 열의 개수인 경우에 적용
- 정렬시 각각의 수의 횟수 파악
- 수의 등장 횟수가 커지는 순으로, 여러가지면 수가 커지는 순으로 정렬(내림차순)
- 배열 A에 정렬된 결과 다시 넣기
- 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저

ex) [3, 1, 1]에는 3이 1번, 1가 2번 등장 -> [3, 1, 1, 2] 
ex) 3이 1번, 1이 2번, 2가 1번 등장 -> [2, 1, 3, 1, 1, 2]

정렬된 결과를 배열에 다시 넣으면 행 또는 열의 크기가 달라질 수 있다. 
R 연산 -> 가장 큰 행을 기준 / C 연산 -> 가장 큰 열을 기준
행 또는 열의 크기가 커진 곳에는 0이 채워짐(수를 정렬 시 0은 무시) 
ex) [3, 2, 0, 0] = [3, 2]

행 또는 열의 크기가 < 100  -> 처음 100개 제외 버림
배열 A에 들어있는 수와 r, c, k가 주어졌을 때, A[r][c] == k인 최소 시간
'''
r, c, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(3)]
time = 0
r, c = r-1, c-1

# 행/열 변환함수 제작
def trans(a):
    return [list(row) for row in zip(*a)]

# 하나의 행에 대한 연산함수 제작
def operation(row):
    count = {}
    
    #1. 0을 제외한 등장횟수 계산
    for x in row:
        if x == 0:
            continue
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1
    
    #2. 딕셔너리를 튜플 리스트로 변환
    pairs = list(count.items())
    
    #3. 등장횟수, 숫자 기준 정렬
    pairs.sort(key=lambda x: (x[1], x[0]))
    
    # 4. 숫자와 등장 횟수를 순서대로 저장
    result = []

    for num, cnt in pairs:
        result.append(num)
        result.append(cnt)

    # 5. 최대 100개까지만 반환
    return result[:100]

while time <= 100: #100초 지나기전까지
    n, m = len(a), len(a[0])
    if r < n and c < m and a[r][c] == k:
        break
    possible = False
    
    # 100초까지 도달하지 못한 경우
    if time == 100:
        time = -1
        break

    # 행과 열 변경(R, L을 한번에 수행할 수 있도록)
    if n < m:
        a = trans(a)
        possible = True
    
    # 함수실행
    new_a = []
    for row in a:
        new_a.append(operation(row))
    
    # 가장 긴 행 기준 0 채우기
    max_len = 0
    for row in new_a:
        max_len = max(max_len, len(row))
    
    # 길이만큼 0 추가
    for row in new_a:
        row.extend([0] * (max_len - len(row)))
    
    a = new_a

    if possible: # 행렬 변경시 원본으로 변환
        a = trans(a)
    
    time += 1

if a[r][c] != k: # k가 안되면 -1 출력
    print(-1)
    
else:
    print(time)
