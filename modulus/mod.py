#!/usr/bin/env python

"""
    Modulus Solution: v0.1
"""

import sys

def mod(n,m):
    q = n/m
    r = n-(q*m)
    return r

if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            n, m = line.strip().split(',')
            print(mod(int(n), int(m)))
    finally:
        infile.close()
    sys.exit(0)
