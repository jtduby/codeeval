#!/usr/bin/env python

"""
    Bit Positions Solution: v0.3
 
    Version history:
        0.1: This could be done a lot more elegantly.
        0.2: Jetisoned the mask silliness.
        0.3: Did some refactoring. 
"""
import sys

def compare(n, x, y):
    """Take integers n, x, y. Shifts n x and y bits to the right. If the
    lowest order bit if equal, returns true. Otherwise returns false.
    """
    n1 = n >> (x - 1)
    n2 = n >> (y - 1)
    if (n1 & 0b1) == (n2 & 0b1):
        return True
    else: return False

def pretty_print(b):
    if b == True: print("true")
    else: print("false")    

def parse_line(line):
    n, x, y = line.strip().split(',')
    return int(n), int(x), int(y)

if __name__ == '__main__': 
    try:
        infile = open(sys.argv[1], 'r')
        for line in infile:
            n, x, y = parse_line(line)
            c = compare(n, x, y)
            pretty_print(c)
    finally:
        infile.close()
    sys.exit(0)
