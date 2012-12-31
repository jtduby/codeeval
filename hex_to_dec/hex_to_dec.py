#!/usr/bin/env python

"""
    Hex to Decimal Solution: v0.2

    Yes, I know that Python will convert between hex and dec. But using that
    ability kind of takes the fun out of the challenge, doesn't it?

    CodeEval breaks spec and passes upper case characters. 

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

def str_to_list(in_str):
    s_list = []
    for c in in_str:
        s_list.append(c.lower())
    return s_list

def gen_hex_dict():
    hex_dict = {}
    for i, h in enumerate(['0','1','2','3','4','5','6','7','8','9','a','b',
                           'c','d','e','f']):
        hex_dict[h] = i
    return hex_dict

def hex_list_to_dec(hex_list):
    hex_dict = gen_hex_dict()
    hex_list.reverse()
    dec_sum = 0
    for i, h in enumerate(hex_list):
        dec_sum += hex_dict[h] * 16**i
    return dec_sum

if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            hex_str = line.strip()
            hex_list = str_to_list(hex_str)
            dec_n = hex_list_to_dec(hex_list)
            print(dec_n)
    finally:
        infile.close()
    sys.exit(0)
