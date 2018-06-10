#!/usr/bin/env python
# writelines() method

f = open("writelines_file.txt", "w")
f.writelines("%s\n" % i for i in range(10))
f.close()

g = open("writelines_file.txt", "r")
print g.read()