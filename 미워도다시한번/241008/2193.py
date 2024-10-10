N = int(input())

dp = [[0,0,0] for _ in range(91)]
dp[1] = [0, 0, 1]
dp[2] = [1,0,1]
dp[3] = [0,1,2]
for i in range(4, N+1):
  dp[i][0] = dp[i-1][1]
  dp[i][1] = dp[i-1][0] + dp[i-1][1]
  dp[i][2] = dp[i][0] + (2 * dp[i][1])
print(dp[N][2])