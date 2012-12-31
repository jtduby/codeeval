#!/usr/bin/env python

"""
    Bit Positions Solution: v0.3
 
    Version history:
        0.1: This could be done a lot more elegantly.
        0.2: Jetisoned the mask silliness.
        0.3: Did some refactoring. 

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

def compare(n, x, y):
    """Take integers n, x, y. Shifts n x and y bits to the right. If the
    lowest order bit if equal, returns true. Otherwise returns false.
    """
    n1 = n >> (x - 1)
    n2 = n >> (y - 1)
    if (n1 & 0b1) == (n2 & 0b1):
        return True
    else: return False

def pretty_print(b):
    if b == True: print("true")
    else: print("false")    

def parse_line(line):
    n, x, y = line.strip().split(',')
    return int(n), int(x), int(y)

if __name__ == '__main__': 
    try:
        infile = open(sys.argv[1], 'r')
        for line in infile:
            n, x, y = parse_line(line)
            c = compare(n, x, y)
            pretty_print(c)
    finally:
        infile.close()
    sys.exit(0)
