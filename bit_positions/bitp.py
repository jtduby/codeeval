#!/usr/bin/env python

"""
    Bit Positions Solution: v0.5

    Taken from: http://www.codeeval.com/open_challenges/19/

    Description:

        Given a number n and two integers p1,p2 determine if the bits in 
        position p1 and p2 are the same or not. Positions p1,p2 and 1 based.

    Input sample:

        The first argument will be a text file containing a comma separated
        list of 3 integers, one list per line. e.g.

            86,2,3
            125,1,2

    Output sample:

        Print to stdout, 'true'(lowercase) if the bits are the same, else 
        'false'(lowercase). e.g.

            true
            false
         
    Version history:
        0.1: This could be done a lot more elegantly.
        0.2: Jetisoned the mask silliness.
        0.3: Did some refactoring.
        0.4/0.5: Code cleaning and documentation fixing. 

    ================================
    Copyright 2012, Jamie Thomas Duby
    ================================

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

def compare(n, p1, p2):
    """Compares two bits in an integer.

    Takes integers n, p1, p2. If the bit of n at positions p1 and p2 are
    the same, true is returned to the caller. Otherwise returns false. Bit
    positions start at 1 and go from low order to high. For example:
        n = 5, p1 = 1, p2 = 2

        n = 0b101, n_p1 = 1, n_p2 = 0
        
        In this case, False is returned.
    """
    n_p1 = n >> (p1 - 1)
    n_p2 = n >> (p2 - 1)
    if (n_p1 & 0b1) == (n_p2 & 0b1):
        return True
    else: return False

def pretty_print(b):
    """Reformats boolean values to a string of all lower case characters e.g.
    True = 'true'. This is to meet codeval specificaions.
    """
    if b == True: print("true")
    else: print("false")    

def parse_line(line):
    """Takes a line formatted as three comma seperated integers. Returns three
    integers.
    """
    n, p1, p2 = line.strip().split(',')
    return int(n), int(p1), int(p2)

if __name__ == '__main__': 
    try:
        infile = open(sys.argv[1], 'r')
        for line in infile:
            n, p1, p2 = parse_line(line)
            c = compare(n, p1, p2)
            pretty_print(c)
    finally:
        infile.close()
    sys.exit(0)
