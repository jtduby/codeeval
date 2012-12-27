#!/usr/bin/env python

"""
    Happy Numbers Solution: v0.1
"""

import sys

def find_digits(n):
    digits = set()
    place = 10
    while n > 0:
        rem = n % place
        digits.add(rem/(place/10))
        n = n - rem
        place = place * 10
    return digits

def sum_squares(digits):
    sum = 0
    for i in digits:
        square = i**2
        sum = sum + square
    return sum

def happy(n):
    candidates = set()
    while not (n == 1):
        if len(candidates & set([n])) == 0:
            candidates.add(n)
            digits = find_digits(n)
            n = sum_squares(digits)
        else: return 0
    return 1
            
if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            n = int(line.strip())
            print(happy(n))
    finally:
        infile.close()
    sys.exit(0)
