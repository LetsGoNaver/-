str1= input()
boom = input()
stack = []


for s in str1:
  stack.append(s)  
  if ''.join(stack[-len(boom):]) == boom:
    for _ in range(len(boom)):
      stack.pop()
if len(stack) == 0:
  print("FRULA")
else:
  print(''.join(stack))