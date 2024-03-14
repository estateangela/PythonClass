#1-100,無限詢問使用者輸入一個數字

'''
import random

answer = random.randint(1,100)
print(f'答案 = {answer}')
'''

import random
A = random.randint(1,100)
print(f'答案={A}')

print('---------')


while True  :
    x = int(input("請輸入數字:"))
    if x <A:
     print('再大一點')
    
    elif x > A  :
        print('再小一點')
        
    else:
           print('BINGO')
           break
