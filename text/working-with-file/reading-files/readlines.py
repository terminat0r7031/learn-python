#!/usr/bin/env python
# read all line

f = open("foo.txt", "r")
lines = f.readlines()
print lines
print "".join(lines)