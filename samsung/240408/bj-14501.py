import sys
input = sys.stdin.readline

N = int(input())
sch = [list(map(int,input().split())) for _ in range(N)]

ans = 0

def dfs(n, sm):
  global ans
  if n >= N:
    ans = max(ans, sm)
    return
  
  # 상담하는 경우
  if n + sch[n][1] <= N:
    dfs(n + sch[n][0], sm + sch[n][1])
  # 상담 안하는 경우
  dfs(n+1, sm)
dfs(0,0)
print(ans)