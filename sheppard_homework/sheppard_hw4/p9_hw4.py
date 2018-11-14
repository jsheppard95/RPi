#!/usr/bin/env python3

# P9) Get Web Page with Requests
# filename: p9_hw4.py
# author: Jackson Sheppard
# Last modified: 22Jul17

# Python program that prints out for user when Phys 129 web page announcements
# were last updated using requests

import requests

# List of days of week and months in year
# Used as comparison tool when parsing course web page
keys = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Open course web page and store contents as string
r = requests.get('http://web.physics.ucsb.edu/~phys129/lipman/')
html_str = r.text

# Parse string until day is found, then add it to output string
output_str = ""
for key in keys:
   if key in html_str: # will match twice, once for day and once for month
      output_str += key
      output_str += ' '

# find day in month:
loc = html_str.find('&nbsp;') # always separates month and day
try:
   day = html_str[loc+6:loc+8] # day is two digit number
   int(day)
except ValueError:
   day = html_str[loc+6:loc+7] # day is one digit number
output_str += day

print("Phys 129 Web Page last updated:")
print(output_str)
