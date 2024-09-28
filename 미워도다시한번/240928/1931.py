import sys
input = sys.stdin.readline
n = int(input())
board = []
for _ in range(n):
  board.append(list(map(int, input().split())))
board.sort(key=lambda x : (x[1], x[0]))

et = 0
cnt = 0

for i in range(len(board)):
  if board[i][0] >= et:
    cnt += 1
    et = board[i][1]

print(cnt)