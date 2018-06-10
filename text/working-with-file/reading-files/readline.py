#!/usr/bin/env python
# readline() function

f = open("foo.txt", "r")
print "The first line:", f.readline()
print "The second line with 7 bytes:", f.readline(7)