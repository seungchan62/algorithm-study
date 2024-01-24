# 퀵 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end: # 종료 조건 - 원소가 한 개일때
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:
    while left <= end and array[pivot] >= array[left]:
      left += 1
    while right > start and array[pivot] <= array[right]:
      right -= 1
    # 작은 수랑 피벗 교체 후 반복문 탈출
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
  
    else:
      array[left], array[right] = array[right], array[left]

  quick_sort(array, start, right - 1) # 왼쪽 리스트
  quick_sort(array, right + 1, end) # 오른쪽 리스트

quick_sort(array, 0, len(array) - 1)
print(array)