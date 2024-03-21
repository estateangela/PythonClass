#使用者輸入n
#輸出 1+2+…+?≥n的"過程跟結果"

n = int(input('請輸入整數:'))

sum = 0
output = ""
for i in range(1,n+1):
    sum +=i
    output += str(i)
    if sum < n:
        output += "+"
  

output +='≥'
print(output,f'{n}')