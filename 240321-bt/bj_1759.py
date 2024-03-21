import sys
input = sys.stdin.readline

L, C = map(int, input().split())
candidates = input().split()
candidates.sort()

indicator = ['a', 'e', 'i', 'o', 'u']

bucket = []
def bt(start, depth, mo, ja):
  global bucket
  if depth == L:
    if mo > 0 and ja > 1:
      print(''.join(bucket))
      return
    else:
      return
  for i in range(start, C):
    if candidates[i] in indicator:
      bucket.append(candidates[i])
      bt(i + 1, depth + 1, mo + 1, ja)
      bucket.pop()
    else:
      bucket.append(candidates[i])
      bt(i + 1, depth + 1, mo, ja + 1)
      bucket.pop()

bt(0, 0, 0, 0)