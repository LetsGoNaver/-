N = int(input())
def hanoi(num, start, to, end):
  if num == 1:
    print(start, end)
  else:
    hanoi(num-1, start, end, to)
    print(start, end)
    hanoi(num-1, to, start, end)
print(2**N - 1)
hanoi(N,1,2,3)