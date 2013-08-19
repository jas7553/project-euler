'''Jason A Smith'''
from math import *

def sumOfFactorialOfDigits(number):
    return sum([factorial(int(i)) for i in list(str(number))])

print(sum([i for i in range(3, 100000) if i == sumOfFactorialOfDigits(i)]))
