from collections import deque

N, M = map(int, input().split())
board = [list(map(int,input())) for _ in range(N)]
q = deque()
q.append((0,0))

d = [(1,0),(0,1),(-1,0),(0,-1)]

while q:
  y, x = q.popleft()
  for i in range(4):
    dy, dx = y + d[i][0], x + d[i][1]
    if 0 <= dy < N and 0 <= dx < M and board[dy][dx] == 1:
      board[dy][dx] = board[y][x] + 1
      q.append((dy,dx))

print(board[N-1][M-1])
      


