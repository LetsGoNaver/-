import sys
input = sys.stdin.readline

N = 9

def solve():
  num = sum(lst) - 100
  for i in range(N-1):
    for j in range(i+1, N):
      if lst[i] + lst[j] == num:
        return lst[i], lst[j]

# 일곱 난쟁이의 키의 합이 100
# 전체 총 합 - 100 = 난장이가 아닌 두 명

lst = [int(input()) for _ in range(N)]
n, m = solve()

for i in sorted(lst):
  if i != n and i != m:
    print(i)

