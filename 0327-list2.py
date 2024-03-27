from random import randint
mdata = [randint(0,9) for _ in range(10)]
print("Generated data:" ,mdata)
#        0  1  2  3  4  5  6  7  8  9
mdata = [5, 9, 1, 3, 0, 7, 10, 9, 8, 1]
#      -10 -9 -8 -7 -6 -5  -4 -3 -2 -1 

#取出第二個到第五個元素並輸出
print(mdata[1:5])
print(mdata[0:3])
print(mdata[:3])
print(mdata[3:len(mdata)]) #也可以不用len

print('mdata[1:5:2]:',mdata[1:5:2])
print('mdata[-9:-5:2]:',mdata[-9:-5:2])
print('mdata[1:-5:2]:',mdata[1:-5:2])


print(mdata[::-1])