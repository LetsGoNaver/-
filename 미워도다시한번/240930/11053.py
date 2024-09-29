
N = int(input())
A = list(map(int, input().split()))
A.insert(0,0)
dp = [0] * 1001

answer = 0
for i in range(1, N+1):
  for j in range(0,i):
    if A[i] > A[j]:
      dp[i] = max(dp[i], dp[j] + 1)
  answer = max(answer, dp[i])

print(answer)