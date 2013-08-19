'''Jason A Smith'''
from math import *

def numDivisors(number):
    count = 0
    for i in range(1, ceil(sqrt(number))):
        if number % i == 0:
            count += 1
    return count * 2

count = 1
triangleNumber = 1

while numDivisors(triangleNumber) <= 500:
    count += 1
    triangleNumber += count

print(triangleNumber)
