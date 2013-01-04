#!/usr/bin/env python

"""
    Self Describing Numbers Solution: v0.4

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


    Version History:
        0.2: Worked on documentation.
        0.3: Major code refactoring and documentation rewrites.
        0.4: Whoops, no dictionary comprehensions in Python 2.6.

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

def gen_digit_dict(n):
    """Creates a dictionary where the keys k range from 0 to the number of 
    digits in n and point to the frequency at which k appears in the positive
    integer n. 

    If a digit outside of the above range is encountered, None is returned to
    the caller instead of the dictionary.
    """
    digit_dict = gen_n_dict(n)
    for d in [int(c) for c in str(n)]:
        try:
            digit_dict[d] += 1
        except:
            return None
    return digit_dict

def gen_n_dict(n):
    """Creates a doctionary where the keys range from 0 to the number of
    digits in n. The definition for each key is 0.
    """
    n_dict = {} 
    for i in range(0, len(str(n))):
        n_dict[i] = 0
    return n_dict

def gen_target_dict(n):
    """Generates the dictionary that should result if n is self describing.
    """
    target = {}
    for i,c in enumerate(str(n)):
        target[i] = int(c)
    return target

def self_describing(n):
    """Determines if the positive integer n is self describing. Returns 
    boolean True if it is self-describing. False if it is not. 
    """
    target = gen_target_dict(n)
    digit_dict = gen_digit_dict(n)
    return target == digit_dict

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as infile:
        for line in infile:
            n = int(line.strip())
            if self_describing(n):
                print('1')
            else:
                print('0')
    sys.exit(0)
