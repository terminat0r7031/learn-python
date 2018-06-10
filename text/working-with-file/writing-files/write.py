#!/usr/bin/env python
# write() method

f = open("some_writeable_file.txt", "w")
f.write("Test\nfile\n")
f.close()

g = open("some_writeable_file.txt", "r")
print g.read()
