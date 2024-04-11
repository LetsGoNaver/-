import sys
input = sys.stdin.readline
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

d = [(1,0),(0,1), (-1,0), (0,-1)]
while True:
  def bfs(i, j):
    global union
    global visited
    q = [(i,j)]
    tuni = [(i,j)]
    visited[i][j] = True
    while q:
      si, sj = q.pop(0)
      for i in range(4):
        ni, nj = si +d[i][0], sj + d[i][1]
        if 0<= ni < N and 0 <= nj < N and not visited[ni][nj] and L <= abs(arr[si][sj] - arr[ni][nj]) <= R:
          tuni.append((ni,nj))
          q.append((ni,nj))
          visited[ni][nj] = True
    union.append(tuni)

  visited = [[False] * N for _ in range(N)]
  union = []
  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        bfs(i,j)
  if max(map(len,union)) <= 1:
    break
  for u in union:
    
    n = len(u)
    if n>= 2:
      t = 0
      for i, j in u:
        t += arr[i][j]
      t = t // n
      for i, j in u:
        arr[i][j] = t
  cnt += 1
      
print(cnt)