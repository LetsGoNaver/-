import sys
input = sys.stdin.readline

def bt(depth, S):
  global numbers
  if depth == 6:
    print(*numbers)
    return
  for i in range(len(S)):
    if len(numbers) != 0:
      if numbers[-1] >= S[i]:
        continue
    numbers.append(S[i])
    bt(depth + 1, S)
    numbers.pop()


while True:
  case = list(map(int, input().split()))
  if case[0] == 0:
    break
  numbers = []
  K, S = case[0], case[1:] 
  bt(0, S)
  print() 
