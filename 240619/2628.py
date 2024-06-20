import sys
input = sys.stdin.readline

w, h = map(int, input().split())
wlst = [0,w]
hlst = [0,h]

C = int(input())

for _ in range(C):
  d, n = map(int, input().split())
  if d == 0:
    hlst.append(n)
  else:
    wlst.append(n)
  
wlst.sort()
hlst.sort()

mw = mh = float("-INF")

for i in range(len(wlst)-1):
  mw = max(mw, wlst[i+1] - wlst[i])

for i in range(len(hlst)-1):
  mh = max(mh, hlst[i+1] - hlst[i])

print( mw * mh )

