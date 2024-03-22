import sys
input = sys.stdin.readline

N = int(input())
requests = list(map(int, input().split()))
budget = int(input())

start, end = 0, max(requests)


while start <= end:
  mid = ( start + end ) // 2
  temp = 0
  
  for req in requests:
    if req >= mid:
      temp += mid
    else:
      temp += req
  if temp > budget:
    end = mid - 1
  else:
    start = mid + 1
print(end)