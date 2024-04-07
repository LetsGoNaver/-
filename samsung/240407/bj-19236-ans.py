import sys
input = sys.stdin.readline

d = [(-1,0),(-1,-1), (0,-1),(1,-1), (1,0),(1,1),(0,1),(-1,1)]

def find(idx, v):
  for i in range(0,4):
    for j in range(0,4):
      if v[i][j][0] == idx:
        return (i, j, v[i][j][1])

def dfs(si,sj,sd,sm,v):
  global ans
  # [0] 정답 갱신: 종료 조건 n 관련 등 명확하지 X
  ans = max(ans, sm)

  # [1] 물고기의 이동 (1~16): 기준 v[]이므로 먼저 i,j 검색
  for idx in range(1, 17):
    ci, cj, dr = find(idx, v)
    if dr == -1: continue
    
    # 물고기의 이동
    for j in range(8):
      td = (dr + j) % 8
      ni, nj = ci + d[td][0], cj + d[td][1]

      # 범위 내이고, 상어가 아니면
      if 0<= ni <4 and 0<=nj <4 and (ni, nj) != (si, sj):
        v[ci][cj][1] = td   # 방향 적용 후 교환
        v[ci][cj], v[ni][nj] = v[ni][nj] , v[ci][cj]
        break
  
  # [2] 상어의 이동(1칸 ~ 3칸) : 범위 내이고 빈칸이 아니면
  for mul in range(1,4):
    ni, nj = si + d[sd][0] * mul, sj + d[sd][1] * mul
    if 0 <= ni < 4 and 0 <= nj < 4 and v[ni][nj][1] != -1:
      fn, fd = v[ni][nj]
      v[ni][nj][1] = -1     # 먹은 것
      nv = [[row[:] for row in lst] for lst in v]   # 물고기 이동 원복 복잡하므로 차라리 복사해서 넘겨주자
      dfs(ni,nj,fd,sm+fn,nv)
      v[ni][nj][1] = fd     # 복구
      

# [0] 물고기 입력, v[] 초기화
v = [[[0] * 2 for _ in range(4)] for _ in range(4)]
for i in range(4):
  fish_list = list(map(int, input().split()))
  for j in range(4):
    v[i][j] = [fish_list[j*2], fish_list[j*2+1]-1] # [0] 번호, [1] 방향

# [1] 상어가 초기 위치 물고기를 먹음
ans = 0
fn, fd = v[0][0]        # 물고기 먹는 처리 주의 (방향 ..[1] = -1)
v[0][0][1] = -1         # (0,0) 위치 물고기 먹음 처리
dfs(0,0,fd,fn,v)        # 상어 위치, 방향, 초기점수, v[] 전달
print(ans)

