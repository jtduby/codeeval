#!/usr/bin/env python

"""
    Unique Elements Solution: v0.1
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
