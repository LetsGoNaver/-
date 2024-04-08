import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
T = [x for x in range(N)]
ans = float("INF")

def bT(team):
  global ans
  if len(team) == N//2:
    ss = ls = 0
    away = []
    for tt in T:
      if tt not in team:
        away.append(tt)
    for i in range(N//2-1):
      for j in range(i+1, N//2):
        ss += S[team[i]][team[j]] + S[team[j]][team[i]]
        ls += S[away[i]][away[j]] + S[away[j]][away[i]]
    ans = min(ans, abs(ss-ls))
    return
  for t in T:
    if t not in team:
      team.append(t)
      bT(team)
      team.pop()
    

bT([])

print(ans)