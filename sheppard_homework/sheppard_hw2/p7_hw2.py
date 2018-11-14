#!/usr/bin/env python3
# P7) Read File and Average
# This program will read numbers from a user-specified file and prints out their average.
# Input file: user-defined but will contain only one number per line with no blank lines

# Read input file:
def file_readlines(filename):
   """Read text file and return the contents as a list of lines.
   """
   infile = open(filename, 'r')
   inlines = infile.readlines()
   infile.close()
   return(inlines)

# Get file name from user
infile = input("Enter filename: ")
inlines = file_readlines(infile) # list whose entries are lines in the file (w/ '\n character)

# Get numbers from list 'infiles'
num_list = []

for i in range(len(inlines)):
   num_str = inlines[i].rstrip('\n') # remove '\n'
   num = float(num_str) # Convert to float to compute average
   num_list.append(num)

# Iterate through 'num_list' to compute average:
total = 0
for entry in num_list:
   total += entry
avg = total / len(num_list)

# Output average:
print("Avgerage: ", avg)

"""
This program iterates through the contents of numbers and then stores each line in a list titled 'inlines'. Since the file contains simply one number per line, each element in the list will accordingly be a string containing the number and '\n' character designating the end of each line. The input file must have this specific format or else an error may occur.
In order to compute the average, we first iterate through the contents of inlines and remove the '\n' character from each line. We then convert what remains from a string to floating point number and store this new value in the list 'num_list'. We can then compute the average by iterating through the floating points in num_list and calculating the sum of all entries and then dividing by the total number of entries.
"""
