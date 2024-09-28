import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

white = 0
blue = 0

def divConq(n,x,y):
  global white, blue
  sameColor = board[x][y]
  for i in range(x,x+n):
    for j in range(y,y+n):
      if board[i][j] != sameColor:
        divConq(n//2, x, y)      
        divConq(n//2, x, y+n//2)      
        divConq(n//2, x+n//2, y)      
        divConq(n//2, x+n//2, y+n//2)
        return
  if sameColor == 0:
    white += 1
    return
  else:
    blue += 1
    return

divConq(N,0,0)
print(white)
print(blue)      