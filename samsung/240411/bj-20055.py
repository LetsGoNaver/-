import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
arr = deque(list(map(int,input().split())))
robots = deque([0] * N)


cnt = 0
while True:
  flag = False
  cnt += 1
  arr.appendleft(arr.pop())
  robots.appendleft(robots.pop())
  if robots[-1] == 1:
    robots[-1] = 0
  for i in range(N-2,-1,-1):
    if robots[i] == 1 and robots[i+1] != 1 and arr[i+1] >= 1:
      robots[i], robots[i+1] = robots[i+1], robots[i]
      arr[i+1] -= 1
      if i+1 == N -1:
        robots[-1] = 0
      if arr.count(0) >= K:
        flag = True
        break
  if flag:
    print(cnt)
    break

  if arr[0] >= 1:
    arr[0] -= 1
    robots[0] = 1
  if arr.count(0) >= K:
    print(cnt)
    break
  

    

