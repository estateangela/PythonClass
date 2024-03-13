#1-100,無限詢問使用者輸入一個數字

'''
import random

answer = random.randint(1,100)
print(f'答案 = {answer}')
'''

import random
A = random.randint(1,100)
print(A)

print('---------')

x = int(input("請輸入數字:"))

while x < A:
    print('再大一點')
    x = int(input("請輸入數字:"))
    if x > A:
        print('再小一點')
        x = int(input("請輸入數字:"))
        if x == A:
           print('BINGO')
           break
