#!/usr/bin/env python

"""
    Set Intersection Solution: v0.1

    Taken from: www.codeeval.com/open_challenges/30/

    Description:

        You are given two sorted list of numbers(ascending order). The lists 
        themselves are comma delimited and the two lists are semicolon 
        delimited. Print out the intersection of these two sets.

    Input sample:

        File containing two lists of ascending order sorted integers, comma 
        delimited, one per line. e.g.

            1,2,3,4;4,5,6
            7,8,9;8,9,10,11,12

    Output sample:

        Print out the ascending order sorted intersection of the two lists, 
        one per line. e.g.

            4
            8,9


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
import re

if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            a_str, b_str = line.split(';')
            a = a_str.strip().split(',')
            b = b_str.strip().split(',')
            aset = set(a)
            bset = set(b)
            cset = aset & bset
            clist = list(cset)
            clist.sort()
            cstr = re.sub("[\[\] \']", '', str(clist)) 
            print(cstr)     
    finally:
        infile.close()
    sys.exit(0)
