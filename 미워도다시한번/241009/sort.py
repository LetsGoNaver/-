def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    swapped = False
    for j in range(1, n-i):
      if arr[j-1] > arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        swapped = True
    if not swapped:
      break
  return arr

def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_idx = i
    for j in range(i+1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr

def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr

def merge_sort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        arr[k] = left[i]
        i += 1
      else:
        arr[k] = right[j]
        j += 1
      k += 1
    while i < len(left):
      arr[k] = left[i]
      i += 1
      k += 1
    
    while j < len(right):
      arr[k] = right[j]
      j += 1
      k += 1
  return arr

def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  right = [x for x in arr if x > pivot]
  mid = [x for x in arr if x == pivot]
  return quick_sort(left) + mid + quick_sort(right)

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
print(selection_sort([64, 25, 12, 22, 11]))
print(insertion_sort([12, 11, 13, 5, 6]))
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
print(quick_sort([3, 6, 8, 10, 1, 2, 1]))