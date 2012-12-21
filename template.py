#!/usr/bin/env python

"""
    Solution: v0.1
"""

import sys

if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
    except IOError:
        sys.exit("Unable to open file: sys.argv[1]")
    except IndexError:
        sys.exit("No arguments given.")
    sys.exit(0)
