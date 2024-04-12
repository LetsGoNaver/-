import sys
input = sys.stdin.readline
n, m, h, k = map(int, input().split())

arr = [[0] * n for _ in range(n)] # 나무 위치면 1 아니면 0
runner = [] # [i, j, 움직이는 방향, 안잡히면 False]
d = []
for _ in range(m):
    i,j,dr = map(int,input().split())
    runner.append([i-1,j-1,dr,False])
    if dr == 1:
        d.append([0,1])
    else:
        d.append([1,0])
for _ in range(h):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1 # 나무의 위치 = 1
ei = ej = n//2

cat_d = [(-1,0),(0,1),(1,0),(0,-1)]
cat_dr = cnt = flag = 0
t_flag = cnt_mx = 1

answer = 0
for t in range(1,k+1):
    def catch(si, sj, sdr, t):
        global answer
        cnt = 0
        for i in range(0,3):
            ni, nj = si + cat_d[sdr][0] * i, sj + cat_d[sdr][1] * i
            if 0 <= ni < n and 0 <= nj < n:
                for ri in range(len(runner)):
                    cri, crj = runner[ri][0], runner[ri][1]
                    if (cri, crj) == (ni, nj) and arr[ni][nj] != 1 and not runner[ri][3]:
                        # 점수 후보군 
                        cnt += 1
                        runner[ri][3] = True
            else:
                break
        answer += (cnt * t)

    # 러너의 이동
    for ri in range(len(runner)):
        ci, cj, cdr, catched = runner[ri]
        if not catched:
            if abs(ci-ei) + abs(cj-ej) <= 3:
                ni, nj = ci + d[ri][0], cj + d[ri][1]
                if 0 <= ni < n and 0 <= nj < n:
                    if (ni, nj) != (ei,ej):
                        runner[ri][:2] = [ni, nj]  # 위치 업데이트
                    # 아니면 정지
                else: # 격자 밖이면
                    # 방향 뒤집기
                    if cdr == 1:
                        d[ri][1] = d[ri][1] * -1
                    else:
                        d[ri][0] = d[ri][0] * -1
                    ni, nj = ci + d[ri][0], cj + d[ri][1]
                    if 0 <= ni < n and 0 <= nj < n:
                        if (ni, nj) != (ei,ej):
                            runner[ri][:2] = [ni, nj]  # 위치 업데이트
                        # 아니면 정지
        
    # 술래의 이동
    ei, ej = ei + cat_d[cat_dr][0], ej + cat_d[cat_dr][1]
    cnt += 1
    arr[ei][ej] = t
    if (ei, ej) == (0,0) or (ei,ej) == (n//2, n//2): # 방향 틀기
        t_flag *= -1
        cat_dr = (cat_dr + +2) % 4 # 방향 틀기
        # 도망자 탐색 ------------------------------
        catch(ei, ej, cat_dr, t)
        cnt = 0
        if t_flag != -1:
            flag = 0
        else:
            cnt += 1
            flag = 1
        
    else:
        if t_flag == 1:
            if cnt == cnt_mx:
                cnt = 0
                cat_dr = (cat_dr + 1) % 4 # 방향 전환 하는 부분 -> 여기서 도망자들 찾기
                # 도망자 탐색 ------------------------------
                catch(ei, ej, cat_dr, t)
                if flag == 0:
                    flag = 1
                else:
                    flag = 0
                    cnt_mx += 1
        else:
            if cnt == cnt_mx:
                cnt = 0
                cat_dr = (cat_dr - 1) % 4 # 방향 전환 하는 부분 -> 여기서 도망자들 찾기
                # 도망자 탐색 ------------------------------
                catch(ei, ej, cat_dr, t)
                if flag == 0:
                    flag = 1
                else:
                    flag = 0
                    cnt_mx -= 1
                    

print(answer)