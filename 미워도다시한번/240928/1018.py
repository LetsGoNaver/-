import sys
input = sys.stdin.readline
N, M = map(int,input().split())
board = [input() for _ in range(N)]
ans = []
print(board)
for i in range(M-7):
  for j in range(N-7):
    countW = 0
    countB = 0
    for y in range(i, i+8):
      for x in range(j, j+8):
        if (x + y) % 2 == 0:
          if board[y][x] != "W": countW +=1
          if board[y][x] != "B": countB += 1
        else:
          if board[y][x] != "W": countB +=1
          if board[y][x] != "B": countW += 1
    ans.append(countW)
    ans.append(countB)
print(min(ans))