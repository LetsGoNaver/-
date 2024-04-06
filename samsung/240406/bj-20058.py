import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
visited = [[False] * (2**N) for _ in range(2**N)]



L = list(map(int,input().split()))

d = [(0,1),(1,0), (-1,0), (0,-1)]

for q in range(Q):
  grid_size = 2 ** L[q]
  for i in range(0, len(arr), grid_size):
    for j in range(0, len(arr), grid_size):
      grid = [row[j:j+grid_size] for row in arr[i:i+grid_size]]
      newGrid = [[0] * grid_size for _ in range(grid_size)]
    
      for y in range(len(grid)):
        for x in range(len(grid[0])):
          newGrid[x][len(grid)-1 - y] = grid[y][x]
      for y in range(len(newGrid)):
        for x in range(len(newGrid[0])):
          arr[i+y][j+x] = newGrid[y][x]
    
  cand_idx = []
  for y in range(len(arr)):
    for x in range(len(arr)):
      if arr[y][x] == 0:
        for i in range(4):
          dy, dx = y + d[i][0], x + d[i][1]
          if 0 <= dy < len(arr) and 0 <= dx < len(arr):
            cand_idx.append((dy,dx))
  # 얼음 녹이기
  while cand_idx:
    cy, cx = cand_idx.pop()
    cnt = 0
    for i in range(4):
      dy, dx = cy + d[i][0], cx + d[i][1]
      if 0 <= dy < len(arr) and 0 <= dx < len(arr):
        if arr[dy][dx] != 0:
          cnt += 1
    if cnt <3:
      if arr[cy][cx] == 0:
        continue
      else: 
        arr[cy][cx] -= 1

sum_ice = 0
max_size = 0
for i in range(2**N):
  for j in range(2**N):
    if not visited[i][j] and arr[i][j] > 0:
      check = [[i,j]]
      sum_ice += arr[i][j]
      visited[i][j] = True
      now = 1
      while check:
        y, x = check.pop()
        for dr in range(4):
          dy, dx = y + d[dr][0], x + d[dr][1]
          if 0 <= dy < 2**N and 0 <= dx < 2**N:
            if arr[dy][dx] > 0 and visited[dy][dx] == False:
              sum_ice += arr[dy][dx]
              check.append([dy,dx])
              visited[dy][dx] = True
              now += 1
      max_size = max(max_size, now)

print(sum_ice)
print(max_size)

