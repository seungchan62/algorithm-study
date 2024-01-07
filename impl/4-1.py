# 상하좌우 v
n = int(input())

x, y = 1, 1

# 방향 헷갈림
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']

plans = input().split()

for plan in plans: # 사용자 입력 확인
  for i in range(len(move_types)): # 리스트 확인
    if plan == move_types[i]: # plans(x)
      nx = x + dx[i]
      ny = y + dy[i]
  
      if nx < 1 or ny < 1 or nx > n or ny > n:
        continue # 이동 수행 x -> x, y값 그대로
      x, y = nx, ny # 이동 수행
  
print(x, y)
      
      