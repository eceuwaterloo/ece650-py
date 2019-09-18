#!/usr/bin/python
from __future__ import print_function

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
        errStr = 'The name ' + name + ' is weird.'
        print(errStr, file=sys.stderr)
    else:
        s = 'The name ' + name + ' is ok.'
        print(s)
