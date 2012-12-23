#!/usr/bin/env python

"""
    Sum of Primes Solution: v0.3
   
    Version History:
        0.1: Brute force.
        0.2: Implemented memoization and use of computed primes for testing
             the current number.
        0.3: Modularization of code. 
"""

import sys
import math

def memo_prime(n, primes):
    """Takes an integer prime candidate n, and a list of known primes primes.
    Checks if n is prime based on the primes list. 

    *Warning*   Assumes that there are no primes between the square root of n
                and n.
    """
    s = int(math.ceil(math.sqrt(n)))
    for p in primes:
        if (p > s): break
        if (n % p == 0): return False
    return True

def sum_n_primes(n):
    primes = []
    i = 2
    sum = 0
    while len(primes) < n:
        if memo_prime(i, primes):
            primes.append(i)
            sum += i
        i += 1
    return sum

if __name__ == '__main__':
    sum = sum_n_primes(1000)
    print(sum)
    sys.exit(0)
