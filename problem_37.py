'''
@author Jason A Smith

@problem
https://projecteuler.net/problem=37

@description
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

@time
real	0m7.095s
user	0m7.045s
sys	0m0.027s

@output
748317
'''

from math import ceil, sqrt
from itertools import islice

def truncate_left(number):
    return int(str(number)[1:])

def truncate_right(number):
    return int(str(number)[:-1])

primes_cache = set([2])

def is_prime(number):
    if number in primes_cache:
        return True
    elif number <= 1:
        return False
    else:
        for i in range(2, ceil(sqrt(number)) + 1):
            if number % i == 0:
                return False
            else:
                continue
    primes_cache.add(number)
    return True

def is_truncatable_prime_with_direction(number, trunction_function):
    if not is_prime(number):
        return False
    elif number < 10:
        return True
    else:
        truncated_number = trunction_function(number)
        if not is_prime(truncated_number):
            return False
        else:
            return is_truncatable_prime_with_direction(truncated_number, \
                                                       trunction_function)

def is_truncatable_prime(number):
    if number < 10:
        return False
    else:
        return is_truncatable_prime_with_direction(number, truncate_left) and \
                is_truncatable_prime_with_direction(number, truncate_right)

def truncatable_primes():
    candidate = 10
    while True:
        if is_truncatable_prime(candidate):
            yield candidate
        candidate += 1

is_testing = False

if is_testing:
    # Test truncate_left
    assert truncate_left(123) == 23

    # Test truncate_right
    assert truncate_right(123) == 12

    # Test is_prime
    assert is_prime(2) == True
    assert is_prime(5) == True
    assert is_prime(8) == False
    assert is_prime(20) == False
    assert is_prime(33) == False
    assert is_prime(37) == True

    # Test is_truncatable_prime_with_direction
    assert is_truncatable_prime_with_direction(7, truncate_left) == True
    assert is_truncatable_prime_with_direction(97, truncate_left) == True
    assert is_truncatable_prime_with_direction(797, truncate_left) == True
    assert is_truncatable_prime_with_direction(3797, truncate_left) == True
    assert is_truncatable_prime_with_direction(3, truncate_right) == True
    assert is_truncatable_prime_with_direction(37, truncate_right) == True
    assert is_truncatable_prime_with_direction(379, truncate_right) == True
    assert is_truncatable_prime_with_direction(3797, truncate_right) == True

    # Test is_truncatable_prime
    assert is_truncatable_prime(2) == False
    assert is_truncatable_prime(23) == True
    assert is_truncatable_prime(3797) == True

print(sum(islice(truncatable_primes(), 11)))
