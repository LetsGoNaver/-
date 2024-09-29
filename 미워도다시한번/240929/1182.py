N, S = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
def bT(idx, sum):
  global ans 
  if idx >= N:
    return
  sum += nums[idx]
  if sum == S:
    ans += 1
  bT(idx+1, sum)
  bT(idx+1, sum - nums[idx])

bT(0,0)
print(ans)