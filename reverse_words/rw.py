#!/usr/bin/env python

"""
    Reverse Words Solution: v0.2
    
    Version History:
        0.1: First try
        0.2: Need to learn to read better. Now ignoring blank lines per the
             specs.
"""

import sys

def reverse_str(s):
    """
    """
    rs = ''
    for w in s.strip().split(' '):
        rs = rs + ' ' + w
    return rs.strip()

if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            r = reverse_str(line)
            if (len(r) > 0):
                print(r)
    except IOError:
        sys.exit("Unable to open file: sys.argv[1]")
    except IndexError:
        sys.exit("No arguments given.")
    except:
        sys.exit(1)
    sys.exit(0)
