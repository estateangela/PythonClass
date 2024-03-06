x = float(input("身高Cm:"))
y = float(input("體重Kg:"))

BMI = y/(x/100)**2
print(f'BMI:{BMI:.2f}',sep="")
