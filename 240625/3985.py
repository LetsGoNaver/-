import sys
input = sys.stdin.readline

L = int(input())
N = int(input())
mx1 = mx2 = mx1_i = mx2_i = 0

lst = [1] * ( L + 1 )

for n in range(1, N+1):
  s, e = map(int, input().split())
  if mx1 < e - s + 1:
    mx1_i = n
    mx1 = e - s + 1
  
  cnt = sum(lst[s:e+1])
  if mx2 < cnt:
    mx2_i = n
    mx2 = cnt
  
  lst[s:e+1] = [0] * (e-s+1)

print(mx1_i)
print(mx2_i)
