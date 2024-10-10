from collections import deque
N = int(input())

q = deque([(i+1, x) for i, x in enumerate(list(map(int, input().split())))])
answer = []
while q:
  i, n = q.popleft()
  answer.append(i)
  if n > 0 :
    q.rotate(-n+1)
  else:
    q.rotate(-n)
print(" ".join(map(str, answer)))