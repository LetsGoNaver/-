N = int(input())

dp = [1,1,1]

for i in range(1, N+1):
  tmp = [0,0,0]
  tmp[0] = sum(dp)
  tmp[1] = tmp[0] - dp[1]
  tmp[2] = tmp[0] - dp[2]
  dp = tmp

print(max(dp) % 9901)
