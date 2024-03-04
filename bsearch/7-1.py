# 순차탐색 소스코드

def ssearch(n, target, array):
  for i in range(n):
    if array[i] == target:
      return i + 1

print ("문자 개수와 타겟 문자를 적어라")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("문자 개수만큼 띄어쓰기로 구분하여 문자를 적어라")
array = input().split()

print(ssearch(n, target, array))