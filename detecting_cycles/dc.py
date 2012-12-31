#!/usr/bin/env python

"""
    Detecting Cycles Solution: v0.1
"""

import sys

if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            d = {}
            seq = line.strip().split(' ')
            for i in range(0, len(seq)):
               pass 
    finally:
        infile.close()
    sys.exit(0)
