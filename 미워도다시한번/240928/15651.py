import sys
input = sys.stdin.readline
N, M = map(int,input().split())

answer = []
def bt(depth):
  if depth == M:
    print(' '.join(map(str, answer)))
    return
  for i in range(1, N+1):
    answer.append(i)
    bt(depth+1)
    answer.pop()
bt(0)
