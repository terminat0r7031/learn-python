#!/usr/bin/env python
# basic regular expression usage

import re

re_string = "{{(.*?)}}"

some_string = "this is a string with {{word}} embedded in\
{{currly brackets}} to show an {{example}} of {{regular expression}}"

for match in re.findall(re_string, some_string):
    print "MATCH->", match