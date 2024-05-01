def mysum(*nums):
    print(type(nums))
    print(len(nums))
    
    result = 0
    for d in nums:
        result+=d
    return result

print(mysum(1,2,3,4,5))

def mydiv(num0,num1,*num2):
    print(f'num0 = {num0}')
    print(f'num1 = {num1}')
    print(f'num2 = {num2}')

mydiv(1,2,3,4,5,-5,-4,-3)

print('test',3,5,sep='@',end='~end~')
print('test',3,5)

