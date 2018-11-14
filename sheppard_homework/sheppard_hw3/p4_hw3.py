#!/usr/bin/env python3
# P4) Valentine's day
# filename: p4_hw3.py
# This program read in a file containing the students in the class, and then prints out a "Happy Valentine's Day!" message for each student.

def file_readlines(filename):
   """Read text file and return the contents as a list of lines.
   """
   infile = open(filename, 'r')
   inlines = infile.readlines()
   infile.close
   return inlines

inlines =  file_readlines('classlist.csv') # list containing each line in file, as strings
for i in range(len(inlines)):
   name_info_str = inlines[i]
   name_info_list = name_info_str.split(',')
   lastname = name_info_list[0].title()
   firstname = name_info_list[1].title()
   print('Happy Valentine\'s Day,', firstname, (lastname+'!'))
