import sys
input = sys.stdin.readline

# 난장이의 키의 합은 100
# 아홉 난쟁이의 키가 주어졌을 때 일곱 난쟁이를 찾아라

def solve():
  for i in range(N-1):
    for j in range(i + 1,N):
      if lst[i] + lst[j] == target:
        return lst[i], lst[j]

# 진짜 난쟁이의 합이 100 -> 가짜 난쟁이의 합 = 전체 합 - 100
N = 9
lst = [int(input()) for _ in range(N)]

target = sum(lst) - 100

li, lj = solve()

lst.sort()
for i in range(N):
  if lst[i] != li and lst[i] != lj: 
    print(lst[i])


