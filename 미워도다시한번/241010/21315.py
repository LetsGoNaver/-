N = int(input())
revArr = list(map(int, input().split()))
K = [1,2,3,4,5,6,7,8,9]
ans = []
def slider(arr, step):
  if step <= 0:
    return arr
  left = arr[:-step]
  right = arr[-step:]

  return slider(right, step // 2) + left

def bT(select, ks):
  global ans
  if select == 2:
    arr = [x for x in range(1, N + 1)]
    for k in ks:
      step = 2 ** k
      arr = slider(arr,step)
    
    if arr == revArr:
      ans.append(list(ks))
      return
    return
      
  for i in range(9):
    ks.append(K[i])
    bT(select + 1, ks)
    ks.pop()

bT(0,[])
print(' '.join(map(str, ans[0])))