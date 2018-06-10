#!/usr/bin/env python
# find() and index() example

import subprocess
res = subprocess.Popen(["uname", "-sv"], stdout=subprocess.PIPE)
uname = res.stdout.read().strip()
print "Value of uname: %s" %uname

#find
print "%s" %uname.find("Linux")
print "%s" %uname.find("Firefox")
