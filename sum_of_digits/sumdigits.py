#!/usr/bin/env python

"""
    Sum of Digits Solution: v0.2

    Taken from: www.codeeval.com/open_challenges/21/

    Description:

        Given a positive integer, find the sum of its constituent digits.

    Input sample:

        The first argument will be a text file containing positive integers,
        one per line. e.g.

            23
            496
  
    Output sample:

        Print to stdout, the sum of the numbers that make up the integer, one
        per line. e.g.

            5
            19


    Version History:
        v0.2: Code refactoring and documentation fixing.


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

def add_intstr(istr):
    """Takes a positive number as a string, returns the integer sum of its 
    digits.
    """
    sum = 0
    for i in istr:
        sum += int(i)
    return sum

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as infile:
        for line in infile:
            sum = add_intstr(line.strip())
            print sum
    sys.exit(0)
