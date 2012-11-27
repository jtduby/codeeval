#!/usr/bin/env python

import sys

if __name__ == '__main__':
    for i in range(1, 13):
        tmp_str = ''
        for j in range(1, 13):
            tmp_str = tmp_str + '{0:>4}'.format(i*j)
        print tmp_str.strip()

    sys.exit(0)

else:
    sys.exit(1)
