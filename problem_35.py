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
    
    return primes

def mkRotationGenerator(number):
    strlist = list(str(number))
    length = len(strlist)
    for i in range(0, length):
        nextNum = ''
        for j in range(0, length):
            nextNum += strlist[(i + j) % length]
        yield int(nextNum)

allPrimes = [i for i in getPrimesBeneath(1000000) if i != 0]
circularPrimes = []

for prime in allPrimes:
    rgen = mkRotationGenerator(prime)
    while 1:
        try:
            if not next(rgen) in allPrimes:
                break
        except StopIteration:
            print('found: ' + str(prime))
            circularPrimes.append(prime)
            break

print(len(circularPrimes))
