#!/usr/bin/env python
# writing something into file

try:
    outfile = open("foo1.txt", "w")
    outfile.write("This is\nsome random\nstring.")
finally:
    outfile.close()