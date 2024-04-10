N = 4

arr = [[[0] * 2 for _ in range(N)] for _ in range(N)]

d = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

for i in range(N):
  flst = list(map(int, input().split()))
  for j in range(N):
    arr[i][j] = [flst[2*j], flst[2*j+1] - 1]

def find(idx, v):
  for i in range(N):
    for j in range(N):
      if v[i][j][0] == idx:
        return (i,j, v[i][j][1])

def dfs(si, sj, sd, sm, arr):
  global answer
  answer = max(answer, sm)

  for idx in range(1, 17):
    fi, fj, fd = find(idx, arr)
    if fd == -1: continue
  
    for di in range(8):
      td = (fd + di) % 8
      ni, nj = fi + d[td][0], fj + d[td][1]
      
      if 0<= ni < N and 0 <= nj < N and (ni, nj) != (si, sj):
        arr[fi][fj][1] = td
        arr[fi][fj], arr[ni][nj] = arr[ni][nj], arr[fi][fj]
        break
  for mul in range(1,4):
    ni, nj = si + d[sd][0] * mul, sj + d[sd][1] * mul
    if 0<= ni <N and 0<= nj < N and arr[ni][nj][1] != -1:
      tfd = arr[ni][nj][1]
      arr[ni][nj][1] = -1
      new = [[row[:] for row in lst] for lst in arr]
      dfs(ni, nj, tfd, sm + arr[ni][nj][0], new)
      arr[ni][nj][1] = tfd
  

# init
answer = 0
fn, fd = arr[0][0]
arr[0][0][1] = -1 
dfs(0,0,fd,fn ,arr)

print(answer)