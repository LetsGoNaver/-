from collections import deque

n = int(input())
graph = []
maxNum = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j]

d = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(a, b, level, visited):
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            dx, dy = x + d[i][0] , y + d[i][1]
            if 0<= dx < n and 0<= dy < n:
                if graph[dx][dy] > level and visited[dx][dy] == 0:
                    visited[dx][dy] = 1
                    q.append((dx,dy))
    return

result = 0
for l in range(maxNum):
    visited = [[0] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] > l and visited[i][j] == 0:
                bfs(i, j, l, visited)
                cnt += 1
    result = max(result, cnt)
print(result)