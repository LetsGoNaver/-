# 좌표 평면은 뒤집어서 x 축은 j, y 축은 i 
# 검은 색종이의 둘레를 구하라
# 22 + 22 + 22 + 22 = 88 + 8 = 96 즉 내부도 포함이다.
# 겉둘레는 쉽게 구할 수 있겠다. 
# 내부 둘레를 어떻게 구할지가 간권

# 전체 순회하면서 1을 만나면
# 4방향을 확인해서 0의 개수가 곧 둘레이다.
import sys
input = sys.stdin.readline

def count(arr):
  cnt = 0
  for lst in arr:
    for i in range(1, len(lst)):
      if lst[i-1] != lst[i]:
        cnt +=1
  return cnt

arr = [ [0] * 102 for _ in range(102)]

N = int(input())
for _ in range(N):
  sj, si = map(int, input().split())
  for i in range(si, si + 10):
    for j in range(sj, sj + 10):
      arr[i][j] = 1

arr_t = list(map(list, zip(*arr))) # 전치행렬
# zip -> 순회하면서 각 인덱스에 있는 요소들을 묶어서 튜플로 만든다.
# * -> 언패킹 연산자로 리스트의 요소들을 개별적인 인자로 풀어준다. 2차원을 1차원으로.
# 그렇기에 행과 열이 바뀌는 것이다.

ans = count(arr) + count(arr_t)

        
print(ans)