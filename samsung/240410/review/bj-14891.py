import sys
input = sys.stdin.readline
N = 4
arr = [[int(x) for x in input().strip()] for _ in range(N)]
K = int(input())

top = [0] * N

for _ in range(K):
  idx, dr = map(int, input().split())
  idx -= 1
  tlst = [(idx, 0)]
  for i in range(idx + 1, N):
    if arr[i-1][(top[i-1] + 2) % 8] != arr[i][(top[i] + 6) % 8]:
      tlst.append((i,abs(idx-i) % 2))
    else:
      break
  for i in range(idx - 1, -1, -1):
    if arr[i][(top[i] + 2) % 8] != arr[i+1][(top[i+1] + 6) % 8]:
      tlst.append((i,abs(idx-i) % 2))
    else:
      break
  
  for i, rot in tlst:
    if rot==0:      # idx 톱니의 dr과 같은 방향
      top[i] = (top[i]-dr+8)%8
    else:
      top[i] = (top[i]+dr+8)%8
  
ans = 0
score = [1, 2, 4, 8]

for i in range(N):
  ans += arr[i][top[i]] * score[i]
print(ans)

  
