import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 토네이도 이동 방향
d = [(0,-1), (1,0), (0,1),(-1,0)]
# y 기준 모래 바람 위치
a = [[(-2,0),(-1,-1), (-1,0), (-1,1),(0,-2), (1,-1),(1,0),(1,1),(2,0),(0,-1)],
     [(0,-2),(1,-1), (0,-1), (-1,-1),(2,0), (1,1),(0,1),(-1,1),(0,2),(1,0)],
     [(2,0),(1,1), (1,0), (1,-1),(0,2), (-1,1),(-1,0),(-1,-1),(-2,0),(0,1)],
     [(0,2),(-1,1), (0,1), (1,1),(-2,0), (-1,-1),(0,-1),(1,-1),(0,-2),(-1,0)]]
# 모래 이동 퍼센트
mul = [2,10,7,1,5,10,7,1,2,0]

cnt_mx = 1
cy = cx = N//2
answer = dr = cnt = flag = 0


while (cy, cx) != (0,0):
  cy, cx = cy + d[dr][0], cx + d[dr][1]
  
  # [1] cy, cx 기준좌표 중심으로 모래량 계산 추가, 범위 밖 => ans 추가
  if (arr[cy][cx] > 0):
    val = arr[cy][cx]  
    sm = arr[cy][cx] = 0    
    

    for i in range(10):   # 위치 0 ~ 9까지 처리
      ny, nx = cy + a[dr][i][0], cx + a[dr][i][1]
      t = (val * mul[i]) // 100
      
      if i == 9: # a position
        t = val - sm

      if 0 <= ny < N and 0 <= nx < N:
        arr[ny][nx] += t
      else:
        answer += t
      sm += t

  cnt += 1
  if cnt == cnt_mx:
    cnt = 0
    dr = (dr + 1) % 4
    if flag == 0:
      flag = 1
    else:
      flag = 0
      cnt_mx += 1
print(answer)
