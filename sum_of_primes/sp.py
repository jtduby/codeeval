#!/usr/bin/env python

"""
    Sum of Primes Solution: v0.2
   
    Version History:
        0.1: Brute force.
        0.2: Implemented memoization and use of computed primes for testing
             the current number.
        0.3: Modularization of code. **WIP**
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

def n_primes(n):

if __name__ == '__main__':
    primes = []
    i = 2
    sum = 0
    while len(primes) < 1000:
        if memo_prime(i, primes):
            primes.append(i)
            sum += i
        i += 1
    print(sum)
    sys.exit(0)
