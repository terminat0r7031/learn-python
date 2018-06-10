#!/usr/bin/env python
# simple regular expression, compiled pattern

import re

re_obj = re.compile("{{(.*?)}}")

some_string = "this is a string with {{word}} embedded in\
{{currly brackets}} to show an {{example}} of {{regular expression}}"

for match in re_obj.findall(some_string):
    print "MATCH->", match