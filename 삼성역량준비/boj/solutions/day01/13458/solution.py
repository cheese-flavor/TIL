n = int(input()) #시험장 수
students = list(map(int, input().split())) #시험장별 학생수
b, c = map(int, input().split()) #감독, 부감독 가능학생수

answer = 0

# 총감독이 무조건 들어가는 전제로 시작
for i in range(n):
    
    # 총감독관만으로 가능할 경우
    if (students[i] - b) <= 0:
        continue
    
    # 부감독이 필요할 경우
    else:
        # 담당가능 학생수가 초과될 경우 + 1
        if (students[i] - b) % c > 0:
            answer += (students[i] - b) // c + 1
            
        else:
            answer += (students[i] - b) // c 
        
print(answer + n)
