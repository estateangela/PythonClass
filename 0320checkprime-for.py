#用for-each寫質數問題
#求質數
num = int(input('請輸入整數:'))

isPrime = True
for n in range(2,num):
    if num %  n==0:
        isPrime = False
        break
    
if isPrime:
    print(f'{num}是質數')
else:
    print(f'{num}不是質數')


