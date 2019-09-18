from __future__ import print_function
import re


 # construct two different patterns
numbers_rx = r'([0-9]+)'
text_rx = r'([a-z]+)'

# find all patterns in given string
print(re.findall(numbers_rx, "my phone number is 555-555-5555") )
print(re.findall(text_rx, "my phone number is 555-555-5555") )
