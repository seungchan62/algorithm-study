# BFS 예제

from collections import deque

def bfs(graph, start, visited):
  queue = deque([start]) # 원소가 있는 큐 생성
  visited[start] = True # visited[start] -> 첫 방문 true
  
  while queue:
    v = queue.popleft() # popleft()
    print(v, end = ' ')
    
    for i in graph[v]: # graph는 2차원 리스트
      if not visited[i]:
        queue.append(i) # append(i)
        visited[i] = True

# 2차원 리스트
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)