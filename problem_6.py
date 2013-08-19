'''Jason A Smith'''
import math

def sumOfSquares(start, end):
    return sum([i * i for i in range(start, end + 1)])

def squareOfSums(start, end):
    return math.pow(sum([i for i in range(start, end + 1)]), 2)

print(squareOfSums(1, 100) - sumOfSquares(1, 100))
