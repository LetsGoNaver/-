import sys
input = sys.stdin.readline

N = int(input())
T = [0] * N
P = [0] * N

for i in range(N):
  T[i], P[i] = map(int, input().split())


def dfs(n, sm):
  global ans
  if n >= N:
    ans = max(ans, sm)
    return
  
  # 상담하는 경우
  if n + T[n] <= N:
    dfs(n + T[n], sm + P[n])
  # 상담 안하는 경우
  dfs(n+1, sm)

ans = 0
dfs(0,0)  
print(ans)