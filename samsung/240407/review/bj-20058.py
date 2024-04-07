import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
N = 2 ** N

data =([[0] * (N+2)]) + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + ([[0] * (N+2)])

d = [(-1,0), (1,0), (0,-1),(0,1)]
L = list(map(int, input().split()))

for l in L:
  l = 2 ** l
  # [1] 격자 회전
  new = [[0] * (N+2) for _ in range(N+2)]
  for sy in range(1,N+1,l):
    for sx in range(1, N+1 , l):
      for y in range(l):
        for x in range(l):
          new[sy + x][sx + l-1-y] = data[sy + y][sx + x]
  data = new
  
  new = [x[:] for x in data]
  for y in range(1, N+1):
    for x in range(1, N+1):
      if data[y][x] == 0:
        continue

      cnt = 0
      for i in range(4):
        if data[y + d[i][0]][x +d[i][1]] ==0:
          cnt += 1
          if cnt >= 2:
            new[y][x] -= 1
            break
  data = new



visited = [[False] * (N+2) for _ in range(N+2)]

# def bfs(x, y):
#   q = []
#   q.append((y,x))
#   visited[y][x] = True
#   cnt = 1
#   while q:
#     cy, cx = q.pop(0)
#     for i in range(4):
#       dy, dx = cy + d[i][0], cx + d[i][1]
#       if not visited[dy][dx] and data[dy][dx]>0:
#         q.append((dy,dx))
#         visited[dy][dx] = True
#         cnt += 1
#   return cnt

def bfs(si, sj):
  q = []                  # [0] q, visitied, 정답관련 변수 등 생성
  q.append((si, sj))      # [1] q에 초기데이터(들) 삽입, v 처리 ...
  visited[si][sj] = True
  cnt = 1

  while q:
    ci, cj = q.pop(0)
    # 네방향, 미방문, 조건: 얼음이면
    for i in range(4):
      ni, nj = ci+d[i][0], cj+d[i][1]  
      if not visited[ni][nj] and data[ni][nj] > 0:
        q.append((ni,nj))
        visited[ni][nj] = True
        cnt += 1
  return cnt

ans = 0
for i in range(1, N+1):
  for j in range(1, N+1):
    if not visited[i][j] and data[i][j] > 0: # 미방문 얼음이면
      ans = max(ans, bfs(i,j))

print(sum(map(sum,data)))
print(ans)


