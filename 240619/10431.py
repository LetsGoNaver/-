import sys
input = sys.stdin.readline
P = int(input())
ans = []
for _ in range(P):
  lst = list(map(int, input().split()))
  tc = lst.pop(0)
  tlst = []
  mov = 0
  for l in lst:
    tlst.append(l)
    for i in range(len(tlst)):
      if tlst[i] > l:
        mov += len(tlst) - 1 - i
        tlst.insert(i,l)
        tlst.pop(len(tlst)-1)
        break
  ans.append([tc, mov])
for a in ans:
  print(*a)

