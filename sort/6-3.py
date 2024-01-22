# 삽입 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  for j in range(i, 0, -1): # i부터 1까지 반복
    if array[j] < array[j - 1]:
      array[j], array[j - 1] = array[j - 1], array[j] # 한 칸씩 왼쪽으로 이동
    else:
      break


print(array)
      