# 꼭 다시풀어보기

def checker(s,e,d,L):
  while s < e:
    m = (s+e) // 2
    if L[m] < d:
      s = m + 1
    else:
      e = m
  return e

N, H = map(int, input().split())
up = []
down = []

for i in range(N):
  if i % 2 == 0:
    down.append(int(input()))
  else:
    up.append(int(input()))

down.sort()
up.sort()

answer = 0
result = [0] * (H+1)
mx = float("INF")

for i in range(1,H):
  idxd = checker(0,len(down),i,down)
  idxu = checker(0, len(up),(H-i+1), up)
  result[i] = N // 2 - idxd + N //2 - idxu
  mx=min(mx, result[i])

for i in range(1, H+1):
  if result[i] == mx : answer += 1

print(mx, answer)
