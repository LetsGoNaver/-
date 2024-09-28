import sys
input = sys.stdin.readline
sik = input().split('-')
answer = 0
for i in range(0, len(sik)):
  s = sum(map(int,sik[i].split("+")))
  if i == 0:
    answer += s
  else:
    answer -= s
print(answer)
