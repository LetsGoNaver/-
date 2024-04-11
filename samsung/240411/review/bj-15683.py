import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[6] * (M + 2)] + [[6] + list(map(int, input().split())) + [6] for _ in range(N)] + [[6] * (M + 2)]
dr = [(-1,0), (0,1),(1,0),(0,-1)]
cctvDr = [[],[1],[1,3],[0,1],[0,1,3],[0,1,2,3]]

cidx =[]

for i in range(N+2):
  for j in range(M+2):
    if 1<= arr[i][j] <= 5:
      cidx.append((i,j))

def cal(tlst):
  visited = [[False] * (M+2) for _ in range(N+2)]
  for i in range(len(cidx)):
    si, sj = cidx[i]
    idx = arr[si][sj]
    for di in cctvDr[idx]:
      ndi = (di + tlst[i]) % 4
      ni, nj = si + dr[ndi][0], sj + dr[ndi][1]
      while True:
        if arr[ni][nj] == 6:
          break
        visited[ni][nj] = True
        ni, nj = ni + dr[ndi][0], nj + dr[ndi][1]
  cnt = 0
  for i in range(N+2):
    for j in range(M+2):
      if arr[i][j] == 0 and not visited[i][j]:
        cnt += 1
  return cnt




def dfs(n, tlst):
  global ans
  if n == len(cidx):
    ans = min(ans, cal(tlst))
    return
  
  for i in range(4):
    dfs(n+1, tlst + [i])


ans = N*M
dfs(0,[])
print(ans)