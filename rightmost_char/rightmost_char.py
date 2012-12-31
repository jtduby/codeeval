#!/usr/bin/env python

"""
    Rightmost Char Solution: v0.1

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

if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            line = line.strip()
            if len(line) > 3:
                s, c = line.split(',')
                i = len(s) - 1
                while (i >= 0):
                    if s[i] == c:
                        break
                    else: i -= 1
            print i
    finally:
        infile.close()
    sys.exit(0)
