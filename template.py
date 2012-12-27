#!/usr/bin/env python

"""
    Solution: v0.1
"""

import sys

if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
    finally:
        infile.close()
    sys.exit(0)
