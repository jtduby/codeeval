#!/usr/bin/env python

"""
    Prime Palidrome Solution: v0.1

    Finds the largest prime palindrome under 1000 and prints it to stdout.


    =================================
    Copyright 2012, Jamie Thomas Duby
    =================================

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
  
    http://www.apache.org/licenses/LICENSE-2.0
 
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import sys
import math

def prime(n):
    """Checks if n is prime. Returns True if it is, False if not."""
    s = int(math.ceil(math.sqrt(n)))
    if n > 3:
        for i in range(2, s+1):
            if (n % i == 0):
                return False
    return True

def palindrome(s, b=0, e=-1):
    """Recurrsively determines if the string s is a palindrome. Returns
    a boolean"""
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
