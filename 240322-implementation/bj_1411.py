import sys
input = sys.stdin.readline
N = int(input())
items = [input() for _ in range(N)]
answer = 0
for i in range(N-1):
  for j in range(i+1, N):
    flag = True
    a = items[i]
    b = items[j]
    for k in range(len(a)-1):
      aidx = [k]
      bidx = [k]
      for l in range(k+1, len(a)):
        if a[k] == a[l]:
          aidx.append(l)
        if b[k] == b[l]:
          bidx.append(l)
      if len(aidx) != len(bidx):
        flag = False
      else:
        for m in range(len(aidx)):
          if aidx[m] != bidx[m]:
            flag = False
    if flag:
      answer += 1
    
print(answer)