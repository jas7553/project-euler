'''Jason A Smith'''
from itertools import permutations

p = permutations(range(10))

for i in range(1000000 - 1):
    print(next(p))

print(next(p))
