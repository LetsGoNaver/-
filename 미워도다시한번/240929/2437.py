N = int(input())
chu = list(map(int, input().split()))

chu.sort()

answer = 1
for i in chu:
  if answer < i:
    break
  answer += i

print(answer)