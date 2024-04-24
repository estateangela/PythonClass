n=30
print(n)

def test():
    global n
    print(n)
    n = 10
    print(n)

test()
print(n)