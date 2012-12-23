#!/usr/bin/env python

"""
    Multiples of a Number Solution: v0.1
"""

import sys

def find_multiple(x, n):
    while n < x:
        n = n << 1
    return n

def parse_line(line):
    try:
        tmp = line.strip().split(',')
        str_x, str_n = tmp
        x = int(str_x)
        n = int(str_n)
    except Exception as e:
        return e
    return x, n
    
if __name__ == '__main__':
    exit_code = 0
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            x, n = parse_line(line)
            m = find_multiple(x, n)
            print(m)
    except IOError:
        exit_code = "Unable to open file: " + sys.argv[1]
    except IndexError:
        exit_code = "No arguments given."
    except ValueError:
        exit_code = "Invalid input file."
    except:
        exit_code = "Unspecified error."
    finally:
        try:
            infile.close()
        except NameError:
            pass            # Look up printing to stderr, then do something
                            # better here
    sys.exit(exit_code)
