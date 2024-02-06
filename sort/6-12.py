# 두 배열의 원소 교체

n, k = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list1.sort()
list2.sort(reverse=True)

for i in range(k):
  if list1[i] < list2[i]:
    list1[i], list2[i] = list2[i], list1[i]
  else:
    break # i=3일 때 조건이 성립하지 않으면 그 이후로도 조건 성립x

print(sum(list1))