#!/usr/bin/env python

"""
    File Size Solution: v0.1
"""

import sys
import os

if __name__ == '__main__':
    exit_code = 0
    try:
        filename = sys.argv[1]
        if os.path.isfile(filename):
            size = os.path.getsize(filename)
            print(size)
    except IOError:
        exit_code = "Unable to open file: " + sys.argv[1]
    except IndexError:
        exit_code = "No arguments given."
    except OSError:
        exit_code = "File doesn't exist." 
    except:
        exit_code = "Unspecified error."
    finally:
        try:
            infile.close()
        except NameError:
            pass            # Look up printing to stderr, then do something
                            # better here
    sys.exit(exit_code)
