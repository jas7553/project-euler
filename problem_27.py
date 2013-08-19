'''Jason A Smith'''
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

allPrimes = set(getPrimesBeneath(100000))

bestN = 0
bestAB = (1, 1)
for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while n**2 + a*n + b in allPrimes:
            n += 1
        if n > bestN:
            bestN = n
            bestAB = (a, b)

print(bestAB[0] * bestAB[1])
