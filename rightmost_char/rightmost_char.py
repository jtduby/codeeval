#!/usr/bin/env python

"""
    Rightmost Char Solution: v0.2

    Taken from: www.codeeval.com/open_challenges/31/

    Description:

        You are given a string 'S' and a character 't'. Print out the position
        of the rightmost occurrence of 't'(case matters) in 'S' or -1 if there
        is none. The position to be printed out is zero based.

    Input sample:

        The first argument is a file, containing a string and a character, 
        comma delimited, one per line. Ignore all empty lines in the input 
        file. e.g.

            Hello World,r
            Hello CodeEval,E

    Output sample:

        Print out the zero based position of the character 't' in string 'S',
        one per line. Do NOT print out empty lines between your output. e.g.

            8
            10

    Version History:
        0.2: Refactored the code, rewrote the documentation accordingly.


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

def parse_line(line):
    """Takes a string assumed to be in the format:
        
        <long string>,<char>
    
    Splits on the comma and returns the substrings.
    """
    s, c = line.split(',')
    return s.strip(), c.strip()

def find_rightmost_char(s, c):
    """Takes a string s and a char (string) c. Returns the integer index of
    the reightmost occurence of c in s. If c is not in s, returns -1.
    """
    i = len(s) - 1
    while (i >= 0):
        if s[i] == c:
            break
        else: i -= 1
    return i

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as infile:
        for line in infile:
            line = line.strip()
            s, c = parse_line(line)
            print(find_rightmost_char(s, c))
    sys.exit(0)
