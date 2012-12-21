#!/usr/bin/env python

"""
    Prime Palidrome Solution: v0.1
"""

import sys
import math

def prime(n):
    s = int(math.ceil(math.sqrt(n)))
    if n > 3:
        for i in range(2, s+1):
            if (n % i == 0):
                return False
    return True

def palindrome(s, b=0, e=-1):
    size = len(s)
    if b < len(s):
        if (s[b] == s[e]):
            return palindrome(s, b+1, e-1)
        else: return False
    return True

if __name__ == '__main__':
    for i in range(1000, 0, -1):
        if prime(i):
            if palindrome(str(i)):
                print(i)
                break

    sys.exit(0)
