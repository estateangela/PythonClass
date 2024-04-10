data = [
    [1,2,3],
    [11,22,33],
    [111,222,333],
    [1111,2222,3333],
]

print(data[1])

print('len=',len(data))
#可以得知串列的邏輯還是一維的

print(f'data[1][0]= {data[1][0]}')

for row in data:
    print(row)
    
for row in data:
    for i in row:
        print(i)

for i in range(len(data)):
    for j in range(len(data[i])):
     print(f'data[{i}][{j}]={data[i][j]}',end='')
    print()