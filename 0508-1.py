# set 集合 會把重複的值去掉
mlist = [10,2,30,5,10,2,30,5]
mSet = {10,2,'test',30,5,10,2,30,5,'test'}
print('mlist =>',mlist)
print('mSet = >',mSet)
#print('mSet[0] =>' , mSet[0]) 會出錯
for d in mSet:
    print(d)

#Dictionary
mDict = {"k1":"value" , "k2" :10 ,"k3" :100,"k4":"test"}
print(mDict)
print(type(mDict))
print('mDict["k2"] =>',mDict["k2"])

mDict = {1:"A", 2:"B", 0:'C', 3:'D'}
print(mDict[0])
#print(mDict['0'])

mDict = {1:"A", 2:"B", 0:'C', 3:'D',2:'A'}
print(mDict)
print(mDict.keys())
print(mDict.values())
print('mDict.items:',mDict.items())

print('-----------------')
mlist = []
mlist.append('A')
print(mlist)
mtuple = ()
mtulple = tuple()
print(mtuple)
mSet = set()
mthing = {}
mDict = dict()
print(type(mthing))

print(list('test-test1-hello'))
print(set('test-test1-hello'))

mlist = []
mlist.append('A')
mlist.append(['A','B'])
mlist.extend(['A','B']) #會拆開加進去
print(mlist)

print('---------------------')

mset = set()
mset.add('A')
mset.add('B')
mset.add('A')
print(mset)

print('---------------------')

mdict = {}
mdict['A'] = 'Hello'
mdict['B'] = 'NTUB'
mdict['A'] = '12345' #後面的value會把前面的覆蓋
print(mdict)
