import sys
input = sys.stdin.readline
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
min_score = float("INF")

def bt(depth, idx):
  global min_score
  if depth == N // 2:
    s = 0
    l = 0
    for i in range(0, N):
      for j in range(0, N):
        if visited[i] and visited[j]:
          s += S[i][j]
        elif not visited[i] and not visited[j]:
          l += S[i][j]
    min_score = min(min_score, abs(s-l))

  for i in range(idx, N):
    if not visited[i]:
      visited[i] = True
      bt(depth + 1, idx + 1)
      visited[i] = False

bt(0,0)
print(min_score)


