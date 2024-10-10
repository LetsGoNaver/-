N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (M+2) for _ in range(N+2)]
for i in range(1, N+1):
  for j in range(1, M+1):
    dp[i][j] = board[i-1][j-1] + max(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])

print(dp[N][M])