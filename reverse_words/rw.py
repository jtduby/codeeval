#!/usr/bin/env python

"""
    Reverse Words Solution: v0.1
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
            print(r)
    except IOError:
        sys.exit("Unable to open file: sys.argv[1]")
    except IndexError:
        sys.exit("No arguments given.")
    except:
        sys.exit(1)
    sys.exit(0)
