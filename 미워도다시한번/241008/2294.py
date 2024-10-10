n, k = map(int, input().split())
coin = set()

for _ in range(n):
  coin.add(int(input()))

INF = k + 1
dp = [INF] * (k+1)
dp[0] = 0

for c in coin:
  for j in range(1, k+1):
    if j - c >= 0:
      dp[j] = min(dp[j], dp[j-c] + 1)
ans = dp[k]

if ans == INF:
  print(-1)
else:
  print(ans)