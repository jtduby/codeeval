#!/usr/bin/env python

"""
    Stack Implementation Solution: v0.1
      
    The specs say we'll be handling integers. There's no need to make this
    stack implementation that narrow. Making it more generic and robust. It
    will handle any object.
"""

import sys

class Stack(object):
    def __init__(self):
        self.stack = []
    def __len__(self):
        return(len(self.stack))
    def push(self, obj):
        self.stack.append(obj)
    def pop(self):
        """Raises StackEmpty instead of returning None so that None can be
        pushed onto the stack.
        """
        try:
            return self.stack.pop()
        except IndexError:
            raise StackEmpty

class StackEmpty(BaseException):
    """Inheriting from BaseException because this isn't really an error."""
    pass
        
class InputFileIncorrect(Exception):
    def __init__(self, msg=''):
        self.message = msg

def parse_line(line):
    if len(line.strip()) > 0:
        line_list = line.strip().split(' ')
        return line_list
    else:
        raise InputFileIncorrect        

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
    except InputFileIncorrect:
        exit_code = "Input file not properly formatted."
    finally:
        try:
            infile.close()
        except NameError:
            pass            # Look up printing to stderr, then do something
                            # better here
    sys.exit(exit_code)
