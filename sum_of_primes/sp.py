#!/usr/bin/env python

"""
    Sum of Primes Solution: v0.2
   
    **Still working on v0.2**
 
    Version History:
        0.1: Brute force.
        0.2: Implemented memoization and use of computed primes for testing
             the current number.
"""

import sys
import math

def prime(n, primes=[]):
    s = int(math.ceil(math.sqrt(n)))
    if primes:
        pass 
    if n > 3:
        for i in range(start, s+1):
            if (n % i == 0):
                return False
    return True

def sum_list(nlist):
    s = 0
    for i in nlist:
        s = s + i
    return s
    
if __name__ == '__main__':
    primes = []
    i = 2   
    while len(primes) < 1000:
        if prime(i):
            primes.append(i)
        i += 1
    sum = sum_list(primes)
    print(sum)
    sys.exit(0)
