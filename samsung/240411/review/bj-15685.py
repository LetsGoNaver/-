import sys
input = sys.stdin.readline

N = int(input())

d = [(0,1),(-1,0),(0,-1),(1,0)]
arr = [[0] * 101 for _ in range(101)]
for _ in range(N):
  sj, si, dr, g = map(int, input().split())
  tlst = [(si, sj)]
  tlst.append((si + d[dr][0], sj + d[dr][1]))

  for _ in range(g):
    ei, ej = tlst[-1]
    for t in range(len(tlst) - 2, -1, -1):
      ci, cj = tlst[t]
      tlst.append((ei-(ej-cj), ej+(ei-ci)))
  for ti, tj in tlst:
    arr[ti][tj] = 1
ans = 0
for i in range(100):
  for j in range(100):
    if arr[i][j] == arr[i+1][j] == arr[i][j+1] == arr[i+1][j+1] == 1:
      ans += 1
print(ans)