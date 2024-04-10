import sys
input = sys.stdin.readline

arr = [[0] * 101 for _ in range(101)]
N = int(input())

d = [(0,1),(-1,0),(0,-1),(1,0)]

for _ in range(N):
  sj, si, dr, g = map(int, input().split())
  lst = [(si,sj)] # 시작 위치
  lst.append((si+d[dr][0], sj+d[dr][1])) # 0세대 끝점 추가

  for _ in range(g):
    # lst 끝 좌표 기준 90도 회전
    ei, ej = lst[-1]
    for i in range(len(lst)-2, -1, -1):
      ci, cj = lst[i]
      lst.append((ei-(ej-cj), ej+(ei-ci)))
  # arr에 드래곤커브 표시
  for i, j in set(lst):
    arr[i][j] = 1 

# 네 칸이 모두 1인 경우
cnt = 0
for i in range(100):
  for j in range(100):
    if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j+1] ==1 :
      cnt += 1

print(cnt)
      

