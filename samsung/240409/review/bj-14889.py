import sys
input = sys.stdin.readline
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

ans = float("INF")
def dfs(n, alst, blst):
  global ans
  if n == N:
    # 시너지 계산
    if len(alst) == len(blst):
      M = N // 2
      sma, smb = 0,0
      for i in range(M):
        for j in range(M):
          sma += S[alst[i]][alst[j]]
          smb += S[blst[i]][blst[j]]
      ans = min(ans, abs(sma-smb))
    return
  
  dfs(n+1, alst+[n], blst)
  dfs(n+1, alst, blst + [n])

dfs(0, [],[])
print(ans)