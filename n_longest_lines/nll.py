#!/usr/bin/env python

"""
    N Longest Lines Solution: v0.2

    Ugly, brute-force solution. Both time and space inefficient.

    Version History:
        0.1 -- Brute-force proof of concept.
        0.2 -- Refactored and modulalized. 
"""
import sys

def run_test(t):
    """Stripped strings are saved in line list with their respective lengths
    in a tuple formatted (len(string), string). This is done so that the 
    list of strings can be sorted and reversed by length.
    """
    line_list = []
    for line in test_cases:
        tmp = line.strip()
        if len(tmp) > 0:
            line_list.append((len(tmp), tmp))
    line_list.sort()
    line_list.reverse()
    return line_list

def print_nll(n, nll):
    for i in range(0, n):
        print nll[i][1]

if __name__ == '__main__': 
    test_cases = open(sys.argv[1], 'r')

    n = int(test_cases.next())
    nll = run_test(test_cases)
    print_nll(n, nll)

    test_cases.close()

    sys.exit(0)

sys.exit(1)
