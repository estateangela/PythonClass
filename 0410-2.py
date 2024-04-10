data = []

for i in range(100):
    if i % 7 == 0:
        data.append(i)
    
print(data)

data = [i for i in range(100)]
print(data)

data = [i for i in range(100) if i % 7 ==0]
print(data)

#把串列最後一個值刪除
del data[-1]
print(data)

#使用索引值之前要先有判斷式
if 57 in data:
    idx = data.index(57)
    print(f'idx={idx}')
    del data[idx]
print(data)

#idx = data.index(57)
#print(f'idx={idx}')
#del data[idx]
