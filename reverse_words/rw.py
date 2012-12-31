#!/usr/bin/env python

"""
    Reverse Words Solution: v0.3
    
    Version History:
        0.1: First try
        0.2: Need to learn to read better. Now ignoring blank lines per the
             specs.
        0.3: It would help if I was actually reversing the string.

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

def reverse_str(s):
    """
    """
    s_list = s.strip().split(' ')
    s_list.reverse()
    rs = ''
    for word in s_list:
        rs = rs + ' ' + word
    return rs.strip()

if __name__ == '__main__':
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            r = reverse_str(line)
            if (len(r) > 0):
                print(r)
    except IOError:
        sys.exit("Unable to open file: sys.argv[1]")
    except IndexError:
        sys.exit("No arguments given.")
    except:
        sys.exit(1)
    sys.exit(0)
