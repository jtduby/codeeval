#!/usr/bin/env python

"""
    Set Intersection Solution: v0.1
"""

import sys
import re

if __name__ == '__main__':
    exit_code = 0
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            a_str, b_str = line.split(';')
            a = a_str.strip().split(',')
            b = b_str.strip().split(',')
            aset = set(a)
            bset = set(b)
            cset = aset & bset
            clist = list(cset)
            clist.sort()
            cstr = re.sub("[\[\] \']", '', str(clist)) 
            print(cstr)     
    except IOError:
        exit_code = "Unable to open file: " + sys.argv[1]
    except IndexError:
        exit_code = "No arguments given."
    finally:
        try:
            infile.close()
        except NameError:
            pass            # Look up printing to stderr, then do something
                            # better here
    sys.exit(exit_code)
