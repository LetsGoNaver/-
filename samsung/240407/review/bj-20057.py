import sys
input = sys.stdin.readline
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

d = [(0,-1),(1,0),(0,1),(-1,0)]
flag = cnt = dr = answer = 0
cnt_mx = 1
cy = cx = N//2

dust = [[0,0,2,0,0],
        [0,10,7,1,0],
        [5,0,0,0,0],
        [0,10,7,1,0],
        [0,0,2,0,0]]
alphas = [(2,1),(3,2),(2,3),(1,2)]
def rotate():
  global dust
  new = [[0] * len(dust) for _ in dust]
  for y in range(len(new)):
    for x in range(len(new[0])):
      new[x][len(new)-1-y] = dust[y][x]
  dust = new



while (cy, cx) != (0, 0):
  
  cy, cx = cy + d[dr][0], cx + d[dr][1]

  sand = grid[cy][cx]
  grid[cy][cx] = 0
  left = sand
  for sy in range(len(dust)):
    for sx in range(len(dust[0])):
      now = sand * dust[sy][sx] // 100
      left -= now
      if 0 <= cy + sy - 2 < N and 0 <= cx + sx -2 < N:
        grid[cy+sy-2][cx+sx-2] += now
      else:
        answer += now
  if 0 <= cy + alphas[dr][0] - 2 < N and 0 <= cx + alphas[dr][1] -2 < N:
    grid[cy + alphas[dr][0]-2][cx + alphas[dr][1] -2] += left
  else:
    answer += left
  
  # 달팽이 이동
  cnt += 1
  if cnt == cnt_mx:
    cnt = 0
    dr = (dr + 1) % 4
    rotate()
    rotate()
    rotate()
    if flag == 0:
      flag = 1
    else:
      flag = 0
      cnt_mx += 1
print(answer)
