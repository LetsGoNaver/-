from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
def bfs():
  drc = [(-1,0),(1,0),(0,-1),(0,1)]
  visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
  q = deque()

  visited[0][0][0] = 1
  q.append((0,0,0))

  while q:
    y, x, chance = q.popleft()

    if y == N-1 and x == M-1:
      return visited[y][x][chance]
    for k in range(4):
      dy, dx = y + drc[k][0], x + drc[k][1]
      if 0 <= dy < N and 0 <= dx < M:
        if board[dy][dx] == 1 and chance == 0:
          visited[dy][dx][1] = visited[y][x][chance] + 1
          q.append((dy,dx,1))
        elif board[dy][dx] == 0 and visited[dy][dx][chance] == 0:
          visited[dy][dx][chance] = visited[y][x][chance] + 1
          q.append((dy,dx,chance))
  return -1

print(bfs())