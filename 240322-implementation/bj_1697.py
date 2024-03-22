import sys
input = sys.stdin.readline
N, K = map(int, input().split())

max_num = 10 ** 5
dp = [0] * (max_num + 1)

q = [N]

while q:
  x = q.pop(0)
  if x == K:
    print(dp[x])
    break
  for nx in [x-1, x+1, x*2]:
    if 0 <= nx <= max_num and not dp[nx]:
      dp[nx] = dp[x] + 1
      q.append(nx)      
  