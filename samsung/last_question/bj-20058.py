N, Q = map(int, input().split())
N = 2 ** N
arr = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))

for L in lst:
  L = 2 ** L
  new = [[0] * N for _ in range(N)]
  for si in range(0,N,L):
    for sj in range(0, N, L):
      for y in range(L):
        for x in range(L):
          new[si + x][sj + L-y-1] = arr[si + y][sj + x]
  arr = new
  
  # 얼음이 주변에 3개 이상 있는지 확인
  new = [row[:] for row in arr]
  for i in range(N):
    for j in range(N):
      if arr[i][j] == 0: continue
      cnt = 0
      for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
        ni, nj = i + di ,j + dj
        if 0 <= ni < N and 0 <= nj < N:
          if arr[ni][nj] == 0:
            cnt += 1
            if cnt >= 2:
              new[i][j] -= 1
              break  
        else:
          cnt += 1
          if cnt >= 2:
            new[i][j] -= 1
            break
  arr = new

print(sum(map(sum, arr)))

def bfs(si, sj):
  q = [(si, sj)]
  visited[si][sj] = True
  cnt = 1
  while q:
    ci, cj = q.pop(0)
    for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
      ni, nj = ci + di ,cj + dj
      if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0 and not visited[ni][nj]:
        cnt += 1
        visited[ni][nj] = True
        q.append((ni,nj))
  return cnt

visited = [[False] * N for _ in range(N)]
answer = 0
for i in range(N):
  for j in range(N):
    if not visited[i][j] and arr[i][j] > 0:
      answer = max(answer, bfs(i,j))
        
print(answer)

