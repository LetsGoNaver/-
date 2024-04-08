N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

M = N // 2

def cal(alst, blst):
  asm = bsm = 0
  for i in range(M):
    for j in range(M):
      asm += S[alst[i]][alst[j]]
      bsm += S[blst[i]][blst[j]]
  return abs(asm - bsm)

def dfs(n, alst, blst):
  global ans
  # # 가지치기: 이미 0 이면, 더 줄일 가능성 X
  # if ans == 0:
  #   return
  # # 한 팀이 이미 M 명 초과인 경우
  # if len(alst) > M or len(blst) > M:
  #   return 
  #
  # 가지치기가 더 시간이 오래 거릴 수 있다.
  #

  if n == N:
    if len(alst) == len(blst):
      ans = min (ans, cal(alst, blst))
    return
  
  dfs(n+1, alst + [n], blst)
  dfs(n+1, alst, blst + [n])

ans = float("INF")
dfs(0,[],[])
print(ans)