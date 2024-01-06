# 큰수의 법칙
'''n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)
sum = 0

while True:
  for i in range(k):
    sum += data[0]
    m -= 1
    if m == 0:
      break
  sum += data[1]
  m -= 1
  if m == 0:
    break

print(sum)'''

# m의 크기가 100억 이상으로 커지면 시간초과 판정을 받을 것임. 따라서 아래와 같이 수식으로 해결함

n,m,k = map(int, input().split())
data = list(map(int, input().split()))
  
data.sort(reverse=True)

result = data[0] * k + data[1]
result *= int(m / k+1)
result += data[0] * (m % (k + 1))

print(result)
...

