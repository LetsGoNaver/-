import sys
input = sys.stdin.readline
N, K = map(int, input().split())
num = input()
answer = []

for n in num:
  if len(answer) == 0:
    answer.append(n)
  else:
    if K > 0:
      while (len(answer) > 0 and answer[-1] < n and K > 0):
        answer.pop()
        K -= 1
      answer.append(n)
    else:
      answer.append(n)
if K > 0:
  answer = answer[:len(answer)-K-1]
print(''.join(answer))
