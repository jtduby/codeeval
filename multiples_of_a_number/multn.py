#!/usr/bin/env python

"""
    Multiples of a Number Solution: v0.3

    Taken from http://www.codeeval.com/open_challenges/18/

    Description:

        Given numbers x and n, where n is a power of 2, print out the smallest
        multiple of n which is greater than or equal to x. Do not use division
        or modulo operator.

    Input sample:

        The first argument will be a text file containing a comma separated
        list of two integers, one list per line. e.g.

            13,8
            17,16

    Output sample:

        Print to stdout, the smallest multiple of n which is greater than or
        equal to x, one per line. e.g.

            16
            32

    
    Version History
        0.2: Code cleaning and refactoring. Cleared up some documentation.
        0.3: --Included the CodeEval specifications as the description.
             --Refactored/cleaned up some code.
 
    ========================================
    Copyright 2012, 2013   Jamie Thomas Duby
    ========================================

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

def find_multiple(x, n):
    """Takes integers x and n. Returns the smallest multiple of n, m where 
    m >= x.
    """
    while n < x:
        n = n << 1
    return n

def parse_line(line):
    """Takes a string of two comma seperated integers. Returns the integers to
    the caller. 
    """
    x, n = line.strip().split(',')
    return int(x), int(n)
    
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as infile:
        for line in infile:
            x, n = parse_line(line)
            m = find_multiple(x, n)
            print(m)
    sys.exit(0)
