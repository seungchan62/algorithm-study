# 미로찾기 v

from collections import deque

# 세로 가로
n, m = map(int, input().split())

# 사용자로부터 미로 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque() # 비어있는 큐 만들기
  queue.append((x, y)) # 큐에 (x, y)삽입
  
  while queue:
    x, y = queue.popleft() # x, y를 큐에서 pop
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 맵 밖으로 벗어나면
      if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
        continue

      # 벽 무시
      if graph[nx][ny] == 0:
        continue
        
      
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny)) # 큐에 (nx, ny)삽입

  return graph[n - 1][m - 1]



print(bfs(0, 0))
        