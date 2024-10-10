n = int(input())
arr = [0] + [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n+1)]

for i in range(1, n+1):
  dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
  dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
  dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]
print(min(dp[n]))