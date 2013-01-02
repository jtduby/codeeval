#!/usr/bin/env python

"""
    Testing two implementations of find_digits for performance.
    Find_digits returns a list of the digits in a number. e.g.
        123 --> [1,2,3]

    Takes a number passes as an argument. Defaults to 1000.

    =================================
    Copyright 2013  Jamie Thomas Duby
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
import time

def test(fn, passes):
    """Takes a function and an integer number of passes. The function is 
    assumed to take a single integer as input. Returns the clock time taken
    to perform fn the specified number of times. Time is returned in seconds.
    """
    start = time.clock()
    for i in range(0, passes):
        temp = fn(i)
    end = time.clock()
    return end - start

def find_digits_arith(n):
    digits = []
    place = 10
    while n > 0:
        rem = n % place
        digits.insert(0, rem/(place/10))
        n = n - rem
        place = place * 10
    return digits

def find_digits_cast(n):
    """I hope this wins, it makes me happy."""
    return [int(c) for c in str(n)]

if __name__ == '__main__':
    if len(sys.argv) > 1:
        passes = int(sys.argv[1])
    else:
        passes = 1000
    t1 = test(find_digits_arith, passes)
    t2 = test(find_digits_arith, passes)
    print("Arithmetic took: " + str(t1) + " sec")
    print("Casting took: " + str(t2) + " sec")
    sys.exit(0)

