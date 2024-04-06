# 부분회전 => 목적지 좌표 기준!!!
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
N = 2 ** N

# 범위 체크를 안하기 위한 방법
arr = [[0]*(N+2)] +[[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
lst = list(map(int,input().split()))

d = [(1,0), (0,1), (-1,0), (0,-1)]

for L in lst: # Q 번 시전할 부분 격자 크기 순차 처리
  L = 2 ** L # 부분 격자 크기 저장
  
  # [1] 부분격자를 시계방향 회전
  new = [[0] * (N+2) for _ in range(N+2)]
  for si in range(1, N+1, L):
    for sj in range(1, N+1, L):
      for i in range(L):
        for j in range(L):
          new[si+i][sj+j] = arr[si+L-1-j][sj+i]
  arr = new
  
  # [2] 네방향, 0이 2개 이상 -> 얼음 -1
  new = [x[:] for x in arr]   # arr를 deepcopy할 때에는 슬라이싱이 빠르다.
  for y in range(1, N+1):
    for x in range(1, N+1):   # 전체를 순회
      if arr[y][x] == 0:      
        continue

      cnt = 0 # 얼음이 아닌 것의 개수
      for i in range(4):
        if arr[y+d[i][0]][x+d[i][1]] == 0:
          cnt += 1
          if cnt >= 2:
            new[y][x] -= 1
            break
  arr = new

def bfs(si, sj):
  q = []                  # [0] q, visitied, 정답관련 변수 등 생성
  q.append((si, sj))      # [1] q에 초기데이터(들) 삽입, v 처리 ...
  visited[si][sj] = True
  cnt = 1

  while q:
    ci, cj = q.pop(0)
    # 네방향, 미방문, 조건: 얼음이면
    for i in range(4):
      ni, nj = ci+d[i][0], cj+d[i][1]  
      if not visited[ni][nj] and arr[ni][nj] > 0:
        q.append((ni,nj))
        visited[ni][nj] = True
        cnt += 1
  return cnt



# [3] 정답처리: 남은 얼음 덩어리 중 가장 큰 크기
visited = [[False] * (N+2) for _ in range(N+2)]
ans = 0
for i in range(1, N+1):
  for j in range(1, N+1):
    if not visited[i][j] and arr[i][j] > 0: # 미방문 얼음이면
      ans = max(ans, bfs(i,j))

print(sum(map(sum,arr)))
print(ans)


  


