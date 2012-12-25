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
    def push(self, obj):
        self.stack.append(obj)
    def pop(self):
        try:
            p = self.pop()
        except IndexError:
            p = None
        finally:
            return p

def parse_line(line):
    line_list = line.strip().split(',')
    return line_list

if __name__ == '__main__':
    exit_code = 0
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            
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
