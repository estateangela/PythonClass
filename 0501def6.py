def mysum(n):
    if n == 1:
        return 1
    return mysum(n-1) + n

print(mysum(10))

def mypower(m,n):
    if n ==0:
        return 1
    return mypower(m,n-1)*m

print(mypower(5,3))

def myfib(n):
    if n == 0: return 0
    if n == 1: return 1
    return myfib(n-1)+myfib(n-2)

print(myfib(2))
print(myfib(3))
print(myfib(4))
print(myfib(10))