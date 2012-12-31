#!/usr/bin/env python

"""
    Sum of Primes Solution: v0.3
   
    Version History:
        0.1: Brute force.
        0.2: Implemented memoization and use of computed primes for testing
             the current number.
        0.3: Modularization of code. 

    =================================
    Copyright 2012, Jamie Thomas Duby
    =================================

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
  
    http://www.apache.org/licenses/LICENSE-2.0
 
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
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
