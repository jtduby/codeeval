#!/usr/bin/env python

"""
    Sum of Digits Solution: v0.1
"""

import sys

def add_intstr(istr):
    try:
        sum = 0
        for i in istr:
            sum += int(i)
    except Exception as e:
        return e
    return sum

if __name__ == '__main__':
    exit_code = 0
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            sum = add_intstr(line.strip())
            print sum
    except IOError:
        exit_code = "Unable to open file: " + sys.argv[1]
    except IndexError:
        exit_code = "No arguments given."
    except ValueError:
        exit_code = "Invalid input format."
    except:
        exit_code = "Unspecified error."
    finally:
        try:
            infile.close()
        except NameError:
            pass            # Look up printing to stderr, then do something
                            # better here
    sys.exit(exit_code)
