N = int(input())

tag = [0] * 10001
for i in range(N):
  tag[int(input())] += 1

for i in range(10001):
  if tag[i] != 0:
    for j in range(tag[i]):
      print(i)