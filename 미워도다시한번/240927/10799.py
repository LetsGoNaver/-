import sys
input = sys.stdin.readline

bim = input()
stack = []
answer = 0
for i in range(len(bim)-1):
  if bim[i] == "(":
    stack.append(bim[i])
  else:
    if bim[i-1] == "(":
      stack.pop()
      answer += len(stack)
    else:
      stack.pop()
      answer += 1
print(answer)

  

