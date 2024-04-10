courses = ['python','管理數學','經濟學','行動商務']

scores = [
    ['學生A' , 60,70,50,90],
    ['學生B' , 50,100,60,70],
    ['學生C' , 40,80,90,100],
    ['學生D' , 100,60,40,80],
    ['學生E' , 90,40,55,100]
]

#五個學生的平均分數
for score in scores:
    print(score[0],end=':')
    msum = 0
    for i in range(1,len(score)):
        msum += score[i]
    print(f'{msum/len(courses):.2f}')

#學生B的最高分是哪一科? 幾分?
b_index = 1
std_b = scores[b_index]
#print(std)
mymax = -1
maxidx = -1
for score in range(1,len(std_b[1:])):
    if std_b[i] >= mymax:
        mymax = std_b[i]
        maxidx = i
print(f'學生B最高分的是{courses[maxidx-1]},分數是{mymax}')

#python的平均分數
python_index = 1
mysum = 0
for i in range(len(scores)):
    mysum += scores[i][python_index]

print(f'{courses[python_index-1]}的平均分數是{mysum/len(scores):.2f}')
    