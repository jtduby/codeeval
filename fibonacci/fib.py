#!/usr/bin/env python

"""
    Fibonacci Solution: v0.5

    Takes, as an argument, the path to a file with a positive integer n on
    each line. Prints the nth number in the Fibonacci sequence to stdout. 
    
    Version History:
        0.2: Couldn't bring myself to calculate the fib each time. Created an
             object to memoize already calculated values.
        0.3:  --Refactored and cleaned up code.
              --Changed memoization storage from list to dict for lower-cost
                lookups.
        0.4/0.5:  More code cleaning and some documentation fixing.
    
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

class Fib(object):
    def __init__(self):
        self._fibs = {0:0, 1:1}      #Seeding the fib sequence.
    def fib(self, n):
        """If the nth Fibonacci number has already been computed, return it.
        Otherwise, have it computed.
        """
        try:
            f = self._fibs[n]
        except:
            self._find_fib(n)
            f = self._fibs[n]
        return f
    def _find_fib(self, n):
        """Computes the fibonacci sequence up to, and including fib(n)."""
        for i in range(self._last_computed_fib()+1, n+1):
            self._fibs[i] = self._fibs[i-1] + self._fibs[i-2]
    def _last_computed_fib(self):
        """Returns the sequence number of the last computed Fibonacci number. 
        If the last fib recorded was the 7th, 7 is returned to the caller.
        """
        computed_fibs = self._fibs.keys()
        computed_fibs.sort()
        return computed_fibs[-1]

if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        fib = Fib()
        for line in infile:
            n = int(line.strip())
            print fib.fib(n)
    finally:
        infile.close()
    sys.exit(0)
