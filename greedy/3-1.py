# 거스름돈
n=1260
count=0

#큰 단위의 화폐부터
array=[500,100,50,10]

for coin in array:
  count+=n//coin 
  n%=coin
print(count)
