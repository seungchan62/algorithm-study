# 왕실의 나이트
data = input() # 리스트로 굳이 안받아도 됨

# 파이썬은 int를 안 붙히면 문자열로 인식한다는 것 생각하자
raw = int(ord(data[0])) - int(ord('a')) + 1 
col = int(data[1])

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]

count = 0
for step in steps:
  next_raw = raw - step[0]
  next_col = col - step[1]
  # or(x) 전부 만족해야함
  if next_raw > 0 and next_raw <= 8 and next_col > 0 and next_col <= 8:
    count += 1

print(count)



