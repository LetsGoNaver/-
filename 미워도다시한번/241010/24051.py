N, K = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
def insertSort(arr):
  global ans
  n = len(arr)
  for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      ans.append(arr[j])
      j -= 1
    if (j+1 != i):
      arr[j+1] = key
      ans.append(key)
insertSort(arr)
if len(ans) < K:
  print(-1)
else:
  print(ans[K-1])