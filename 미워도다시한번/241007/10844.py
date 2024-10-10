n = int(input())
MOD = 1000000000

# dp[i][j]: i자리 계단 수 중에 맨 끝이 j인 수의 개수
dp = [[0] * 10 for _ in range(n + 1)]

# 1자리 계단 수 초기화
for i in range(1, 10):
    dp[1][i] = 1

# DP 테이블 채우기
for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][1] % MOD
    for j in range(1, 9):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD
    dp[i][9] = dp[i - 1][8] % MOD

# 모든 i자리 계단 수의 합
result = sum(dp[n]) % MOD
print(result)
