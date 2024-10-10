n = int(input())
arr = list(map(int, input().split()))

# dp[i]: arr[i]를 포함하는 연속 부분합 중 최대 합
dp = [0] * n
dp[0] = arr[0]  # 첫 번째 원소로 초기화

# dp 테이블 채우기
for i in range(1, n):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])

# dp 배열 중 가장 큰 값을 출력 (최대 연속합)
print(max(dp))
