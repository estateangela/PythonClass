data = [10,9,'test',12,'hello world']

for i in data:
    print(i)

print('test' not in data)

data.append('NTUB')
print(data)
data.append([1,2,3])
print(data)
data.extend([4,5,6])
print(data)

data = [204,20,-1,10,-5]
data.sort()
print(data)
data.reverse()
print(data)