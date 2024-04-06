import sys
input = sys.stdin.readline
N = int(input())
visited = [[False] * N for _ in range(N)]
grid = [list(map(int, input().split())) for _ in range(N)]

answer = 0

d = [(0, -1), (1,0), (0,1), (-1,0)]
direction = 0
y, x = N//2, N//2
visited[y][x] = True

dust = [[0,0,0.02,0,0], 
        [0, 0.1,0.07,0.01,0], 
        [0.05, 0,0,0,0], 
        [0,0.1,0.07,0.01,0], 
        [0,0,0.02,0,0]]

def rotateDust():
    global dust  # 전역 변수 사용 선언
    y = len(dust)
    x = len(dust[0])
    newDust = [[0] * x for _ in range(y)]
    for _ in range(3):
      for i in range(y):
          for j in range(x):
              newDust[j][y-i-1] = dust[i][j]
    dust = newDust  # 수정된 회전 로직 적용 후 전역 dust 배열 갱신


def spreadSand(y,x):
  global answer
  original_sand = grid[y][x]
  moved_sand = 0
  for oy in range(-2,3):
    for ox in range(-2,3):
      if dust[oy+2][ox+2] != 0:
        ny, nx = y + oy, x + ox
        sand = int(original_sand * dust[oy+2][ox+2]) 
        moved_sand += sand
        if 0<=ny<N and 0<=nx<N:
          grid[ny][nx] += sand
        else:
          answer += sand
  alpha_sand = original_sand - moved_sand
  ay, ax = y+d[direction][0], x+d[direction][1]
  if 0<= ay <N and 0<=ax<N:
    grid[ay][ax] += alpha_sand
  else:
    answer += alpha_sand
  grid[y][x] =0 



while True:
  dy, dx = y + d[direction][0], x +d[direction][1]
  print(dy,dx)
  if 0<=dy<N and 0<=dx<N:
    spreadSand(dy,dx)
    y,x = dy, dx
    visited[y][x] = True
    td = (direction + 1) % 4
    ny, nx = y + d[td][0], x+d[td][1]
    if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
      direction = td
      rotateDust()
  else:
    td = (direction + 1) % 4
    ny, nx = y + d[td][0], x+d[td][1]
    if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
      direction = td
      rotateDust()
    else:
      break
print(answer)
