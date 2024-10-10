T = int(input())
for _ in range(T):
  answer = 0
  N = int(input())
  lst = []
  for _ in range(N):
    s, e = map(int, input().split())
    if s > e: # 14번방 -> 13번방도 가능하기 때문
      s, e = e, s
    lst.append((s,e))
  lst.sort()
  
  group = [0] * 201

  for s, e in lst:
    for i in range((s+1)//2, (e+1)//2 + 1):
      group[i] += 1
  answer = max(group) * 10
  print(answer)

