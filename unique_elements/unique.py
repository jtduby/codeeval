#!/usr/bin/env python

"""
    Unique Elements Solution: v0.1

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
import re

def make_line_list(line):
    try:
        line_lst = line.strip().split(',')
    except Exception as e:
        return e
    return line_lst

def unique_items(L):
    unique = set(L)
    ulist = list(unique)
    ulist.sort()
    return ulist

def list_to_string(L):
    s = str(L)
    s = re.sub("[\[\] ']", '' , s)
    return s

if __name__ == '__main__':
    exit_code = 0
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            line_list = make_line_list(line)
            unique_list = unique_items(line_list)
            unique_str = list_to_string(unique_list)
            print(unique_str)
    except IOError:
        exit_code = "Unable to open file: " + sys.argv[1]
    except IndexError:
        exit_code = "No arguments given."
    except:
        exit_code = "Unspecified error."
    finally:
        try:
            infile.close()
        except NameError:
            pass            # Look up printing to stderr, then do something
                            # better here
    sys.exit(exit_code)
