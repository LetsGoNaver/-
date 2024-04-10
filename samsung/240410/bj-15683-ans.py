import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 벽(6번) 으로 가장 자리를 막음
arr = [[6] * (M+2)] + [[6] + list(map(int, input().split())) + [6] for _ in range(N)] + [[6] * (M+2)]

d = [(-1,0),(0,1),(1,0),(0,-1)]
cctv = [[], [1],[1,3],[0,1],[0,1,3], [0,1,2,3]]

# 1~5번 cctv 저장
lst = []
for i in range(1, N+1):
  for j in range(1, M+1):
    if 1 <= arr[i][j] <= 5:
      lst.append((i,j))
  
CNT = len(lst)

ans = N * M

def cal(tlst):
  v = [[0] * (M+2) for _ in range(N+2)]

  # 모든 CCTV에 대해서 처리 (좌표, type, rot)
  for i in range(CNT):
    si, sj = lst[i] # 1~N, 1~M
    rot = tlst[i]
    ctype = arr[si][sj] # 1 ~ 5

    # type에 따른 모든 방향 뻣어가면서 v[] 1표시
    for dr in cctv[ctype]:
      dr = (dr + rot) % 4
      ci, cj = si, sj
      while True:
        ci, cj = ci + d[dr][0], cj + d[dr][1]
        if arr[ci][cj] == 6:
          break

        v[ci][cj] = 1
  # 사각지대 ( 0 이고, 미방문 ) 개수 카운트
  cnt = 0
  for i in range(1,N+1):  
    for j in range(1, M+1):
      if arr[i][j] == 0 and v[i][j] == 0:
        cnt += 1
  return cnt


def dfs(n, tlst):
  global ans
  if n == CNT: # 모든 CCTV의 방향 정함
    ans = min(ans, cal(tlst))
    return

  dfs(n+1, tlst + [0]) # 회전 X
  dfs(n+1, tlst + [1]) # 회전 1
  dfs(n+1, tlst + [2]) # 회전 2
  dfs(n+1, tlst + [3]) # 회전 3


dfs(0, [])
print(ans)