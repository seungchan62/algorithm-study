# 1이 될때까지
n, k = map(int,input().split())

count = 0

while True:
  if n == 1:
    break
  elif n % k != 0:
    n -= 1
    count += 1
  elif n % k == 0:
    n = n // k
    count += 1

print(count)

# 아래 방법은 나중에 이해
n, k = map(int,input().split())
result = 0
while True:
  target = (n // k) * k
  result += (n - target)
  n = target
  if n < k:
    break
  result += 1
  n //= k

result += (n - 1)
print(result)

  