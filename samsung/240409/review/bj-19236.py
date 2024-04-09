import sys
input = sys.stdin.readline

d = [(-1,0),(-1,-1), (0,-1),(1,-1), (1,0),(1,1),(0,1),(-1,1)]


def find(idx, v):
  for i in range(0,4):
    for j in range(0,4):
      if v[i][j][0] == idx:
        return (i, j, v[i][j][1])

def dfs(si, sj, sdr, sm, data):
  global ans
  ans = max(ans, sm)

  for idx in range(1,17):
    fi, fj, dr = find(idx, data)
    if dr == -1: continue

    for ddr in range(8):
      tdr = (dr + ddr) % 8
      ni, nj = fi + d[tdr][0], fj + d[tdr][1]
      if 0<= ni < 4 and 0<= nj < 4 and (ni,nj) != (si, sj):
        # 이동가능
        data[fi][fj][1] = tdr
        data[fi][fj], data[ni][nj] = data[ni][nj], data[fi][fj]
        break
  for mul in range(1,4):
    ni, nj = si + d[sdr][0] * mul, sj + d[sdr][1] * mul
    if 0<= ni < 4 and 0 <= nj < 4 and data[ni][nj][1] != -1:
      fn, fd = data[ni][nj]
      data[ni][nj][1] = -1
      new_data = [[row[:] for row in lst] for lst in data]
      print(new_data)
      dfs(ni, nj, fd, sm + fn, new_data)
      data[ni][nj][1] = fd


data = [[[0] * 2 for _ in range(4)] for _ in range(4)]

for i in range(4):
  fish_list = list(map(int, input().split()))
  for j in range(4):
    data[i][j] = [fish_list[j*2], fish_list[j*2+1]-1] # [0] 번호, [1] 방향


# init
ans = 0
fn, fd = data[0][0]        # 물고기 먹는 처리 주의 (방향 ..[1] = -1)
data[0][0][1] = -1         # (0,0) 위치 물고기 먹음 처리
dfs(0,0,fd,fn,data)        # 상어 위치, 방향, 초기점수, v[] 전달
print(ans)