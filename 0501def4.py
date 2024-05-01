x = 5
y= -5

x,y = y,x

print(f'x={x} , y = {y}')

#x=-5 , y=5
def myswap(x,y):
    return y,x

x,y = myswap(x,y)
print(f'x={x} , y={y}')