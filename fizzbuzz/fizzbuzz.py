#!/usr/bin/env python

import sys

def fizzbuzz(a, b, n):
    if n % (a*b) == 0:
        return 'FB'
    elif n%a == 0:
        return 'F'
    elif n%b == 0:
        return 'B'
    else: return str(n)

def parse_test(t):
    tlist = test.split()
    a = int(tlist[0].strip())
    b = int(tlist[1].strip())
    n = int(tlist[2].strip())
    return (a, b, n)

def run_test(t):
    a, b, n = t
    tmp_str = ''
    for i in range(1, n+1):
        fb = fizzbuzz(a, b, i)
        tmp_str = tmp_str + fb + ' '
    return tmp_str.strip()

if __name__ == '__main__': 
    test_cases = open(sys.argv[1], 'r')
    
    for test in test_cases:
        t = parse_test(test)
        print run_test(t)
    
    test_cases.close()

    sys.exit(0)

else: sys.exit(1)
