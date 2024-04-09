import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
operation = list(map(int,input().split()))


mx_ans = float("-INF")
mi_ans = float("INF")
def bt(depth, sm):
  global mx_ans, mi_ans
  if depth == N-1:
    mx_ans = max(mx_ans, sm)
    mi_ans = min(mi_ans, sm)
    return

  for i in range(4):
    t = sm
    if operation[i] == 0:
      continue
    if i == 0:
      sm += A[depth+1]
    elif i == 1:
      sm -= A[depth+1]
    elif i == 2:
      sm *= A[depth+1]
    else:
      if sm < 0:
        sm = (abs(sm) // A[depth+1]) * (-1)
      else:
        sm = abs(sm) // A[depth+1]
    operation[i] -= 1
    bt(depth + 1, sm)
    sm = t
    operation[i] += 1

bt(0,A[0])
print(mx_ans)
print(mi_ans)
