#!/usr/bin/env python

"""
    N Longest Lines Solution: v0.2

    Takes, as an argument, the path to a file formatted as:
        <integer N>
        <str 1>
        <str ...>
    e.g.
        2
        Hello World
        Hi
        Foo
        Hello, World

    Prints, to stdout, the N longest lines, in order of decreasing length. In 
    the above example, the output would be:
        Hello, World
        Hello World


    Version History:
        0.1 -- Brute-force proof of concept.
        0.2 -- Refactored and modulalized. 

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

def sort_lines(t):
    """Takes a file. Returns a list of the lines of the file, as strings, in
    order by descending length. Equal length lines should, but are not 
    guaranteed to be in the order they were encountered.
    """
    line_list = []
    for line in t:
        line = line.strip()
        if len(line) > 0:
            line_list.append(line)
    line_list.sort(lambda a,b: len(b) - len(a))
    return line_list

def print_nll(n, nll):
    """Prints the first n lines from the line list. Assumes that n < len(nll).
    """
    for i in range(0, n):
        print nll[i]

if __name__ == '__main__': 
    test_cases = open(sys.argv[1], 'r')

    n = int(test_cases.next())
    nll = sort_lines(test_cases)
    print_nll(n, nll)

    test_cases.close()

    sys.exit(0)

sys.exit(1)
