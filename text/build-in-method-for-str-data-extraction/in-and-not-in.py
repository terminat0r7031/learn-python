#!/usr/bin/env python

# in and not in example
import subprocess
res = subprocess.Popen(["uname", "-sv"], stdout=subprocess.PIPE)
uname = res.stdout.read().strip()
print "Value of uname: %s" %uname

ret = "Linux" in uname
print "'Linux' in uname: %s" % ret

ret = "Firefox" in uname
print "'Firefox' in uname: %s" % ret

ret = "Linux" not in uname
print "'Linux' not in uname: %s" % ret

ret = "Firefox" not in uname
print "'Firefox' not in uname: %s" % ret