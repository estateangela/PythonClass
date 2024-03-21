#使用者輸入n
#輸出 1+2+…+n的"結果"

n = int(input('請輸入整數:'))

sum = 0
for n in range(1,n+1):
    sum +=n

print(sum)