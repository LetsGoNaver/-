import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
operators = list(map(int,input().split()))

mxAns = float("-INF")
mnAns = float("INF")
def bt(idx, sm):
  global mxAns, mnAns
  if idx == N-1:
    mxAns = max(mxAns, sm)
    mnAns = min(mnAns, sm)
    return
  for i in range(4):
    tmp = sm
    if operators[i] == 0:
      continue
    if i == 0:
      sm += nums[idx+1]
    elif i == 1:
      sm -= nums[idx+1]
    elif i == 2:
      sm *= nums[idx+1]
    else:
      if sm < 0:
        sm = -1 * (abs(sm) // nums[idx+1])
      else:
        sm //= nums[idx+1]
    operators[i] -= 1
    bt(idx+1, sm)
    operators[i] += 1
    sm = tmp
bt(0,nums[0])
print(mxAns)
print(mnAns)
