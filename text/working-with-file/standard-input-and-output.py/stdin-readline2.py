#!/usr/bin/env python
# using enumerate() function

import sys

for i, line in enumerate(sys.stdin):
    print "%s: %s" %(i, line)