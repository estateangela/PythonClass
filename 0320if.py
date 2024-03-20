num = 20
n=2
isPrime = True
while n<num:
    if num % n ==0:
        isPrime = False
        break
    n +=1
else:
    print('here is else')
if isPrime:
    print(num)
print('end-of-program')

#==
num = 20
n=2

while n<num:
    if num % n ==0:
        break
    n +=1
else:
    print('here is else')
if isPrime:
    print(num)
print('end-of-program')


