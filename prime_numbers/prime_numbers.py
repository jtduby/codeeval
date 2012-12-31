#!/usr/bin/env python

"""
    Prime Numbers Solution: v0.1

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

def parse_infile(infile):
    largest = 1
    n_list = []
    for line in infile:
        n_str = line.strip()
        n = int(n_str)
        if n > largest:
            largest = n
        n_list.append(n)
    return largest, n_list

def prime_sieve(n):
    candidates = [x for x in range(2, n)]
    
if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        largest, n_list = parse_infile(infile)
    finally:
        infile.close()
    sys.exit(0)
