import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = []

def bt(depth):
  if depth == M:
    print(*numbers)
    return
  for i in range(1, N+1):
    if len(numbers) != 0:
      if i <= numbers[-1]:
        continue
    numbers.append(i)
    bt(depth + 1)
    numbers.pop()

bt(0)