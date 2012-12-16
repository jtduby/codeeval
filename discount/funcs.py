#!/usr/bin/env python

import sys

if __name__ == '__main__':
    infile = open(sys.argv[1], 'r')
    for line in infile:
        if line.startswith('def'):
            print line.strip()[4:]
    infile.close()
