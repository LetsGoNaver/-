import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lans = [int(input()) for _ in range(K)]

start, end = 1, max(lans)

while start <= end:
  mid = ( start + end ) // 2
  cutoff = 0
  for lan in lans:
    cutoff += lan // mid

  if cutoff >= N:
    start = mid + 1
  else:
    end = mid - 1
print(end)


