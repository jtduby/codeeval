#!/usr/bin/env python

"""
    Self Describing Numbers Solution: v0.1

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

def find_digits(n):
    digits = []
    place = 10
    while n > 0:
        rem = n % place
        digits.insert(0, rem/(place/10))
        n = n - rem
        place = place * 10
    return digits

def self_describing(digits):
    target = {}
    digit_dict = {}
    for i, d in enumerate(digits):
        if d > 0:
            target[i] = d
        if digit_dict.has_key(d):
            digit_dict[d] += 1
        else:
            digit_dict[d] = 1
    if digit_dict == target:
        return 1
    else:
        return 0

if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            n = int(line.strip())
            digits = find_digits(n)
            print(self_describing(digits))
    finally:
        infile.close()
    sys.exit(0)
