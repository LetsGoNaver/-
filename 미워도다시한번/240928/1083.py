import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
S = int(input())
for i in range(len(nums)):
  if S <= 0:
    break
  mx = float("-INF")
  idx = i
  for j in range(i+1, min(i + S + 1, len(nums))):
    if mx < nums[j]:
      mx = nums[j]
      idx = j
  if idx != i:
    if nums[i] < mx:
      nums[i], nums[idx] = nums[idx], nums[i]
      S -= (idx - i)
print(*nums)
