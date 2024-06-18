# import sys
# input = sys.stdin.readline
# j, i = map(int, input().split())
# arr = [[0] * j for _ in range(i)]
# N = int(input())
# for ca in range(1,N+1):
#   d, n = map(int,input().split())
#   if d == 0:
#     for i in range(len(arr)):
#       for j in range(len(arr[0])):
#         if i < n:
#           arr[i][j] += 0
#         else:
#           arr[i][j] += ca
#   else:
#     for j in range(len(arr[0])):
#       for i in range(len(arr)):
#         if j < n:
#           arr[i][j] += 0
#         else:
#           arr[i][j] += ca

# # print(*arr, sep="\n")

# cnt = [0] * (j*i + 1)
# for i in range(len(arr)):
#   for j in range(len(arr[0])):
#     cnt[arr[i][j]] += 1
# print(max(cnt))

import sys
input = sys.stdin.readline
R, C = map(int, input().split())
N = int(input())

c_lst = [0,C] # 세로
r_lst = [0,R] # 가로

for _ in range(N):
  d, n = map(int, input().split())
  if d == 0:
    c_lst.append(n)
  else:
    r_lst.append(n)
c_lst.sort()
r_lst.sort()

mw = float("-INF")
mh = float("-INF")

for i in range(len(c_lst)-1):
  mh = max(mh, c_lst[i+1] - c_lst[i])
for i in range(len(r_lst)-1):
  mw = max(mw, r_lst[i+1] - r_lst[i])
print(mh * mw)