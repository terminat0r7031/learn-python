#!/usr/bin/env python
# with statement

from __future__ import with_statement
with open("writeable.txt", "w") as f:
    f.write("this is writeable file\n")