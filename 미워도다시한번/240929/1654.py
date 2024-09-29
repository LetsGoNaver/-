K, N = map(int, input().split())
arr = sorted([int(input()) for _ in range(K)])

s = 1
e = 10000000000000
m = (s+e) // 2

answer = []
while s <= e:
  m = (s + e ) // 2
  cnt = 0
  for a in arr:
    cnt += a // m
  if cnt >= N:
    answer.append(m)
    s = m + 1
  else:
    e = m - 1
print(max(answer))