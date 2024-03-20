#求質數
userinput = int(input('請輸入整數:'))

i = 1
mcount = 0
while i <= userinput:
    if userinput % i == 0:
        mcount += 1
    i += 1
    print('----->')

if mcount == 2:
    print(f'{userinput}是質數')
else:
    print(f'{userinput}不是質數')
