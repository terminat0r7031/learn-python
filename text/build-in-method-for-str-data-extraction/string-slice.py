#!/usr/bin/env python
# string slice

import subprocess
res = subprocess.Popen(["uname", "-sv"], stdout=subprocess.PIPE)
uname = res.stdout.read().strip()

print "Value of uname: %s" %uname

smp_index = uname.index("SMP")
print "'SMP' index: %s" %smp_index

print uname[smp_index:]
print uname[:smp_index]