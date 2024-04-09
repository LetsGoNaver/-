import sys
input = sys.stdin.readline
N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
# 달팽이 이동

# 달팽이 이동을 하며 모래 흩뿌리기 구현

# 종료 - (0,0)에 도착시
# 목표 - 격자 밖으로 나간 모래의 총량

cnt_mx = 1
d = [(0,-1), (1,0), (0,1),(-1,0)]
dr = cnt = flag = ans = 0
cy = cx = N // 2

dust = [[0,0,2,0,0],
        [0,10,7,1,0],
        [5,0,0,0,0],
        [0,10,7,1,0],
        [0,0,2,0,0]]

alpha = [(2,1), (3,2), (2,3), (1,2)]

def rotate():
  global dust
  for _ in range(3):
    new = [row[:] for row in dust]
    for i in range(5):
      for j in range(5):
        new[j][5-1-i] = dust[i][j]
    dust = new

while (cy, cx) != (0,0):
  cy, cx = cy + d[dr][0], cx +d[dr][1]
  cnt += 1

  origin_sand = grid[cy][cx]
  sand = grid[cy][cx] = 0
  for i in range(5):
    for j in range(5):
      ny, nx = cy + i -2, cx + j -2
      flow = ( origin_sand * dust[i][j] ) // 100
      if 0 <= ny < N and 0 <= nx < N:
        grid[ny][nx] += flow
        sand += flow
      else:
        ans += flow
        sand += flow
  ay, ax = cy + alpha[dr][0] - 2, cx + alpha[dr][1] -2

  if 0<= ay < N and 0<= ax < N:
    grid[ay][ax] += origin_sand - sand
  else:
    ans += origin_sand - sand


  if cnt == cnt_mx:
    cnt = 0
    dr = (dr + 1) % 4
    rotate()
    if flag == 0:
      flag = 1
    else:
      flag = 0
      cnt_mx += 1
print(ans)