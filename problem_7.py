'''Jason A Smith'''
def isPrime(number):
    for i in range(2, number//2 + 1):
        if number % i == 0:
            return False
    return True

def findNthPrime(n):
    count = 0
    prime = 1
    while count < n:
        prime += 1
        if isPrime(prime):
            count += 1
    return prime

print(findNthPrime(10001))
