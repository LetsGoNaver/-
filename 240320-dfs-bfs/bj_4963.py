import sys
input = sys.stdin.readline

d = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1, -1)]

def bfs(y, x):
  q = [[y, x]]
  while q:
    y, x = q.pop(0)
    for i in range(8):
      dy, dx = y + d[i][0], x + d[i][1]
      if 0 <= dy < h and 0 <= dx < w:
        if not visited[dy][dx] and graph[dy][dx] == 1:
          visited[dy][dx] = True
          q.append([dy,dx])


while True:
  w, h = map(int, input().split())
  if (w == 0 and h == 0):
    break
  graph = [list(map(int, input().split())) for _ in range(h)]
  visited = [[False] * w for _ in range(h)]
  q = []
  
  for y in range(h):
    for x in range(w):
      if graph[y][x] == 1:
        q.append([y,x])
  
  cnt = 0
  while q:
    y, x = q.pop(0)
    if not visited[y][x]:
      bfs(y, x)
      cnt += 1
  print(cnt)
