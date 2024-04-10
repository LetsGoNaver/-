import sys
input = sys.stdin.readline

N, M, ci, cj, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
d = [(0,1), (0,-1),(-1,0),(1,0)]

orders = [int(x) -1 for x in input().split()]
dice = [0,0,0,0,0,0] # [2] 천장 [5] 바닥
for o in orders:
  ni, nj = ci + d[o][0], cj + d[o][1]
  if 0 <= ni < N and 0 <= nj < M:
    if o == 0: # 동쪽
      dice[3],dice[0],dice[2],dice[5] = dice[0], dice[2], dice[5], dice[3]
    elif o == 1: # 서쪽
      dice[2], dice[0], dice[3], dice[5] = dice[0], dice[3], dice[5], dice[2]
    elif o == 2: # 북쪽
      dice[4], dice[0], dice[1], dice[5] = dice[0], dice[1], dice[5], dice[4]
    else:
      dice[1], dice[0], dice[4], dice[5] = dice[0], dice[4], dice[5], dice[1]
    
    if arr[ni][nj] != 0:
      dice[-1] = arr[ni][nj]
      arr[ni][nj] = 0
    else:
      arr[ni][nj] = dice[-1]
    ci, cj = ni, nj
    
    print(dice[0])
