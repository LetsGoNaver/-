arr = [[[0] * 2 for _ in range(4)] for _ in range(4)]

for i in range(4):
  fish_info = list(map(int, input().split()))
  for j in range(4):
    arr[i][j] = [fish_info[2*j], fish_info[2*j+1] - 1]

dr = [(-1,0), (-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

def find(v, idx):
  for i in range(4):
    for j in range(4):
      if v[i][j][0] == idx:
        return (i, j, v[i][j][1])

def dfs(si, sj, sdr, sm, v):
  global answer
  answer = max(answer, sm)

  # [1] 물고기 이동
  for idx in range(1, 17):
    fi, fj, fdr = find(v, idx)
    if fdr == -1: continue
    
    for di in range(8):
      td = (fdr + di) % 8
      ni, nj = fi + dr[td][0], fj + dr[td][1]
      if 0 <= ni < 4 and 0 <= nj < 4 and (ni, nj) != (si, sj):
        v[fi][fj][1] = td
        v[ni][nj], v[fi][fj] = v[fi][fj] , v[ni][nj]
        break
  # [2] 상어의 이동
  for mul in range(1,4):
    ni, nj = si + dr[sdr][0] * mul, sj + dr[sdr][1] * mul
    if 0 <= ni < 4 and 0<= nj < 4 and v[ni][nj][1] != -1:
      tdr = v[ni][nj][1]
      v[ni][nj][1] = -1
      new = [[row[:] for row in lst] for lst in v]
      dfs(ni, nj, tdr, sm + v[ni][nj][0], new)
      v[ni][nj][1] = tdr
  


# si, sj, dr, sm, v
fn, fdr = arr[0][0]
answer = 0
arr[0][0][1] = -1 
dfs(0, 0, fdr, fn, arr)

print(answer)