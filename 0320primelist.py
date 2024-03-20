#用for-each寫質數問題
#求質數
for num in range(100,1001):
  isPrime = True
  for n in range(2,num):
        if num %  n==0:
         isPrime = False
         break
  if isPrime:
    print(num) 


