# 사용자가 마지막으로 공유한 회전 수정 시도 (전체 코드는 draft.py 참조)
# 과정1: 벨트랑 같이 돌리기
belt = [belt.pop()]+belt[:-1]
loca = [loca.pop()]+loca[:-1]
