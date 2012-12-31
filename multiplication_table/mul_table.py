#!/usr/bin/env python

"""

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

if __name__ == '__main__':
    for i in range(1, 13):
        tmp_str = ''
        for j in range(1, 13):
            tmp_str = tmp_str + '{0:>4}'.format(i*j)
        print tmp_str.strip()

    sys.exit(0)

else:
    sys.exit(1)
