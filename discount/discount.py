#!/usr/bin/env python

"""
    Discount Offers Solution: v0.1
"""
import sys

class Factors(object):
    def __init__(self):
        self.f = {}
    def factors_of(self, n):
        if (not self.f.has_key(n)):
            self.find_factors(n)
        return self.f[n]
    def find_factors(self, n):
        print "in find"
        self.f[n] = set([n])
        for i in range(2, n):
            if (n%i==0):
                self.f[n].add(i)
    def common_factors(self, x, y):
        cf = self.factors_of(x) & self.factors_of(y)
        return cf
    def has_common_factors(self, x, y):
        cf = self.common_factors(x, y)
        if len(cf) > 0:
            return True
        else:
            return False
        
 
if __name__ == '__main__': 
    test_cases = open(sys.argv[1], 'r')

    for line in test_cases:
    test_cases.close()
    f = Factors()
    sys.exit(0)

sys.exit(1)
