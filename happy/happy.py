#!/usr/bin/env python

"""
    Happy Numbers Solution: v0.3

    From http://codeeval.com/open_challenges/39/:
    "A happy number is defined by the following process. Starting with any 
    positive integer, replace the number by the sum of the squares of its
    digits, and repeat the process until the number equals 1 (where it will
    stay), or it loops endlessly in a cycle which does not include 1. Those
    numbers for which this process ends in 1 are happy numbers, while those
    that do not end in 1 are unhappy numbers."
 
    Takes, as an argument, the path to a file that is formatted with a
    positive integer n on each line. If n is a happy number, a 1 is printed to
    stdout. Otherwise, 0 is printed.

    Version History:
        0.1: Completed
        0.2: Won't work if two or more places share the same number, i.e.,
             12234. Fixed.
        0.3: Refactoring, code cleaning, documentation fixing.


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

def find_digits(n):
    """Takes an integer n and returns a list of the digits in n. Digits are
    listed from low order to high as this was easier and does not impact the
    future computations. For example, if n=123, [1,2,3] is returned to the
    caller. 

    Yes, I could have done this by casting the integer to a string and
    iterating through the characters. However, I felt that would have
    violated the spirit of the challenge.
    """
    digits = [] 
    place = 10
    while n > 0:
        rem = n % place
        digits.append(rem/(place/10))
        n = n - rem
        place = place * 10
    return digits

def sum_squares(digits):
    """Takes a list of integers. The sum of the squares of the numbers is 
    returned to the caller.
    """
    sum = 0
    for i in digits:
        square = i**2
        sum = sum + square
    return sum

def happy(n):
    """If the n is a happy number, 1 is returned to the caller. Else 0 is
    returned. An unhappy number is determined by a cycle in the sequence
    returned by the summing of sums of digits of n. 
    """
    candidates = set()
    while not (n == 1):
        if len(candidates & set([n])) == 0:
            candidates.add(n)
            digits = find_digits(n)
            n = sum_squares(digits)
        else: return 0
    return 1
            
if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            n = int(line.strip())
            print(happy(n))
    finally:
        infile.close()
    sys.exit(0)
