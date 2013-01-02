#!/usr/bin/env python

"""
    Lowercase Solution: v0.3

    Takes, as an argument, the path to a file with a a string on each line.
    Prints each string, with all lower case characters, to stdout.

    This is just a gimme in Python. First implementation will use the string
    lower method. After that, I'll make it more interesting.

    Version History:
        0.1: Yawn
        0.2: Refactored/cleaned some code.
        0.3: Fixed some documentation

    =======================================
    Copyright 2012, 2013  Jamie Thomas Duby
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
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            print line.strip().lower()
    finally:
        infile.close()
    sys.exit(0)
