import sys
input = sys.stdin.readline

arr = [[0] * 1001 for _ in range(1001)]

cands = {}

N = int(input())
for n in range(1,N+1):
  sj, si, w, h = map(int,input().split())
  for i in range(si,si+h):
    arr[i][sj:sj+w] = [n] * w
    # for j in range(sj,sj+w):
    #   arr[i][j] = n
    #   cands[n] = 0

# 내코드
for i in range(len(arr)):
  for j in range(len(arr[0])):
    if arr[i][j] != 0:
      cands[arr[i][j]] += 1

for k,v in cands.items():
  print(v)

# [1] 색종이 개수별로 전체 arr 순회 : 시간 오래걸려
for n in range(1, N+1):
  cnt = 0
  for lst in arr:
    cnt += lst.count(n)
  print(cnt)

# [2] cnts: 빈도수 배열 사용해서 arr을 한 번만 순회
cnts = [0] * (N+1)
for lst in arr:
  for n in lst:
    cnts[n] += 1
print(*cnts[1:], sep="\n")