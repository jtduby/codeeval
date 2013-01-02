#!/usr/bin/env python

"""
    Multiplication Tables Solution: v0.2

    Taken from: http://www.codeeval.com/open_challenges/23/

    Print out the grade school multiplication table upto 12*12. Print out the
    table in a matrix like fashion, each number formatted to a width of 4 
    (The numbers are right-aligned and strip out leadeing/trailing spaces on 
    each line).

    =======================================
    Copyright 2012,2013   Jamie Thomas Duby
    =======================================

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

if __name__ == '__main__':
    for i in range(1, 13):
        tmp_str = ''
        for j in range(1, 13):
            tmp_str = tmp_str + '{0:>4}'.format(i*j)
        print tmp_str.strip()
    sys.exit(0)
