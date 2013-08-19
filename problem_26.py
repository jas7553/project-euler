def isPrime(number):
    for i in range(2, number//2 + 1):
        if number % i == 0:
            return False
    return True

def primeGenerator():
    prime = 0
    while 1:
        prime += 1
        if isPrime(prime):
            yield prime    

p = primeGenerator()

result = {}

d = next(p)
while d < 1000:
    result[d] = 1 / d
    d = next(p)

for key in result:
    print(str(key) + ': ' + str(result[key]))

