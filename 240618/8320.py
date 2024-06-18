# import sys
# input = sys.stdin.readline
# N = int(input())

# ans = 0
# for x in range(1,101):
#   for i in range(x,N+1):
#     if x * i <= N:
#       ans += 1
#     else:
#       break

# print(ans)

import sys
input = sys.stdin.readline
N = int(input())
ans = N

for i in range(2,N+1):
  n = (N // i) - (i-1)
  if n < 1:
    break
  ans += n

print(ans)