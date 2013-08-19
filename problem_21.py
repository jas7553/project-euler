'''Jason A Smith'''
def isAmicableNumber(number):
    a = sumOfProperDivisors(number)
    b = sumOfProperDivisors(a)
    return b == number and a != b

def sumOfProperDivisors(number):
    return sum([divisor for divisor in getAllProperDivisors(number)])

def getAllProperDivisors(number):
    return [i for i in range(1, number) if number % i == 0]

allAmicableNumbers = [i for i in range(10000) if isAmicableNumber(i)]
print(sum(allAmicableNumbers))
