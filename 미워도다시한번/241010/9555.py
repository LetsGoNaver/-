T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range(N)]
  visited = [[0] * M for _ in range(N)]
  ans = set()

  for i in range(N):
    for j in range(M):
      visited[i][j] = 1
      for di, dj in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
        ni, nj = i + di ,j + dj
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
            if arr[ni][nj] == arr[i][j]:
              if arr[i][j] != -1:
                ans.add(arr[i][j])
  print(len(ans))