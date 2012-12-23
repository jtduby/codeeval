#!/usr/bin/env python

"""
    Lowercase Solution: v0.1

    This is just a gimme in Python. First implementation will use the string
    lower method. After that, I'll make it more interesting.

    Version History:
        v0.1: Yawn
"""

import sys
    
if __name__ == '__main__':
    exit_code = 0
    try: 
        infile = open(sys.argv[1], 'r')
        for line in infile:
            print line.strip().lower()
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
