#使用者輸入n
#輸出 1+2+…+n的"過程跟結果"

n = int(input('請輸入整數:'))
#使用者輸入

sum = 0
output = ""
#宣告變數
#i介於1~n之間，sum+i，output就加一次i
for i in range(1,n+1):
    sum +=i
    output += str(i)
#i<n時，output則在i後面多加+
    if i < n:
        output += "+"
#i>n時跳出迴圈
#在最後output＝sum
output +='=' + str(sum)
print(output)