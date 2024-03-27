
mlist = [1,20,-20,30,44,55,39]

#mlist 最大值
print(max(mlist))
#mlist最小值
print(min(mlist))
#mlist平均值
print(sum(mlist)/len(mlist))

import random
random.shuffle(mlist)
print(mlist)

#mlist排序
mlist.sort()
print(mlist)

#mlist反轉
mlist.reverse()
print(mlist)
