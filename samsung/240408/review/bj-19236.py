import sys
input = sys.stdin.readline
data = [[[0,0] for _ in range(4)] for _ in range(4)]

d = [(-1,0),(-1,-1), (0,-1),(1,-1), (1,0),(1,1),(0,1),(-1,1)]

for i in range(4):
  v = list(map(int,input().split()))
  for j in range(4):
    data[i][j] = [v[2*j], v[2*j+1] -1]

def find(idx, data):
  for i in range(4):
    for j in range(4):
      if data[i][j][0] == idx:
        return (i, j, data[i][j][1])



def bt(si, sj, sd, sm, data):
  global ans
  ans = max(ans, sm)

  for idx in range(1,17):
    ci, cj, dr = find(idx,data) # [NA] 달라진 배열을 전달해주어야함.
    if dr == -1 : continue # [NA] 먹힌 경우는 제외

    for j in range(8):
      td = (dr + j) % 8
      ni, nj = ci + d[td][0], cj + d[td][1]

      if 0<=ni<4 and 0<=nj<4 and (ni, nj) != (si, sj):
        data[ci][cj][1] = td # [NA] 방향을 바꿔놓고 적용을 안했음.
        data[ci][cj], data[ni][nj] = data[ni][nj], data[ci][cj]
        break
      
  
  for step in range(1,4):
    nsi, nsj = si + d[sd][0] * step, sj + d[sd][1] * step

    if 0 <= nsi < 4 and 0 <= nsj < 4 and data[nsi][nsj][1] != -1:
      tfn, tfd = data[nsi][nsj]
      data[nsi][nsj][1] = -1
      new = [[row[:] for row in lst] for lst in data]
      bt(nsi, nsj, tfd, sm + tfn, new)
      data[nsi][nsj][1] = tfd
 


ans = 0
fn, fd = data[0][0]
data[0][0][1] = -1
bt(0,0,fd,fn,data)
print(ans)


