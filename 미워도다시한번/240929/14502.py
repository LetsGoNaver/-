from collections import deque
import copy
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

maxAns = float("-INF")

vt1= [[0] * M for _ in range(N)]

def bT(depth):
  global maxAns
  if depth == 3:
    maxAns = max(maxAns, bfs())
    return
  for i in range(N):
    for j in range(M):
      if board[i][j] == 0 and vt1[i][j] == 0:
        vt1[i][j] = 1
        board[i][j] = 1
        bT(depth + 1)
        board[i][j] = 0
        vt1[i][j] = 0

def bfs():
  direct = [(-1,0),(1,0), (0,-1),(0,1)]
  visited = [[0] * M for _ in range(N)]
  q = deque()
  
  for i in range(N):
    for j in range(M):
      if board[i][j] == 2:
        q.append((i,j))
        visited[i][j] = 1
  
  while q:
    y, x = q.popleft()

    for k in range(4):
      dy, dx = y + direct[k][0], x + direct[k][1]
      if 0 <= dy < N and 0 <= dx < M:
        if board[dy][dx] == 0 and visited[dy][dx] == 0:
          visited[dy][dx] = 1
          q.append((dy,dx))
  cnt = 0
  for i in range(N):
    for j in range(M):
      if board[i][j] == 0 and visited[i][j] == 0:
        cnt += 1
  return cnt
bT(0)
print(maxAns)
