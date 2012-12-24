#!/usr/bin/env python

"""
    Fibonacci Solution: v0.1
    
    Couldn't bring myself to calculate the fib each time. Created an object
    to memoize already calculated values.
"""

import sys

class Fib(object):
    def __init__(self):
        self.fibs = [0, 1]
        self.nth_fib = 1
    def fib(self, n):
        if (self.nth_fib >= n):
            return self.fibs[n]
        else:
            self.find_fib(n)
            self.nth_fib = n
            return self.fibs[-1]
    def find_fib(self, n):
        while (self.nth_fib < n):
            self.fibs.append(self.fibs[-1] + self.fibs[-2])
            self.nth_fib += 1

if __name__ == '__main__':
    exit_code = 0
    try: 
        infile = open(sys.argv[1], 'r')
        fib = Fib()
        for line in infile:
            n = int(line.strip())
            print fib.fib(n)
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
