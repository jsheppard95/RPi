#!/usr/bin/env python3

# P4) User Input:
# This program takes in an input string from the user and prints it to the monitor 10 times
printed_string = input("Please enter a string: ") # Get string from user
for i in range(10):
  print('%d:' % (i+1), printed_string) # Print string 10 times, number each time


