import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[6] * (M+2)] + [[6] + list(map(int,input().split())) + [6] for _ in range(N)] + [[6] * (M+2)]
cctv = [[],[1],[1,3],[0,1],[0,1,3],[0,1,2,3]]

d = [(-1,0),(0,1),(1,0),(0,-1)]
lst = []

for i in range(1,N+1):
  for j in range(1, M+1):
    if 1 <= arr[i][j] <= 5:
      lst.append((i,j))

def cal(tlst):
  v = [[0] * (M+2) for _ in range(N+2)]
  for i in range(len(tlst)):
    si, sj = lst[i]
    rot = tlst[i]
    ctype = arr[si][sj]
    for dr in cctv[ctype]:
      dr = (dr + rot) % 4
      ci, cj = si, sj
      while True:
        ci, cj = ci + d[dr][0], cj + d[dr][1]
        if arr[ci][cj] == 6:
          break
        v[ci][cj] = 1
  cnt = 0
  for i in range(1, N+1):
    for j in range(1, M+1):
      if arr[i][j] == 0 and v[i][j] == 0:
        cnt += 1
  return cnt
      


def dfs(n, tlst):
  global ans
  if n == len(lst):
    ans = min(ans, cal(tlst))
    return

  dfs(n+1, tlst + [0])
  dfs(n+1, tlst + [1])
  dfs(n+1, tlst + [2])
  dfs(n+1, tlst + [3])
ans = N * M
dfs(0,[])

print(ans)