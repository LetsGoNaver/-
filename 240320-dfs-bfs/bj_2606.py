import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
M = int(input())
vertex = [[0] * (N+1) for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
  x, y = map(int, input().split())
  vertex[x][y] = 1
  vertex[y][x] = 1

cnt = 0
q = deque([1])
visited[1] = 1
while q:
  node = q.popleft()
  for i in range(N+1):
    if visited[i] == 0 and vertex[node][i] == 1:
      visited[i] = 1
      q.append(i)
      cnt += 1

print(cnt)


