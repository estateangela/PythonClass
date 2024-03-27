#九九乘法表

for i in range(1,7):
 for j in range(1,i):
    print(f'{i}x{j}={i*j}',end='   ')
 print()

print('--------------')
#左下角
 
N = 5
for i in range(N):  #range(N)=range(0,N)=range(1,N+1)
    for j in range(i+1):
        print('*',end='')
    print()

print('--------------')    
#左上角

n=5
for i in range(n,0,-1):
    for j in range(i):
         print('*',end='')
    print()

print('--------------')    
#右下角

for i in range(N):
    for j in range(N-i): #i=1 => for j in range(4): => [0,1,2,3]
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
    
print('--------------')
#右上角

for i in range(n,0,-1):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(i): #i=1 => for j in range(4): => [0,1,2,3]
        print('*',end=' ')
    print()
    
print('--------------')
#python限定快速寫法

for i in range(n,0,-1):
    print("" * (n - i)+ '*' * i)
    
print('--------------')
    
    