import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
N = 2 ** N
data = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))

d = [(-1,0),(1,0),(0,-1),(0,1)]
for l in lst:
  L = 2 ** l
  new = [row[:] for row in data]
  for sy in range(0, N, L):
    for sx in range(0, N, L):
      for y in range(0,L):
        for x in range(0,L):
          new[sy+x][sx+L-1-y] = data[sy+ y][sx + x]
  data = new
  
  new = [row[:] for row in data]
  for y in range(N):
    for x in range(N):
      if data[y][x] == 0:
        continue

      cnt = 0
      for i in range(4):
        ny, nx = y + d[i][0], x + d[i][1]
        if 0<= ny < N and 0 <= nx < N:
          if data[ny][nx] == 0:
            cnt += 1
            if cnt >= 2:
              new[y][x] -= 1
              break
        else:
          cnt += 1
          if cnt >= 2:
            new[y][x] -= 1
            break
  data = new

ans = 0
visit = [[False] * N for _ in range(N)]

def bfs(si, sj):
  q = []
  q.append((si,sj))
  visit[si][sj] = True
  cnt = 1
  while q:
    ci, cj = q.pop(0)

    for i in range(4):
      ni, nj = ci + d[i][0], cj + d[i][1]
      if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj] and data[ni][nj] != 0:
        q.append((ni,nj))
        visit[ni][nj] = True
        cnt += 1
  return cnt
    
  
for i in range(N):
  for j in range(N):
    if not visit[i][j] and data[i][j] != 0:
      ans = max(ans, bfs(i, j))



print(sum(map(sum,data)))
print(ans)
