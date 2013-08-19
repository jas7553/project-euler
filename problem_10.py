'''Jason A Smith'''
import time

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
    
    return primes 

print(sum(getPrimesBeneath(2000000)))
