fruit = ['apple', 'banana','cherry','date','elderberry']
#使用索引值取列表第二個項目
print(fruit[2])
#更新列表中第四個項目
fruit[3]='grape'
print(fruit)
#刪除列表中第三個項目
del fruit[2]
print(fruit)
#在列表中新增一個項目
fruit.append('Friday')
print(fruit)
#計算列表長度
print(len(fruit))
fruit.append('Great')
print(len(fruit))