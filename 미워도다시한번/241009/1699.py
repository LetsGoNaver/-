N = int(input())

M = int(N**(1/2))
dp = [n for n in range(N+1)]

for i in range(2, M+1):
  for j in range(i*i,N+1):
      dp[j] = min(dp[j], dp[j-i*i] + 1)

print(dp[N])