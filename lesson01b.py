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
# methods
#************************************************************

#******************************
# Fibonacci series
# Param   n     limit of series
# Return        list of Fibonacci numbers
#******************************
def fib2(n): # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result


#******************************
# Example method with keywords
# DO NOT NAME YOUR FUNCTIONS WITH ONE LETTER!
# input parameters b and L have default values
# we can call with 1-3 input parameters
# f(a) will use the defaults for b and L
# f(a, L=[1] will use the defaults for b and populate L
# ...
# Important warning: The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls for L but b does not:
#
# Play with to understand
#******************************
def f(a, b=None, L=[]):
    L.append(a)
    print 'b = ', b
    return L


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
# if statements
#******************************
if test == 0:

    # Basic if example, we also have elif
    # raw_input is a method of python to retrieve input and print a prompt
    # int() converts that input to an integer
    if 5 < int(raw_input("Please enter an integer greater then 5: ")):
        print 'True'
    else:
        print 'False'


#******************************
# for statements
#******************************
if test == 1:
    a = ['cat', 'window', 'defenestrate']
    
    # for statements are loops that iterate over a list (python)
    # here we are iterating over the list of a
    for x in a:
        # note the use of a coma is convenient instead of constructing a single string
        print x, len(x)


#******************************
# break
#******************************
if test == 2:

    # The range statement allows for your normal counting for loop
    for n in range(2, 10):
        for x in range(2, n):
            # % is modulus. In this example n is divisible by x and so we quit
            if n % x == 0:
                print n, 'equals', x, '*', n/x
                # this exits the existing for loop: for x in range(2, n):
                break
        else:
            # loop fell through without finding a factor
            print n, 'is a prime number'


#******************************
# continue
#******************************
if test == 3:

    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            # Continue will exit this iteration of the for loop and continue with the next iteration
            # This is unlike break which terminates the for loop
            continue
        print("Found a number", num)



#******************************
# method intro
#******************************
if test == 4:

    # see documentation for fib2()
    print fib2(100)


#******************************
# default values / keywords
#******************************
if test == 5:

    # see documentation for f()
    print f(1)
    print f(2)
    print f(3)
    print f(1,[])
    print f(1,5)
    print f(1,L=[])


#******************************
# Lambda Forms
#******************************
if test == 6:

    # lambda is a special constructor for small functions (not needed)
    print (lambda a,b: a+b)(2,3)


#******************************
# Coding Style
#******************************
if test == 7:

    # Play with the spacing. Once there is no indent after the for it will yell at you.
    for x in range(10):
        pass
        
        
        
