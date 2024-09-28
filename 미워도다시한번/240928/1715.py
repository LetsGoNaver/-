import sys
import heapq
n = int(input())
deq = []
for _ in range(n):
  heapq.heappush(deq, int(input()))

answer = 0
while (len(deq) > 1):
  x, y = heapq.heappop(deq), heapq.heappop(deq)
  answer += x + y
  heapq.heappush(deq, x+y)

print(answer)