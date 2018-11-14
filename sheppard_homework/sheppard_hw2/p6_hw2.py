#!/usr/bin/env python3
# P6) Write File
# This program creates a file containing two user-provided strings, one per line in the file:

def careful_write(outlines, filename):
   """Write a list of strings to a file, if the file doesn't yet exist.

      outlines: a list of the strings to be written
      filename: where the strings will be written
   """
   import os
   import sys
   if os.access(filename, os.F_OK):
      sys.stderr.write('\nOutput file already exists: %s\n\n' % filename)
      return

   outfile = open(filename, 'w')
   for i in outlines:
      outfile.write(i)
      outfile.write('\n')
   outfile.close()

# User enters strings to write to file:
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

input_list = [string1, string2]
outfile_name = input("Enter filename, or press enter for default name: ")
if outfile_name == '':
   outfile_name = "p6_hw2_outfile.txt"
# Write strings to file
careful_write(input_list, outfile_name)

"""
Comments on Outfile:
This program will automatically write the output to the file p6_hw2_outfile.txt which will be created and saved in the working directory when the program is called. If this filename already exists, it will return an error message informing the user of this. The user can then simply delete the original file under this name or select a different name.

NB: The default output file "p6_hw2_outfile.txt" is initially present in the homework directory with the other problems, containing the output of the last used test. If one wishes to initially use the default filename, this file should be removed from the working director.
"""
