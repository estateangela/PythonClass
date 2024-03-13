import random
answer = random.randint(1,100)
print(f'answer = {answer}')

print('---------')

while True:
    userinput = int(input('請輸入整數:'))
    if userinput > answer:
        print('再小一點')
    elif userinput < answer:
        print('再大一點')
    else:
        print('bingo!!')
        break