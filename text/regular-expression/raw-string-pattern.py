#!/usr/bin/env python
# raw strings and regular expression

import re

#example 1
print "Example 1"
raw_pattern = r'\b[a-z]+\b'
some_string = "a few little words"
print re.findall(raw_pattern, some_string)


#example 2
print "Example 2"
re_obj = re.compile(r'\bt\w*e\b')
some_string = "time tame tune tint tire"
print re_obj.findall(some_string)

