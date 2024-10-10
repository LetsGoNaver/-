N, K = map(int, input().split())

dp = [1] * (N+1)

for i in range(2, K+1):
  for j in range(1, N+1): 
    dp[j] += dp[j-1]
print(dp[N] % 1000000000)