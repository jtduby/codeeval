#!/usr/bin/env python

"""
    Unique Elements Solution: v0.2

    Description:

        You are given a sorted list of numbers with duplicates. Print out the
        sorted list with duplicates removed.

    Input sample:

        File containing a list of sorted integers, comma delimited, one per 
        line. e.g.

            1,1,1,2,2,3,3,4,4
            2,3,4,5,5

    Output sample:

        Print out the sorted list with duplicates removed, one per line
        e.g.

            1,2,3,4
            2,3,4,5

    Version History:
        v0.2: Refactored code, rewrote documentation.


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

def unique_items(L):
    """Returns a sorted list of unique items from the list L.
    """
    unique = set(L)
    ulist = list(unique)
    ulist.sort()
    return ulist

def list_to_string(L):
    """Concatenates the items of a list into a string.
    """
    s = str(L)
    s = re.sub("[\[\] ']", '' , s)
    return s

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as infile:
        for line in infile:
            line_list = line.strip().split(',')
            unique_list = unique_items(line_list)
            unique_str = list_to_string(unique_list)
            print(unique_str)
    sys.exit(0)
