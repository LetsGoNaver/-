import sys
input = sys.stdin.readline

# 주어지는 input값들은 왼쪽아래 꼭짓점의 좌표
# 익숙한 형태로 바꾸기 input값들을 왼쪽 위 꼭짓점좌표로
N = int(input())
arr = [[0] * 100 for _ in range(100)]
for _ in range(N):
  sj, si = map(int, input().split())
  for i in range(si, si+10):
    for j in range(sj, sj+10):
      arr[i][j] = 1

print(sum(map(sum, arr)))
