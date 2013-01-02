#!/usr/bin/env python

"""
    Self Describing Numbers Solution: v0.2

    Taken from: www.codeeval.com/open_challenges/40/

    Description:

        A number is a self-describing number when (assuming digit positions 
        are labeled 0 to N-1), the digit in each position is equal to the 
        number of times that that digit appears in the number.

    Input sample:

        The first argument is the pathname to a file which contains test data,
        one test case per line. Each line contains a positive integer. Each 
        line is in the format: N i.e. a positive integer. e.g.

            2020
            22
            1210

    Output sample:

        If the number is a self-describing number, print out a 1. If not, 
        print out a 0. e.g.

            1
            0
            1


    ======================================
    Copyright 2012,2013  Jamie Thomas Duby
    ======================================

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
    """Takes an integer n and returns a list of the digits of n. The digit
    list is in order from highest order place to lowest. e.g.

    1234 --> [1, 2, 3, 4]
    936  --> [9, 3, 6]
    
    This was originally implemented without any casting, and found the digits
    via modulus and arithmetic as it was assumed that casting would have higher
    computational overhead. However, this assumption was tested, and found to
    be false:
        $ ./casting_vs_arith.py 10000000
        Arithmetic took: 35.53 sec
        Casting took: 35.47 sec
    """
    return [int(c) for c in str(n)]

def self_describing(digits):
    target = {}
    digit_dict = {}
    for i, d in enumerate(digits):
        if d > 0:
            target[i] = d
        if digit_dict.has_key(d):
            digit_dict[d] += 1
        else:
            digit_dict[d] = 1
    if digit_dict == target:
        return 1
    else:
        return 0

if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            n = int(line.strip())
            digits = find_digits(n)
            print(self_describing(digits))
    finally:
        infile.close()
    sys.exit(0)
