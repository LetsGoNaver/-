# N 장의 카드 중 3장의 카드를 고른다.
# M 과 최대한 가까운 숫자가 되도록 만든다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

ans = float("-INF")

for i in range(N-2):
  for j in range(i+1, N-1):
    for k in range(j+1,N):
      if lst[i] + lst[j] + lst[k] <= M:
        ans = max(ans, lst[i] + lst[j] + lst[k])
print(ans)