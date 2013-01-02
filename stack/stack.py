#!/usr/bin/env python

"""
    Stack Implementation Solution: v0.3
      
    The specs say we'll be handling integers. There's no need to make this
    stack implementation that narrow. Making it more generic and robust. It
    will handle any object.

    Version History:
        v0.1: Works according to spec.
        v0.2: CodeEval passes a blank line in input. They imply that there
              will be no blanks and do not state how to handle them. Fixed.
        v0.3: Performed some code cleaning.
    ========================================
    Copyright 2012, 2013,  Jamie Thomas Duby
    ========================================

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

class Stack(object):
    def __init__(self):
        self._stack = []
    def __len__(self):
        return(len(self._stack))
    def push(self, obj):
        self._stack.append(obj)
    def pop(self):
        """Raises StackEmpty instead of returning None so that None can be
        pushed onto the stack.
        """
        try:
            return self._stack.pop()
        except IndexError:
            raise StackEmpty

class StackEmpty(BaseException):
    """Inheriting from BaseException because this isn't really an error."""
    pass
        
def parse_line(line):
    line_list = line.strip().split(' ')
    return line_list

def batch_push(stack, items):
    for i in items:
        stack.push(i)

def alt_print(stack):
    alt = True
    out = ''
    while True:
        try:
            n = stack.pop()
            if alt:
                out = out + n
                alt = False
            else:
                out = out + ' '
                alt = True
        except StackEmpty:
            print(out.strip())
            break
 
if __name__ == '__main__':
    exit_code = 0
    try: 
        infile = open(sys.argv[1], 'r')
        s = Stack()
        for line in infile:
            items = parse_line(line)
            batch_push(s, items)
            alt_print(s)
    except IOError:
        exit_code = "Unable to open file: " + sys.argv[1]
    except IndexError:
        exit_code = "No arguments given."
    finally:
        try:
            infile.close()
        except NameError:
            pass            # Look up printing to stderr, then do something
                            # better here
    sys.exit(exit_code)
