#!/usr/bin/env python

"""
    Rightmost Char Solution: v0.1
"""

import sys

if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            line = line.strip()
            if len(line) > 3:
                s, c = line.split(',')
                i = len(s) - 1
                while (i >= 0):
                    if s[i] == c:
                        break
                    else: i -= 1
            print i
    finally:
        infile.close()
    sys.exit(0)
