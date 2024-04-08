import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

cnt_mx = 1
dr = flag = cnt = answer = 0
cy = cx = N//2

d = [(0,-1),(1,0),(0,1),(-1,0)]

dust = [[0,0,2,0,0],
        [0,10,7,1,0],
        [5,0,0,0,0],
        [0,10,7,1,0],
        [0,0,2,0,0]]

alpha = [(2,1),(3,2),(2,3),(1,2)]

def rotate():
  global dust
  dn = len(dust)
  for _ in range(3):
    new = [[0] * dn for _ in range(dn)]
    for y in range(dn):
      for x in range(dn):
        new[x][dn-1-y] = dust[y][x]
    dust = new

while (cy,cx) != (0,0):
  cy, cx = cy + d[dr][0], cx + d[dr][1]
  original_sand = grid[cy][cx]
  grid[cy][cx] = 0
  sand = 0
  for sy in range(5):
    for sx in range(5):
      now = original_sand * dust[sy][sx] // 100
      if 0 <= cy + sy - 2 < N and 0 <= cx + sx -2 < N:
        grid[cy+sy-2][cx+sx-2] += now
        sand += now
      else:
        answer += now
        sand += now
  ay, ax = alpha[dr][0], alpha[dr][1]
  ny, nx = cy + ay -2, cx + ax-2

  if 0 <= ny < N and 0<= nx < N:
    grid[ny][nx] += original_sand - sand
  else:
    answer += original_sand - sand
  cnt += 1
  if cnt == cnt_mx:
    dr = (dr + 1) % 4
    rotate()
    cnt = 0
    if flag == 0:
      flag = 1
    else:
      flag = 0 
      cnt_mx += 1

print(answer)