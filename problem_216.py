'''Jason A Smith'''
'''unsolved'''
from math import *

def isPrime(number):
    for i in range(2, ceil(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def sieve(lst):
    index = 0

    while index < len(lst) // 2:
        p = lst[index]
        count = 1

        while index + count * p < len(lst):
            lst[index + count * p] = 0
            count += 1

        index += 1
        while lst[index] == 0:
            index += 1

def getPrimesBeneath(max):
    primes = list(range(2, max + 1))
    sieve(primes)
    
    return [i for i in primes if i != 0]

'''
allPrimes = getPrimesBeneath(10000000)
biggest = allPrimes[-1]
print(len(allPrimes))
print(biggest)
allPrimes = set(allPrimes)
'''

count = 0
for n in range(2, 10000 + 1):
    number = 2 * n**2 - 1
    if isPrime(number):
        count += 1

print(count)
