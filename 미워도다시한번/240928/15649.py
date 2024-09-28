import sys
input = sys.stdin.readline

N, M = map(int, input().split())

answer = []
def bt(depth):
  if depth == M:
    print(' '.join(map(str, answer)))
    return
  for i in range(1, N+1):
    if i in answer:
      continue
    answer.append(i)
    bt(depth+1)
    answer.pop()
bt(0)