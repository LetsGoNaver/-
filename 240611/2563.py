# 좌표는 뒤집어라. x 축이 j, y 축이 i 
# 영역의 넓이는 1로 채워넣자.

import sys
input = sys.stdin.readline

N = int(input())
arr = [ [0] * 100 for _ in range(100)]

for _ in range(N):
  sj, si = map(int, input().split())
  for i in range(si, si+10):
    for j in range(sj, sj + 10):
      arr[i][j] = 1

print(sum(map(sum,arr))) 