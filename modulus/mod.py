#!/usr/bin/env python

"""
    Modulus Solution: v0.2

    Takes, as an argument, the path to a file where each line is a two 
    integers, n and m, seperated by a comma. n mod m is printed to stdout.

    Version History:
        0.2: Code cleaning, refactoring, fixing documentation.

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

def mod(n,m):
    """Takes integers n and m. Returns n modulo m to the caller."""
    q = n/m
    r = n-(q*m)
    return r

if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            n, m = line.strip().split(',')
            print(mod(int(n), int(m)))
    finally:
        infile.close()
    sys.exit(0)
