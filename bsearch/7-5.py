# 이진 탐색을 이용한 부품 찾기

n = int(input())

a = list(map(int, input().split()))
a.sort() # 이진탐색을 하기위해 사전 정렬

m = int(input())

b = list(map(int, input().split()))

def bsearch(a, target, start, end):
  if start > end:
    return 'no'

  mid = (start + end) // 2
  if a[mid] == target:
    return 'yes'

  elif a[mid] < target:
    return bsearch(a, target, mid + 1, end)
    

  elif a[mid] > target:
    return bsearch(a, target, start, mid - 1)


for i in range(m):
  print(bsearch(a, b[i], 0, n - 1), end=' ')


