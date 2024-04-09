# 전체 데이터를 2^L 크기 만큼의 격자로 나눈다
# 나눈 격자 모두를 90도 회전시킨다.
# 주위에 얼음이 3개 이상 있지 않으면 녹인다.
# < 목표 >
# 남은 얼음의 합
# 가장 큰덩어리 크기

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
N = 2 ** N
data = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))

d = [(1,0),(0,1), (-1,0), (0,-1)]

for l in lst:
  l = 2 ** l
  
  new = [row[:] for row in data]
  for si in range(0, N, l):
    for sj in range(0, N, l):
      for i in range(l):
        for j in range(l):
          
          new[si + j][sj+l-1-i] = data[si+i][sj+j]
  data = new

  new = [row[:] for row in data]
  for i in range(N):
    for j in range(N):
      if data[i][j] == 0:
        continue
      cnt = 0
      for dr in range(4):
        ni, nj = i+d[dr][0] ,j +d[dr][1]
        if 0 <= ni < N and 0 <= nj < N:
          if data[ni][nj] == 0:
            cnt += 1     
          if cnt >= 2:
            new[i][j] -= 1
            break
        else:
          cnt += 1
          if cnt >= 2:
            new[i][j] -= 1
            break
  data = new




def bfs(si, sj):
  q = [(si, sj)]
  visited[si][sj] = True
  cnt = 1

  while q:
    ci, cj = q.pop(0)
    for i in range(4):
      ni, nj = ci + d[i][0], cj + d[i][1]
      if 0 <= ni < N and 0<=nj < N and not visited[ni][nj] and data[ni][nj] > 0:
        visited[ni][nj] = True
        cnt += 1
        q.append((ni,nj))
  return cnt

ans = 0
visited = [[False] * N for _ in range(N)]

for i in range(N):
  for j in range(N):
    if not visited[i][j] and data[i][j] > 0:
      ans = max(ans, bfs(i,j))


print(sum(map(sum,data)))
print(ans)