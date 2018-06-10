#!/usr/bin/env python
# startswith() and endswith() replacement hack

some_string = "Raymond Luxury-Yacht"

ret = some_string[:len("Raymond")] == "Raymond"
print "Start with 'Raymond': %s" %ret

ret = some_string[:len("Firefox")] == "Firefox"
print "Start with 'Firefox': %s" %ret

ret = some_string[-len("Yacht"):] == "Yacht"
print "End with 'Yacht': %s" %ret

ret = some_string[-len("Firefox"):] == "Firefox"
print "End with 'Firefox': %s" %ret