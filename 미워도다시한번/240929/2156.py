N = int(input())
table = [0] * 10001
dp = [0] * 10001

for i in range(1,N+1):
  table[i] = int(input())

dp[1] = table[1]
dp[2] = table[2] + table[1]

for i in range(3, N+1):
  dp[i] = max(dp[i-1], dp[i-2] + table[i], dp[i-3] + table[i-1] + table[i])
print(dp[N])


