#!/usr/bin/env python
# http://docs.python.org/tutorial/

# ssh user@ecelinux.uwaterloo.ca
# sftp user@ecelinux.uwaterloo.ca
# scp file(s) user@ecelinux.uwaterloo.ca:destination

# http://docs.python.org/tutorial/introduction.html
# http://docs.python.org/tutorial/controlflow.html
# http://docs.python.org/tutorial/modules.html
# http://docs.python.org/tutorial/inputoutput.html
# http://docs.python.org/library/re.html

# http://stackoverflow.com/
# http://www.udacity.com/overview/Course/cs101/CourseRev/apr2012


#************************************************************
# imports
#************************************************************

import re
import sys
import random




#************************************************************
# main
#************************************************************

#******************************
# try/except
# call the program with a number argument to run different areas of the code
# this statement would fail with no arguments if it wasn't for the try:
#******************************
try:
    test = int(sys.argv[1])
except :
    test = 0

#******************************
# Numbers
#******************************
if test == 0:

    # normal math
    print 2+2

    # casting of an int and float
    a = 2
    b = 2.0
    
    # addition of two different types
    print a + b
    
    # type conversion
    print int(b)
    

#******************************
# Strings
#******************************
if test == 1:

    # casting of a str
    c = "hello world "
    
    # playing with sub-strings and indices
    print c
    print c[:2] + c[4:6] + c[-2:]
    print c[1:]

    # building new strings (you cannot manipulate strings, python will always create a new string)
    print str(5) + ": " + c*5
    
    # string properties (works for lists as well)
    print len(c)
    
    # .find is a object method of strings, it returns the index of where world is found
    print c[ c.find("world") : ]


#******************************
# Lists
#******************************
if test == 2:

    # casting a list
    a = ['spam', 'eggs', 100, 123.4]

    # playing with indices
    print a
    print a[0]
    print a[2:]

    # WARNING - b points to the same list!
    b = a
    # This changes both lists
    b[0] = 'maps'
    print a
    print b

    # the list constructor makes a new list using a to populate
    b = list(a)
    # now when we change it, a stays the same (it was 'maps')
    b[0] = 'spam'
    print a
    print b
    
    # other fun object methods for lists
    a.extend(b)
    b.append(b[0])
    print a
    print b


