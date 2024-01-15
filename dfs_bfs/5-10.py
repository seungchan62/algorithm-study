# 음료수 얼려 먹기

n, m = map(int, input().split()) # 세로, 가로

graph = [] # 그래프 초기화
for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x, y):
  if x < 0 or x >= m or y < 0 or y >= n: # 범위 착각하지 말기
    return False

  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True
  return False

count = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True: # 메게변수 똑바로,,
      count += 1

print (count)
      
    