# from collections import deque
# N, M = map(int, input().split())
# mount = [list(map(int, input().split())) for _ in range(N)]

# dp = [[0] * M for _ in range(N)]

# q = deque()
# q.append((N-1, M-1))

# direct = [(-1,0),(1,0),(0,-1),(0,1)]

# while q:
#   y, x = q.popleft()
#   if y == 0 and x == 0:
#     break
#   for i in range(4):
#     dy, dx = y + direct[i][0], x + direct[i][1]
#     if 0 <= dy < N and 0 <= dx < M  and mount[dy][dx] > mount[y][x]:
#       dp[dy][dx] = dp[y][x] + 1
# print(dp)