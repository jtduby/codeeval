#!/usr/bin/env python

"""
    Fizzbuzz Solution: v0.3

    Takes, as an argument, the path to a file whose lines are formatted:
    <integer a> <integer b> <integer n>
    e.g.
    3 5 10
    Both a and b are assumed to be non-zero.
 
    Iterates from 1 through n. Prints a space-seperated line to stdout where
    each iteration i is represented by:
    -- F if i is divisible by a.
    -- B if i is divisible by b.
    -- FB if i is divisible by both a and b
    -- otherwise i.

    In the example above the following is output:
    1 2 F 4 B F 7 8 F B

    
    Version History:
        0.2: Code cleaning.
        0.3: Refactoring, cleaning, fixing documentation.


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

def fizzbuzz(a, b, n):
    if n % (a*b) == 0:
        return 'FB'
    elif n%a == 0:
        return 'F'
    elif n%b == 0:
        return 'B'
    else: return str(n)

def parse_test(t):
    tlist = test.split()
    a = int(tlist[0].strip())
    b = int(tlist[1].strip())
    n = int(tlist[2].strip())
    return (a, b, n)

def run_test(t):
    a, b, n = t
    tmp_str = ''
    for i in range(1, n+1):
        fb = fizzbuzz(a, b, i)
        tmp_str = tmp_str + fb + ' '
    return tmp_str.strip()

if __name__ == '__main__':
    try: 
        test_cases = open(sys.argv[1], 'r')
    
        for test in test_cases:
            t = parse_test(test)
            print run_test(t)
    finally:
        test_cases.close()
    sys.exit(0)
