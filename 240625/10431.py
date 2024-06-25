import sys
input = sys.stdin.readline

P = int(input())
for case in range(1, P+1):
  lst = list(map(int, input().split()))[1:]
  cnt = 0
  for i in range(1,len(lst)):
    for j in range(i):
      if lst[j] > lst[i]:
        cnt += 1
  print(case, cnt)
