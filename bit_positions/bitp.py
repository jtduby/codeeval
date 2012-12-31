#!/usr/bin/env python

"""
    Bit Positions Solution: v0.4

        Given a file whose lines are formatted as:
        <Integer n>,<Integer p1>,<Integer p2>
        e.g.
        82,2,3

        If bit positions p1 and p2 in n are the same, true is printed to
        stdout. If not, false is printed. Bit posititions are from low order
        to high, starting with 1.
         
    Version history:
        0.1: This could be done a lot more elegantly.
        0.2: Jetisoned the mask silliness.
        0.3: Did some refactoring.
        0.4: Code cleaning and documentation fixing. 

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
    """Takes integers n, p1, p2. If the bit of n at positions p1 and p2 are
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
    if b == True: print("true")
    else: print("false")    

def parse_line(line):
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
