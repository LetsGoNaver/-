import sys 
input = sys.stdin.readline

M, N, K = map(int, input().split())

graph = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

d = [[0,1], [0, -1], [1,0], [-1,0]]

for _ in range(K):
  sx, sy, ex, ey = map(int, input().split())
  for y in range(sy, ey):
    for x in range(sx, ex):
      graph[y][x] = 1

q = []

for y in range(M):
  for x in range(N):
    if graph[y][x] == 0:
      q.append([y,x])

answer = []

def bfs(y, x, visited):
  cnt = 1
  tq = [[y, x]]
  visited[y][x] = True

  while tq:
    y, x = tq.pop(0)
    for i in range(4):
      dy, dx = y + d[i][0], x + d[i][1]
      if 0 <= dy < M and 0 <= dx < N:
        if graph[dy][dx] == 0 and not visited[dy][dx]:
          visited[dy][dx] = True
          tq.append([dy,dx])
          cnt += 1
  return cnt

while q:
  y, x = q.pop(0)
  if not visited[y][x]:
    answer.append(bfs(y,x, visited))

print(len(answer))
print(" ".join(list(map(str,sorted(answer)))))