import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[6] * (M+2)] + [[6] + list(map(int, input().split())) + [6] for _ in range(N)] + [[6] * (M+2)]
d = [(-1,0),(0,1),(1,0),(0,-1)]
cctv = [[],[1],[1,3],[0,1],[0,1,3],[0,1,2,3]]
cctv_idx = []

for i in range(1,N+1):
  for j in range(1,M+1):
    if 1 <= arr[i][j] <= 5:
      cctv_idx.append((i,j))

ans = N*M

def count(tlst):
  visited = [[False] * (M+2) for _ in range(N+2)]
  for t in range(len(tlst)):
    ci, cj = cctv_idx[t]
    cctvNum = arr[ci][cj]
    
    for ct in cctv[cctvNum]:

      ni, nj = ci, cj
      ct = (ct + tlst[t]) % 4
      while True:
        if arr[ni][nj] == 6:
          break
        ni, nj = ni + d[ct][0], nj + d[ct][1]
        if arr[ni][nj] != 6 and not visited[ni][nj]:
          visited[ni][nj] = True
  cnt = 0
  for i in range(N+1):
    for j in range(M+1):
      if arr[i][j] == 0 and not visited[i][j]:
        cnt += 1
  return cnt
def dfs(n, tlst):
  global ans
  if n == len(cctv_idx):
    ans = min(ans, count(tlst))
    return
  
  dfs(n+1, tlst+[0])
  dfs(n+1, tlst+[1])
  dfs(n+1, tlst+[2])
  dfs(n+1, tlst+[3])

dfs(0,[])
print(ans)