dp = [0] * 1000001

n = int(input())

dp[2] = 1
dp[3] = 1

# for num in range(4, n+1):
#   if num % 2 == 0 and num % 3 == 0:
#     dp[num] = min(1+dp[num//2], 1+dp[num//3])
#   elif num % 2 == 0 and num %3 != 0:
#     dp[num] = min(1+dp[num//2], 1+dp[num-1])
#   elif num % 2 != 0 and num % 3 ==0 :
#     dp[num] = min(1+dp[num//3], 1+dp[num-1])
#   elif num % 2 != 0 and num % 3 != 0:
#     dp[num] = 1+dp[num-1]

# print(dp[n])

for num in range(4, n+1):
  dp[num] = dp[num-1] + 1
  if num % 2 == 0:
    dp[num] = min(dp[num], dp[num//2] + 1)
  if num % 3 == 0:
    dp[num] = min(dp[num], dp[num//3] + 1)
print(dp[n])