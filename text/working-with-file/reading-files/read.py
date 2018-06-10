#!/usr/bin/env python
# read() function

f = open("foo.txt", "r")
# read 5 bytes
print "Read 5 bytes:", f.read(5)
print "remain:", f.read()