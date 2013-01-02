#!/usr/bin/env python

"""
    File Size Solution: v0.2

    Takes, and an argument, the path to a file. Prints the size of the file
    in bytes to stout.

    Specifications did not state how to handle a non-existent file. I elected
    to do nothing and just exit.

    Version History:
        0.2: Cleaned up code.

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
import os

if __name__ == '__main__':
    filename = sys.argv[1]
    if os.path.isfile(filename):
        size = os.path.getsize(filename)
        print(size)
    sys.exit(0)
