import sys
input = sys.stdin.readline

N = int(input())

arr = [[0] * 101 for _ in range(101)]

d = [(0,1), (-1,0),(0,-1),(1,0)]
for _ in range(N):
  sj, si, dr, g = map(int, input().split())
  lst = [(si,sj)]
  lst.append((si+d[dr][0], sj+d[dr][1]))

  for i in range(g):
    ei, ej = lst[-1]
    for idx in range(len(lst)-2, -1, -1):
      ci, cj = lst[idx]
      lst.append((ei-(ej-cj), ej + (ei-ci)))
  for i, j in set(lst):
    arr[i][j] = 1
cnt = 0
for i in range(100):
  for j in range(100):
    if arr[i][j] == arr[i+1][j] == arr[i][j+1] == arr[i+1][j+1] == 1:
      cnt += 1
print(cnt)