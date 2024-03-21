import sys
input = sys.stdin.readline
N = int(input())

numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))

max_result = float("-INF")
min_result = float("INF")

def bt(sum, idx):
  global max_result
  global min_result
  global operations
  if idx == len(numbers):
    max_result = max(max_result, sum)
    min_result = min(min_result, sum)
    return
  temp = sum
  for i in range(len(operations)):
    if operations[i] == 0:
      continue
    if i == 0:
      sum += numbers[idx]
    elif i == 1:
      sum -= numbers[idx]
    elif i == 2:
      sum *= numbers[idx]
    else:
      if sum < 0:
        sum = (abs(sum) // numbers[idx]) * -1
      else:
        sum //= numbers[idx]
    operations[i] -= 1
    bt(sum, idx + 1)
    sum = temp
    operations[i] += 1

bt(numbers[0],1)

print(max_result, min_result)
