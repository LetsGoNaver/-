import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
network = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
  x, y = map(int, input().split())
  network[x][y] = 1
  network[y][x] = 1

def dfs(v):
  visited[v] = 1
  print(v, end = " ")
  for i in range(1, N+1):
    if visited[i] == 0 and network[v][i] == 1:
      dfs(i)

def bfs(v):
  q = deque([v])
  visited[v] = 1
  while q:
    node = q.popleft()
    print(node, end=" ")
    for i in range(1, N+1):
      if visited[i] == 0 and network[node][i] == 1:
        visited[i] = 1
        q.append(i)

dfs(V)
print()
visited = [0] * (N+1)
bfs(V)
