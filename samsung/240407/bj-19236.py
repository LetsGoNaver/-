import sys
input = sys.stdin.readline

d = [(-1,0),(-1,-1), (0,-1),(1,-1), (1,0),(1,1),(0,1),(-1,1)]

def find(idx, v):
  for i in range(4):
    for j in range(4):
      if v[i][j][0] == idx:
        return (i,j, v[i][j][1])


def dfs(si,sj,sd, sm, v):
  # 종료조건 모호
  global ans
  ans = max(ans, sm)

  # [2] 물고기 이동 (1~16)
  for idx in range(1,17):
    ci, cj, dr = find(idx, v)
    if dr == -1: continue

    for j in range(8):
      td = (dr + j) % 8
      ni, nj = ci + d[td][0], cj + d[td][1]
      # 범위 내이고 상어가 아니면
      if 0 <= ni < 4 and 0 <= nj < 4 and (ni, nj) != (si,sj):
        v[ci][cj][1] = td
        v[ci][cj], v[ni][nj] = v[ni][nj], v[ci][cj]
        break
  
  # [3] 상어 이동(1칸~3칸) : 범위 내, and 물고기
  for mul in range(1,4):
    ni, nj = si + d[sd][0] * mul, sj + d[sd][1] * mul
    if 0 <= ni < 4 and 0 <= nj < 4 and v[ni][nj][1] != -1:
      fn, fd = v[ni][nj]
      v[ni][nj][1] = -1
      nv = [[l[:] for l in lst] for lst in v]
      dfs(ni,nj,fd,sm+fn,nv)
      v[ni][nj][1] = td

# [0] 물고기 입력
v = [[[0]*2 for _ in range(4)] for _ in range(4)]
for i in range(4):
  fish_list = list(map(int,input().split()))
  for j in range(4):
    v[i][j] = [fish_list[j * 2], fish_list[j*2+1]-1]

# [1] 상어의 초기 위치
ans = 0
fn, fd = v[0][0]
v[0][0][1] = -1
dfs(0,0,fd,fn,v)
print(ans)










# import sys
# input = sys.stdin.readline

# d = [(-1,0),(-1,-1), (0,-1),(1,-1), (1,0),(1,1),(0,1),(-1,1)]

# locate = {}

# info = []
# for _ in range(4):
#   temp = []
#   v = True # 홀수일 때 True
#   t = []

#   for x in list(map(int,input().split())):
#     if v:
#       t.append(x)
#       v = False
#     else:
#       t.append(x-1)
#       temp.append(t)
#       t = []
#       v = True
#   info.append(temp)

# for i in range(len(info)):
#   for j in range(len(info)):
#     num = info[i][j][0]
#     locate[num] = [i,j]

# # init
# ans = info[0][0][0]
# locate["S"] = [0,0]
# info[0][0] = ["S",info[0][0][1]]
# # 먹히면 -1
# locate[ans] = -1

# def fishMove():
#   for i in range(1,17):
#     if locate[i] == -1:
#       continue
#     cy, cx = locate[i]
#     dr = info[cy][cx][1]
#     dy, dx = cy + d[dr][0], cx + d[dr][1]
    
#     cnt = 0
#     while True:
#       if cnt == 4:
#         break

#       if 0<=dy<4 and 0<=dx<4:
#         if info[dy][dx] == "S":
#           dr = (dr + 1) % 8
#           cnt += 1
#         else:
#           if info[dy][dx] == []:
#             info[dy][dx] = [i,dr]
#             info[cy][cx] = []
#             break
#           else:
#             other = info[dy][dx]
#             target = info[cy][cx]
#             info[cy][cx] = other
#             info[dy][dx] = target
#             break
#       else:
#         dr = (dr + 1) % 8
#         cnt += 1

# def sharkMove(shAble, ate):
#   if len(shAble) == 0:
#     return ate
  
#   for i in range(1,4):
#     shy, shx = locate["S"]
#     if 0 <= shy + i < 4 and 0 <= shx + i < 4:
#       shAble.append(i)


# print(info)
# print(locate)

  
# # shAble = []
# #   for i in range(1,4):
# #     shy, shx = locate["S"]
# #     if 0 <= shy + i < 4 and 0 <= shx + i < 4:
# #       shAble.append(i)

# #   if len(shAble) == 0:
    
  

  
    










      



