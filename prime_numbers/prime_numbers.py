#!/usr/bin/env python

"""
    Prime Numbers Solution: v0.1
"""

import sys

def parse_infile(infile):
    largest = 1
    n_list = []
    for line in infile:
        n_str = line.strip()
        n = int(n_str)
        if n > largest:
            largest = n
        n_list.append(n)
    return largest, n_list

def prime_sieve(n):
    candidates = [x for x in range(2, n)]
    
if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        largest, n_list = parse_infile(infile)
    finally:
        infile.close()
    sys.exit(0)
