def trapezoidArea(top,bottom,height):
    return (top+bottom)*height/2

print(trapezoidArea(2,10,6)) # position based 
print(trapezoidArea(2,height=6,bottom=10)) # keyword based

#print(trapezoidArea(top=2,6,10)) #error
print(trapezoidArea(bottom=2,height=6,top=10))