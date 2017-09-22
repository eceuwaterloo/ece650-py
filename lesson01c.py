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
import math
import random
import string


#************************************************************
# methods
#************************************************************




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
# Files
#******************************
if test == 0:

    # open the file with minimum attributes 'r' = read
    f = open('input.txt', 'r')
    print f.read()
    f.close()                           # always close the file
    
    # 'a' = append
    f = open('input.txt', 'a')
    f.write('new entry \n')
    f.close()


#******************************
# regular expressions
# used for pattern matching
# see http://docs.python.org/library/re.html for documentation
#******************************
if test == 1:
    
    # construct two different patterns
    numbers_rx = r'([0-9]+)'
    text_rx = r'([a-z]+)'
    
    # find all patterns in given string
    print re.findall(numbers_rx, "my phone number is 555-555-5555")
    print re.findall(text_rx, "my phone number is 555-555-5555")








