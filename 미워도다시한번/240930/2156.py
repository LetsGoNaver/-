# 꼭 다시 풀어보기
n = int(input())

t = []

for _ in range(n):
  t.append(int(input()))

dp = [0] * n

dp[0] = t[0]

if n > 1:
  dp[1] = t[0] + t[1]

if n > 2:
  dp[2] = max(t[2] + t[1], t[2] + t[0], dp[1])

for i in range(3,n):
  dp[i] = max(dp[i-1], dp[i-2] + t[i], dp[i-3] + t[i] + t[i-1])
print(dp[n-1])