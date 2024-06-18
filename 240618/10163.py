import sys
input = sys.stdin.readline

arr = [[0] * 1001 for _ in range(1001)]

N = int(input())
for num in range(1, N+1):
  sj, si, w, h = map(int, input().split())
  for i in range(si, si+h):
    for j in range(sj, sj+w):
      arr[i][j] = num

cnts = [0] * (N+1)
for lst in arr:
  for n in lst:
    cnts[n] += 1
print(*cnts[1:], sep="\n")