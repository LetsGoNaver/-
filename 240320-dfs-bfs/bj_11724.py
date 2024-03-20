import sys
input = sys.stdin.readline

N, M = map(int, sys.stdin.readline().split())
network = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())
  network[u][v] = 1
  network[v][u] = 1

def bfs(i):
  q = [i]
  while q:
    n = q.pop(0)
    for j in range(1, N+1):
      if visited[j] == 0 and network[n][j] == 1:
        q.append(j)
        visited[j] = 1
cnt = 0
for i in range(1, N+1):
  if visited[i] == 0:
    bfs(i)
    cnt += 1
print(cnt)
