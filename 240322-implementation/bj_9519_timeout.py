import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
word = [x for x in input().rstrip()]
n = len(word)
for _ in range(N):
  even = deque([])
  ordi = deque([])
  for i in range(n):
    if n % 2 == 1:
      if i % 2 == 0:
        even.append(word[i])
      elif i % 2 == 1:
        ordi.appendleft(word[i])
    if n % 2 == 0:
      if i % 2 == 0:
        even.append(word[i])
      elif i % 2 == 1:
        if i == n-1:
          even.append(word[i])
        else:
          ordi.appendleft(word[i])
  word = list(even) + list(ordi)
print("".join(word))      
