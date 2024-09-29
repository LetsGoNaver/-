N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())
cand = list(map(int, input().split()))

for c in cand:
  flag = False
  s = 0
  e = len(arr) - 1
  m = (s + e) // 2
  while s <= e:
    if arr[m] == c:
      flag = True
      break
    elif arr[m] > c:
      e = m - 1
      m = (s+e) //2
    else:
      s = m + 1
      m = (s+e) // 2
  if flag:
    print(1)
  else:
    print(0)
