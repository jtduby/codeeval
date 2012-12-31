#!/usr/bin/env python

"""
    Fibonacci Solution: v0.1
    
    Couldn't bring myself to calculate the fib each time. Created an object
    to memoize already calculated values.
"""

import sys

class Fib(object):
    def __init__(self):
        self.fibs = {0:0, 1:1}
    def fib(self, n):
        try:
            f = self.fibs[n]
        except:
            self._find_fib(n)
            f = self.fibs[n]
        return f
    def _find_fib(self, n):
        for i in range(self._last_computed_fib()+1, n+1):
            self.fibs[i] = self.fibs[i-1] + self.fibs[i-2]
    def _last_computed_fib(self):
        computed_fibs = self.fibs.keys()
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
