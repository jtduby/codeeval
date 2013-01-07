#!/usr/bin/env python

"""
    Hex to Decimal Solution: v0.5

    Takes, as an argument, the path to a file formatted as a hexidecimal
    number on each line. All hex numbers are to be formatted as just the
    number, without any prefix. 
    1a2b3c not 0x1a2b3c

    Prints the base 10 representation of each hexidecimal number to stdout.


    Yes, I know that Python will convert between hex and dec. But using that
    ability kind of takes the fun out of the challenge, doesn't it?


    Version History:
        0.2: CodeEval breaks spec and passes upper case characters. 
        0.3 - 0.5: Cleaning code, refactoring, fixing documentation.


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

def gen_hex_dict():
    """Returns a dictionary where the keys are string equivalents of 
    hexidecimal digits. Each key defines the an integer representation of the
    key's base 10 value. e.g. 'a': 10
    """
    hex_dict = {}
    for i, h in enumerate(['0','1','2','3','4','5','6','7','8','9','a','b',
                           'c','d','e','f']):
        hex_dict[h] = i
    return hex_dict

def hex_list_to_dec(hex_list):
    """Takes a hexidecimal number as a list of its digits represented as 
    strings. Returns the base 10 conversion of the hex as an integer.
    """
    hex_dict = gen_hex_dict()
    hex_list.reverse()
    dec_sum = 0
    for i, h in enumerate(hex_list):
        dec_sum += hex_dict[h] * 16**i
    return dec_sum

def yes_i_know_that_python_handles_hex(h_string):
    """Just to prove that I know the right way to do this in Python."""
    return int(h_string, 16)

if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            hex_str = line.strip()
            #hex_list = str_to_list(hex_str)
            hex_list = [c.lower() for c in hex_str]
            dec_n = hex_list_to_dec(hex_list)
            print(dec_n)
    finally:
        infile.close()
    sys.exit(0)
