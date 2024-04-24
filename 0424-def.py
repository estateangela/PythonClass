def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            print(f'{n} is not a prime')
            break
    else:
        print(f'{n} is a prime')
if __name__ == '__main__':
 isPrime(10)
 isPrime(11)
 isPrime(12)
 isPrime(13)
 isPrime(16)




