# 시각
'''n = int(input())
count = 0
time = [0] * 3
print(time)

for i in range(n):
  for j in range(60):
    for k in range(60):
      time[2] += 1
      if time[2] // 10 == 3 or time[2] % 10 == 3:
        count += 1
    time[2] = 0
    time[1] += 1
    if time[1] // 10 == 3 or time[1] % 10 == 3:
      count += 1
  time[1] = 0
  time[0] += 1
  if time[0] // 10 == 3 or time[0] % 10 == 3:
    count += 1

print (count)'''

# 위와 같이 작성하면 10 미만에서 조건이 성립하지 않음

n = int(input())
count = 0
time = [0] * 3

for i in range(n + 1): # ex) input: 5 -> 0 ~ 4
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1

print (count)