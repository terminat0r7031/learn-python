#!/usr/bin/env python
# splitlines()

multiline_string = """This
is
a multiline
piece of
text"""

lines = multiline_string.splitlines()
print lines

# using for loop
for line in lines:
    print "START LINE::"
    print line.split()
    print "::END LINE"