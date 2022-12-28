def isPrime(num):
    for i in range(2, num):
        if ((num % i) == 0):
            return(False)
    return(True)


def listPrime(len_num):
    primes = []
    j = 2
    while len(primes) != len_num:
        if isPrime(j):
            primes.append(j)
        j += 1
    return(primes)


def sumPrime(num):
    sum = 0
    i = 2
    while i < num:
        if isPrime(i):
            sum += i
            print(sum)
        i += 1
    return(sum)
