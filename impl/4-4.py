# 게임 개발(미완) v
'''n, m = map(int, input().split())
a, b, d = map(int, input().split())

visited = [[0] * m for _ in range(n)] # 방문한 위치 저장 맵 초기화 v
visited[a][b] = 1

# [0, 1, 2, 3] # 북, 동, 남, 서
# 앞으로 가기(전진)기준
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
turn_time = 0 # 몇 번 회전했나

# 전체 맵 입력받기 v
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# 회전 함수 v
def turn_left():
  global d
  d = d - 1
  if d == -1:
    d = 3

while True:
  
  turn_left() # 왼쪽 방향의 칸의 상태를 확인해야 하므로
  turn_time += 1
  if array[a + dx[d]][b + dy[d]] == 0:
    na = a + dx[d]
    nb = b + dy[d]
    count += 1
    array[na][nb] = 1
    turn_time = 0
    continue
    
  else:
    turn_left()
    turn_time += 1

  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    na = a - dx[d]
    nb = b - dy[d] 
    count += 1
    array[na][nb] = 1
    turn_time = 0
    # 뒤로가기 가능
    if array[na][nb] == 0:
      a = na
      b = nb
    # 불가능
    else:
      break

print(count)'''

# 정답 코드

# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)
  