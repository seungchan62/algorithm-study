# 성적 낮은 순서대로 학생 출력하기

n = int(input())

list = []
for i in range(n):
  input_data = input().split()
  list.append((input_data[0], int(input_data[1])))

# 키를 이용하여 점수를 기준으로 정렬
result = sorted(list, key = lambda student : student[1])

# for i in range(n):
#   print(result[i][0], end = ' ')

for student in result:
  print(student[0], end = ' ')