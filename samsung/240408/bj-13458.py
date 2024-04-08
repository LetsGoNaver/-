import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int,input().split())
answer = 0

for a in A:
  answer += 1
  t = a - B
  if t > 0:
    if t % C == 0:
      answer += (t // C)
    else:
      answer += (t // C) + 1
print(answer)


