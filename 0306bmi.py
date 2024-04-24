x = float(input("身高Cm:"))
y = float(input("體重Kg:"))

BMI = y/(x/100)**2
print(f'BMI:{BMI:.2f}',sep="")


if BMI < 18.5:
    print('體重過輕')
elif BMI < 24:
     print('正常範圍')
else:
    print('異常範圍-',end="")
    if 24<= BMI < 27:
        print('過重')
    elif BMI<30:
        print('輕度肥胖')
    else:
        print('重度肥胖')
    
    
    

print('最後一行')