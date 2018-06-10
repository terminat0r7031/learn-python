#!/usr/bin/env python

def myRange(r):
    i = 0
    while i < r:
        yield  "%s\n" %i
        i += 1
f = open("writelines_generator_function_outfile", "w")
f.writelines(myRange(10))

f.close()

g = open("writelines_generator_function_outfile", "r")
print g.read()
