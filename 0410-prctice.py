data=[ [60,70,50,90],
      [55,100,60,70],
      [40,80,90,100],
]

for i in range(len(data)):
    for j in range(len(data[i])):
     print(f'data[{i}][{j}]={data[i][j]}',end=' ')
    print()
    
print('-----------')

A = 0
B = 1
C = 2

sum = 0
for i in range(4):
    sum += data[A][i]
print(f'AVG OF A = {sum/4}') 

sum = 0
for i in range(4):
    sum += data[B][i]
print(f'AVG OF B = {sum/4}')

sum = 0
for i in range(4):
    sum += data[C][i]
print(f'AVG OF C = {sum/4}')  