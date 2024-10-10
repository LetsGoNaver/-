N, M = map(int, input().split())
board = [[0]*(M+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(M+2)]

dp = [[-1] * (M+2) for _ in range(N+2)]
dp[1][1] = 1

def dfs(i, j):
  if dp[i][j] == -1:
    dp[i][j] = 0
    for d in [(1,0),(0,1),(-1,0),(0,-1)]:
      pi, pj = i + d[0], j + d[1]
      if board[pi][pj] > board[i][j]:
        dp[i][j] += dfs(pi, pj)
  return dp[i][j]

dfs(N, M)
print(dp[N][M])