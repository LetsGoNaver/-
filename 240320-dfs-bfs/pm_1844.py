from collections import deque
def solution(maps):
    q = deque([[0,0]])
    w, h = len(maps[0]), len(maps)
    
    d = [(0,1), (1,0), (-1,0), (0,-1)]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < w and 0 <= ny < h:
                if maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    q.append([nx, ny])
    if maps[h-1][w-1] == 1:
        return -1
    else:
        return maps[h-1][w-1]
