import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())),reverse=True)

answer = 0

for i in range(N):
  for j in range(N):
    if A[i] > B[j] and A[i] != 0 and B[j] != 0:
      answer += 2
      A[i] = 0
      B[j] = 0
      break

for i in range(N):
  if A[i] == 0:
    continue
  for j in range(N):
    if A[i] >= B[j] and A[i] != 0 and B[j] != 0:
      answer += 1
      A[i] = 0
      B[j] = 0
      break
print(answer)
