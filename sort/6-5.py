# 파이썬의 장점을 살린 퀵 정렬 (리스트 컴프리헨션 이용)
# 단점 : 전통적인 방법에 비해 수행 속도 느림

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  if len(array) <= 1: # basecase
    return array # out of place, 추가적인 공간 이용

  pivot = array[0]
  tail = array[1:]

  left_side = [i for i in tail if i <= pivot] 
  right_side = [i for i in tail if i > pivot]

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
  