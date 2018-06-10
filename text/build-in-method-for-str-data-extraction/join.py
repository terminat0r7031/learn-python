#!/usr/bin/env python
# join()
# using "list comprehension" to join not string array

some_list = ["one", "two", "three", "four"]

print ",".join(some_list)

print ", ".join(some_list)

print "\t".join(some_list)

print "".join(some_list)

# integer array
some_list = range(10)
print ", ".join([str(i) for i in some_list])

print ", ".join(str(i) for i in some_list)
