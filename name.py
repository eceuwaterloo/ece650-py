#!/usr/bin/python

# Sample program for names

import re
import sys

while(True):
    try:
	name = raw_input()
    except EOFError:
	break;
    r = '\('
    p = re.compile(r)
    if(p.match(name)):
	errStr = 'The name ' + name + ' is weird.\n'
	sys.stderr.write(errStr)
    else:
	s = 'The name ' + name + ' is ok.'
	print s
